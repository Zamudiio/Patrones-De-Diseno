package content.creacionales.factory_method.java.zamudiio;

import content.creacionales.factory_method.java.zamudiio.interfaces.Product;

public class BoxFactory extends ProductFactory {

   @Override
   public Product createProduct() {
      return new Box();
   }
   
}
