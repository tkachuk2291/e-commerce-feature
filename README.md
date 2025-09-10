````
# E-Commerce Feature Project
````

```markdown
## Project Overview
Full-stack e-commerce platform built with FastAPI and React.

```

```
## Repository Structure
```
e-commerce-feature/

├── [backend_e_commerce](backend_e_commerce)   # FastAPI Backend  

└── [frontEnd-e-commerce](frontEnd-e-commerce)  # React Frontend  
```

## Backend Setup (FastAPI)


1. Create virtual environment:
```bash
cd backend_e_commerce
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure PostgreSQL:
```bash
# Install PostgreSQL (if already have postgres , skip this step)
brew install postgresql@14
brew services start postgresql@14
```

3.1 Create database
```bash
# Create database
createdb ecommerce_db
```

4. Create `.env` file:
```env
DATABASE_URL="postgresql+psycopg2://user:@localhost/ecommerce_db"
```

5. Run migrations and seeds:
```bash
alembic upgrade head
```
5.1 Run seeds:
````bash
python -m database.seed_db
````
6. Start backend server(copu and paste in terminal):
```bash
uvicorn main:app --reload
```

Backend runs at: `http://localhost:8000`

### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Products

````
GET /products - get Product list
GET /products/search/?name={search_term} - filtering product list by name
GET /products/{id} - get one product by id
POST /products - create new product
PUT /products/{id} - update product by id
DELETE /products/{product_id} - delete product by id
````

## Users
````
POST /users/register - crate user
````

## Frontend Setup (React)

### Prerequisites
- Node.js 16+
- npm

### Installation Steps
1. Install dependencies:
```bash
cd frontEnd-e-commerce
npm install
```

1.2

4. Create `.env` file:
```env
http://127.0.0.1:8000/ or server link it avaliable to
```

2.Start development server:
```bash
npm run dev
```

Frontend runs at: `http://localhost:5173`

### Available Pages
- `/products` - Product list
- `/products/:id` - Product details


## Technologies

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic

### Frontend
- React 18
- Vite
- React Router 6

