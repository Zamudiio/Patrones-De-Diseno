package content.creacionales.factory_method.java.zamudiio;

import content.creacionales.factory_method.java.zamudiio.interfaces.Product;

public class Box implements Product {

   @Override
   public int getId() {
      return 1;
   }

   @Override
   public int getStack() {
      return 10;
   }
   
}
