
cd ./cb_viagens_api

# Run the Django server in the background
pip install -r requirements.txt
python manage.py migrate
py manage.py runserver 3000 &

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
