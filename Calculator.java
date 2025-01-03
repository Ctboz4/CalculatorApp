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
        FirstNumberUsed = sNumber;
    }

    public void setOperator(String op){
        Operator = op;
    }
}
