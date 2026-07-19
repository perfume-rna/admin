def check_productId(db, id):
    with db.connect() as conn_product:
        result = conn_product.execute(text("SELECT 1 FROM products_tbl WHERE product_id = :id"), {
          "id": id
      }).fetchone()
        if result is None:
            return True
        else:
            return False

def get_data(db):
    with db.connect() as conn:
      items = conn.execute(text("SELECT product_id, name, quantity, price, image_link, description FROM products_tbl"))
      list_items = []
      for x in items:
          list_items.append([x.product_id, x.name, x.quantity, str(x.price), x.image_link, x.description])
      return list_items
