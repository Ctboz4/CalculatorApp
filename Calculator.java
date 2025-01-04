public class Calculator {
    private double FirstNumberUsed;
    private double SecondNumberUsed;
    private String Operator;  

    public Calculator(){
        FirstNumberUsed = 0;
        SecondNumberUsed = 0;
        Operator = "";
    }  

    public double getFirstNumberUsed(){
        return FirstNumberUsed;
    }

    public double getSecondNumberUsed(){
        return SecondNumberUsed;
    }

    public String getOperator(){
        return Operator;
    }

    public void setFirstNumberUsed(double fNumber){
        FirstNumberUsed = fNumber;
    }

    public void setSecondNumberUsed(double sNumber){
        SecondNumberUsed = sNumber;
    }

    public void setOperator(String op){
        Operator = op;
    }

    public double operation(){
        switch(Operator){
            
            case "+":
                return FirstNumberUsed + SecondNumberUsed;
            case "-":
                return FirstNumberUsed - SecondNumberUsed;
            case "*":
                return FirstNumberUsed * SecondNumberUsed;

            case "/":
            //This means that the first number isnt 0!
                if (FirstNumberUsed != 0){
                    return FirstNumberUsed / SecondNumberUsed;
                }
                else{
                    System.out.println("Error");
                    return Double.NaN;
                }
            default:
            System.out.println("Error");
            return Double.NaN;
        }
    }
}
