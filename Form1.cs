using System;
using System.Windows.Forms;

namespace SimpleCounter
{
    public partial class Form1 : Form
    {
        private int count = 0;
        private Label countLabel;
        private Button plusButton;
        private Button minusButton;
        private Button resetButton;

        public Form1()
        {
            InitializeComponent();
            CreateControls();
            UpdateCountLabel();
        }

        private void CreateControls()
        {
            countLabel = new Label();
            countLabel.Font = new System.Drawing.Font("Arial", 48, System.Drawing.FontStyle.Bold);
            countLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            countLabel.Dock = DockStyle.Top;
            countLabel.Height = 150;

            plusButton = new Button();
            plusButton.Text = "+";
            plusButton.Font = new System.Drawing.Font("Arial", 24, System.Drawing.FontStyle.Bold);
            plusButton.Dock = DockStyle.Top;
            plusButton.Height = 70;
            plusButton.Click += PlusButton_Click;

            minusButton = new Button();
            minusButton.Text = "-";
            minusButton.Font = new System.Drawing.Font("Arial", 24, System.Drawing.FontStyle.Bold);
            minusButton.Dock = DockStyle.Top;
            minusButton.Height = 70;
            minusButton.Click += MinusButton_Click;

            resetButton = new Button();
            resetButton.Text = "Сброс";
            resetButton.Font = new System.Drawing.Font("Arial", 16);
            resetButton.Dock = DockStyle.Bottom;
            resetButton.Height = 50;
            resetButton.Click += ResetButton_Click;

            Controls.Add(resetButton);
            Controls.Add(minusButton);
            Controls.Add(plusButton);
            Controls.Add(countLabel);

            Text = "Простой счётчик";
            Width = 400;
            Height = 400;
            StartPosition = FormStartPosition.CenterScreen;
        }

        private void PlusButton_Click(object sender, EventArgs e)
        {
            count++;
            UpdateCountLabel();
        }

        private void MinusButton_Click(object sender, EventArgs e)
        {
            count--;
            UpdateCountLabel();
        }

        private void ResetButton_Click(object sender, EventArgs e)
        {
            count = 0;
            UpdateCountLabel();
        }

        private void UpdateCountLabel()
        {
            countLabel.Text = count.ToString();

            if (count > 0)
                countLabel.ForeColor = System.Drawing.Color.Green;
            else if (count < 0)
                countLabel.ForeColor = System.Drawing.Color.Red;
            else
                countLabel.ForeColor = System.Drawing.Color.Black;
        }
    }
}
