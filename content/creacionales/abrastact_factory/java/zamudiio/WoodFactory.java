package content.creacionales.abrastact_factory.java.zamudiio;

public class WoodFactory implements ShopProductFactory {

   @Override
   public Chair createChair() {
      return new Chair(Material.WOOD);
   }

   @Override
   public Sofa createSofa() {
      return new Sofa(Material.WOOD);
   }
   
}
