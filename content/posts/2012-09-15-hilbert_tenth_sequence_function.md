---
id: 2187
title: "הבעיה העשירית של הילברט - איך מקודדים דיופנטית את כל הסדרות הסופיות?"
date: 2012-09-15 14:52:58
layout: post
categories: 
  - תורת המספרים
tags: 
  - הבעיה העשירית של הילברט
---
בסיום הפוסט הקודם על הבעיה העשירית של הילברט הגענו למסקנה שכדי להוכיח שהבעיה העשירית של הילברט אינה כריעה (על ידי כך שנוכיח שכל פונקציה רקורסיבית היא דיופנטית) אנחנו נזקקים לפונקציה דיופנטית מיוחדת, שמסוגלת באורח קסום כלשהו לקודד <strong>כל סדרה סופית</strong>.

עזבו אתכם לרגע משאלת הדיופנטיותת איך בכלל נראית פונקציה כזו? פשוט מאוד: זו תהיה פונקציה {% equation %}S\left(i,u\right){% endequation %} על שני משתנים שהם מספרים טבעיים חיוביים, כך שלכל סדרה סופית {% equation %}a_{1},\dots,a_{N}{% endequation %} של מספרים טבעיים חיוביים, יהיה קיים {% equation %}u{% endequation %} כך ש-{% equation %}S\left(i,u\right)=a_{i}{% endequation %} לכל {% equation %}1\le i\le N{% endequation %}. במילים אחרות, תחשבו שהתאמנו מספר טבעי לכל סדרה סופית, ואז {% equation %}S{% endequation %} מקבלת הן את מספר הסדרה הזו ({% equation %}u{% endequation %}) והן את האינדקס של איבר ספציפי בסדרה ({% equation %}i{% endequation %}) ומחזירה אותו. מכיוון שיש רק מספר בן מניה של סדרות סופיות, ברור שקיימת פונקציה כמו {% equation %}S{% endequation %}; למעשה, קיימות המון פונקציות שמקיימות את התכונה של {% equation %}S{% endequation %} כי יש לנו לא מעט חופש בחירה (מה יהיה המספר שמקודד כל סדרה, ומה הערכים ש-{% equation %}S\left(i,u\right){% endequation %} מחזירה כאשר {% equation %}i{% endequation %} גדול מהאינדקס של האיבר האחרון בסדרה {% equation %}u{% endequation %}).

האתגר שלנו, אם כן, הוא למצוא פונקציה {% equation %}S\left(i,u\right){% endequation %} שכזו שתהיה גם <strong>דיופנטית</strong>. כלומר, שיהיה פולינום במספר משתנים {% equation %}p\left(x_{1},x_{2},x_{3},y_{1},\dots,y_{k}\right){% endequation %} כך שלכל הצבה של ערכים ב-{% equation %}x_{1},x_{2},x_{3}{% endequation %}, המשוואה הדיופנטית המתקבלת {% equation %}p\left(a_{1},a_{2},a_{3},y_{1},\dots,y_{k}\right)=0{% endequation %} במשתנים {% equation %}y_{1},\dots,y_{k}{% endequation %} היא פתירה אם ורק אם {% equation %}a_{3}=S\left(a_{1},a_{2}\right){% endequation %}.

יפה, אז הבנו מה היעד שלנו. לפני שנגיע אליו, בואו נפתור בעיה פשוטה יותר, שאחר כך נשתמש, כמובן, בפתרונה: פונקציות דיופנטיות שממירות זוגות של טבעיים למספר טבעי באופן חד-חד-ערכי ועל, וההפך.

בואו נתחיל עם פונקציה דיופנטית תמימה למראה - הפונקציה של <strong>המספרים המשולשיים</strong>, {% equation %}T\left(n\right)=1+2+3+\dots+n=\frac{n\left(n+1\right)}{2}{% endequation %}. למי שתוהה איך הגעתי לנוסחה באגף ימין, זה תעלול של גאוס: אם ניקח את הסדרה {% equation %}1,2,\dots,n{% endequation %}, נכתוב מתחתיה את הסדרה {% equation %}n,n-1,\dots,1{% endequation %} ונחבר כל שני איברים שנמצאים האחד מעל השני, נקבל תמיד {% equation %}n+1{% endequation %}, ויש לנו בדיוק {% equation %}n{% endequation %} איברים כאלו. זה מראה ש-{% equation %}T\left(n\right)+T\left(n\right)=n\left(n+1\right){% endequation %} ולכן {% equation %}T\left(n\right)=\frac{n\left(n+1\right)}{2}{% endequation %}. ולמה "מספרים משולשיים"? כי אם נצייר משולש שמורכב מתפוזים כך שבקודקוד העליון שלו יש תפוז אחד, בשורה שמתחתיו שני תפוזים, מתחת לכך שלושה תפוזים וכן הלאה - מספר התפוזים במשולש יהיה {% equation %}T\left(n\right){% endequation %} כאשר {% equation %}n{% endequation %} הוא מספר השורות.

למה הפונקציה הזו דיופנטית? ובכן, {% equation %}p\left(x_{1},x_{2}\right)=2x_{2}-x_{1}\left(x_{1}+1\right){% endequation %} עושה את העבודה - היא מקיימת {% equation %}p\left(n,T\left(n\right)\right)=0{% endequation %} וכמו כן {% equation %}p\left(a,b\right)\ne0{% endequation %} אם {% equation %}b\ne T\left(a\right){% endequation %}.

עכשיו נתחיל עם להטוטים של תורת המספרים. ראשית, שימו לב לכך ש-{% equation %}T\left(n\right){% endequation %} היא פונקציה <strong>עולה ממש</strong>, כלומר {% equation %}T\left(n\right)&lt;T\left(n+1\right){% endequation %} תמיד, וכמו כן היא אינה חסומה (זה מובן מאליו - כל פונקציה עולה ממש של טבעיים אינה חסומה). זה אומר שלכל מספר טבעי {% equation %}z{% endequation %}, קיים איזה שהוא {% equation %}n\ge0{% endequation %} כך ש-{% equation %}T\left(n\right)&lt;z\le T\left(n+1\right){% endequation %}, כלומר {% equation %}z{% endequation %} נופל באיזה שהוא קטע שבין {% equation %}T\left(n\right){% endequation %} ו-{% equation %}T\left(n+1\right){% endequation %} (ורק בקטע אחד כזה!). לכן אפשר לכתוב את {% equation %}z{% endequation %} בצורה <strong>יחידה</strong> בתור {% equation %}z=T\left(n\right)+y{% endequation %} כך ש-{% equation %}1\le y\le n+1{% endequation %} והערכים של {% equation %}n,y{% endequation %} נקבעים באופן יחיד בהינתן {% equation %}z{% endequation %}.

בעיה קטנה שצצה עכשיו היא ש-{% equation %}n{% endequation %} יכול להיות שווה 0 אבל אנחנו מתעסקים רק במספרים שערכם לפחות 1. לכן את {% equation %}n{% endequation %} נכתוב בעזרת {% equation %}y{% endequation %}: {% equation %}n=y+x-2{% endequation %}, כאשר {% equation %}x{% endequation %} הוא משתנה כלשהו שערכו נע בין 1 ובין {% equation %}n+1{% endequation %}, כמו {% equation %}y{% endequation %}. אם כן, אפשר לכתוב:

{% equation %}z=T\left(x+y-2\right)+y{% endequation %}

ושוב - {% equation %}x,y{% endequation %} נקבעים <strong>ביחידות</strong>בהינתן {% equation %}z{% endequation %}. נגדיר כעת שלוש פונקציות:
<ol>
	<li>{% equation %}L\left(z\right)=x{% endequation %}</li>
	<li>{% equation %}R\left(z\right)=y{% endequation %}</li>
	<li>{% equation %}P\left(x,y\right)=T\left(x+y-2\right)+y{% endequation %}</li>
</ol>
בואו נבין מה הפונקציות הללו עושות. ראשית אכתוב את הזוגות {% equation %}\left(L\left(z\right),R\left(z\right)\right){% endequation %} עבור הערכים הראשונים של {% equation %}z=1,2,3,4,\dots{% endequation %}. עבור {% equation %}z=1{% endequation %} ברור ש-{% equation %}n=0{% endequation %} ו-{% equation %}y=1{% endequation %}, ולכן {% equation %}x=1{% endequation %}, כלומר הזוג הראשון הוא {% equation %}\left(1,1\right){% endequation %}. עבור {% equation %}z=2{% endequation %} ברור ש-{% equation %}n=1{% endequation %} ו-{% equation %}y=1{% endequation %} ולכן {% equation %}x=2{% endequation %} ולכן הזוג השני הוא {% equation %}\left(2,1\right){% endequation %}, וכן הלאה. נקבל את הסדרה:

{% equation %}\left(1,1\right),\left(2,1\right),\left(1,2\right),\left(3,1\right),\left(2,2\right),\left(1,3\right),\dots{% endequation %}

העקרון די ברור: אנחנו קודם כל עוברים על כל הזוגות {% equation %}\left(x,y\right){% endequation %} שבהם {% equation %}x+y=2{% endequation %} - יש רק זוג אחד כזה - ולכן על כל הזוגות שמתאימים ל-{% equation %}n=0{% endequation %} (כזכור, {% equation %}n=x+y-2{% endequation %}). אחר כך אנחנו עוברים על כל הזוגות שמתאימים ל{% equation %}n=1{% endequation %}, כלומר {% equation %}x+y=3{% endequation %}, לאחר מכן על הזוגות של {% equation %}n=2{% endequation %}, כלומר {% equation %}x+y=4{% endequation %}, וכן הלאה. בכל הזוגות הללו אנחנו מתחילים מ-{% equation %}x{% endequation %} הגדול ביותר האפשרי ובמעבר לזוג הבא מקטינים אותו ב-1 ומגדילים את {% equation %}y{% endequation %} ב-1.

{% equation %}P\left(x,y\right){% endequation %} היא בבירור הפונקציה ההפוכה ל-{% equation %}L,R{% endequation %}, כלומר מתקיים {% equation %}P\left(L\left(z\right),R\left(z\right)\right)=z{% endequation %} לכל {% equation %}z{% endequation %}, כמו גם {% equation %}L\left(P\left(x,y\right)\right)=x{% endequation %} ו-{% equation %}R\left(P\left(x,y\right)\right)=y{% endequation %}. בראשית ימי הבלוג <a href="http://www.gadial.net/2007/09/18/r_and_re/">הצגתי</a>את הפונקציה הזו (בניסוח טיפה יותר מפורש וטיפה שונה) ואמרתי ש"רק אתמול גיליתי" את הפונקציה (מה שנכון נכון). בתגובות לפוסט העירו לי שאם מעוניינים לקודד כל זוג מספרים טבעיים באופן חח"ע ועל באמצעות מספר טבעי יחיד אפשר גם להשתמש בפונקציה {% equation %}f\left(x,y\right)=2^{x}\left(2y+1\right)-1{% endequation %} (שהולכת מהטבעיים עם 0 לטבעיים עם 0, אבל זה לא באמת משנה) שהיא קצת יותר ברורה. החסרון של הפונקציה הזו בהקשר הנוכחי היא שבגלל ה-{% equation %}2^{x}{% endequation %} שמופיע שם לא ברור איך להוכיח שהיא דיופנטית בלי עוד עבודה, וגם לא ברור איך "להפוך" אותה באמצעות פונקציות דמויות {% equation %}L,R{% endequation %}. במקרה שלנו, לעומת זאת, קל לראות שכל הפונקציות שהצגתי הן דיופנטיות. הבה ונעשה זאת במפורש:
<ol>
	<li>{% equation %}x=L\left(z\right)\iff\exists y\left(2z=\left(x+y-2\right)\left(x+y-1\right)+2y\right){% endequation %}</li>
	<li>{% equation %}y=R\left(z\right)\iff\exists x\left(2z=\left(x+y-2\right)\left(x+y-1\right)+2y\right){% endequation %}</li>
	<li>{% equation %}z=P\left(x,y\right)\iff2z=\left(x+y-2\right)\left(x+y-1\right)+2y{% endequation %}</li>
</ol>
זה משלים את החלק הראשון של הבניה שלנו: הראנו שמספור (והיפוך המספור) של זוגות של טבעיים הוא פונקציה דיופנטית. כעת - להגדרת הפונקציה {% equation %}S\left(i,u\right){% endequation %}, שהיא כבר ממש בהישג ידינו!

נגדיר {% equation %}S\left(i,u\right)=L\left(u\right)\mbox{ mod }\left(1+iR\left(u\right)\right){% endequation %}, וזו הפונקציה המבוקשת. רגע, מה?

ראשית, צריך טיפה להיזהר פה עם ההגדרה שלנו. אני מגדיר את {% equation %}a\mbox{ mod }b{% endequation %} להיות כאן המספר החיובי שמתקבל כשמחלקים {% equation %}a{% endequation %} ב-{% equation %}b{% endequation %} ולוקחים שארית, אלא אם {% equation %}a{% endequation %} מתחלק ממש ב-{% equation %}b{% endequation %} ואז במקום 0 הפונקציה מחזירה את {% equation %}b{% endequation %} (אני עושה את זה כדי לחמוק מהחזרה של 0).

כעת, בואו ננסה להבין איך הפונקציה "עובדת". כל סדרה מקודדת על ידי מספר {% equation %}u{% endequation %}, שבעצם אנחנו חושבים עליו כאילו הוא מקודד זוג מספרים טבעיים, {% equation %}\left(a,b\right){% endequation %}. עכשיו לוקחים את {% equation %}a{% endequation %} ומתחילים "לגרד" ממנו את אברי הסדרה: מחלקים אותו ב-{% equation %}1+b{% endequation %}, ב-{% equation %}1+2b{% endequation %}, ב-{% equation %}1+3b{% endequation %} וכן הלאה... בכל פעם לוקחים את השארית ומוסיפים אותה לסדרה. מתישהו {% equation %}1+ib{% endequation %} הולך להיות גדול יותר מ-{% equation %}a{% endequation %} ואז הסדרה "תתקע" על להחזיר {% equation %}a,a,a,\dots{% endequation %} כל הזמן, אבל זה לא מפריע לנו - אנחנו רוצים רק לקודד סדרות סופיות ולא מעניין אותנו מה קורה עבור {% equation %}i{% endequation %}-ים שגדולים מאורך הסדרה.

מה שאני צריך לשכנע אתכם בו הוא כפול: ראשית, שהפונקציה הזו דיופנטית; את זה אעשה אחר כך. שנית, שאכן אפשר לקבל כל סדרה סופית בעזרת השיטה הזו של לקחת {% equation %}a{% endequation %} מסויים ולהתחיל "לקלף" אותו עם {% equation %}1+ib{% endequation %}.

כאן נכנס <a href="http://www.gadial.net/2012/09/12/chinese_remainder_theorem/">משפט השאריות הסיני</a> לתמונה. נניח שאנחנו רוצים לקודד את הסדרה {% equation %}a_{1},\dots,a_{N}{% endequation %}. בואו נניח גם שאנחנו מכירים {% equation %}b{% endequation %} כלשהו כך ש-{% equation %}1+b,1+2b,\dots,1+Nb{% endequation %} כולם זרים זה לזה. במקרה הזה, ניצחנו, כי נסתכל על מערכת המשוואות:

{% equation %}x\equiv_{1+b}a_{1}{% endequation %}

{% equation %}\vdots{% endequation %}

{% equation %}x\equiv_{1+Nb}a_{N}{% endequation %}

משפט השאריות הסיני מבטיח שקיים למערכת הזו פתרון. ניקח את הפתרון הזה להיות {% equation %}a{% endequation %}, וסיימנו. השאלה, אם כן, היא רק האם לכל {% equation %}N{% endequation %} טבעי קיים {% equation %}b{% endequation %} טבעי כך ש-{% equation %}1+b,1+2b,\dots,1+Nb{% endequation %} כולם זרים זה לזה. בואו נשאל את עצמנו מה יגרום לכך שעבור {% equation %}N{% endequation %} מסויים {% equation %}b{% endequation %} ספציפי לא יעבוד, כלומר יהיו {% equation %}i,j{% endequation %} כך ש-{% equation %}1+ib,1+jb{% endequation %} לא יהיו זרים, כלומר יהיה איזה שהוא מספר {% equation %}d{% endequation %} שמחלק את שניהם.

אם {% equation %}d{% endequation %} מחלק את שניהם, הוא מחלק גם כל צירוף לינארי שלהם, כלומר סכום שלהם כשהם מוכפלים במספר שלם כלשהו, כלומר {% equation %}d{% endequation %} בפרט מחלק גם את {% equation %}j\left(1+ib\right)-i\left(1+jb\right)=j-i{% endequation %}. עכשיו, מכיוון ש-{% equation %}1\le i,j\le N{% endequation %} הרי שבהכרח גם {% equation %}1\le d\le N{% endequation %}; לכן כדי שנקבל מספרים זרים די לנו להבטיח שאף אחד מהם לא יוכל להתחלק על ידי מספר שבין 1 ל-{% equation %}N{% endequation %}. התעלול פשוט: נבחר את {% equation %}b{% endequation %} להיות מספר שמתחלק ב-{% equation %}N!{% endequation %}, ובנוסף לכך הוא גם גדול מכל האיברים {% equation %}a_{1},\dots,a_{N}{% endequation %} של סדרה (כדי להבטיח ש-{% equation %}a{% endequation %} מודולו {% equation %}1+ib{% endequation %} אכן יחזיר את {% equation %}a_{i}{% endequation %} ולא רק מספר ששקול לו). כעת, אם {% equation %}b{% endequation %} מתחלק ב-{% equation %}N!{% endequation %} אז בפרט כל {% equation %}1\le d\le N{% endequation %} מחלק את {% equation %}b{% endequation %}, ולכן מחלק את {% equation %}ib{% endequation %}, ולכן <strong>לא</strong> מחלק את {% equation %}1+ib{% endequation %}; זו הסיבה לבחירה ה"מוזרה" שלנו בסדרת המודולוסים.

התעלול המקסים הזה קודם לעיסוק בפונקציות דיופנטיות; הוא מופיע כבר במאמר המפורסם של קורט גדל שבו הוא הוכיח את משפט אי השלמות שלו (כזכור, זה גם המאמר שבו הופיעו הפונקציות הרקורסיביות לראשונה). עם זאת, אנחנו הולכים צעד אחד מעבר לגדל בכך שאנחנו מוכיחים גם ש-{% equation %}S\left(i,u\right){% endequation %} היא דיופנטית.

הנה מערכת משוואות דיופנטיות שמראה ש-{% equation %}S\left(i,u\right){% endequation %} דיופנטית:

{% equation %}S\left(i,u\right)=w{% endequation %}

{% equation %}\iff{% endequation %}

{% equation %}x=L\left(u\right)\wedge y=R\left(u\right){% endequation %}

{% equation %}\wedge\exists z\left(x=w+z\left(1+iy\right)\right){% endequation %}

{% equation %}\wedge\exists v\left(1+iy=w+v-1\right){% endequation %}

שתי המשוואות הראשונות נתונות בצורה לא מפורשת על ידי {% equation %}x=L\left(u\right)\wedge y=R\left(u\right){% endequation %} שכבר ראינו. זו בעצם דרך "לפרק" את{% equation %}u{% endequation %} לתוך המשתנים {% equation %}x,y{% endequation %} של המשוואה הדיופנטית. השורה הבאה אומרת לנו ש-{% equation %}w{% endequation %} התקבל מ-{% equation %}x{% endequation %} על ידי חלוקה ב-{% equation %}\left(1+iy\right){% endequation %} ולקיחת שארית ({% equation %}z{% endequation %} הוא המנה של החלוקה). השורה האחרונה אומרת לנו במפורש ש-{% equation %}w\le1+iy{% endequation %} (העדפתי לכתוב זאת במפורש מאשר לכתוב את הנוסחה עם סימן האי-שוויון, כי מי זוכר כבר איך הראינו שהיחס הזה דיופנטי). בקיצור, ההוכחה היא פשוטה למדי, בהינתן מה שכבר למדנו על פונקציות דיופנטיות!

סיימנו עם קידוד לכל הסדרות הסופיות, ועוד נשתמש בו בעתיד. בפוסט הבא על הבעיה העשירית של הילברט נעבור לבנות את הכלי הכבד המרכזי שלנו - הוכחה שהפונקציה האקספוננציאלית היא דיופנטית. יהיה אקשן.
