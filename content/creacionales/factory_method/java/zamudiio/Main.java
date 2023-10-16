package content.creacionales.factory_method.java.zamudiio;

public class Main {
   public static void main(String[] args) {
      ProductFactory productA = new BoxFactory();
      ProductFactory productB = new RadioFactory();
      
      System.out.println(productA.createProduct().getClass()); // output = Box
      System.out.println(productB.createProduct().getClass()); // output = Radio
   }
}
