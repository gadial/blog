---
id: 3675
title: "”הוכחה ראשונה לעליונות מחשב קוונטי“ - מה כן (אזהרה - עלול לכלול מתמטיקה)"
date: 2018-11-07 21:37:41
layout: post
categories: 
  - תורת הסיבוכיות
  - חישוב קוונטי
tags: 
  - חישוב קוונטי
---
<h2>מבוא</h2>
אחרי <a href="https://gadial.net/2018/10/23/quantum_advantage_with_shallow_circuits/">שבפוסט הקודם</a> הסברתי קצת בנפנופי ידיים מה הסיפור עם <a href="https://arxiv.org/abs/1704.00690">המאמר</a> ש"הוכיח עליונות קוונטית", בפוסט הזה אני רוצה לגשת לעובי הקורה המתמטי. אני לא לגמרי אניח ידע מוקדם כלשהו, אבל בלי ידע מוקדם שכזה ללא ספק יידרש יותר מאמץ להבין על מה אני מדבר - כדאי לקחת את זה בחשבון.

התוצאה של המאמר היא הפרדה בין שני מודלים חישוביים. בהקשר שלנו, "מודל חישובי" הוא <strong>משהו</strong> שמקבל קלט ומוציא פלט, ויש אילוצים שונים ומשונים לגבי הצורה שבה הוא עושה את זה ואיך מותר לו לעשות את זה. קשר של קלט-פלט נקרא "פונקציה", ומודל חישובי א' הוא חזק יותר ממודל חישובי ב' אם כל מה פונקציה שב' יודע לחשב, גם א' יודע, ובנוסף לכך יש משהו שא' יודע לחשב וב' לא.

המודלים החישוביים שאנחנו מדברים עליהם כאן מנסים למדל <strong>חישוב מקביל</strong>י<strong> קצר</strong>. המודל ה"קלאסי" שמתאר חישוב מקבילי נקרא <strong>מעגלים בוליאניים</strong> ומחלקת הסיבוכיות המתאימה לו מסומנת ב-NC (ראשי תיבות של Nick's Class. כן, ניק זה שם של מישהו. אל תשאלו). תיארתי <a href="https://gadial.net/2011/01/18/what_are_boolean_circuits/">מעגלים בוליאניים</a> כאן, אבל הנה שוב הרעיון: מעגל בוליאני הוא גרף מכוון חסר מעגלים; כל צומת שלא נכנס אליה כלום היא <strong>קלט</strong> וכל צומת שלא יוצא ממנה כלום היא <strong>פלט</strong> וכל צומת פנימי הוא <strong>שער לוגי</strong>. את הקלטים מסמנים ב-{% equation %}x_{1},x_{2},\dots,x_{n}{% endequation %} ואת הפלטים ב-{% equation %}y_{1},y_{2},\dots,y_{m}{% endequation %} (שימו לב שמספר הקלטים והפלטים יכול להיות שונה). השערים הלוגיים יכולים להיות AND, OR, NOT ואנחנו דורשים שלכל שער כזה ייכנסו שתי קשתות לכל היותר.

<strong>חישוב</strong> שמבצע המעגל מתבצע בדרך המתבקשת: מציבים ב-{% equation %}x{% endequation %}-ים ערכים כלשהם של 0 ו-1 ו"מפעפעים" את הערכים הללו בגרף: לכל שער לוגי שהכניסות אליו הן מצמתים שהערך שלהם כבר נקבע, מחשבים את הערך של השער הלוגי בהתאם לפונקציה שלו (שער AND שנכנסים אליו 1 ו-0? הערך שלו יהיה 0). בצורה הזו בסופו של דבר נקבעים הערכים של הפלטים, והרי לנו חישוב של פונקציה. שימו לב שזו פונקציה {% equation %}f:\left\{ 0,1\right\} ^{n}\to\left\{ 0,1\right\} ^{m}{% endequation %}, כלומר בפרט מספר הביטים בכניסה הוא קבוע (מכונות טיורינג, להבדיל, יודעות לפעול על קלטים מאורך כלשהו של ביטים). לכן יותר נפוץ לדבר על <strong>משפחה</strong> של מעגלים - לכל {% equation %}n{% endequation %} יש לנו מעגל שמחשב פונקציה על הקלטים מאורך {% equation %}n{% endequation %}; בדרך כלל דורשים שבהינתן {% equation %}n{% endequation %} נדע לבנות את המעגל הזה אלגוריתמית, אחרת משפחה של מעגלים שכזו עלולה לעשות דברים מוזרים כמו לפתור את בעיית העצירה.

יש לנו שני מדדי סיבוכיות למעגלים - <strong>הגודל</strong> של המעגל, כלומר כמה צמתים יש בו בסך הכל, וה<strong>עומק</strong> שלו, כלומר מה אורך המסלול המקסימלי מקלט אל פלט. האינטואיציה היא כזו: שערים לוגיים שאין תלות בין הקלטים שלהם יכולים לבצע חישובים באופן מקבילי; לכן במקרה הכי קיצוני שבו כל שער לוגי הוא מחשב שפועל עצמאית, אפשר לחשוב על גודל המעגל בתור חסם על מספר המחשבים שנדרשים כדי להריץ את המעגל באופן מקבילי. העומק של המעגל הוא מדד לזמן החישוב - כל מסלול במעגל מייצג סיטואציה שבה מחשב אחד כן צריך לחכות לקלט מהמחשבים שבאים לפניו במסלול כדי שיוכל להמשיך בחישוב.

המחלקה {% equation %}\text{NC}{% endequation %} מחולקת ל"תת-מחלקות": {% equation %}\text{NC}^{k}{% endequation %} כוללת את משפחות המעגלים שבהן <strong>הגודל</strong> של מעגל עם {% equation %}n{% endequation %} קלטים הוא <strong>פולינומי</strong> ב-{% equation %}n{% endequation %}, ואילו העומק שלו הוא {% equation %}O\left(\log^{k}n\right){% endequation %}, מה שנקרא "פולי-לוגריתמי". המחלקה {% equation %}\text{NC}^{0}{% endequation %} כוללת, אם כן, מעגלים שבהם יש לנו חסם עליון על העומק <strong>שלא תלוי בגודל הקלט</strong>. כלומר, לא משנה אם הקלט הוא מאורך 2 ביטים או 200, עומק המעגל עדיין יהיה חסום על ידי, נאמר, 17. לא קשה לראות שההגבלה הזו יוצרת מגבלה רצינית על הפונקציות שאפשר לחשב במחלקה הזו - כל ביט של פלט יכול להיות תלוי רק במספר סופי של ביטים מהקלט (משהו כמו 2 בחזקת עומק המעגל לכל היותר).
<h2>מעגלים ושערים קוונטיים</h2>
נעבור למעגלים קוונטיים. גם על זה <a href="https://gadial.net/2014/08/19/quantum_circuits_intro/">יש לי פוסט</a>, אבל הנה הסבר שבאמת דורש מינימום היכרות עם קוונטים. אם יש לנו מעגל על {% equation %}n{% endequation %} קיוביטים, אנחנו לא מפרידים אותם, כמו ב-{% equation %}\text{NC}^{0}{% endequation %}, לכל מני אותות שרצים להם על גרף. במקום זה, אנחנו חושבים על המצב של המעגל בכל רגע נתון בתור וקטור במרחב וקטורי מעל {% equation %}\mathbb{C}{% endequation %} ממימד {% equation %}2^{n}{% endequation %}. כל אביר בסיס של המרחב הזה הוא מחרוזת ב-{% equation %}\left\{ 0,1\right\} ^{n}{% endequation %}. למשל, אם {% equation %}n=3{% endequation %} אז אברי הבסיס של המרחב הם {% equation %}\left|000\right\rangle ,\left|001\right\rangle ,\left|010\right\rangle ,\left|011\right\rangle ,\left|100\right\rangle ,\left|101\right\rangle ,\left|110\right\rangle ,\left|111\right\rangle {% endequation %}.

הפעלה של שער במעגל היא כפל של הוקטור הזה במטריצה <strong>אוניטרית</strong> מעל {% equation %}\mathbb{C}_{2^{n}\times2^{n}}{% endequation %}. זה כל מה שמעגל קוונטי עושה - כופל את הוקטור בעוד ועוד מטריצות. כדי לשמור את העניינים פשוטים יותר וקרובים יותר למציאות, על פי שער קוונטי משפיע רק על קיוביט אחד או שניים בכל פעם. אבל "משפיע על קיוביט אחד" לא אומר שהפעולה שלו על הוקטור שמייצג את המצב הקוונטי תשנה רק כניסה אחת או שתיים בו; זה רק אומר שמה שהשער בעצם עושה לכל קואורדינטה יושפע רק מביט אחד או שניים במחרוזת שמתארת את הקואורדינטה הזו.

בואו נראה דוגמא מרכזית שנשתמש בה כל הזמן - שער הדאמר, {% equation %}H{% endequation %}. כשחושבים על השער הזה בתור מטריצה שפועלת על מרחב עם קיוביט בודד, התיאור המפורש הוא {% equation %}H=\frac{\sqrt{2}}{2}\left(\begin{array}{cc} 1 & 1\\ 1 & -1 \end{array}\right){% endequation %}. זו צורת כתיב סבירה, אבל אני אשתמש בצורת כתיב קצת שונה, שבה קצת יותר קל להרגיש מה {% equation %}H{% endequation %} עושה:
<ul>
 	<li>{% equation %}H\left|0\right\rangle =\left|0\right\rangle +\left|1\right\rangle {% endequation %}</li>
 	<li>{% equation %}H\left|1\right\rangle =\left|0\right\rangle -\left|1\right\rangle {% endequation %}</li>
</ul>
הכתיב הזה קצת מרמה - מה שאני <strong>באמת</strong> צריך לכתוב הוא {% equation %}H\left|0\right\rangle =\frac{\sqrt{2}}{2}\left|0\right\rangle +\frac{\sqrt{2}}{2}\left|1\right\rangle {% endequation %} כי בלי המקדמים הללו המצב הוא לא תקין (הוא חייב להיות וקטור מנורמה 1) אבל אני מחפף בזה כי בלי המקדמים העסק יותר קריא ואין סכנה אמיתית לבלבול.

עכשיו, איך {% equation %}H{% endequation %} פועל על מצב קוונטי שמורכב מ<strong>שני</strong> קיוביטים? כאן צריך להיזהר - אין משמעות לומר ש-{% equation %}H{% endequation %} פועל על המצב בלי לומר על איזה מהקיוביטים הוא פועל. אז אני אכתוב {% equation %}H^{1}{% endequation %} כדי להגיד \textquotedblright{% equation %}H{% endequation %} שמופעל על הקיוביט הראשון" ו-{% equation %}H^{2}{% endequation %} כדי לומר \textquotedblright{% equation %}H{% endequation %} שמופעל על הקיוביט השני". תחת הסימן הזה:
<ul>
 	<li>{% equation %}H^{1}\left|00\right\rangle =\left|00\right\rangle +\left|10\right\rangle {% endequation %}</li>
 	<li>{% equation %}H^{1}\left|10\right\rangle =\left|00\right\rangle -\left|10\right\rangle {% endequation %}</li>
 	<li>{% equation %}H^{1}\left|01\right\rangle =\left|01\right\rangle +\left|11\right\rangle {% endequation %}</li>
 	<li>{% equation %}H^{1}\left|11\right\rangle =\left|01\right\rangle -\left|11\right\rangle {% endequation %}</li>
</ul>
ואתם כבר יכולים להשלים את מה ש-{% equation %}H^{2}{% endequation %} עושה בעצמכם. עכשיו, הנה השאלה המעניינת באמת - מה מקבלים אם מפעילים את {% equation %}H^{1}{% endequation %} ואחריו את {% equation %}H^{2}{% endequation %}? אפשר גם בסדר ההפעלה ההפוך, מקבלים את אותו הדבר. בואו נכתוב רגע מקרה אחד במפורש:

{% equation %}H^{2}\left(H^{1}\left|00\right\rangle \right)=H^{2}\left|00\right\rangle +H^{2}\left|10\right\rangle =\left|00\right\rangle +\left|01\right\rangle +\left|10\right\rangle +\left|11\right\rangle {% endequation %}

כלומר, קיבלנו מצב של "פיזור אחיד" בין כל וקטורי הבסיס הקיימים במרחב. כדי לפשט את הסימנים, במקום לכתוב {% equation %}H^{2}H^{1}{% endequation %} אפשר לכתוב {% equation %}H^{\otimes2}{% endequation %}, וגם אפשר "לקודד" את הפעולה הזו בתור אופרטור יחיד, כלומר מטריצה בודדת במקום מכפלה של שתי מטריצות בזו אחר זו (פשוט כפלו את האחת בשניה וקיבלתם את האופרטור). כל הסיפור הזה עובד גם ל-{% equation %}n{% endequation %} ביטים; אנחנו תמיד נקבל

{% equation %}H^{\otimes n}\left|0^{n}\right\rangle =\sum_{x}\left|x\right\rangle {% endequation %}

כאשר הסכום רץ על כל ה-{% equation %}x\in\left\{ 0,1\right\} ^{n}{% endequation %} (אני לא כותב את זה במפורש בסכום כי אשמיט את זה גם בהמשך וכדאי שנתרגל). למעשה, המון אלגוריתמים קוונטיים מתחילים בדיוק כך - לוקחים את המצב התמים {% equation %}\left|0^{n}\right\rangle {% endequation %} ומייצרים ממנו סופרפוזיציה אחידה שכזו על כל המרחב. גם אנחנו נפעל בצורה הזו בהמשך.

אוקיי, אבל מה קורה אם אנחנו מפעילים את {% equation %}H^{\otimes n}{% endequation %} על וקטור בסיס שאינו מחרוזת שכולה אפסים? אני מציע לכם לנסות לעשות את התרגיל הזה בעצמכם קודם, כי זו דרך טובה להבין מה לכל הרוחות הולך פה - וזה גם יהיה קריטי בהמשך, כך שעדיף לכם לגלות את זה עצמאית מאשר שאספר לכם.

חוץ מ-{% equation %}H{% endequation %} יש עוד כמה וכמה שערים נפוצים מאוד. ראשית, ישנם <strong>שערי פאולי</strong> שמסומנים ב-{% equation %}X,Y,Z{% endequation %} ומתוארים על ידי המטריצות

{% equation %}X=\left(\begin{array}{cc} 0 & 1\\ 1 & 0 \end{array}\right),Y=\left(\begin{array}{cc} 0 & -i\\ i & 0 \end{array}\right),Z=\left(\begin{array}{cc} 1 & 0\\ 0 & -1 \end{array}\right){% endequation %}

מה ש-{% equation %}X{% endequation %} עושה הוא בעצם פעולת NOT:
<ul>
 	<li>{% equation %}X\left|0\right\rangle =\left|1\right\rangle {% endequation %}</li>
 	<li>{% equation %}X\left|1\right\rangle =\left|0\right\rangle {% endequation %}</li>
</ul>
מה ש-{% equation %}Z{% endequation %} עושה מזכיר קצת את {% equation %}H{% endequation %}, רק ש-{% equation %}Z{% endequation %} לא מפצל לשניים, רק מכפיל במינוס 1 באחד מהמקרים:
<ul>
 	<li>{% equation %}Z\left|0\right\rangle =\left|0\right\rangle {% endequation %}</li>
 	<li>{% equation %}Z\left|1\right\rangle =-\left|1\right\rangle {% endequation %}</li>
</ul>
ואילו מה ש-{% equation %}Y{% endequation %} עושה נראה כמו שילוב של {% equation %}X{% endequation %} ו-{% equation %}Z{% endequation %} כשגם מכניסים פנימה את המספר המרוכב {% equation %}i{% endequation %}:
<ul>
 	<li>{% equation %}Y\left|0\right\rangle =-i\left|1\right\rangle {% endequation %}</li>
 	<li>{% equation %}Y\left|1\right\rangle =i\left|0\right\rangle {% endequation %}</li>
</ul>
הדמיון הזה לא מקרי - קל לראות ש-{% equation %}Y=iXZ{% endequation %}, ובאופן דומה גם {% equation %}Z=iXY{% endequation %} וכדומה, כל מטריצת פאולי מתקבלת מכפל של שתי האחרות וסקלר הפיך. תחת ההגדרה המתאימה (שתזהה את כל הכפולות בסקלר הפיך של המטריצות בתור אותו איבר) ותוספת מטריצת היחידה מקבלים פה חבורה - <strong>חבורת פאולי</strong>.

אל האוסף הזה מצטרפת מטריצה נוספת שנקראת לפעמים <strong>פאזה</strong> ומזכירה את {% equation %}Z{% endequation %}:

{% equation %}S=\left(\begin{array}{cc} 1 & 0\\ 0 & -i \end{array}\right){% endequation %}

קל לבדוק ש-{% equation %}S^{2}=Z{% endequation %}, כך שאפשר לחשוב על {% equation %}S{% endequation %} בתור "שורש" של {% equation %}Z{% endequation %} (למעשה, כמעט תמיד בוחרים בתור {% equation %}S{% endequation %} את המטריצה שבה הכניסה השניה היא {% equation %}i{% endequation %} ולא {% equation %}-i{% endequation %}, אבל המאמר הנוכחי לקח את זו אז אני דבק בסימון הזה). עוד דבר שקל לבדוק הוא ש-{% equation %}X=HZH{% endequation %} (תנסו!) ולכן בעצם אפשר לקבל את כל מטריצות פאולי מתוך {% equation %}H,S{% endequation %} לבד. החבורה שנוצרת על ידי {% equation %}H,S{% endequation %} באופן הזה (כזכור, כשמזהים שתי מטריצות שנבדלות זו מזו על ידי כפל בקבוע) נקראת <strong>חבורת קליפורד</strong> (עבור קיוביט בודד) והיא עומדת במרכז אחד מהמשפטים היפים שאני מכיר בתחום - משפט Gottesman--Knill שמראה כיצד ניתן לבצע סימולציה של מעגל קוונטי שנבנה מתוך שערים מחבורת קליפורד בלבד <strong>בזמן ומקום פולינומיים</strong>. אני מקווה להקדיש לזה פוסט מתישהו, אבל כרגע השורה התחתונה היא שהשערים שראינו עד כה הם לא בדיוק מה שנותן לחישוב קוונטי את הכוח שלו - צריך "עוד משהו". ה"עוד משהו" הזה נקרא שער-{% equation %}T{% endequation %} והוא מוגדר כך: {% equation %}T=\left(\begin{array}{cc} 1 & 0\\ 0 & e^{\frac{i\pi}{4}} \end{array}\right){% endequation %}.

עד עכשיו דיברתי רק על שערים על קיוביט בודד, אבל זו בעצם קצת רמאות. כל עוד כל מה שמבצעים במעגל קוונטי הוא פעולות על קיוביט בודד, אין שום דבר מעניין במעגל הזה ואפשר לסמלץ אותו קלאסית בלי בעיה - בודקים מה קורה לכל קיוביט בנפרד, וזהו. הכוח של מעגלים קוונטיים מגיע כשגורמים לקיוביטים להיות תלויים זה בזה. למשל, אם אני יוצר את המצב הקוונטי {% equation %}\left|00\right\rangle +\left|11\right\rangle {% endequation %} אז קיבלתי מצב שאי אפשר להבין אותו על ידי חשיבה על כל קיוביט בנפרד (להבדיל מ-{% equation %}\left|00\right\rangle +\left|01\right\rangle +\left|10\right\rangle \left|11\right\rangle {% endequation %} שעליו אפשר לחשוב בתור {% equation %}\left(\left|0\right\rangle +\left|1\right\rangle \right)\left(\left|0\right\rangle +\left|1\right\rangle \right){% endequation %} שכזה). אז מה עושים? שערים "נשלטים". אלו שערים של שני קיוביטים, ולכן כאלו שמיוצגים על ידי מטריצה מסדר {% equation %}4\times4{% endequation %}. אני אציג שלושה כאלו - בשניהם הרעיון הוא "אם הקיוביט הראשון הוא 0 לא לעשות כלום, ואם הוא 1 אז להפעיל שער פאולי מסויים על הקיוביט השני". כשמפעילים {% equation %}X{% endequation %} השער נקרא CNOT וכשמפעילים {% equation %}Z{% endequation %} או {% equation %}S{% endequation %} השער נקרא, ובכן, Controlled-Z ו-Controlled-S, או בקיצור {% equation %}CZ{% endequation %} ו-{% equation %}CS{% endequation %}. דווקא {% equation %}CZ{% endequation %} ו-{% equation %}CS{% endequation %} יהיו השערים שבהם נשתמש עבור התוצאה הנוכחית למרות ש-CNOT הוא יותר פופולרי באופן כללי.

המטריצות של השערים הרלוונטיים הן {% equation %}CNOT=\left(\begin{array}{cccc} 1 & 0 & 0 & 0\\ 0 & 1 & 0 & 0\\ 0 & 0 & 0 & 1\\ 0 & 0 & 1 & 0 \end{array}\right),CZ=\left(\begin{array}{cccc} 1 & 0 & 0 & 0\\ 0 & 1 & 0 & 0\\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & -1 \end{array}\right),CS=\left(\begin{array}{cccc} 1 & 0 & 0 & 0\\ 0 & 1 & 0 & 0\\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & -i \end{array}\right){% endequation %} והן פשוטות למדי - הן פשוט <strong>מטריצות בלוקים אלכסוניות</strong> שבהן הבלוק הראשון הוא מטריצת היחידה והשני הוא {% equation %}X{% endequation %} או {% equation %}Z{% endequation %} או {% equation %}S{% endequation %}, בהתאמה. הפעולה שלהן מתוארת כך:
<ul>
 	<li>{% equation %}CNOT\left|00\right\rangle =\left|00\right\rangle {% endequation %}</li>
 	<li>{% equation %}CNOT\left|01\right\rangle =\left|01\right\rangle {% endequation %}</li>
 	<li>{% equation %}CNOT\left|10\right\rangle =\left|11\right\rangle {% endequation %}</li>
 	<li>{% equation %}CNOT\left|11\right\rangle =\left|10\right\rangle {% endequation %}</li>
</ul>
ו-
<ul>
 	<li>{% equation %}CZ\left|00\right\rangle =\left|00\right\rangle {% endequation %}</li>
 	<li>{% equation %}CZ\left|01\right\rangle =\left|01\right\rangle {% endequation %}</li>
 	<li>{% equation %}CZ\left|10\right\rangle =\left|10\right\rangle {% endequation %}</li>
 	<li>{% equation %}CZ\left|11\right\rangle =-\left|11\right\rangle {% endequation %}</li>
</ul>
ו-
<ul>
 	<li>{% equation %}CS\left|00\right\rangle =\left|00\right\rangle {% endequation %}</li>
 	<li>{% equation %}CS\left|01\right\rangle =\left|01\right\rangle {% endequation %}</li>
 	<li>{% equation %}CS\left|10\right\rangle =\left|10\right\rangle {% endequation %}</li>
 	<li>{% equation %}CS\left|11\right\rangle =-i\left|11\right\rangle {% endequation %}</li>
</ul>
שערי {% equation %}CZ{% endequation %} ו-{% equation %}CS{% endequation %} הם מאוד <strong>סימטריים</strong>, להבדיל מ-{% equation %}CNOT{% endequation %} - אפשר לחשוב עליהם בתור מעין שערי AND שכאלו, שמכפילים בקבוע ספציפי רק אם ה-AND של שני הקלטים הוא 1. במובן מסויים הסימטריה לא מפתיעה כי גם {% equation %}CNOT{% endequation %} הוא שער סימטרי, אם מסתכלים על הקלטים כשהם מיוצגים בבסיס קצת שונה, אבל לא ניכנס לזה כרגע.

וזהו, סיימנו להציג את כל השערים הקוונטיים שיהיו רלוונטיים לנו. עכשיו אפשר לחזור למה שקראתי לו "חבורת קליפורד" קודם; ההגדרה המלאה של החבורה היא בתור החבורה שנוצרת על ידי {% equation %}H,S{% endequation %} ו-{% equation %}\text{CNOT}{% endequation %}, ומשפט Gottesman--Knill תקף עבורה - כלומר, הוספת {% equation %}\text{CNOT}{% endequation %}-ים לא מקלקלת את היכולת שלנו לסמלץ מעגלים כאלו באופן קלאסי.

<strong>מעגל קוונטי</strong> הוא בסך הכל סדרה של השערים הללו. את הסדרה אפשר לחלק ל"שכבות" - בכל שכבה אנחנו דורשים שכל השערים יפעלו על קיוביטים שונים (כלומר, אין שני שערים באותה שכבה שפועלים על אותו קיוביט). למשל, ביצוע פעולת {% equation %}H^{\otimes n}{% endequation %} דורש {% equation %}n{% endequation %} שערי {% equation %}H{% endequation %}, אבל כולם יכולים להתבצע "בבת אחת", באותה שכבה. המחלקה SQC כוללת את כל המשפחות של מעגלים קוונטיים עם מספר שערים פולינומי שמספר השכבות שלהם הוא חסום על ידי קבוע שלא תלוי ב-{% equation %}n{% endequation %}.

עכשיו אנחנו מבינים את התוצאה: הוכחה ש-{% equation %}\text{SQC}\ne\text{NC}^{0}{% endequation %}. אבל עדיין צריך להבין את <strong>הבעיה</strong> שתהיה שייכת למחלקה אחת ולא לשניה.
<h2>בעיית ברנשטיין-וזירני</h2>
לפני שנציג את הבעיה שבה עוסק המאמר, בואו נעשה כמוהו ונסתכל קודם על בעיה פשוטה יותר, שגם התוכן שלה וגם הפתרון שלה יהיו דומים מאוד למה שנעשה בהמשך. הבעיה נקראת "בעיית ברנשטיין-וזירני" והיא עוסקת בלמידה של פונקציה לינארית "חבויה" שנתונה באמצעות אורקל. בואו ניכנס לפורמליזם.

באופן כללי אם {% equation %}F^{n}{% endequation %} הוא מרחב וקטורי ממימד {% equation %}n{% endequation %} מעל שדה {% equation %}F{% endequation %} ו-{% equation %}f:F^{n}\to F{% endequation %} היא פונקציונל לינארי ({% equation %}f\left(\lambda x+y\right)=\lambda f\left(x\right)+f\left(y\right){% endequation %}) אז קל לראות שקיים {% equation %}z\in F^{n}{% endequation %} כך ש-{% equation %}f\left(x\right)=z\cdot x=\sum_{i=1}^{n}z_{i}x_{i}{% endequation %} ; פשוט מגדירים {% equation %}z_{i}=f\left(e_{i}\right){% endequation %} כאשר {% equation %}e_{i}{% endequation %} הוקטור ב-{% equation %}F^{n}{% endequation %} שכולו 0 למעט 1 במקום {% equation %}i{% endequation %}. כעת,

{% equation %}f\left(x\right)=f\left(\sum_{i=1}^{n}x_{i}e_{i}\right)=\sum_{i=1}^{n}x_{i}f\left(e_{i}\right)=\sum_{i=1}^{n}z_{i}x_{i}{% endequation %}

כלומר, כל פונקציונל לינארי הוא בעצם "מכפלה סקלרית", ואם יש לנו דרך לחשב את {% equation %}f{% endequation %} על הערכים {% equation %}e_{1},\dots,e_{n}{% endequation %} נוכל תוך {% equation %}n{% endequation %} הפעלות של {% equation %}f{% endequation %} "ללמוד" מהו ה-{% equation %}z{% endequation %} שמגדיר את הפונקציונל הזה, ולא משנה באיזו דרך הפונקציונל נתון לנו. גם אם הוא נתון בתור "קופסה שחורה" שכל מה שאנחנו יכולים לעשות איתה הוא להכניס קלט ולקבל פלט, תוך {% equation %}n{% endequation %} שאילתות נלמד את {% equation %}f{% endequation %}.

בהקשר הקונקרטי שלנו, {% equation %}F=\mathbb{Z}_{2}{% endequation %} ו-{% equation %}f{% endequation %} נתונה באמצעות <strong>אורקל</strong>, שהוא הפורמליזם המתמטי של "קופסה שחורה" שכזו. לא קשה להוכיח, אחרי פירמול מתאים, ש<strong>חייבים</strong> {% equation %}n{% endequation %} שאילתות כדי ללמוד את {% equation %}z{% endequation %} - אחרי {% equation %}n-1{% endequation %} שאילתות, האינפורמציה שהתקבלה עדיין מתאימה לשני ערכים שונים של {% equation %}z{% endequation %}. מצד שני, אם האורקל שלנו הוא <strong>קוונטי</strong>, אפשר בקריאות - באופן דרסטי! מספיקה קריאה אחת בלבד לאורקל.

אבל מה זה "אורקל קוונטי"? אורקל רגיל הוא <strong>משהו</strong> שמקבל {% equation %}x{% endequation %} ומחזיר {% equation %}f\left(x\right){% endequation %}. האורקל הקוונטי שבו נשתמש כאן עושה משהו מוזר יותר: הוא מקבל סופרפוזיציה {% equation %}\sum_{x\in\mathbb{Z}_{2}^{n}}a_{x}\left|x\right\rangle {% endequation %} ומחזיר סופרפוזיציה {% equation %}\sum_{x\in\mathbb{Z}_{2}^{n}}a_{x}\left(-1\right)^{f\left(x\right)}\left|x\right\rangle {% endequation %}. באופן קומפקטי, אם אסמן אותו {% equation %}U_{f}{% endequation %}, הוא אופרטור אוניטרי שמבצע את הפעולה הבאה: {% equation %}U_{f}\left|x\right\rangle =\left(-1\right)^{f\left(x\right)}\left|x\right\rangle {% endequation %}.

אפשר לטעון שהאורקל הזה הוא מטבעו חזק יותר מאורקל רגיל - אבל העניין הוא שבמימושים מעשיים של אורקל כזה, ה"עבודה" שנדרשת ממנו לא תהיה שונה מהעבודה שנדרשת מאורקל "רגיל" שמחשב את {% equation %}f{% endequation %}. למרבה השמחה אני לא צריך להיכנס לעובי הטיעון הזה בגלל שמה שהמאמר החדש עושה הוא בדיוק <strong>לבטל את השימוש באורקל</strong>; הוא מעין ניסוח מחודש, מתוחכם יותר, של ברנשטיין-וזירני בגרסה שבה הכל נתון במפורש.

עדיין, איך משתמשים באורקל הקוונטי כדי לפתור את ברנשטיין-וזירני בקריאה אחת בלבד? המעגל שפותר את הבעיה הוא פשוט להחריד:

{% equation %}\left|z\right\rangle =H^{\otimes n}U_{f}H^{\otimes n}\left|0\right\rangle {% endequation %}

המעגל הזה עושה שלושה דברים: מתחילים מהמצב {% equation %}\left|0\right\rangle {% endequation %} ומפעילים עליו {% equation %}H^{\otimes n}{% endequation %}, מה שכפי שכבר ראינו מייצר את הסופרפוזיציה האחידה של כל המצבים הקוונטיים האפשריים על {% equation %}n{% endequation %} קיוביטים. אחר כך מפעילים את {% equation %}U_{f}{% endequation %} על המצב הזה - מחשבים "במקביל" את {% equation %}f{% endequation %} על כל הקלטים האפשריים. לבסוף, "מקפלים חזרה" את הסופרפוזיציה באמצעות עוד הפעלה של {% equation %}H^{\otimes n}{% endequation %} ובאופן פלאי היא תתקפל למצב קוונטי אחד ויחיד - {% equation %}\left|z\right\rangle {% endequation %} - שמקודד בדיוק את הוקטור שחיפשנו. כל מה שנשאר בסיום הוא לבצע מדידה, ומכיוון שאנחנו במצב בסיס אחד ויחיד, המדידה תחזיר את התשובה הנכונה בהסתברות 1: האלגוריתם הוא אפילו לא הסתברותי באופיו, הצלחה תמיד מובטחת. זה יפהפה.

למה זה עובד? בשביל להבין את זה צריך לחזור לשאלה ששאלתי קודם - מהו באופן כללי {% equation %}H^{\otimes n}\left|y\right\rangle {% endequation %}, עבור {% equation %}\left|y\right\rangle {% endequation %} שהוא לא בהכרח {% equation %}\left|0\right\rangle {% endequation %}? לשם כך בואו נזכיר לעצמנו את ההגדרה של {% equation %}H{% endequation %}:
<ul>
 	<li>{% equation %}H\left|0\right\rangle =\left|0\right\rangle +\left|1\right\rangle {% endequation %}</li>
 	<li>{% equation %}H\left|1\right\rangle =\left|0\right\rangle -\left|1\right\rangle {% endequation %}</li>
</ul>
אפשר לחשוב על {% equation %}H{% endequation %} שפועל על וקטור של {% equation %}n{% endequation %} קיוביטים באופן הבא: הוא פועל על קיוביט ספציפי (סימנתי ב-{% equation %}H^{i}{% endequation %} את שער {% equation %}H{% endequation %} שפועל על הקיוביט ה-{% equation %}i{% endequation %}) והוא מייצר שני וקטורים מוקטור הקלט - אחד שבו הקיוביט נותר כמות שהוא, ואחד שבו הקיוביט התהפך. בשלושה מבין ארבעת המקרים הללו הוא לא משנה את הסימן של הוקטור, אבל במקרה אחד הוא מכפיל את הסימן של הוקטור במינוס 1 - במקרה שבו הקיוביט שעליו הוא פועל הוא 1, והוא <strong>הותיר אותו כמות שהוא</strong>.

כעת, נניח ש-{% equation %}\left|y\right\rangle =\left|0110\right\rangle {% endequation %}. כשאנחנו מפעילים את {% equation %}H^{\otimes4}{% endequation %} על {% equation %}\left|y\right\rangle {% endequation %} נקבל סופרפוזיציה של מצבים. מה יהיה הסימן של המצב {% equation %}\left|1100\right\rangle {% endequation %}? לשם כך, בואו נבין מה ה"מסלול" שבו נוצר המצב הזה. הפעלנו {% equation %}H^{1}{% endequation %} על {% equation %}\left|y\right\rangle {% endequation %} והחלטנו להפוך את הקיוביט הראשון ל-{% equation %}1{% endequation %} - זה לא כופל במינוס 1 כי הקיוביט לא היה 1 קודם. אחר כך הפעלנו את {% equation %}H^{2}{% endequation %} על התוצאה, {% equation %}\left|1110\right\rangle {% endequation %} והחלטנו <strong>לא</strong> להפוך את הקיוביט השני, מה שמשאיר אותנו ב-{% equation %}\left|1110\right\rangle {% endequation %} ומכפיל את המקדם שלנו ב-{% equation %}-1{% endequation %}. את הקיוביט השלישי בחרנו להפוך (<strong>לא</strong> מכפיל במינוס 1) ואת הרביעי בחרנו להותיר כמות שהוא, כך שבסופו של דבר קיבלנו {% equation %}-\left|1100\right\rangle {% endequation %}.

אם כן, כדי לדעת מה יהיה הסימן של {% equation %}\left|x\right\rangle {% endequation %} שהתקבל מ-{% equation %}\left|y\right\rangle {% endequation %} צריך לעשות שני דברים:
<ul>
 	<li>לבדוק אילו קיוביטים הם 1 ב-{% equation %}\left|y\right\rangle {% endequation %} ונשארו כאלו גם ב-{% equation %}\left|x\right\rangle {% endequation %}.</li>
 	<li>לספור האם המספר שלהם הוא זוגי (ואז ביצענו מספר זוגי של מכפלות במינוס 1 וכלום לא השתנה) או אי-זוגי.</li>
</ul>
לשני אלו יחד יש תיאור פשוט במיוחד: אנחנו מתעניינים ב-{% equation %}x\cdot y{% endequation %} מודולו 2 - וזה, במקרה, בדיוק גם מה שברנשטיין וזירני מתעסק בו. פורמלית:

{% equation %}H^{\otimes n}\left|y\right\rangle =\sum_{x\in\mathbb{Z}_{2}^{n}}\left(-1\right)^{x\cdot y}\left|x\right\rangle {% endequation %}

ועכשיו קל לראות למה המעגל הקוונטי עובד:

{% equation %}H^{\otimes n}U_{f}H^{\otimes n}\left|0\right\rangle =H^{\otimes n}U_{f}\sum_{y}\left|y\right\rangle ={% endequation %}

{% equation %}=H^{\otimes n}\sum_{y}\left(-1\right)^{z\cdot y}\left|y\right\rangle =\sum_{y}\sum_{x}\left(-1\right)^{z\cdot y}\left(-1\right)^{x\cdot y}\left|x\right\rangle =\sum_{x}\left(\sum_{y}\left(-1\right)^{\left(x+z\right)\cdot y}\right)\left|x\right\rangle {% endequation %}

כדי להבין מה קורה עכשיו, בואו נקבע את {% equation %}x{% endequation %} להיות משהו, ונבדוק את הערך של המחובר הפנימי, {% equation %}\sum_{y}\left(-1\right)^{\left(x+z\right)\cdot y}{% endequation %}. אולי יהיה יותר קל אם במקום {% equation %}x+z{% endequation %} יופיע שם {% equation %}x-z{% endequation %}, מה ששקול לחלוטין כי אנחנו מעל {% equation %}\mathbb{Z}_{2}{% endequation %} ולכן {% equation %}1=-1{% endequation %}. אז מהו {% equation %}\sum_{y}\left(-1\right)^{\left(x-z\right)\cdot y}{% endequation %}? יש פה שתי אפשרויות. ראשית, אם {% equation %}x=z{% endequation %} אז נקבל את הסכום {% equation %}\sum_{y}1=2^{n}{% endequation %} כי {% equation %}y{% endequation %} רץ על כל {% equation %}\left\{ 0,1\right\} ^{n}{% endequation %}. כעת, אם {% equation %}x\ne z{% endequation %} ולו בקואורדינטה בודדת אז נקבל 0. למה? בואו נניח שההבדל הוא בקואורדינטה הראשונה, כלומר {% equation %}x-z=1w^{\prime}{% endequation %} כך ש-{% equation %}w^{\prime}{% endequation %} היא מחרוזת של {% equation %}n-1{% endequation %} ביטים. עכשיו אפשר לחלק את כל ה-{% equation %}y{% endequation %}-ים לזוגות זוגות של איברים מהצורה {% equation %}0y^{\prime}{% endequation %} ו-{% equation %}1y^{\prime}{% endequation %} כך ש-{% equation %}y^{\prime}{% endequation %} היא מחרוזת של {% equation %}n-1{% endequation %} ביטים; בבירור {% equation %}\left(0y^{\prime}\right)\cdot\left(1w^{\prime}\right)\ne\left(1y^{\prime}\right)\cdot\left(1w^{\prime}\right){% endequation %} כי באגף שמאל הקואורדינטה הראשונה לא תורמת כלום למכפלה הסקלרית, ובאגף ימין הוא תורמת 1. לכן {% equation %}\left(-1\right)^{\left(0y^{\prime}\right)\cdot\left(1w^{\prime}\right)}+\left(-1\right)^{\left(1y^{\prime}\right)\cdot\left(1w^{\prime}\right)}=0{% endequation %} ולכן כל הסכום {% equation %}\sum_{y}\left(-1\right)^{\left(x-z\right)\cdot y}{% endequation %} יהיה שווה אפס כי הוא סכום של זוגות של איברים שסכומם הוא אפס.

המסקנה? {% equation %}\sum_{x}\left(\sum_{y}\left(-1\right)^{\left(x-z\right)\cdot y}\right)\left|x\right\rangle =2^{n}\left|z\right\rangle {% endequation %}, אבל הקבוע לא באמת צריך להיות שם. זוכרים שאני מחפף בכתיבת הקבועים? כשאני כותב {% equation %}H^{\otimes n}\left|0\right\rangle =\sum_{x}\left|x\right\rangle {% endequation %} זה שקר; אני באמת צריך לכתוב {% equation %}\left(\frac{1}{\sqrt{2}}\right)^{n}\sum_{x}\left|x\right\rangle {% endequation %}; וגם ההפעלה השניה של {% equation %}H^{\otimes n}{% endequation %} מכפילה בקבוע הזה, כך שבסך הכל הכפלנו בקבוע {% equation %}\frac{1}{2^{n}}{% endequation %} שמתקזז בדיוק עם ה-{% equation %}2^{n}{% endequation %} שהתווסף לנו. המסקנה הסופית היא ש-{% equation %}H^{\otimes n}U_{f}H^{\otimes n}\left|0\right\rangle =\left|z\right\rangle {% endequation %}, כפי שהבטחתי.
<h2>בעיית הפונקציה הלינארית החבויה</h2>
עכשיו נעבור אל הבעיה שהמאמר מתאר. נתחיל עם גרסה פשוטה שלה, ואז נסבך אותה עוד טיפה מסיבה שתכף אבהיר. הרעיון הבסיסי זהה לברנשטיין-וזיראני: יש פונקציה לינארית שמוגדרת על ידי כפל סקלרי בוקטור כלשהו - יש למצוא את הוקטור. ההבדל המהותי? הפונקציה <strong>לא נתונה על ידי אורקל</strong> אלא על ידי פונקציה אחרת, מסובכת יותר, ש"מחביאה" בתוך ההגדרה שלה את הפונקציה הפשוטה.

הפונקציה המורכבת יותר תהיה סוג של <strong>תבנית ריבועית</strong> עם הזזה אפינית. לא אומר לכם כלום? זו פשוט פונקציה {% equation %}q\left(x\right):\mathbb{Z}_{2}^{n}\to\mathbb{Z}_{4}{% endequation %} (שימו לב: הטווח הוא {% equation %}\mathbb{Z}_{4}{% endequation %} ולא {% equation %}\mathbb{Z}_{2}{% endequation %}) שמוגדרת בעזרת מטריצה {% equation %}A\in\mathbb{Z}_{2}^{n\times n}{% endequation %} ווקטור {% equation %}b\in\mathbb{Z}_{2}^{n}{% endequation %} כך ש-

{% equation %}q\left(x\right)=2x^{t}Ax+bx=2\sum_{1\le i&lt;j\le n}A_{i,j}x_{i}x_{j}+\sum_{i=1}^{n}b_{i}x_{i}{% endequation %}

הפונקציה {% equation %}q{% endequation %} נתונה במפורש; אנחנו לא מתעניינים בדיוק בה, אלא בפונקציה לינארית {% equation %}f{% endequation %} שהיא <strong>הצמצום</strong> של {% equation %}q{% endequation %} לתת-מרחב מסויים של {% equation %}\mathbb{Z}_{2}^{n}{% endequation %}. תת-המרחב מוגדר כך:

{% equation %}\mathcal{L}_{q}=\left\{ x\in\mathbb{Z}_{2}^{n}\ |\ \forall y\in\mathbb{Z}_{2}^{n}:q\left(x+y\right)=q\left(x\right)+q\left(y\right)\right\} {% endequation %}

כלומר, {% equation %}\mathcal{L}_{q}{% endequation %} כולל את כל הוקטורים ב-{% equation %}\mathbb{Z}_{2}^{n}{% endequation %} שעבורם {% equation %}q{% endequation %} "נראית לינארית" ביחס ל<strong>כל</strong> הוקטורים ב-{% equation %}\mathbb{Z}_{2}^{n}{% endequation %}. אנחנו רוצים להשתכנע ש-{% equation %}\mathcal{L}_{q}{% endequation %} הוא באמת תת-מרחב לינארי וש-{% equation %}q{% endequation %} מצומצמת אליו היא פונקציה לינארית. מכיוון שאנחנו מעל {% equation %}\mathbb{Z}_{2}{% endequation %}, כלומר הסקלרים היחידים הם 0 ו-1, העבודה שלנו קלה יחסית: כדי להוכיח שקבוצה היא תת-מרחב מספיק להראות שהיא סגורה לחיבור, וכדי להראות שפונקציה היא לינארית מספיק להראות שהיא מקיימת {% equation %}q\left(x+y\right)=q\left(x\right)+q\left(y\right){% endequation %}, מה שאוטומטית הולך להתקיים עבור אברי {% equation %}\mathcal{L}_{q}{% endequation %} כי כך המרחב הזה מוגדר.

כדי להראות ש-{% equation %}\mathcal{L}_{q}{% endequation %} הוא מרחב וקטורי צריך להראות שאם {% equation %}x,z\in\mathcal{L}_{q}{% endequation %} אז גם {% equation %}x+z\in\mathcal{L}_{q}{% endequation %}, כלומר שלכל {% equation %}y{% endequation %} מתקיים {% equation %}q\left(\left(x+z\right)+y\right)=q\left(x+z\right)+q\left(y\right){% endequation %}. כדי לראות את זה, נשים לב לכך ש-{% equation %}q\left(\left(x+z\right)+y\right)=q\left(x+\left(z+y\right)\right){% endequation %} ומכיוון ש-{% equation %}x\in\mathcal{L}_{q}{% endequation %} נסיק ש

{% equation %}q\left(x+\left(z+y\right)\right)=q\left(x\right)+q\left(z+y\right){% endequation %}

ומכיוון ש-{% equation %}z\in\mathcal{L}_{q}{% endequation %} אפשר לפתוח גם את המחובר השמאלי ולקבל

{% equation %}q\left(x\right)+q\left(z+y\right)=q\left(x\right)+q\left(z\right)+q\left(y\right){% endequation %}

ולסיום, {% equation %}q\left(x\right)+q\left(z\right)=q\left(x+z\right){% endequation %} כמובן שמתקיים בגלל ש-{% equation %}x\in\mathcal{L}_{q}{% endequation %}. זה מסיים את ההוכחה הזו.

אם נצמצם את {% equation %}q{% endequation %} אל {% equation %}\mathcal{L}_{q}{% endequation %} עדיין קשה יהיה לקרוא למה שנקבל "פונקציה לינארית" כי הטווח של פונקציה לינארית צריך להיות מרחב וקטורי בעצמו מעל השדה שלנו, במקרה הזה {% equation %}\mathbb{Z}_{2}{% endequation %}, אבל {% equation %}\mathbb{Z}_{4}{% endequation %} אינו כזה (כי אם {% equation %}V{% endequation %} מרחב וקטורי מעל {% equation %}\mathbb{Z}_{2}{% endequation %} אז {% equation %}v+v=\left(1+1\right)v=0\cdot v=0{% endequation %}, אבל ב-{% equation %}\mathbb{Z}_{4}{% endequation %} קיים איבר מסדר 4). מה שכן קל לראות הוא שדה-פקטו, {% equation %}q{% endequation %} מחזירה רק 0 או 2 על אברי {% equation %}\mathcal{L}_{q}{% endequation %}, כי {% equation %}q\left(x\right)+q\left(x\right)=q\left(x+x\right)=q\left(0\right)=0{% endequation %}, כלומר {% equation %}2q\left(x\right)=0{% endequation %} מה שקורה רק אם {% equation %}q\left(x\right)\in\left\{ 0,2\right\} {% endequation %}. לכן אפשר להגדיר פונקציה {% equation %}f:\mathcal{L}_{q}\to\mathbb{Z}_{2}{% endequation %} על ידי {% equation %}f\left(x\right)=\frac{q\left(x\right)}{2}{% endequation %} ו<strong>זו</strong> תהיה הפונקציה הלינארית שלנו, כלומר קיים {% equation %}z\in\mathbb{Z}_{2}^{n}{% endequation %} כך ש-{% equation %}f\left(x\right)=z\cdot x{% endequation %}, מה שאומר ש-{% equation %}q\left(x\right)=2z\cdot x{% endequation %} לכל {% equation %}x\in\mathcal{L}_{q}{% endequation %}. הנה האתגר שלנו במפורש - למצוא את ה-{% equation %}z{% endequation %} הזה. לבעיה הזו המאמר קורא Hidden Linear Function Problem, והיא <strong>כמעט</strong> הבעיה ששייכת ל-SQC אבל לא ל-{% equation %}\text{NC}^{0}{% endequation %}; הבעיה פה תהיה שהבעיה לא שייכת ל-SQC ויהיה צורך בהגבלה נוספת עליה כדי להכניס אותה ל-SQC למרות שזה לא יהיה מספיק כדי להכניס אותה ל-{% equation %}\text{NC}^{0}{% endequation %}.

המעגל הקוונטי שפותר את הבעיה הזו יהיה שוב פשוט עד להפתיע, ובערך מהצורה {% equation %}H^{\otimes n}U_{q}H^{\otimes n}\left|0\right\rangle {% endequation %}. אני אומר "בערך" כי החלק של ה-{% equation %}U_{q}{% endequation %} הוא עכשיו לא אורקל אלא מעגל קונקרטי שמקבל כקלט, בנוסף ל-{% equation %}H^{\otimes n}\left|0\right\rangle {% endequation %}, גם את {% equation %}A{% endequation %} ו-{% equation %}b{% endequation %}. האפקט של {% equation %}U_{q}{% endequation %} על {% equation %}\left|x\right\rangle {% endequation %} מאוד דומה לזה של ברנשטיין וזירני אבל מביא בחשבון את זה שהפעם יש <strong>ארבעה</strong> פלטים אפשריים שונים של {% equation %}q{% endequation %} על קלט כללי, ולכן המקדם שהוא מצמיד ל-{% equation %}\left|x\right\rangle {% endequation %} יהיה בעל אחד מבין ארבעה ערכים מובחנים:

{% equation %}U_{q}\left|x\right\rangle =i^{q\left(x\right)}\left|x\right\rangle {% endequation %}

כאשר {% equation %}i{% endequation %} הוא מספר מדומה שמקיים {% equation %}i^{2}=-1{% endequation %}.

עוד דבר שהוא קצת שונה הוא שהפעם לא יתקיים {% equation %}H^{\otimes n}U_{q}H^{\otimes n}\left|0\right\rangle =\left|z\right\rangle {% endequation %}; הפלט יהיה סופרפוזיציה של מצבים. רק ש<strong>כל</strong> המצבים הללו יתאימו לערכים אפשריים של {% equation %}z{% endequation %} שפותר את הבעיה; הפעם פשוט יש יותר מערך אחד כזה.

אז יש לנו שתי שאלות:
<ol>
 	<li>איך אנחנו מממשים את {% equation %}U_{q}{% endequation %} עם שערים קוונטיים?</li>
 	<li>למה בדיוק כל איבר שכלול ב-{% equation %}H^{\otimes n}U_{q}H^{\otimes n}\left|0\right\rangle {% endequation %} הוא פתרון?</li>
</ol>
התשובה ל-1 פשוטה ויפה: {% equation %}U_{q}=\bigotimes_{j}S_{j}^{b_{j}}\cdot\prod_{1\le i\le j\le n}CZ_{i,j}^{A_{i,j}}{% endequation %}, אבל בואו נסביר מה זה אומר.

שער {% equation %}CZ_{i,j}{% endequation %} מפעיל Controlled-Z על {% equation %}i,j{% endequation %} כש-{% equation %}i{% endequation %} הוא קיוביט ה"בקרה". כשאני מסמן {% equation %}CZ_{i,j}^{A_{i,j}}{% endequation %} פירוש הדבר הוא שאני מוסיף <strong>עוד התניה</strong> על השער הזה - אם {% equation %}A_{i,j}=1{% endequation %} אז הוא יופעל, ואם {% equation %}A_{i,j}=0{% endequation %} הוא לא יופעל; דה פקטו אפשר לקרוא לזה שער {% equation %}CCZ{% endequation %}. הסימון {% equation %}\prod{% endequation %} בא לומר שאני מפעיל את השערים הללו סדרתית ולא "בבת אחת", למרות שאם אפשר למקבל חלק מההפעלות מן הסתם נעשה את זה.

אחרי שערי ה-{% equation %}CZ{% endequation %} מגיעה הפעלה "בבת אחת" של שערי פאזה: {% equation %}S_{j}{% endequation %} מסמן הפעלה של שער פאזה, כלומר {% equation %}\left(\begin{array}{cc} 1 & 0\\ 0 & -i \end{array}\right){% endequation %}, על קיוביט מספר {% equation %}j{% endequation %}. רק שכאן גם שערי הפאזה מותנים בכך ש-{% equation %}b_{j}=1{% endequation %} ואחרת הם לא מופעלים; קראתי לשער כזה {% equation %}CS{% endequation %} בהתחלה.

עכשיו, למה שיתקיים {% equation %}U_{q}\left|x\right\rangle =i^{q\left(x\right)}\left|x\right\rangle {% endequation %}?

ראשית, {% equation %}CZ_{i,j}\left|x\right\rangle =\left(-1\right)^{x_{i}\cdot x_{j}}\left|x\right\rangle {% endequation %} - זוכרים שאמרתי ש-{% equation %}CZ{% endequation %} הוא סוג של AND? כאן רואים את זה. על כן, {% equation %}CZ_{i,j}^{A_{i,j}}\left|x\right\rangle =\left(-1\right)^{A_{i,j}x_{i}\cdot x_{j}}\left|x\right\rangle {% endequation %}. מכיוון ש-{% equation %}i^{2}=-1{% endequation %} אפשר גם לכתוב {% equation %}CZ_{i,j}^{A_{i,j}}\left|x\right\rangle =i^{2A_{i,j}x_{i}\cdot x_{j}}\left|x\right\rangle {% endequation %}

שנית, {% equation %}S_{j}^{b_{j}}\left|x\right\rangle =i^{b_{j}\cdot x_{j}}\left|x\right\rangle {% endequation %}; גם שער {% equation %}CS{% endequation %} הוא מעין AND, הפעם בין {% equation %}b_{i}{% endequation %} ו-{% equation %}x_{i}{% endequation %}.

משני אלו נקבל:

{% equation %}U_{q}\left|x\right\rangle =i^{q\left(x\right)}\left|x\right\rangle =\prod_{i,j}i^{\left(2A_{i,j}x_{i}\cdot x_{j}\right)}\prod_{j}i^{b_{j}\cdot x_{j}}\left|x\right\rangle {% endequation %}

{% equation %}=i^{\left(2\sum_{i,j}A_{i,j}x_{i}x_{j}+\sum_{j}b_{j}x_{j}\right)}\left|x\right\rangle =i^{q\left(x\right)}\left|x\right\rangle {% endequation %}

שזה בדיוק מה שרצינו. האורקל נעלם; אנחנו רואים איך אפשר לממש את האפקט {% equation %}U_{q}\left|x\right\rangle =i^{q\left(x\right)}\left|x\right\rangle {% endequation %} עם שערים קונקרטיים לחלוטין. הבעיה היחידה היא <strong>עומק</strong> המעגל שמבצע את החישוב, ונדבר על זה עוד מעט.

עכשיו ננסה להבין איך נראה המצב הקוונטי {% equation %}H^{\otimes n}U_{q}H^{\otimes n}\left|0\right\rangle {% endequation %}. ה-{% equation %}H^{\otimes n}\left|0\right\rangle {% endequation %} שבהתחלה מייצר את הסופרפוזיציה האחידה, {% equation %}\sum_{x\in\mathbb{Z}_{2}^{n}}\left|x\right\rangle {% endequation %}, וה-{% equation %}U_{q}{% endequation %} שאחר כך מייצר לנו את הסופרפוזיציה {% equation %}\sum_{y\in\mathbb{Z}_{2}^{n}}i^{q\left(y\right)}\left|y\right\rangle {% endequation %}. מה עכשיו?

יותר מוקדם בפוסט ראינו ש-{% equation %}H^{\otimes n}\left|y\right\rangle =\sum_{z\in\mathbb{Z}_{2}^{n}}\left(-1\right)^{z\cdot y}\left|z\right\rangle {% endequation %}. אם נשתמש בזה כאן, נקבל שהסופרפוזיציה שמגיעים אליה בסיום היא

{% equation %}\sum_{y\in\mathbb{Z}_{2}^{n}}i^{q\left(y\right)}\left(\sum_{z\in\mathbb{Z}_{2}^{n}}\left(-1\right)^{z\cdot y}\left|z\right\rangle \right){% endequation %}

או, אם נחליף את סדר הסכימה:

{% equation %}\sum_{z\in\mathbb{Z}_{2}^{n}}\left(\sum_{y\in\mathbb{Z}_{2}^{n}}i^{q\left(y\right)}\left(-1\right)^{z\cdot y}\right)\left|z\right\rangle {% endequation %}

כלומר, המקדם של {% equation %}\left|z\right\rangle {% endequation %} בסופרפוזיציה שבסיום הוא הביטוי {% equation %}\sum_{y\in\mathbb{Z}_{2}^{n}}i^{q\left(y\right)}\left(-1\right)^{z\cdot y}{% endequation %}. כדי להקל על חישוב הביטוי הזה, המאמר מאמץ את הסימון הבא, עבור כל תת-מרחב לינארי {% equation %}\mathcal{L}{% endequation %} של {% equation %}\mathbb{Z}_{2}^{n}{% endequation %}:

{% equation %}\Gamma\left(\mathcal{L},z\right)=\sum_{y\in\mathbb{Z}_{2}^{n}}i^{q\left(y\right)}\left(-1\right)^{z\cdot y}{% endequation %}

אז המטרה שלנו היא להבין מהו {% equation %}\Gamma\left(\mathbb{Z}_{2}^{n},z\right){% endequation %}. המאמר נכנס לחישוב בפירוט, אבל לנו מספיק להבין כרגע למה זה אפס אם {% equation %}z{% endequation %} הוא לא פתרון לבעיית הפונקציה הלינארית החבויה ומשהו שונה מאפס אם הוא כן. לשם כך, המאמר נוקט בגישה הבאה: ניקח משלים ישר {% equation %}\mathcal{K}{% endequation %} <strong>כלשהו</strong> של {% equation %}\mathcal{L}_{q}{% endequation %}, כלומר תת-מרחב וקטורי של {% equation %}\mathbb{Z}_{2}^{n}{% endequation %} כך שמתקיים {% equation %}\mathbb{Z}_{2}^{n}=\mathcal{L}_{q}\oplus\mathcal{K}{% endequation %}. כעת ניתן להוכיח שמתקיים

{% equation %}\Gamma\left(\mathbb{Z}_{2}^{n},z\right)=\Gamma\left(\mathcal{L}_{q},z\right)\cdot\Gamma\left(\mathcal{K},z\right){% endequation %}

האינטואיציה לכך פשוטה: כל {% equation %}y\in\mathbb{Z}_{2}^{n}{% endequation %} אפשר להציג <strong>באופן יחיד </strong>בתור {% equation %}y=y_{1}+y_{2}{% endequation %} כך ש-{% equation %}y_{1}\in\mathcal{L}_{q}{% endequation %} ו-{% equation %}y_{2}\in\mathcal{K}{% endequation %}. כעת קחו את הביטוי {% equation %}\Gamma\left(\mathcal{L},z\right)=\sum_{y\in\mathbb{Z}_{2}^{n}}i^{q\left(y\right)}\left(-1\right)^{z\cdot y}{% endequation %} והציבו {% equation %}y_{1}+y_{2}{% endequation %} במקום {% equation %}y{% endequation %}: שימו לב ש-{% equation %}q\left(y_{1}+y_{2}\right)=q\left(y_{1}\right)+q\left(y_{2}\right){% endequation %} כי {% equation %}y_{1}\in\mathcal{L}_{q}{% endequation %} וזו בדיוק התכונה המייחדת של {% equation %}\mathcal{L}_{q}{% endequation %}, שהקסם הזה מתקיים בה.

בואו נשתכנע עכשיו ש-{% equation %}\Gamma\left(\mathcal{L}_{q},z\right){% endequation %} מתאפס אם ורק אם {% equation %}z{% endequation %} הוא לא פתרון של בעיית הפונקציה הלינארית החבויה. הרעיון הוא כזה: אנחנו רוצים לחשב את {% equation %}\sum_{y\in\mathcal{L}_{q}}i^{q\left(y\right)}\left(-1\right)^{z\cdot y}{% endequation %} ויכולים להיעזר בכך שאנחנו יודעים שמעל {% equation %}\mathcal{L}_{q}{% endequation %}, הפונקציה {% equation %}q\left(y\right){% endequation %} מתנהגת כמו מכפלה באיבר ספציפי שנקרא לו {% equation %}z^{\prime}{% endequation %}. פורמלית: {% equation %}q\left(y\right)=2z^{\prime}\cdot y{% endequation %}. לכן נקבל:

{% equation %}\Gamma\left(\mathcal{L}_{q},z\right)=\sum_{y\in\mathcal{L}_{q}}i^{2z^{\prime}\cdot y}\left(-1\right)^{z\cdot y}=\sum_{y\in\mathcal{L}_{q}}\left(-1\right)^{z^{\prime}\cdot y}\left(-1\right)^{z\cdot y}=\sum_{y\in\mathcal{L}_{q}}\left(-1\right)^{\left(z-z^{\prime}\right)\cdot y}{% endequation %}

קיבלנו כמעט את אותו הדבר עם ברנשטיין-וזירני, רק ששם הסכום רץ על כל {% equation %}\mathbb{Z}_{2}^{n}{% endequation %} וכאן הוא רץ רק על {% equation %}\mathcal{L}_{q}{% endequation %}. בברנשטיין-וזירני הסכום לא התאפס רק אם המכפלה הפנימית <strong>כן</strong> התאפסה לכל {% equation %}y{% endequation %}; מכיוון ששם {% equation %}y{% endequation %} רץ על כל {% equation %}\mathbb{Z}_{2}^{n}{% endequation %} זה קרה רק אם {% equation %}z-z^{\prime}{% endequation %} היה וקטור האפס, אבל עכשיו {% equation %}y{% endequation %} רץ רק על {% equation %}\mathcal{L}_{q}{% endequation %} ולכן המכפלה הפנימית יכולה להתאפס לעוד איברים; כזכור, משתמשים בסימון {% equation %}\mathcal{L}_{q}^{\perp}{% endequation %} כדי לתאר את קבוצת האיברים הזו - <strong>המרחב האורתוגונלי</strong> של {% equation %}\mathcal{L}_{q}{% endequation %}. אז אם {% equation %}z-z^{\prime}\in\mathcal{L}_{q}^{\perp}{% endequation %}, הסכום לא מתאפס. במקרה שבו {% equation %}z-z^{\prime}\in\mathcal{L}_{q}^{\perp}{% endequation %}, לכל {% equation %}y\in\mathcal{L}_{q}{% endequation %} מתקיים {% equation %}\left(z-z^{\prime}\right)y=0{% endequation %}, כלומר {% equation %}zy=z^{\prime}y{% endequation %}, כלומר {% equation %}q\left(y\right)=2z\cdot y{% endequation %} וקיבלנו שגם {% equation %}z{% endequation %} הוא פתרון לבעיית הפונקציה הלינארית החבויה - כפי שרצינו.

מה קורה אם {% equation %}z-z^{\prime}\notin\mathcal{L}_{q}^{\perp}{% endequation %}? במקרה הזה, קיים {% equation %}a\in\mathcal{L}_{q}{% endequation %} כך ש-{% equation %}\left(z-z^{\prime}\right)a=1{% endequation %}, ועכשיו אפשר לחלק את אברי {% equation %}\mathcal{L}_{q}{% endequation %} לזוגות-זוגות: לכל {% equation %}y\in\mathcal{L}_{q}{% endequation %}, בן הזוג שלו יהיה {% equation %}y+a{% endequation %} (ובן הזוג של {% equation %}y+a{% endequation %} יהיה, ובכן, {% equation %}\left(y+a\right)+a=y+2a=y{% endequation %} כי אנחנו מעל {% equation %}\mathbb{Z}_{2}{% endequation %}). בבירור {% equation %}\left(z-z^{\prime}\right)\left(y+a\right)=\left(z-z^{\prime}\right)y+1{% endequation %} כך ששני האיברים הללו מחזירים ערך שונה בכפל סקלרי ב-{% equation %}z-z^{\prime}{% endequation %} ולכן {% equation %}\left(-1\right)^{\left(z-z^{\prime}\right)y}+\left(-1\right)^{\left(z-z^{\prime}\right)\left(y+a\right)}=0{% endequation %} וקיבלנו ש-{% equation %}\Gamma\left(\mathcal{L}_{q},z\right)=0{% endequation %} אם {% equation %}z-z^{\prime}\notin\mathcal{L}_{q}^{\perp}{% endequation %}, כלומר במקרה שבו {% equation %}z{% endequation %} <strong>אינו</strong> פתרון של בעיית הפונקציה הלינארית החבויה.
<h2>סיכום ביניים זריז ופרידה שהיא בריחה מהירה</h2>
בשלב הזה כיסינו את החלק מהמאמר שקל לתאר ודורש רק קצת אלגברה לינארית נחמדה. ההמשך קצת פחות נחמד והפוסט הזה כבר ארוך דיו, כך שלא אמשיך לתאר את המאמר כאן. עדיין, מה עוד נשאר לעשות?

ראשית, הבעיה עצמה: מה שקראתי לו "בעיית הפונקציה הלינארית החבויה" היא אמנם בעיה שלא שייכת ל-{% equation %}\text{NC}^{0}{% endequation %} אבל גם ל-{% equation %}\text{SQC}{% endequation %} היא כנראה לא שייכת. כדי לקבל בעיה ששייכת ל-{% equation %}\text{SQL}{% endequation %} צריך להגביל את הסיטואציה קצת יותר. בבעיית הפונקציה הלינארית החבויה יש לנו תבנית ריבועית שנתונה על ידי מטריצה {% equation %}A\in\mathbb{Z}_{2}^{n\times n}{% endequation %} ווקטור {% equation %}b\in\mathbb{Z}_{2}^{n}{% endequation %}. ההגבלה הנוספת היא הדרישה שיתקיים {% equation %}A_{i,j}=0{% endequation %} עבור רוב הכניסות של {% equation %}A{% endequation %}. הנה הפורמליזם: בואו נסתכל על השריג {% equation %}\mathbb{Z}_{N}\times\mathbb{Z}_{N}{% endequation %} עבור {% equation %}N{% endequation %} כלשהו; כל נקודה בשריג היא מהצורה {% equation %}\left(i,j\right){% endequation %} כך ש-{% equation %}0\le i,j\le N-1{% endequation %} - יש בסך הכל {% equation %}N^{2}{% endequation %} נקודות כאלו. נבחר {% equation %}n=N^{2}{% endequation %} (זה מספר השורות והעמודות של {% equation %}A{% endequation %}) וכעת כל כניסה של {% equation %}A{% endequation %} ניתנת לייצוג בתור נקודה בשריג. כעת, {% equation %}A{% endequation %} מכילה 0 בכל כניסה שמתאימה לזוג נקודות ש<strong>אינן</strong> שכנות בשריג - כלומר, המרחק ביניהן על פי המטריקה {% equation %}d\left(\left(i,j\right),\left(x,y\right)\right)=\left|i-x\right|+\left|j-y\right|{% endequation %} שונה מ-1. עבור כניסות במטריצה שמייצגות נקודות שכנות, הערך יכול להיות 0 או 1. לבעיה <strong>הזו</strong> קורא המאמר "בעיית הפונקציה הלינארית החבויה הדו-ממדית" והיא הבעיה שהיא קלה מספיק כדי להיות ב-{% equation %}\text{SQC}{% endequation %} אבל לא ב-{% equation %}\text{NC}^{0}{% endequation %}.

נותרו שני דברים לעשות, שהם ה"בשר" האמיתי של המאמר - להראות איך לבנות מעגל קוונטי מעומק קבוע עבור הבעיה (בדיוק בעזרת מימוש ה-{% equation %}U_{q}{% endequation %} שראינו למעלה, רק צריך לראות שזה ניתן למימוש), ולהראות שהבעיה לא ב-{% equation %}\text{NC}^{0}{% endequation %}. לעת עתה אני אמלט באלגנטיות מלהציג את הדברים הללו כאן.

