---
id: 1510
title: "מכפלות פנימיות"
date: 2012-02-06 13:28:00
layout: post
categories: 
  - אלגברה לינארית
tags: 
  - בסיס אורתונורמלי
  - מכפלה פנימית
  - תהליך גרם-שמידט
---
בפוסט הקודם הצגתי את מושג המכפלה הסקלרית, והפעם אני רוצה לקפוץ ישר להכללה בלי לתת יותר מדי מוטיבציה. אז בואו נחזור לדבר על ההקשר הרגיל של אלגברה לינארית - מרחבים וקטוריים מעל שדה {% equation %}\mathbb{F}{% endequation %}. נתחיל מלדבר על המרחב {% equation %}\mathbb{F}^{n}{% endequation %}. וקטור ממוצע בו נראה כך: {% equation %}x=\left(x_{1},x_{2},\dots,x_{n}\right){% endequation %} כאשר {% equation %}x_{i}\in\mathbb{F}{% endequation %}. בהינתן וקטור אחר {% equation %}y=\left(y_{1},\dots,y_{n}\right){% endequation %}, <strong>נגדיר</strong> את המכפלה הסקלרית שלהם להיות {% equation %}x\cdot y=\sum_{i=1}^{n}x_{i}y_{i}{% endequation %}. כלומר, כופלים כל "רכיב" לחוד, וסוכמים את התוצאה.

יפה. הגדרנו פונקציה חשובה ושימושית בהקשרים רבים ושונים שלא אציג כעת. אלא שלפונקציה הזו יש הכללה רבת עוצמה ביותר, שפותחת פתח לתחום נרחב באלגברה לינארית שטרם נגעתי בו - מרחבי מכפלה פנימית - ולכן אני רוצה להבין קצת איך הפונקציה הזו מתנהגת.

האבחנה הראשונה היא שהכפל הזה מקיים דיסטריביוטיביות: {% equation %}\left(x+y\right)\cdot z=x\cdot z+y\cdot z{% endequation %} (בדקו זאת - זה נובע ישירות מההגדרה), אבל כבר צריך להיזהר כאן - החיבור שבאגף שמאל הוא חיבור וקטורים, בעוד שהחיבור באגף ימין הוא חיבור סקלרים, מכיוון שמכפלה סקלרית לוקחת זוג וקטורים והופכת אותו לסקלר. לכן אין שום משמעות לביטוי כמו {% equation %}x\cdot y\cdot z{% endequation %}: שכן {% equation %}x\cdot y{% endequation %} הוא סקלר, ולכן אי אפשר לכפול אותו סקלרית ב-{% equation %}z{% endequation %}. מה שכן, אם {% equation %}\lambda{% endequation %} הוא סקלר, אז קל לראות ש-{% equation %}\lambda\times\left(x\cdot y\right)=\left(\lambda\otimes x\right)\cdot y{% endequation %}. כאן מופיעים שלושה כפלים שונים בו זמנית ולכן הרשיתי לעצמי לסמן אותם בסימונים מוזרים: {% equation %}\cdot{% endequation %} היא המכפלה הסקלרית (של שני וקטורים), {% equation %}\times{% endequation %} היא מכפלה של שני סקלרים ב-{% equation %}\mathbb{F}{% endequation %} ו-{% equation %}\otimes{% endequation %} היא המכפלה של סקלר בוקטור. הערבוב הגדול הזה של סוגי המכפלות השונות הוא כנראה אחת מהסיבות שבגללן נשתמש בעיקר בסימון {% equation %}\left\langle x,y\right\rangle {% endequation %} כדי לתאר מכפלה פנימית של וקטורים.

פעולה כזו, שלוקחת וקטורים ומחזירה סקלר, אינה חדשה לנו - כבר ראינו בעבר פוסטים על <a href="http://www.gadial.net/?p=1408">פונקציונלים לינאריים</a> שהן טרנספורמציות לינארית שלוקחות וקטור ומחזירות סקלר, וגם ראינו ש<a href="http://www.gadial.net/?p=1418">דטרמיננטה</a> היא טרנספורמציה מולטי-לינארית שלוקחת וקטורים ומחזירה סקלר. מכפלה סקלרית היא מה שנקרא פונקציה בילינארית ("דו-לינארית") כי היא על שני משתנים (חשבו על הפונקציה {% equation %}f\left(x,y\right)=x\cdot y{% endequation %}).

תכונה אחת שיש למכפלה סקלרית ולא קיימת אצל חלק מהפונקציות הבילינאריות היא <strong>סימטריה</strong>: {% equation %}x\cdot y=y\cdot x{% endequation %}. טבעי יהיה להכניס גם את התכונה הזו להכללה שלנו (ומן הסתם נראה בהמשך כיצד היא מסייעת).

התכונה האחרונה היא הבעייתית ביותר. הבה ונשאל את עצמנו מה קורה ב-{% equation %}\mathbb{R}{% endequation %} כאשר אנחנו כופלים וקטור סקלרית עם עצמו. מכיוון שהזווית בינו לעצמו היא 0, נקבל פשוט {% equation %}\left|v\right|^{2}{% endequation %}, כלומר את האורך של {% equation %}\left|v\right|{% endequation %} בריבוע. לכן אנחנו יכולים לצפות שהאורך של וקטור תמיד יהיה נתון על ידי שורש של המכפלה הפנימית שלו בעצמו. עם מושג של אורך אפשר לעשות דברים נפלאים, אבל כדי שאפשר יהיה לעשות אותם האורך צריך להיות מה שאנחנו מצפים שהוא יהיה - מספר ממשי, וכזה שגדול מאפס אם הוקטור שונה מאפס (שוב, קשה להצדיק את זה כרגע בלי שתראו מה עושים עם זה, אבל סמכו עלי שזהו המצב).

לרוע המזל, מעל שדה {% equation %}\mathbb{F}{% endequation %} כללי אין שום סיבה להניח שנקבל ש-{% equation %}\left|v\right|^{2}{% endequation %} הוא בכלל איבר של {% equation %}\mathbb{R}{% endequation %}, לא כל שכן איבר חיובי ששונה מאפס אם {% equation %}v{% endequation %} שונה מאפס. זה מוביל אותנו להגבלה המצערת הראשונה שלנו - אנחנו הולכים להגדיר מכפלה פנימית אך ורק במקרים שבהם {% equation %}\mathbb{F=R}{% endequation %} או {% equation %}\mathbb{F=C}{% endequation %}, ושום מקרה אחר. היינו יכולים לנסות ולעשות את זה גם במקרים אחרים, אבל התיאוריה פשוט לא הייתה עובדת. זו דוגמה לסיטואציה במתמטיקה שבה אנחנו צריכים להיות אבסטרקטיים <strong>פחות</strong>, כי תוצאות יפות וחזקות ספציפיות תקפות רק במקרה פרטי מסויים.

עכשיו אני יכול להציג את ההכללה סוף סוף. אם {% equation %}V{% endequation %} הוא מרחב וקטורי מעל {% equation %}\mathbb{R}{% endequation %}, אז <strong>מכפלה פנימית</strong> היא פונקציה {% equation %}\left\langle \cdot,\cdot\right\rangle :V\times V\to\mathbb{R}{% endequation %} אשר מקיימת:
<ol>
	<li> {% equation %}\left\langle x+y,z\right\rangle =\left\langle x,z\right\rangle +\left\langle y,z\right\rangle {% endequation %} לכל {% equation %}x,y,z\in V{% endequation %}.</li>
	<li> {% equation %}\left\langle \lambda x,y\right\rangle =\lambda\left\langle x,y\right\rangle {% endequation %} לכל {% equation %}x,y\in V{% endequation %} ו-{% equation %}\lambda\in\mathbb{R}{% endequation %}.</li>
	<li> {% equation %}\left\langle x,y\right\rangle =\left\langle y,x\right\rangle {% endequation %} לכל {% equation %}x,y\in V{% endequation %}.</li>
	<li> {% equation %}\left\langle x,x\right\rangle \ge0{% endequation %} לכל {% equation %}x\in V{% endequation %} ו-{% equation %}x=0\iff\left\langle x,x\right\rangle =0{% endequation %}.</li>
</ol>
שימו לב שהסימטריה נותנת לי מייד תכונות כמו {% equation %}\left\langle x,y+z\right\rangle =\left\langle x,y\right\rangle +\left\langle x,z\right\rangle {% endequation %} ו-{% equation %}\left\langle x,\lambda y\right\rangle =\lambda\left\langle x,y\right\rangle {% endequation %}.

טוב, אז הגדרנו הגדרה. כדי שהיא תהיה מעניינת, צריך להראות שיש לה באמת דוגמאות לא טריוויאליות, חוץ מהמכפלה הסקלרית שכבר ראינו. הנה הדוגמה הקלאסית שקופצת לי לראש: נסתכל במרחב {% equation %}V=\mbox{C}\left[0,1\right]{% endequation %} - מרחב הפונקציות {% equation %}f:\left[0,1\right]\to\mathbb{R}{% endequation %} ({% equation %}\left[0,1\right]{% endequation %} הוא הקטע הסגור שכולל את כל הממשיים בין 0 ל-1 כולל) שהן רציפות (אני מניח שהמושג מוכר לקוראים - אם לא, אני ממליץ לקרוא על פונקציות רציפות; ואם לא, לא סוף העולם - זו רק דוגמה). לא קשה לראות שזה אכן מרחב וקטורי מעל {% equation %}\mathbb{R}{% endequation %}. את המכפלה הפנימית נגדיר כך:

{% equation %}\left\langle f,g\right\rangle =\int_{0}^{1}f\left(x\right)g\left(x\right)dx{% endequation %}

קל למדי לראות שתכונות 1-3 מתקיימות, בזכות תכונות הלינאריות של האינטגרל. תכונה 4 היא מאתגרת קצת יותר - אנחנו רוצים לטעון שאם {% equation %}f\not\equiv0{% endequation %} (כאן {% equation %}0{% endequation %} היא הפונקציה שמחזירה 0 לכל אברי {% equation %}\left[0,1\right]{% endequation %}) אז {% equation %}\int_{0}^{1}f^{2}\left(x\right)dx&gt;0{% endequation %}. כאן הרציפות של {% equation %}f{% endequation %} קריטית; אם היינו מרשים ל-{% equation %}f{% endequation %} להיות לא רציפה, ולו בנקודה אחת, היינו מקבלים פונקציות שונות מאפס שהמכפלה הפנימית שלהן עם עצמן היא 0 (פשוט תבחרו פונקציה שהיא 0 בכל מקום חוץ מבנקודת האי-רציפות, ושם היא תהיה 1 למשל).

אם כן, {% equation %}f{% endequation %} רציפה. בנוסף, {% equation %}f^{2}\left(x\right)\ge0{% endequation %} לכל {% equation %}x\in\left[0,1\right]{% endequation %}, ולכן {% equation %}\int_{0}^{1}f^{2}\left(x\right)dx{% endequation %} חיובי או אפס. מה שאני הולך לעשות עכשיו הוא פשוט לטעון שיש סביבה כלשהי שבה כל ערכי {% equation %}f{% endequation %} גדולים מאפס ולכן השטח שלה חיובי: מכיוון ש-{% equation %}f{% endequation %} רציפה ושונה מאפס, אז קיים {% equation %}c\in\left[0,1\right]{% endequation %} כך ש-{% equation %}f\left(c\right)&gt;0{% endequation %}. מכיוון שהיא רציפה, אז עבור {% equation %}\varepsilon=\frac{f\left(c\right)}{2}{% endequation %} קיימת {% equation %}\delta&gt;0{% endequation %} כך ש-{% equation %}\left|f\left(x\right)-f\left(c\right)\right|&lt;\varepsilon{% endequation %} אם {% equation %}\left|x-c\right|&lt;\delta{% endequation %}. לכן יש לנו קטע, מאורך {% equation %}\delta{% endequation %} לכל הפחות, שלכל הנקודות בו מתקיים {% equation %}f\left(x\right)&lt;\varepsilon-f\left(c\right)=\frac{1}{2}f\left(c\right){% endequation %} (למה מאורך {% equation %}\delta{% endequation %} ולא {% equation %}2\delta{% endequation %}? כי {% equation %}c{% endequation %} יכולה להיות גם בקצוות). מכאן שהאינטגרל מקיים {% equation %}\int_{0}^{1}f^{2}\left(x\right)dx\ge\delta\cdot\left(\frac{1}{2}f\left(c\right)\right)^{2}&gt;0{% endequation %} וסיימנו.

לפני שאמשיך, אני רוצה לדבר על מה קורה מעל {% equation %}\mathbb{C}{% endequation %}. אפשר היה לקוות שנוכל לקחת את ההגדרה שלעיל ופשוט להחליף כל מופע של {% equation %}\mathbb{R}{% endequation %} ב-{% equation %}\mathbb{C}{% endequation %}, אבל לרוע המזל זה לא עובד. בואו ונראה למה:

{% equation %}\left\langle i,i\right\rangle =i\left\langle 1,i\right\rangle =i\left\langle i,1\right\rangle =i^{2}\left\langle 1,1\right\rangle =-\left\langle 1,1\right\rangle {% endequation %}

ומה קיבלנו כאן? מצד אחד, {% equation %}\left\langle 1,1\right\rangle &gt;0{% endequation %} כי {% equation %}1\ne0{% endequation %} ותכונה 4; מצד שני, זה אומר ש-{% equation %}\left\langle i,i\right\rangle {% endequation %} חייב להיות שלילי, בסתירה לתכונה 4. משהו נשתבש בהגדרות שלנו, ומסתבר שהתכונה הסוררת היא 3, וניתן לתקנה די בקלות, אם כי במחיר של אובדן חלק מה"טבעיות" של ההגדרה (אחרי שמתרגלים מבינים שזה כן טבעי). בואו נזכור שאם {% equation %}z=a+bi{% endequation %} הוא מספר מרוכב ({% equation %}a,b\in\mathbb{R}{% endequation %}) אז ה<strong>צמוד</strong> שלו מוגדר כ-{% equation %}\overline{z}=\overline{a+bi}=a-bi{% endequation %}. את תכונה 3 נגדיר כעת מחדש כך: {% equation %}\left\langle x,y\right\rangle =\overline{\left\langle y,x\right\rangle }{% endequation %} לכל {% equation %}x,y\in V{% endequation %}. זה הכל, ובמקרה שאנחנו מעל השדה {% equation %}\mathbb{R}{% endequation %} לא שינינו כלום כי {% equation %}\overline{\left\langle x,y\right\rangle }=\left\langle x,y\right\rangle {% endequation %} עבור מספרים ממשיים. לתכונה 3 המשודרגת קוראים <strong>הרמיטיות</strong> (על שם המתמטיקאי הרמיט). שימו לב שבמקרה של {% equation %}\mathbb{C}{% endequation %}, תכונה 4 היא משמעותית חזקה יותר מאשר קודם - אם {% equation %}\left\langle x,x\right\rangle \ge0{% endequation %} זה בפרט אומר ש-{% equation %}\left\langle x,x\right\rangle {% endequation %} הוא מספר ממשי (מספרים מרוכבים לא ממשיים לא ניתנים להשוואה עם אפס).

מה שכן, עלינו להיות טיפה זהירים. אמנם, עדיין מתקיים ש-{% equation %}\left\langle \lambda x,y\right\rangle =\lambda\left\langle x,y\right\rangle {% endequation %}, אבל לחלוטין לא מתקיים {% equation %}\left\langle x,\lambda y\right\rangle =\lambda\left\langle x,y\right\rangle {% endequation %}; אם נשתמש בהרמיטיות נקבל {% equation %}\left\langle x,\lambda y\right\rangle =\overline{\lambda}\left\langle x,y\right\rangle {% endequation %}.

מעכשיו אמשיך לפתח את כל התורה עבור {% equation %}\mathbb{C}{% endequation %} בלבד, והסימן של הצמוד יופיע לא מעט, אבל זכרו שאפשר לעשות את אותם דברים בדיוק שאעשה כאן גם עבור {% equation %}\mathbb{R}{% endequation %} ופשוט להסיר את הצמוד.

מכפלה סקלרית על {% equation %}\mathbb{C}^{n}{% endequation %} נראית כמעט כמו מכפלה סקלרית "רגילה", רק שצריך להכניס את הצמוד לתמונה אחרת נאבד את ההרמיטיות. כלומר, אם {% equation %}x,y\in\mathbb{C}^{n}{% endequation %} אז נגדיר {% equation %}x\cdot y=\sum_{i=1}^{n}x_{i}\overline{y_{i}}{% endequation %}, וזו תהיה ההגדרה שנעבוד איתה מעתה למכפלה סקלרית.

בואו ניגש לעבודה האמיתית - נתחיל מלהבין איך נראות <strong>כל</strong> המכפלות הפנימיות על מרחב וקטורי {% equation %}V{% endequation %} שהוא סוף-ממדי (במרחבים אינסוף ממדיים הסיפור, כרגיל, מסובך פי כמה וכמה). יהי אם כן {% equation %}V{% endequation %} מרחב וקטורי כלשהו ממימד {% equation %}n{% endequation %} ו-{% equation %}B=\left\{ b_{1},\dots,b_{n}\right\} {% endequation %} בסיס סדור כלשהו שלו. כזכור, לכל {% equation %}v\in V{% endequation %} אני מגדיר <strong>וקטור קואורדינטות</strong> {% equation %}\left[v\right]_{B}=\left(\lambda_{1},\dots,\lambda_{n}\right){% endequation %} כך ש-{% equation %}\sum\lambda_{i}b_{i}=v{% endequation %} (מכיוון ש-{% equation %}B{% endequation %} בסיס אז קיים צירוף לינארי של אבריו שנותן את {% equation %}v{% endequation %} והוא יחיד, כך שההגדרה הגיונית). כעת אפשר להגדיר מכפלה פנימית {% equation %}\left\langle x,y\right\rangle _{B}{% endequation %} באופן הבא: {% equation %}\left\langle x,y\right\rangle _{B}=\left[x\right]_{B}\cdot\left[y\right]_{B}{% endequation %}. כלומר: אנחנו לוקחים את וקטורי הקואורדינטות של {% equation %}x,y{% endequation %} וכופלים אותם מכפלה סקלרית "רגילה" ב-{% equation %}\mathbb{C}^{n}{% endequation %}. הגדרה טבעית למדי, יש להודות, והיא דוגמה לרעיון נפוץ במתמטיקה - אם יש לך שני מבנים שהם איזומורפיים (במקרה שלנו, {% equation %}V{% endequation %} איזומורפי ל-{% equation %}\mathbb{C}^{n}{% endequation %}, כשכל בסיס {% equation %}B{% endequation %} קובע איזומורפיזם אחר) אפשר להשתמש באיזומורפיזם ובפעולה שכבר קיימת באחד מהמבנים כדי להגדיר פעולה במבנה השני (הפעולה תיקבע גם על פי הפעולה על המבנה הראשון, אבל גם על פי האיזומורפיזם עצמו - שני איזומורפיזמים שונים יתנו פעולות שונות).

אם כן, ראינו שאפשר לקבל מכפלות פנימיות על כל מרחב {% equation %}V{% endequation %} סוף-ממדי מעל {% equation %}\mathbb{C}{% endequation %} באמצעות בסיס. אני רוצה לטעון שגם ההפך נכון - ש<strong>כל</strong> מכפלה פנימית על על מרחב וקטורי סוף ממדי {% equation %}V{% endequation %} ניתן להציג בתור מכפלה סקלרית ביחס לבסיס מסוים. במקום להוכיח את זה מייד, אני רוצה לעצור לרגע ולהבין איך נראים בסיסים כאלו.

ובכן, נניח שיש לי בסיס {% equation %}B{% endequation %} והגדרתי מכפלה פנימית {% equation %}\left\langle \cdot,\cdot\right\rangle {% endequation %} באמצעות {% equation %}B{% endequation %}. השאלה הראשונה היא מהם {% equation %}\left\langle b_{i},b_{j}\right\rangle {% endequation %} כאשר {% equation %}b_{i},b_{j}{% endequation %} הם עצמם איברי {% equation %}B{% endequation %}. התשובה פשוטה: {% equation %}\left[b_{i}\right]_{B}=\left(0,0,\dots,1,\dots,0\right){% endequation %} כאשר ה-1 היחיד הוא בקואורדינטה ה-{% equation %}i{% endequation %}-ית, ולכן {% equation %}\left\langle b_{i,},b_{j}\right\rangle =0{% endequation %} אם {% equation %}i\ne j{% endequation %} ו-{% equation %}\left\langle b_{i},b_{i}\right\rangle =1{% endequation %} (בקיצור אפשר לכתוב זאת {% equation %}\left\langle b_{i},b_{j}\right\rangle =\delta_{ij}{% endequation %}). בסיס שאיבריו מקיימים תכונות אלו (ביחס למכפלה פנימית מסויימת) נקרא <strong>בסיס אורתונורמלי</strong> (ביחס לאותה מכפלה פנימית). מבחינה גיאומטרית נכון לחשוב עליו כעל בסיס שהוקטורים השונים בו מאונכים - <strong>אורתוגונליים - </strong>זה לזה (זו משמעות {% equation %}\left\langle b_{i},b_{j}\right\rangle =0{% endequation %}) ואורכם הוא 1 (זו משמעות {% equation %}\left\langle b_{i},b_{i}\right\rangle =1{% endequation %}) - אסביר זאת יותר בפוסט הבא שבו אדבר על ההיבטים הגיאומטריים של מרחבי מכפלה פנימית.

בואו נניח עתה שיש לנו מרחב מכפלה פנימית {% equation %}V{% endequation %} עם מכפלה {% equation %}\left\langle \cdot,\cdot\right\rangle {% endequation %} שלאו דווקא התקבלה מתוך בסיס מסויים. כל מה שאני יודע עליה הוא שהיא מקיימת את תכונות 1-4. אם אני אצליח למצוא בסיס {% equation %}B{% endequation %} של {% equation %}v{% endequation %} שמקיים {% equation %}\left\langle b_{i},b_{j}\right\rangle =\delta_{ij}{% endequation %} - כלומר, בסיס אורתונורמלי ביחס למכפלה הפנימית הזו - אני טוען שינבע מכך שהמכפלה הפנימית היא בדיוק {% equation %}\left\langle \cdot,\cdot\right\rangle _{B}{% endequation %}. מדוע? ובכן, נניח ש-{% equation %}x,y{% endequation %} הם שני וקטורים כלשהם ב-{% equation %}V{% endequation %} וניתן להציג אותם כ-{% equation %}x=\sum x_{i}b_{i}{% endequation %} ו-{% equation %}y=\sum y_{i}b_{i}{% endequation %} כאשר {% equation %}x_{i},y_{i}{% endequation %} הם סקלרים. אז מתקיים:

{% equation %}\left\langle x,y\right\rangle =\left\langle \sum x_{i}b_{i},\sum y_{i}b_{j}\right\rangle =\sum_{i,j}x_{i}\overline{y_{j}}\left\langle b_{i},b_{j}\right\rangle =\sum_{i=1}^{n}x_{i}\overline{y_{i}}=\left[x\right]_{B}\cdot\left[y\right]_{B}{% endequation %}

המעבר השני מתבסס על תכונות 1-3 של המכפלה הפנימית, והמעבר שאחריו נובע מכך ש-{% equation %}B{% endequation %} הוא בסיס אורתונורמלי.

אם תחשבו על זה, מה שקורה כאן די דומה למה שקרה בלכסון מטריצות. שם חיפשנו בסיס שבו טרנספורמציה לינארית מסויימת היא "פשוטה" - מיוצגת על ידי מטריצה אלכסונית; כאן אנחנו רואים שאם יש לנו מכפלה פנימית אז יש בסיס - בסיס אורתונורמלי - שבו היא "פשוטה" - ניתן לחשוב עליה כעל מכפלה סקלרית (השיא כמובן יהיה בשילוב של שני הדברים הללו - בסיס אורתונורמלי שגם מלכסן טרנספורמציה מסויימת; זה יהיה מה שנקרא <strong>משפט הפירוק הספקטרלי</strong> והוא אחד מהגביעים הקדושים של סדרת הפוסטים הזו).

הבה ונחדד את הנקודה הזו על ידי כך שנראה שכל מכפלה פנימית במרחב ממימד סופי אכן ניתנת לייצוג באופן מסויים באמצעות מטריצה. בואו ניקח מכפלה פנימית כלשהי {% equation %}\left\langle \cdot,\cdot\right\rangle {% endequation %} ובסיס {% equation %}B{% endequation %} כלשהו למרחב; ובואו נגדיר מטריצה {% equation %}B{% endequation %} על ידי {% equation %}B_{ij}=\left\langle b_{j},b_{i}\right\rangle {% endequation %} (שימו לב להיפוך סדר האינדקסים!). כבר ראינו ש-{% equation %}\left\langle x,y\right\rangle =\sum_{i,j}x_{i}\overline{y_{j}}\left\langle b_{i},b_{j}\right\rangle {% endequation %}; דרך אחרת לכתוב את המשוואה הזו היא בתור {% equation %}\left\langle x,y\right\rangle =y^{*}Bx{% endequation %} כאשר {% equation %}y^{*}{% endequation %} מסמן הצמדה של כל רכיבי {% equation %}y{% endequation %} (אני לא כותב {% equation %}\overline{y}{% endequation %} כי לפעמים פשוט משתמשים בקו עליון כדי להבהיר ש-{% equation %}y{% endequation %} הוא וקטור). אם כן, בסיס אורתונורמלי הוא בסיס שבו המכפלה הפנימית מיוצגת על ידי מטריצת היחידה (ובסיס אורתוגונלי - שבו כל שני וקטורים הם אורתוגונליים אבל לא בהכרח מקיימים {% equation %}\left\langle b_{i},b_{i}\right\rangle =1{% endequation %} - הוא בסיס שבו המטריצה המייצגת היא אלכסונית).

נשאלת אם כן השאלה - האם לכל מרחב מכפלה פנימית סוף ממדי קיים בסיס אורתונורמלי? התשובה חיובית, ולא רק שהיא חיובית - ההוכחה שלה קונסטרוקטיבית לגמרי. אנחנו נראה כיצד ניתן להתחיל מבסיס כלשהו ל-{% equation %}V{% endequation %} ולבנות מתוכו בסיס אורתונורמלי - לאלגוריתם הזה קוראים "תהליך גרם-שמידט".

נתחיל בשאלה תמימה. נניח ש-{% equation %}B=\left\{ b_{1},\dots,b_{n}\right\} {% endequation %} הוא בסיס למרחב וקטורי {% equation %}B{% endequation %}, ו-{% equation %}v\in V{% endequation %} הוא וקטור תמים כלשהו ב-{% equation %}V{% endequation %}. אנחנו יודעים ש-{% equation %}v=\sum\lambda_{i}b_{i}{% endequation %} ושצירוף לינארי זה הוא יחיד. אבל האם אנחנו יודעים למצוא את {% equation %}\lambda_{i}{% endequation %} לכל {% equation %}i{% endequation %}?

השאלה הזו ערמומית הרבה יותר משנדמה במבט ראשון. נסו שניה לפתור אותה ותראו אילו בעיות מתעוררות מייד. בכלל לא ברור לנו איך {% equation %}V{% endequation %} מיוצג; איך {% equation %}v{% endequation %} נתון לנו; מה בדיוק אנחנו יודעים על {% equation %}B{% endequation %}. במקרה שבו {% equation %}V=\mathbb{C}^{n}{% endequation %} עוד אפשר לעשות משהו - כל הוקטורים הם סדרות סופיות של מרוכבים, ולמצוא את ה-{% equation %}\lambda_{i}{% endequation %} -ים דורש לפתור מערכת של משוואות לינאריות מעל המרוכבים. אבל במרחבים כלליים יותר, שבהם אין לנו איזומורפיזם ברור ל-{% equation %}\mathbb{C}^{n}{% endequation %}, פתאום השאלה נהיית בעייתית ותלויה מאוד בייצוג שיש לנו של {% equation %}V{% endequation %}. ובכלל, לפתור מערכת משוואות זה גם כן לא הדבר הכי אינפורמטיבי בעולם.

אבל, אם {% equation %}B{% endequation %} הוא בסיס <strong>אורתונורמלי</strong> ביחס למכפלה פנימית שאנו יודעים לחשב, פתאום העסק הופך לפשוט בצורה בלתי רגילה. כי בואו נראה מה קורה כשכופלים את {% equation %}v{% endequation %} ב-{% equation %}b_{i}{% endequation %}:

{% equation %}\left\langle v,b_{i}\right\rangle =\left\langle \sum\lambda_{j}b_{j},b_{i}\right\rangle =\sum\lambda_{j}\left\langle b_{j},b_{i}\right\rangle =\lambda_{i}{% endequation %}

כל הגורמים {% equation %}\lambda_{j}\left\langle b_{j},b_{i}\right\rangle {% endequation %} עבור {% equation %}j\ne i{% endequation %} מתאפסים ואנחנו נשארים בדיוק עם המכפלה הפנימית של {% equation %}v{% endequation %} עם {% equation %}b_{i}{% endequation %}. חשבו על זה בתור <strong>הטלה</strong> של {% equation %}v{% endequation %} על מערכת צירים, כאשר כל ציר מוגדר על ידי אחד מ-{% equation %}b_{i}{% endequation %}-ים. מה שאנחנו רואים כאן הוא שכדי לדעת את הקואורדינטה ה-{% equation %}i{% endequation %} של {% equation %}v{% endequation %} בבסיס האורתונורמלי {% equation %}B{% endequation %} אנחנו צריכים לדעת רק את {% equation %}b_{i}{% endequation %} ולא שום דבר אחר. בפרט, וזה לב הרעיון בגרם-שמידט, אם אנחנו באמצע תהליך הבנייה של {% equation %}B{% endequation %} ובנינו עד כה רק <strong>חלק</strong> מהוקטורים בו, אז לכל וקטור חדש אנחנו כבר יודעים <strong>חלק</strong> מהצירוף הלינארי שייצג את {% equation %}v{% endequation %} בבסיס ה"מלא", ואותו חלק לא הולך להשתנות יותר אף פעם.

עוד מושג אחד ודי. אם {% equation %}v\in V{% endequation %} הוא וקטור כלשהו השונה מאפס, אנחנו נרצה למצוא {% equation %}\lambda{% endequation %} כך ש-{% equation %}\left\langle \lambda v,\lambda v\right\rangle =1{% endequation %}. מתכונות המכפלה הפנימית אנחנו רואים חיש קל שנובע מכך כי {% equation %}\left|\lambda\right|^{2}=\frac{1}{\left\langle v,v\right\rangle }{% endequation %}, ולכן טבעי לבחור ש-{% equation %}\lambda=\frac{1}{\sqrt{\left\langle v,v\right\rangle }}{% endequation %}. שימו לב שתכונה 4 של המכפלה הפנימית ש-{% equation %}\left\langle v,v\right\rangle {% endequation %} מבטיחה יהיה מספר ממשי חיובי ולכן יהיה ניתן להוציא לו שורש. אם אנחנו מעל שדה שאינו {% equation %}\mathbb{R}{% endequation %} או {% equation %}\mathbb{C}{% endequation %}, הנקודה הזו היא בדיוק אחת מהנקודות שבהן "הכל קורס" - בכלל לא בטוח שיהיה לנו בסיס אורתונורמלי במרחבים כאלו.

לסקלר {% equation %}\sqrt{\left\langle v,v\right\rangle }{% endequation %} הזה יש סימון ושם, שנעמוד על משמעותם המלאה רק בפוסט הבא - {% equation %}\|v\|{% endequation %}, <strong>הנורמה</strong> של {% equation %}v{% endequation %}. בפשטות, נורמה היא הכללה של מושג האורך, אבל על המבנה המעניין שקיומה משרה על {% equation %}V{% endequation %} אני לא אדבר עכשיו; העניין שלי בה נובע מכך שאם {% equation %}v{% endequation %} הוא וקטור שונה מאפס כלשהו, אז כפי שראינו - {% equation %}\frac{v}{\|v\|}{% endequation %} הוא וקטור שהמכפלה הפנימית שלו עם עצמו היא 1. לחלוקת {% equation %}v{% endequation %} ב-{% equation %}\|v\|{% endequation %} קוראים <strong>לנרמל</strong> את {% equation %}v{% endequation %}.

עכשיו בואו נראה את גרם-שמידט. אנחנו מתחילים מבסיס כלשהו {% equation %}\left\{ v_{1},\dots,v_{n}\right\} {% endequation %} למרחב מכפלה פנימית מסויים ובונים בסיס אורתונורמלי {% equation %}\left\{ b_{1},\dots,b_{n}\right\} {% endequation %} לאותו מרחב. הבניה היא אינדוקטיבית; בשלב ה-{% equation %}i{% endequation %} כבר בנינו את {% equation %}\left\{ b_{1},\dots,b_{i-1}\right\} {% endequation %} כך שהם אורתונורמליים ופורשים בדיוק את אותו מרחב כמו {% equation %}\left\{ v_{1},\dots,v_{i-1}\right\} {% endequation %}, ואל הקבוצה הזו אנו מוסיפים את {% equation %}b_{i}{% endequation %}. איך? ראשית אנו לוקחים את {% equation %}v_{i}{% endequation %}. כעת, לכל {% equation %}1\le j&lt;i{% endequation %} אנו יודעים ש-{% equation %}\left\langle v_{i},b_{j}\right\rangle {% endequation %} יהיה המקדם של {% equation %}b_{j}{% endequation %} בצירוף הלינארי שפורש את {% equation %}v_{i}{% endequation %}; כלומר, {% equation %}\left\langle v_{i},b_{j}\right\rangle b_{j}{% endequation %} הוא בדיוק אותו חלק של {% equation %}v_{i}{% endequation %} ש"כבר מטופל" על ידי {% equation %}b_{j}{% endequation %}, ולכן אפשר להחסיר אותו מ-{% equation %}v_{i}{% endequation %} בלב שקט. כלומר, אנו מגדירים וקטור חדש {% equation %}u_{i}=v_{i}-\left(\sum_{j=1}^{i-1}\left\langle v_{i},b_{j}\right\rangle b_{j}\right){% endequation %}.

כעת נשים לב לכך שעבור {% equation %}1\le j&lt;i{% endequation %}, {% equation %}\left\langle u_{i},b_{j}\right\rangle =\left\langle v_{i},b_{j}\right\rangle -\left(\sum_{k=1}^{i-1}\left\langle v_{i},b_{k}\right\rangle \left\langle b_{k},b_{j}\right\rangle \right)=\left\langle v_{i},b_{j}\right\rangle -\left\langle v_{i},b_{j}\right\rangle =0{% endequation %}, כלומר {% equation %}u_{i}{% endequation %} הוא אורתוגונלי לכל האיברים שבנינו עד כה של {% equation %}B{% endequation %}. עם זאת, קיימת הסכנה ש-{% equation %}u_{i}=0{% endequation %} וחסל. אבל אמרנו ש-{% equation %}b_{1},\dots,b_{i-1}{% endequation %} פורשים את אותו מרחב כמו {% equation %}v_{1},\dots,v_{i-1}{% endequation %}, ואם {% equation %}u_{i}=0{% endequation %} זה אומר ש-{% equation %}v_{i}=\sum_{j=1}^{i-1}\left\langle v_{i},b_{j}\right\rangle b_{j}\in\mbox{span}\left\{ v_{1},\dots,v_{i-1}\right\} {% endequation %} בסתירה לכך ש-{% equation %}v_{i}{% endequation %} היה בלתי תלוי באיברים אלו (כי {% equation %}\left\{ v_{1},\dots,v_{n}\right\} {% endequation %} היא <strong>בסיס</strong>). כל שנותר לעשות הוא לנרמל אותו ולהוסיף לקבוצה: נגדיר {% equation %}b_{i}=\frac{u_{i}}{\|u_{i}\|}{% endequation %} וסיימנו. אנחנו עדיין צריכים להוכיח ש-{% equation %}\mbox{span}\left\{ v_{1},\dots,v_{i}\right\} =\mbox{span}\left\{ b_{1},\dots,b_{i}\right\} {% endequation %}, אבל אני עצל מכדי לכתוב במפורש את ההוכחה ומשאיר לכם את זה כתרגיל.

אחרי שהתהליך יסיים לזלול את כל הבסיס {% equation %}\left\{ v_{1},\dots,v_{n}\right\} {% endequation %} נקבל קבוצה {% equation %}\left\{ b_{1},\dots,b_{n}\right\} {% endequation %} שפורשת את אותו מרחב כמו {% equation %}\left\{ v_{1},\dots,v_{n}\right\} {% endequation %} (ולכן היא בסיס), ובנוסף היא אורתונורמלית, בדיוק מה שרצינו. למען הדורות הבאים, בואו נכתוב את התהליך במפורש בתור אלגוריתם:
<ol>
	<li> לכל {% equation %}i=1,2,\dots,n{% endequation %}:
<ol>
	<li> הגדר {% equation %}u_{i}=v_{i}-\left(\sum_{j=1}^{i-1}\left\langle v_{i},b_{j}\right\rangle b_{j}\right){% endequation %}</li>
	<li> הגדר {% equation %}b_{i}=\frac{u_{i}}{\|u_{i}\|}{% endequation %}</li>
</ol>
</li>
	<li> החזר את {% equation %}\left\{ b_{1},\dots,b_{n}\right\} {% endequation %}</li>
</ol>
די פשוט, כשחושבים על זה. לרוע המזל, כשעושים את התהליך בפועל בעולם האמיתי, מהר מאוד מקבלים גועל נפש שאין כדוגמתו (כשמנרמלים וקטור לרוב צצים שורשים מזוויעים). תודה לאל על קיומם של מחשבים.