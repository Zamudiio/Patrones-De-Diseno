package content.creacionales.abrastact_factory.java.zamudiio;

public class AluminumFactory implements ShopProductFactory {

   @Override
   public Chair createChair() {
      return new Chair(Material.ALUMINIUM);
   }

   @Override
   public Sofa createSofa() {
      return new Sofa(Material.ALUMINIUM);
   }
   
}
