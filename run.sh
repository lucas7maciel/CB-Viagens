
cd ./cb_viagens_api

# Run the Django server in the background
pip install -r requirements.txt

if command -v python3 &>/dev/null; then
    PYTHON=python3
else
    PYTHON=python
fi

PYTHON manage.py migrate
PYTHON manage.py loaddata ../data.json # populates database
PYTHON manage.py runserver 3000 &      # runs server with port 3000

# Save the PID of the Django server process
DJANGO_PID=$!

# Navigate to the directory where your Vue project is located
cd ../cb_viagens

# Run the Vue development server in the background
npm install
npm run dev &

# Save the PID of the Vue development server process
VUE_PID=$!

# Wait for both processes to finish
wait $DJANGO_PID
wait $VUE_PID
