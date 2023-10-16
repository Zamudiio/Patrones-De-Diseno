package content.creacionales.factory_method.java.zamudiio;

public class Main {
   public static void main(String[] args) {
      ProductFactory productA = new BoxFactory();
      
      System.out.println(productA.createProduct().getClass());
   }
}
