package content.creacionales.factory_method.java.zamudiio;

import content.creacionales.factory_method.java.zamudiio.interfaces.Product;

public class Radio implements Product {

   @Override
   public int getId() {
      return 2;
   }

   @Override
   public int getStack() {
      return 29;
   }
 
}
