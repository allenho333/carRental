echo "Starting backtend..."
cd ./mysite
python manage.py runserver &
echo "Backend started."
cd ..
echo "Starting frontend..."
cd ./vite-project
npm run dev
echo "Frontend started."
