# GPAWrld.Calc

A simple command-line GPA Calculator written in Python. This tool allows students to calculate their GPA using multiple methods based on class or semester data, and even helps estimate the credits or GPA needed to reach a desired goal.

---

## 📌 Features

* 📘 **Class-Based GPA Calculation**
  Input your number of classes, credit hours, and grades (A–F).

* 📚 **Semester-Based GPA Calculation**
  Input your completed semesters, GPA per semester, and credit hours.

* 🎯 **Target GPA Estimator**
  Enter your current GPA, completed credits, and a desired GPA to determine:

  * Credits needed if you maintain a 4.0
  * GPA needed for upcoming credits to reach your goal

---

## 🧠 How It Works

After launching, the program provides the following options:

```
0: Exit the application.
1: GPA by number of classes (grade + credit per class)
2: GPA by number of semesters (GPA + credit per semester)
3: Estimate credits/GPA required to reach your desired GPA
```

---

## ▶️ Usage

### Run the Program:

```bash
python gpa_calculator.py
```

### Example:

```
* * * GPA CALCULATOR * * *
Select the method you want.
1: GPA by class
2: GPA by semester
3: Desired GPA Estimator
Enter your choice: 1
```

---

## ✅ Input Examples

### Option 1: GPA by Class

* Number of classes: `3`
* Credit for class 1: `3`, Grade: `A`
* Credit for class 2: `4`, Grade: `B`
* Credit for class 3: `3`, Grade: `C`

### Option 2: GPA by Semester

* Number of semesters: `2`
* Semester 1: 12 credits, GPA: 3.5
* Semester 2: 15 credits, GPA: 3.8

### Option 3: Reach Desired GPA

* Current GPA: `3.2`
* Completed credits: `45`
* Desired GPA: `3.7`
* Projected GPA for future classes: `3.9`

---

## 🧰 Requirements

* Python 3.x

No external libraries required.

---

## 🚀 Future Improvements

* GUI version using Tkinter or PyQt
* Web-based interface (Flask or Django)
* GPA scale customization (4.3, weighted, +/- grades)

---

## 📄 License

This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).
