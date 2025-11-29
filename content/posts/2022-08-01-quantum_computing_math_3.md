---
title: "חישוב קוונטי בגישה מתמטית, חלק ג'"
layout: post
categories:
  - חישוב קוונטי
tags:
  - חישוב קוונטי
description: 'הדרך שבה אוהבים לייצג דברים באלגברה לינארית היא עם וקטורים ומטריצות. בפוסט הזה נראה איך זה מסתדר עם חישוב קוונטי בכלל ועם מכפלות טנזוריות בפרט'
image: "2022/quantum_computer3.png"
---


<h2>איך לייצג מצב קוונטי של מספר קיוביטים עם וקטור?</h2>

<a href="https://gadial.net/2022/07/31/quantum_computing_math_2/">בפוסט הקודם</a> שלי על חישוב קוונטי הצגתי את הפורמליזם המתמטי שבו אנחנו משתמשים כדי לתאר מצב קוונטי של שני קיובטים או יותר - <strong>מכפלה טנזורית</strong>. הצגתי את זה למכפלה של שני מרחבים, אבל אפשר להמשיך באינדוקציה לכל מספר של מרחבים. מה שאני רוצה לדבר עליו הפעם הוא איך עושים דברים תכל'ס, ברמה הטכנית. יש לי מצב קוונטי - איך אני מייצג אותו, למשל, במחשב? זה הולך להיות פוסט טכני יחסית, והחלק האחרון שלו יוכיח שהכל עובד ולא באמת יוסיף אינפורמציה חדשה כך שאפשר לדלג עליו, ואני אדחה לפוסט הבא את הדברים המגניבים שרציתי לתאר אחריו (איזה אופרטור משמש אותנו כדי לייצר מצבים שזורים וכאלה). עדיין, שני החלקים הראשונים של הפוסט יוסיפו לנו מושגים שאני כנראה אשתמש בהם בחופשיות מכאן והלאה.

אנחנו בעולם האלגברה הלינארית, וכבר בקורס הראשון באלגברה לינארית רואים את הפתרונות הפשוטים לכל הבעיות הללו. ספציפית, לכל מרחב וקטורי סוף-ממדי {% equation %}V{% endequation %}, לא משנה כמה האיברים שלו משונים או מתוסבכים, יש דרך ייצוג פשוטה: ראשית לוקחים בסיס שלו, {% equation %}B=\left\{ b_{1},\ldots,b_{n}\right\} {% endequation %}. כעת, לכל איבר {% equation %}v\in V{% endequation %} קיים ייצוג <strong>יחיד</strong> בתור צירוף לינארי {% equation %}v=\sum_{i=1}^{n}\lambda_{i}b_{i}{% endequation %}, אז מגדירים את <strong>וקטור הקואורדינטות</strong> של {% equation %}v{% endequation %} על פי הבסיס {% equation %}B{% endequation %} בתור הוקטור

{% equation %}\left[v\right]_{B}\triangleq\left(\begin{array}{c} \lambda_{1}\\ \vdots\\ \lambda_{n} \end{array}\right){% endequation %}

של כל המקדמים של {% equation %}v{% endequation %} בצירוף הלינארי הזה. מרגע זה ואילך אפשר להתעסק עם {% equation %}V{% endequation %} כאילו הוא {% equation %}\mathbb{F}^{n}{% endequation %} ({% equation %}\mathbb{F}{% endequation %} הוא השדה מעליו המרחב מוגדר; אצלנו זה {% equation %}\mathbb{C}{% endequation %}), מה שמפשט את העניינים.

דבר אחד שצריך לשים לב אליו הוא שההתאמה הזו של וקטורי קואורדינטות לאיברים <strong>תלויה בבסיס</strong> - תיקחו בסיס שונה, תקבלו וקטורי קואורדינטות שונים. יותר מזה, זה תלוי <strong>בסדר שבו האיברים מופיעים בבסיס</strong>, מה שאצלי היה קיים באופן מובלע על ידי המספור {% equation %}b_{1},\ldots,b_{n}{% endequation %} של איברי הבסיס. אם אנחנו רוצים להשתמש בוקטורי קואורדינטות בהקשר של חישוב קוונטי, נצטרך למצוא דרך מוסכמת למספר את אברי הבסיס שבו נשתמש.

בפוסט הקודם שלי ראינו בסיס סטנדרטי למרחב של שני קיוביטים: {% equation %}\left|00\right\rangle ,\left|01\right\rangle ,\left|10\right\rangle ,\left|11\right\rangle {% endequation %}. למה כתבתי את האיברים בסדר הזה? פשוט: כי אם אני חושב על מחרוזות הביטים הללו כאילו הן מייצגות מספר בייצוג בינארי, הן מתארות את המספרים {% equation %}0,1,2,3{% endequation %} בהתאמה. הסדר בא מעצמו. אבל עבור מי שלא מכירים ייצוג בינארי בואו נסביר קצת יותר בפירוט.

בייצוג "רגיל" של מספר, למשל {% equation %}142{% endequation %}, יש ספרת אחדות, וספרות עשרות, וספרת מאות. אחד, עשר ומאה כולם חזקות של {% equation %}10{% endequation %}, והספרות אומרות לנו במה לכפול את החזקות הללו לפני שמחברים את הכל: {% equation %}1\cdot10^{2}+4\cdot10^{1}+2\cdot10^{0}{% endequation %}. בייצוג בינארי קורה אותו דבר רק עם חזקות של 2. ספרה בינארית היא או 0, או 1, כלומר ייצוג בינארי אומר או "תוסיף את החזקה הזו של 2 לסכום" או "אל תוסיף אותה". למשל {% equation %}1101{% endequation %} מייצג את הסכום {% equation %}2^{3}+2^{2}+2^{0}=8+4+1=13{% endequation %}.

בשביל להבין איך אני מגדיר את הסדר לא חייבים לדעת אפילו את זה, רק את השיטה שבה אני עובר ממחרוזת אחת לבאה אחריה בתור: המחרוזת הראשונה היא זו שכולה 0 והאחרונה היא זו שכולה 1. כדי לעבור ממחרוזת אחת לבאה אחריה, עוברים על המספר מימין לשמאל. כל עוד הספרה שרואים היא 1, הופכים אותה ל-0; כשמגיעים לספרה 0, משנים אותה ל-1 ועוצרים. בואו נראה את זה קורה עבור שלושה קיוביטים:

{% equation %}000\to001\to010\to011\to100\to101\to110\to111{% endequation %}

עכשיו שיש לנו לכל {% equation %}n{% endequation %} בסיס למרחב הקיוביטים על {% equation %}n{% endequation %} איברים, וסדר על אברי הבסיס הזה, ברור איך אפשר לייצג כל מצב של המערכת בעזרת וקטור - וקטור שמכונה <strong>וקטור המצב</strong> (state vector) של המערכת. לדוגמא, עבור שני קיוביטים, המצב {% equation %}\alpha\left|00\right\rangle +\beta\left|01\right\rangle +\gamma\left|10\right\rangle +\delta\left|11\right\rangle {% endequation %} מיוצג בידי הוקטור

{% equation %}\left(\begin{array}{c} \alpha\\ \beta\\ \gamma\\ \delta \end{array}\right){% endequation %}

מעכשיו אני מרשה לעצמי לחשוב על מרחב של {% equation %}n{% endequation %} קיוביטים, כלומר על המכפלה הטנזורית {% equation %}\underset{n}{\underbrace{\mathbb{C}^{2}\otimes\ldots\otimes\mathbb{C}^{2}}}{% endequation %}, בתור {% equation %}\mathbb{C}^{2^{n}}{% endequation %}.

<h2>איך לייצג אופרטור אוניטרי שפועל על מספר קיוביטים?</h2>

עד עכשיו הכל היה נחמד וכיפי ועכשיו העניינים עומדים להסתבך נורא. לב העניין הוא בכך שבחישוב קוונטי, אנחנו בדרך כלל מפעילים פעולות על קיוביט בודד בכל פעם, או שני קיוביטים. על שלושה ויותר זה כבר די נדיר בפועל (למשל, כי מימוש של פעולה כזו במחשב קוונטי הוא מאתגר). זה לכשעצמו לא היה כזה נורא אם לא היינו רואים בפוסט הקודם שמצב קוונטי יכול להיות <strong>שזור</strong>, כלומר בנוי כך שלא ניתן לחשוב עליו בתור קיוביטים בודדים, ועדיין אני צריך להסביר איך משפיעה פעולה על קיוביט בודד על המצב השזור כולו. כמו שקורה כל פעם מחדש בחישוב קוונטי, נפנופי הידיים המילוליים שאני יכול להשתמש בהם פשוט עושים עבודה הרבה פחות טובה מהפרטים המתמטיים הטכניים.

אם יש לי מצב של {% equation %}n{% endequation %} קיוביטים, כל פעולה שאני מבצע עליו הולכת להיות אופרטור אוניטרי שמבחינה פורמלית פועל על כל הקיוביטים בבת אחת: {% equation %}U:\mathbb{C}^{2^{n}}\to\mathbb{C}^{2^{n}}{% endequation %}. אחד היתרונות הגדולים של חשיבה על איברים של מרחב וקטורי בתור וקטורי עמודה הוא בכך שעל אופרטורים אפשר לחשוב בתור <strong>מטריצות</strong> ואז הפעולה של האופרטור על וקטור מתורגמת לכפל של מטריצה בוקטור. אז אצלנו {% equation %}U{% endequation %} יהיה מטריצה; מטריצה אוניטרית מסדר {% equation %}2^{n}\times2^{n}{% endequation %}. השאלה היא איך לקבל את המטריצה הזו אם אני מתחיל מ"כן אני מפעיל פעולת {% equation %}X{% endequation %} על קיוביט מספר 3 מתוך 7". התשובה היא, איך לא, <strong>מכפלה טנזורית</strong>. ליתר דיוק, פעולה על מטריצות שמסומנת ב-{% equation %}\otimes{% endequation %} אבל נקראת <strong>מכפלת קרונקר</strong> (שאפשר גם לראות בתור מכפלה טנזורית במובן הרגיל אבל לא אכנס לזה בפוסט הזה כי זה לא באמת חשוב). וכדי להבין מה זו הפעולה הזו ואיך היא מתקשרת לענייננו, בואו נפשיל שרוולים ונעשה חישובים.

ראשית, בואו ניזכר מה זו הפעולה {% equation %}X{% endequation %}. תיארתי אותה כבר בעזרת מטריצה:

{% equation %}X=\left(\begin{array}{cc} 0 & 1\\ 1 & 0 \end{array}\right){% endequation %}

הפעולה שלה על אברי הבסיס היא זו:

{% equation %}X\left|0\right\rangle =\left|1\right\rangle {% endequation %}

{% equation %}X\left|1\right\rangle =\left|0\right\rangle {% endequation %}

עכשיו, כשיש לי מצב של שני קיוביטים ואני רוצה להפעיל פעולת {% equation %}X{% endequation %} על אחד מהם, אני צריך לציין על מי אני מפעיל אותה. דרך אפשרית אחת לסמן את זה שבה אשתמש היא להוסיף מספר למטה: {% equation %}X_{1}{% endequation %} הוא "הפעלה של {% equation %}X{% endequation %} על הקיוביט הראשון" ו-{% equation %}X_{2}{% endequation %} הוא "הפעלה של {% equation %}X{% endequation %} על הקיוביט השני". אינטואיטיבית, מה ש-{% equation %}X_{1}{% endequation %} אמור לעשות על מצב בסיס של שני קיוביטים הוא די ברור - מצב כזה הוא לא שזור, ולכן אפשר לחשוב ש-{% equation %}X{% endequation %} משנה את הקיוביט הראשון ולא נוגע בשני. כלומר:

{% equation %}X_{1}\left|00\right\rangle =\left|10\right\rangle {% endequation %}

{% equation %}X_{1}\left|01\right\rangle =\left|11\right\rangle {% endequation %}

{% equation %}X_{1}\left|10\right\rangle =\left|00\right\rangle {% endequation %}

{% equation %}X_{1}\left|11\right\rangle =\left|01\right\rangle {% endequation %}

האופן שבו אני מוצא את המטריצה מסדר {% equation %}4\times4{% endequation %} שמייצגת את האופרטור {% equation %}X_{1}{% endequation %} היא בדיוק בעזרת הרשימה למעלה: אם {% equation %}b_{1},\ldots,b_{n}{% endequation %} הוא הבסיס שבו אני משתמש עבור וקטורי קואורדינטות, ו-{% equation %}U{% endequation %} הוא אופרטור לינארי כלשהו, אז המטריצה שמייצגת את {% equation %}U{% endequation %} לפי הבסיס הזה היא כזו שבה העמודה ה-{% equation %}i{% endequation %} היא וקטור הקואורדינטות של {% equation %}U\left(b_{i}\right){% endequation %}. אז במטריצה של {% equation %}X_{1}{% endequation %} העמודה הראשונה תהיה וקטור הקואורדינטות של {% equation %}\left|10\right\rangle {% endequation %}, השניה תהיה וקטור הקואורדינטות של {% equation %}\left|11\right\rangle {% endequation %} וכן הלאה. נקבל:

{% equation %}X_{1}=\left(\begin{array}{cccc} 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\\ 1 & 0 & 0 & 0\\ 0 & 1 & 0 & 0 \end{array}\right){% endequation %}

זו מטריצה טיפה מבלבלת, אבל הכל מתבהר אם מחלקים אותה לארבעה בלוקים של {% equation %}2\times2{% endequation %}:

{% equation %}X_{1}=\left(\begin{array}{ccccc} 0 & 0 &  & 1 & 0\\ 0 & 0 &  & 0 & 1\\ \\ 1 & 0 &  & 0 & 0\\ 0 & 1 &  & 0 & 0 \end{array}\right){% endequation %}

אנחנו רואים ש-{% equation %}X_{1}{% endequation %} מורכבת משני בלוקים שכולם 0, ושני בלוקים שנראים כמו {% equation %}I{% endequation %}. או בסימון מקובל עבור מטריצת בלוקים:

{% equation %}X_{1}=\left(\begin{array}{cc} 0 & I\\ I & 0 \end{array}\right){% endequation %}

וזה נראה באופן חשוד כמו המטריצה של האופרטור {% equation %}X{% endequation %} בגרסה שלו שפועלת על קיוביט בודד:

{% equation %}X=\left(\begin{array}{cc} 0 & 1\\ 1 & 0 \end{array}\right){% endequation %}

רק עם מטריצת היחידה במקום 1. הדמיון הזה הוא כמובן לא מקרי <strong>בכלל</strong>.

בואו נראה מה קורה עם {% equation %}X_{2}{% endequation %}, בצורה זהירה ועם אותו חישוב פדנטי על אברי הבסיס:

{% equation %}X_{2}\left|00\right\rangle =\left|01\right\rangle {% endequation %}

{% equation %}X_{2}\left|01\right\rangle =\left|00\right\rangle {% endequation %}

{% equation %}X_{2}\left|10\right\rangle =\left|11\right\rangle {% endequation %}

{% equation %}X_{2}\left|11\right\rangle =\left|10\right\rangle {% endequation %}

שמוביל למטריצת הבלוקים

{% equation %}X_{2}=\left(\begin{array}{ccccc} 0 & 1 &  & 0 & 0\\ 1 & 0 &  & 0 & 0\\ \\ 0 & 0 &  & 0 & 1\\ 0 & 0 &  & 1 & 0 \end{array}\right){% endequation %}

או במילים אחרות, מטריצת הבלוקים

{% equation %}X_{2}=\left(\begin{array}{cc} X & 0\\ 0 & X \end{array}\right){% endequation %}

תראו מה קיבלנו עכשיו: משהו שנראה כמו מטריצת היחידה, {% equation %}I=\left(\begin{array}{cc} 1 & 0\\ 0 & 1 \end{array}\right){% endequation %}, רק עם {% equation %}X{% endequation %} במקום {% equation %}1{% endequation %}. מה הולך פה?

ובכן, הנה ה"סוד" הגדול: במקרה הראשון קיבלנו את המטריצה {% equation %}X\otimes I{% endequation %}, שמייצגת את הפעולה "הפעילו {% equation %}X{% endequation %} על האיבר השמאלי במכפלה הטנזורית ו-{% equation %}I{% endequation %} על האיבר הימני", ובמקרה השני קיבלנו את {% equation %}I\otimes X{% endequation %}, ונשאלת השאלה מה החוקיות מאחורי מכפלת קרונקר {% equation %}\otimes{% endequation %} שמניבה את המטריצות שקיבלנו.

במקרה הראשון, {% equation %}X\otimes I{% endequation %}, קיבלנו כזכור את {% equation %}\left(\begin{array}{cc} 0 & I\\ I & 0 \end{array}\right){% endequation %} שהיא "המטריצה {% equation %}X{% endequation %} כאשר מציבים {% equation %}I{% endequation %} במקום 1" ובמקרה השני, {% equation %}I\otimes X{% endequation %}, קיבלנו את {% equation %}\left(\begin{array}{cc} X & 0\\ 0 & X \end{array}\right){% endequation %} שהיא "המטריצה {% equation %}I{% endequation %} כאשר מציבים {% equation %}X{% endequation %} במקום 1". אם כן, ההשערה היא שבאופן כללי {% equation %}A\otimes B{% endequation %} הולכת להיות "המטריצה {% equation %}A{% endequation %} כאשר מציבים {% equation %}B{% endequation %} במקום 1". אבל במטריצות כלליות יש יותר דברים מאשר 1 ו-0; הרעיון הכללי הוא להחליף את הסקלר {% equation %}\lambda{% endequation %} במטריצה {% equation %}\lambda B{% endequation %}. במילים אחרות, אם 

{% equation %}A=\left(\begin{array}{cc} a_{11} & a_{12}\\ a_{21} & a_{22} \end{array}\right){% endequation %}

אז 

{% equation %}A\otimes B=\left(\begin{array}{cc} a_{11}B & a_{12}B\\ a_{21}B & a_{22}B \end{array}\right){% endequation %}

ובאופן כללי יותר, אם {% equation %}A{% endequation %} היא מטריצה כלשהי מסדר {% equation %}n\times m{% endequation %}

{% equation %}A=\left(\begin{array}{ccc} a_{11} & \cdots & a_{1m}\\ \vdots & \ddots & \vdots\\ a_{n1} & \cdots & a_{nm} \end{array}\right){% endequation %}

אז 

{% equation %}A\otimes B=\left(\begin{array}{ccc} a_{11}B & \cdots & a_{1m}B\\ \vdots & \ddots & \vdots\\ a_{n1}B & \cdots & a_{nm}B \end{array}\right){% endequation %}

אפשר גם לכתוב ביטוי מפורש ל-{% equation %}A\otimes B{% endequation %} שלא כמטריצת בלוקים אבל עזבו אותי מכאב הראש הזה, לכו להסתכל עליו בויקיפדיה (האנגלית, בעברית אין את זה כרגע).

<h2>למה כל זה עובד, בעצם?</h2>

אם כן, ראינו דוגמא קונקרטית אחת ואז את ההגדרה הכללית שתופסת אותה, אבל למה ההגדרה הכללית הזו עובדת? אני רוצה לחדד את מה שאני רוצה להוכיח: שאם {% equation %}u\otimes w{% endequation %} הוא איבר במכפלה טנזורית {% equation %}U\otimes W{% endequation %}, ו-{% equation %}A:U\to U,B:W\to W{% endequation %} הם שני אופרטורים, אז האופרטור {% equation %}A\otimes B{% endequation %} מקיים {% equation %}\left(A\otimes B\right)\left(u\otimes w\right)=Au\otimes Bw{% endequation %}.

בשביל להוכיח את זה, ראשית בואו נראה מה {% equation %}\otimes{% endequation %} עושה לזוג איברים {% equation %}u,w{% endequation %} כאשר מתייחסים לוקטורי הקואורדינטות. ניקח בסיסים {% equation %}\mathcal{B}_{U}=\left\{ e_{1},\ldots,e_{n}\right\} {% endequation %} ו-{% equation %}\mathcal{B}_{W}=\left\{ f_{1},\ldots,f_{m}\right\} {% endequation %} ונסמן ב-{% equation %}\mathcal{B}_{U\otimes W}{% endequation %} את הבסיס שהם משרים על המכפלה הטנזורית:

{% equation %}\mathcal{B}_{U\otimes W}=\left\{ e_{1}\otimes f_{1},e_{1}\otimes f_{2},\ldots,e_{1}\otimes f_{m},\ldots,e_{n}\otimes f_{m}\right\} {% endequation %}

כלומר, אני מסדר את האיברים של הבסיס כך שקודם יש את כל המכפלות שמערבות את {% equation %}e_{1}{% endequation %}, אחר כך כל המכפלות שמערבות את {% equation %}e_{2}{% endequation %} וכן הלאה.

עכשיו הטענה הפורמלית שאני רוצה לטעון היא:

{% equation %}\left[u\otimes w\right]_{\mathcal{B}_{U\otimes W}}=\left[u\right]_{\mathcal{\mathcal{B}_{U}}}\otimes\left[w\right]_{\mathcal{B}_{W}}{% endequation %}

מה הולך בשוויון הזה? אגף שמאל הוא וקטור הקואורדינטות של הטנזור {% equation %}u\otimes w{% endequation %} על פי הבסיס {% equation %}\mathcal{B}_{U\otimes W}{% endequation %}. אגף ימין הוא מכפלת <strong>קרונקר</strong> של שני <strong>וקטורים</strong>, הוקטור {% equation %}\left[u\right]_{\mathcal{\mathcal{B}_{U}}}{% endequation %} והוקטור {% equation %}\left[w\right]_{\mathcal{B}_{W}}{% endequation %}. מכיוון שוקטור הוא בעצם מטריצה עם עמודה אחת, מכפלת קרונקר מוגדרת היטב כאן: אם הכניסות של הוקטורים הן {% equation %}a_{1},\ldots,a_{n}{% endequation %} ו-{% equation %}b_{1},\ldots,b_{m}{% endequation %}, בהתאמה, אז הכניסות במכפלת הקרונקר הן {% equation %}a_{1}b_{1},a_{1}b_{2},a_{1}b_{3},\ldots,a_{2}b_{1},\ldots,a_{n}b_{m}{% endequation %} (כלומר - חוזרים שוב ושוב על הוקטור <strong>השני</strong> כשהוא מוכפל כל פעם בכניסה אחרת של הוקטור <strong>הראשון</strong>).

ולמה זה עובד? ובכן, די הינדסתי הכל כדי שזה יעבוד. אם {% equation %}\left[u\right]_{\mathcal{\mathcal{B}_{U}}}=\left(a_{1},a_{2},\ldots,a_{n}\right){% endequation %} ו-{% equation %}\left[w\right]_{\mathcal{B}_{W}}=\left(b_{1},b_{2},\ldots,b_{m}\right){% endequation %} (אני מרשה לעצמי לכתוב בשורה ולא בעמודה כי, נו, כמה אפשר) אז אני אכן מקבל

{% equation %}\left[u\right]_{\mathcal{\mathcal{B}_{U}}}\otimes\left[w\right]_{\mathcal{B}_{W}}=\left(a_{1}b_{1},a_{1}b_{2},a_{1}b_{3},\ldots,a_{2}b_{1},\ldots,a_{n}b_{m}\right){% endequation %}

וזה אגף ימין. באגף שמאל יש לנו וקטור שמייצג את {% equation %}u\otimes w{% endequation %} בבסיס המשולב {% equation %}\mathcal{B}_{U\otimes W}{% endequation %}. בשביל לדעת איך {% equation %}u\otimes w{% endequation %} נראה בבסיס הזה אנחנו כותבים כל וקטור באמצעות הבסיס המתאים, ואז "פותחים" את המכפלה הטנזורית עם כללי הוצאת הסקלר החוצה וחוק הפילוג שראינו בפוסט הקודם. כלומר:

{% equation %}u\otimes w=\left(\sum_{i=1}^{n}a_{i}e_{i}\right)\otimes\left(\sum_{j=1}^{m}b_{j}f_{j}\right)=\sum_{i,j}a_{i}b_{j}\left(e_{i}\otimes f_{j}\right){% endequation %}

כלומר, המקדם של {% equation %}e_{i}\otimes f_{j}{% endequation %} הוא {% equation %}a_{i}b_{j}{% endequation %}, ולכן אם אנחנו מסדרים את הבסיס לפי הסדר

{% equation %}e_{1}\otimes f_{1},e_{1}\otimes f_{2},\ldots,e_{1}\otimes f_{m},\ldots,e_{n}\otimes f_{m}{% endequation %}

אנחנו מקבלים בוקטור הקואורדינטות את סדרת הערכים

{% equation %}\left(a_{1}b_{1},a_{1}b_{2},a_{1}b_{3},\ldots,a_{2}b_{1},\ldots,a_{n}b_{m}\right){% endequation %}

וזה בדיוק מה שרצינו. יופי, כמו תמיד באלגברה לינארית, אנחנו עושים הרבה עבודה טכנית כדי לראות שמתקיים מה שנראה לנו אינטואיטיבית מובן מאליו.

עכשיו אפשר לחזור אל {% equation %}\left(A\otimes B\right)\left(u\otimes w\right)=Au\otimes Bw{% endequation %}, הנוסחה שמקשרת בין מכפלת קרונקר של אופרטורים (משמאל) למכפלה טנזורית של וקטורים, ולכן למכפלת קרונקר של וקטורים (מימין). אפשר להיכנס לנוסחה הזו ברמת האינדקס הבודד והכל יעבוד אבל זה יהיה ממש מבלבל, ואני רוצה שכן תהיה לנו אינטואיציה כלשהי לגבי מה שקורה כאן. אז בואו נבין למה הכניסה הראשונה בוקטור {% equation %}\left(A\otimes B\right)\left(u\otimes w\right){% endequation %} שווה לכניסה הראשונה בוקטור {% equation %}Au\otimes Bw{% endequation %} ומכאן זה יהיה די ברור.

הכניסה הראשונה היא המכפלה של <strong>השורה הראשונה</strong> של {% equation %}A\otimes B{% endequation %} בכל הוקטור {% equation %}u\otimes w{% endequation %}. מהי השורה הראשונה הזו? ובכן, אם {% equation %}A{% endequation %} הוא אופרטור {% equation %}n\times n{% endequation %} אז זה כזכור, 

{% equation %}A\otimes B=\left(\begin{array}{ccc} a_{11}B & \cdots & a_{1n}B\\ \vdots & \ddots & \vdots\\ a_{n1}B & \cdots & a_{nn}B \end{array}\right){% endequation %}

ולכן השורה הראשונה היא וקטור של אברי השורה הראשונה של {% equation %}A{% endequation %}, כאשר כל ערך כזה מוכפל ב<strong>כל</strong> ערכי השורה הראשונה של {% equation %}B{% endequation %} לפי הסדר. אם אברי {% equation %}B{% endequation %} הם מהצורה {% equation %}b_{i,j}{% endequation %} והסדר של {% equation %}B{% endequation %} הוא {% equation %}m\times m{% endequation %} אז נקבל שהשורה הראשונה הזו היא

{% equation %}a_{11}b_{11},a_{11}b_{12},\ldots,a_{11}b_{1m},a_{12}b_{11},\ldots,a_{1n}b_{1m}{% endequation %}

כלומר אפשר לחלק את הוקטור לקבוצות. כל קבוצה כוללת איבר אחד מהשורה של {% equation %}A{% endequation %}, כפול כל השורה של {% equation %}B{% endequation %}, וחוזר חלילה.

עכשיו, מה האיברים של {% equation %}u\otimes w{% endequation %} כבר ראינו לפני זה: זה וקטור שבו הכניסות גם כן מחולקות לקבוצות: האיבר הראשון של {% equation %}u{% endequation %} כפול כל האיברים של {% equation %}w{% endequation %}, וחוזר חלילה. בואו נסמן אותן באותיות שונות מאלו שבהן השתמשנו קודם: אם {% equation %}u=\left(\alpha_{1},\ldots,\alpha_{n}\right){% endequation %} ו-{% equation %}w=\left(\beta_{1},\ldots,\beta_{m}\right){% endequation %} (אלו ה-{% equation %}n,m{% endequation %} של {% equation %}A,B{% endequation %} כי {% equation %}A{% endequation %} הוא הרי אופרטור שפועל על {% equation %}u{% endequation %} ו-{% equation %}B{% endequation %} אופרטור שפועל על {% equation %}w{% endequation %}), אז אברי {% equation %}u\otimes w{% endequation %} הם

{% equation %}\alpha_{1}\beta_{1},\alpha_{1}\beta_{2},\ldots,\alpha_{1}\beta_{m},\alpha_{2}\beta_{1},\ldots,\alpha_{n}\beta_{m}{% endequation %}

לכן כשאני כופל את השורה הראשונה של {% equation %}A\otimes B{% endequation %} בוקטור {% equation %}u\otimes w{% endequation %} אני מקבל סכום שאני יכול לחלק באופן הבא:

{% equation %}\left(a_{11}b_{11}\alpha_{1}\beta_{1}+\ldots+a_{11}b_{1m}\alpha_{1}\beta_{m}\right)+\ldots+a_{1n}b_{1m}\alpha_{n}\alpha_{m}{% endequation %}

מהקבוצה הראשונה אפשר להוציא את {% equation %}a_{11}\alpha_{1}{% endequation %} ולקבל את הסכום

{% equation %}a_{11}\alpha_{1}\left(b_{11}\beta_{1}+\ldots+b_{1m}\beta_{m}\right){% endequation %}

כאן האיבר שבסוגריים הוא פשוט הכניסה הראשונה במכפלה {% equation %}Bw{% endequation %}. והאיבר הזה הולך לחזור על עצמו שוב ושוב לאורך הסכום של השורה הראשונה של {% equation %}A\otimes B{% endequation %} שמוכפלת ב-{% equation %}u\otimes w{% endequation %}. לכן אם נקבץ איברים נקבל שהסכום כולו הוא

{% equation %}\left(a_{11}\alpha_{1}+\ldots+a_{1n}\alpha_{n}\right)\left(b_{11}\beta_{1}+\ldots+b_{1m}\beta_{m}\right){% endequation %}

כלומר קיבלנו בדיוק את המכפלה של הכניסה הראשונה של {% equation %}Au{% endequation %} בכניסה הראשונה של {% equation %}Bw{% endequation %}.

מה יקרה עבור השורה השניה? שווה להסתכל <strong>שוב</strong> על {% equation %}A\otimes B{% endequation %}:

{% equation %}A\otimes B=\left(\begin{array}{ccc} a_{11}B & \cdots & a_{1n}B\\ \vdots & \ddots & \vdots\\ a_{n1}B & \cdots & a_{nn}B \end{array}\right){% endequation %}

השורה השניה של המטריצה הזו כוללת את אותו {% equation %}a_{11}{% endequation %} מקודם, כשהוא מוכפל בשורה <strong>השניה</strong> של {% equation %}B{% endequation %}. לכן מה שנקבל הוא את הכניסה <strong>הראשונה</strong> של {% equation %}Au{% endequation %} מוכפלת בכניסה <strong>השניה</strong> של {% equation %}Bw{% endequation %}. אם שרדתם את כל ענייני הטנזורים הללו זה אמור להיראות מוכר - ככה נבנית המכפלה הטנזורית של שני הוקטורים {% equation %}Au{% endequation %} ו-{% equation %}Bw{% endequation %}: קודם כל הכניסה <strong>הראשונה</strong> של {% equation %}Au{% endequation %} כשהיא מוכפלת בכל הכניסות של {% equation %}Bw{% endequation %} לפי הסדרה, אחר כך הכניסה השניה של {% equation %}Au{% endequation %} וחוזר חלילה. זה בדיוק מה שנשיג כשנעבור על השורות של {% equation %}A\otimes B{% endequation %} ונכפיל ב-{% equation %}u\otimes w{% endequation %}.

האם אפשר לעשות את זה יותר פורמלי ועם אינדקסים וכל זה? כמובן. זה בדיוק מסוג הדברים שאוהבים להשאיר כתרגיל כי הם וידוא טכני משעמם שבפני עצמו לא מוסיף לאינטואיציה. אני מעדיף להסתפק בהסבר הלא מדויק. 
