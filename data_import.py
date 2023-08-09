from apscheduler.schedulers.background import BackgroundScheduler
from models import db, Store, Product  # Import your database models
import api_client  # Import your API client functions

# Create a scheduler instance
scheduler = BackgroundScheduler()

# Function to import data from API and update the database
def import_data():
    # Fetch data from API endpoints
    clusters = api_client.fetch_clusters()
    regions = api_client.fetch_regions()
    stores = api_client.fetch_stores()
    products = api_client.fetch_store_products()

    # Update the database with fetched data
    with app.app_context():
        db.session.query(Store).delete()  # Clear existing data before updating
        for cluster in clusters:
            db.session.add(Cluster(name=cluster['name']))
        for region in regions:
            db.session.add(Region(name=region['name']))
        for store in stores:
            db.session.add(Store(name=store['name'], theme=store['theme'], region=store['region'], cluster=store['cluster']))
        for product in products:
            db.session.add(Product(name=product['name'], sku=product['sku'], season=product['season']))

        db.session.commit()

# Schedule the import_data function to run every hour
scheduler.add_job(import_data, 'interval', hours=1)

# Start the scheduler
scheduler.start()
