import javax.swing.*;
import java.awt.*;

public class App{
    public static void main(String[] args){

        Calculator calculator = new Calculator();

        //Frame info
        JFrame frame = new JFrame("Calculator");
        frame.setVisible(true);//Without this it wont even show
        frame.setSize(200,200);

        //Panel Info
        JPanel panel = new JPanel(new GridLayout(5, 4));
        frame.add(panel);//This is a must
        
        //This is for the actual display
        JTextField display = new JTextField();


        //Button Info
        JButton plus_button = new JButton("+");
        JButton minus_button = new JButton("-");
        JButton equals_button = new JButton("=");
        JButton zero_Button = new JButton("0");
        JButton one_Button = new JButton("1");
        JButton two_Button = new JButton("2");
        JButton three_Button = new JButton("3");
        JButton four_Button = new JButton("4");
        JButton five_Button = new JButton("5");


        //This will add the button to the screen
        panel.add(display);
        panel.add(equals_button);
        panel.add(plus_button);
        panel.add(minus_button);
        panel.add(zero_Button);
        panel.add(one_Button);
        panel.add(two_Button);
        panel.add(three_Button);
        panel.add(four_Button);
        panel.add(five_Button);



        
        

        //Here is going to be ActionListeners for number buttons
        one_Button.addActionListener(e -> display.setText(display.getText() + "1"));
        two_Button.addActionListener(e -> display.setText(display.getText() + "2"));
        three_Button.addActionListener(e -> display.setText(display.getText() + "3"));
        four_Button.addActionListener(e -> display.setText(display.getText() + "4"));
        five_Button.addActionListener(e -> display.setText(display.getText() + "5"));

        //Here is going to be ActionListeners for operator buttons
        plus_button.addActionListener(e -> {
            calculator.setFirstNumberUsed(Double.parseDouble(display.getText()));
            
            calculator.setOperator("+");
            display.setText("");

        });


        equals_button.addActionListener(e -> {
            calculator.setSecondNumberUsed(Double.parseDouble(display.getText()));
            double answer = calculator.operation();
            display.setText(String.valueOf(answer));
            System.out.println("First " + calculator.getFirstNumberUsed());
            System.out.println("S " + calculator.getSecondNumberUsed());
            System.out.println("O " + calculator.getOperator());
        });

        

        


    }
}