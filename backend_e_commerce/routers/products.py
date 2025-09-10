from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import select, update
from sqlalchemy.orm import Session

from database.database_manager import get_session
from database.models import Product
from schemas.products_shemas import ProductSchema, ProductUpdateSchema

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[ProductSchema], status_code=200)
async def get_list_products(session: Session = Depends(get_session)):
    try:
        stmt = select(Product)
        products_list = session.scalars(stmt).all()
        return products_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Помилка при отриманні списку продуктів: {str(e)}")


@router.get("/search/", response_model=list[ProductSchema], status_code=200)
async def get_product_by_name(name: str, session: Session = Depends(get_session)):
    search = "%{}%".format(name)
    stmt = select(Product).where(Product.name.ilike(search))
    products_list = session.scalars(stmt).all()
    return products_list


@router.post("/", response_model=ProductSchema, status_code=201)
async def create_products(product: ProductSchema, session: Session = Depends(get_session)):
    try:
        new_product = Product(
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock,
            category=product.category,
            image=product.image,
            user_id=product.user_id
        )
        session.add(new_product)
        session.commit()
        return new_product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Помилка при створенні нового продукта: {str(e)}")


@router.get("/{id}", response_model=ProductSchema, status_code=200)
async def get_detail_product(id, session: Session = Depends(get_session)):
    try:
        stmt = select(Product).where(Product.id == id)
        product = session.scalars(stmt).one_or_none()
        if not product:
            raise HTTPException(status_code=404, detail=f"Продукт з id={id} не знайдено")
        return product
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Помилка при отриманні продукту: {str(e)}")


@router.put("/{id}", status_code=200 ,  response_model=ProductUpdateSchema)
async def update_products(id, product: ProductUpdateSchema, session: Session = Depends(get_session)):
    try:
        update_data = product.model_dump(exclude_unset=True)

        if not update_data:
            raise HTTPException(status_code=400, detail="Немає данных для оновлення")
        stmt = (
            update(Product)
            .where(Product.id == id)
            .values(**update_data)
            .returning(Product)
        )

        result = session.execute(stmt)
        updated_product = result.scalar_one_or_none()

        if not updated_product:
            raise HTTPException(status_code=404, detail="Продукт не знайдено")

        session.commit()
        return updated_product

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Помилка при оновлені: {str(e)}")


@router.delete("/{product_id}", status_code=200)
async def delete_products(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Продукт не знайдено")

    session.delete(product)
    session.commit()
    return {"message": f"Продукт  з ид {product_id} видалено"}
