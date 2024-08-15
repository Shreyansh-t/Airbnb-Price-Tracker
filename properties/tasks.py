# properties/tasks.py

from celery import shared_task
from home.scraper import fetch_data  # import your scraping function
from .models import *
from home.scraper import *
from django.core.mail import send_mail
from selenium.common.exceptions import WebDriverException

@shared_task
def scrape_property_data():
    driver = None
    try:
        driver = start()  # Initialize the Selenium WebDriver
        search_params = SearchParams.objects.all()
        
        for params in search_params:
            try:
                # Open Airbnb and perform the search
                open_site(driver)
                entry = Entry(
                    where=params.destination,
                    check_in=params.check_in,
                    check_out=params.check_out,
                    adults=params.adults,
                    children=params.children,
                    infants=params.infants
                )
                entry.add_details(driver)
                
                # Fetch the data from the results page
                titles, descs, prices = fetch_data(driver)
                
                # Match the results with properties in the database
                for title, desc, price in zip(titles, descs, prices):
                    try:
                        property, created = Property.objects.get_or_create(
                            title=title,
                            desc=desc,
                            search_params=params,
                            defaults={'price': price, 'user': params.user}
                        )
                        
                        # Always create a history entry
                        History.objects.create(property=property, price=price)
                        
                        # Update the property's current price
                        if property.price != price:
                            old_price = property.price
                            property.price = price
                            property.save()
                            
                            # Send email alert only if price has dropped
                            if price < old_price:
                                send_mail(
                                    "Price Drop Alert!!",
                                    f"The price for {property.title} in {property.search_params.destination} has dropped from {old_price} to {price}.",
                                    "1209shreyansh.tehanguria@gmail.com",
                                    [property.user.email],
                                    fail_silently=False,
                                )
                    except Exception as e:
                        print(f"Error processing property {title}: {str(e)}")
                        # Log this error
                        continue
            except WebDriverException as e:
                print(f"WebDriver error for params {params.id}: {str(e)}")
                # Log this error or send an alert
                continue
    finally:
        if driver:
            driver.quit()  # Ensure the driver is always closed