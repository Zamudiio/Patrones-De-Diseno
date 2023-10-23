package content.creacionales.abrastact_factory.java.zamudiio;

public class Main {
   public static void main(String[] args) {
      
      /** 
       * You can change the Factory to another Factory and the code will continue to work.
      */

      ShopProductFactory factory = new WoodFactory();

      Chair chair = factory.createChair();
      Sofa sofa = factory.createSofa();

      System.out.println(chair);
      System.out.println(sofa);
   }
}
