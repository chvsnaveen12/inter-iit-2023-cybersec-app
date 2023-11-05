// Source code is decompiled from a .class file using FernFlower decompiler.
package passcheck;

public class PassCheck {
   static final int[] lookup = new int[]{158, 152, 106, 153, 44, 139, 54, 67, 169, 156, 159, 192, 243, 88, 96, 189, 225, 33, 79, 3, 248, 100, 145, 14, 76, 126, 141, 224, 64, 74, 86, 55, 220, 49, 150, 71, 187, 22, 40, 162};

   public PassCheck() {
   }

   public static char hash(int var0, int var1) {
      int var2 = ((var0 ^ var1) + var0 & var0 + var1) % 26;
      return (char)(65 + var2);
   }

   public static void nuh() {
      System.out.println("Wrong password!");
   }

   public static void yuh() {
      System.out.println("Correct password!");
   }

   public static void check(String var0) {
      if (var0.length() * 2 != lookup.length) {
         nuh();
      } else {
         for(int var1 = 0; var1 < var0.length(); ++var1) {
            if (var0.charAt(var1) != hash(lookup[2 * var1], lookup[2 * var1 + 1])) {
               nuh();
               return;
            }
         }

         yuh();
      }
   }
}
