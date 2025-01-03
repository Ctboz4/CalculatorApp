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
        JButton zero_Button = new JButton("0");
        JButton one_Button = new JButton("1");
        JButton two_Button = new JButton("2");
        JButton three_Button = new JButton("3");
        JButton four_Button = new JButton("4");
        JButton five_Button = new JButton("5");


        //This will add the button to the screen
        panel.add(display);
        panel.add(zero_Button);
        panel.add(one_Button);
        panel.add(two_Button);
        panel.add(three_Button);
        panel.add(four_Button);
        panel.add(five_Button);



        //I want to get the text and save it for later
        String currentTextDisplayed = display.getText();

        //Here is going to be ActionListeners
        one_Button.addActionListener(e -> display.setText(currentTextDisplayed + "1"));
        two_Button.addActionListener(k -> display.setText(currentTextDisplayed + "2"));
        //ToDo figure out how to stop it from deleting whats already there


    }
}