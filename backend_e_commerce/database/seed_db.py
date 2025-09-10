from .database_manager import SessionLocal, Base, engine
from .models import User, Product

Base.metadata.create_all(bind=engine)


def seed_data():
    db = SessionLocal()
    try:
        if not db.query(User).first():
            user = User(
                username="admin",
                email="admin@example.com",
                name="admin",
                password="test1234"
            )
            db.add(user)

        if not db.query(Product).first():
            products = [
                Product(
                    name="13-inch M4 MacBook Air",
                    description="Latest Apple M4 chip",
                    price=2000,
                    stock=5000,
                    category="technique",
                    image="https://cdn.thewirecutter.com/wp-content/media/2025/03/BEST-MACBOOKS-2048px-hero-3x2-1.jpg?auto=webp&quality=75&width=980&dpr=2",
                    user_id=1
                ),
                Product(
                    name="iPhone 15 Pro Max",
                    description="Newest Apple smartphone",
                    price=1200,
                    stock=3000,
                    category="technique",
                    image="https://www.istore.ua/upload/iblock/596/g95thtt5tajbw0p6z3v41dbzl4ttrgtk/15_pro_max_black_titan_4_is-kopiya.png",
                    user_id=1
                ),
                Product(
                    name="Sony WH-1000XM5 Headphones",
                    description="Noise cancelling over-ear headphones",
                    price=400,
                    stock=1500,
                    category="technique",
                    image="https://www.sony.ua/image/6145c1d32e6ac8e63a46c912dc33c5bb?fmt=pjpeg&wid=330&bgcolor=FFFFFF&bgc=FFFFFF",
                    user_id=1
                ),
                Product(
                    name="Samsung 55\" QLED TV",
                    description="Smart 4K UHD TV",
                    price=900,
                    stock=200,
                    category="technique",
                    image="https://images.samsung.com/is/image/samsung/p6pim/ua/qe55q60dauxua/gallery/ua-qled-q60d-qe55q60dauxua-541615873?$684_547_PNG$",
                    user_id=1
                ),
                Product(
                    name="Dell XPS 13 Laptop",
                    description="Portable Windows laptop",
                    price=1500,
                    stock=1000,
                    category="technique",
                    image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReIfyYr82J64zOBkQPwEwyBxLaBiLAsRMGVw&s",
                    user_id=1
                ),
                Product(
                    name="Logitech MX Master 3",
                    description="Advanced wireless mouse",
                    price=100,
                    stock=2000,
                    category="accessories",
                    image="https://artline.ua/storage/images/products/15529/gallery/258484/600_gallery_1716279616990083_0.webp",
                    user_id=1
                ),
                Product(
                    name="Apple Magic Keyboard",
                    description="Wireless keyboard for Mac",
                    price=120,
                    stock=1500,
                    category="accessories",
                    image="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MK2A3?wid=2000&hei=2000&fmt=jpeg&qlt=90&.v=1628010471000",
                    user_id=1
                ),
                Product(
                    name="Amazon Echo Dot 5th Gen",
                    description="Smart speaker with Alexa",
                    price=60,
                    stock=2500,
                    category="smart-home",
                    image="https://smart-gadget.club/image/cache/catalog/Products/home-gadgets/Echo-Dot-5th-Gen/echo-dot-5gen-5-800x800.jpg",
                    user_id=1
                ),
                Product(
                    name="Fitbit Charge 6",
                    description="Fitness & health tracker",
                    price=180,
                    stock=1200,
                    category="fitness",
                    image="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/rockcms/2024-03/240327-fit-bit-charger-6-review-ode-bd-main-c35d82.jpg",
                    user_id=1
                ),
                Product(
                    name="Nintendo Switch OLED",
                    description="Portable gaming console",
                    price=350,
                    stock=800,
                    category="gaming",
                    image="https://sota.store/image/cache/catalog/IP/Nintendo-Joy-Con-white-01-1600x1600.webp",
                    user_id=1
                ),
            ]

            db.add_all(products)

        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
    print("Seeding completed!")
