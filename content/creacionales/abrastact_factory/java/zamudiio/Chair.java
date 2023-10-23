package content.creacionales.abrastact_factory.java.zamudiio;

import content.creacionales.abrastact_factory.java.zamudiio.interfaces.ShopProduct;

public class Chair implements ShopProduct {

   Material materialType;

   public Chair(Material material){
      materialType = material;
   }

   @Override
   public boolean hasLegs() {
      return true;
   }

   @Override
   public int legs() {
      return 4;
   }
   
}
