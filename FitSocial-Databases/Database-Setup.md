# network name: netFitSocialPRO290
# Volume name: fitsocialMongoDB
# How to connect? connection string URI: mongodb://localhost:28000

# First time set up:
docker volume create fitsocialMongoDB

docker run -p 28000:27017 --name PRO290FitSocialMongoDB -v fitsocialMongoDB:/data/db  --net netFitSocialPRO290 mongo:latest


# Create one new database.
FitSocialPRO290

# Create 3 collections in the new database:
Users
Friends
Posts