---
title: "תורת הקבוצות - מה זו בעצם קבוצה אינסופית?"
layout: post
categories:
  - תורת הקבוצות
tags:
  - קבוצה סופית
  - קבוצה אינסופית
---


<h2>חלק ראשון, שבו אנחנו מגדירים מהי קבוצה אינסופית</h2>

בסדרת הפוסטים שלי על תורת הקבוצות התחלתי ממושג אחד בודד - <strong>קבוצה</strong>. מתוך המושג הזה בניתי הרבה מושגים מתמטיים אחרים, ובפרט את המושג של <strong>פונקציה</strong>. כל זה היה כיף ונחמד, אבל במשך כל הזמן הזה נשאר פיל גדול במרכז החדר שהתעלמתי ממנו - אולי דיברתי פה ושם על "קבוצה סופית" ו"קבוצה אינסופית", אבל לא הגדרתי את המושג הזה בשום צורה. ומכיוון שהרגע שבו מתחילים לדבר על קבוצות אינסופית הוא הרגע שבו דברים <strong>ממש מגניבים</strong> מתחילים לקרות, כדאי שנעשה את זה.

האתגר שלנו הוא לפרמל מושג אינטואיטיבי, של <strong>גודל</strong> של קבוצה. בואו נסתכל למשל על הקבוצה {% equation %}\left\{ \pi,e,\sqrt{2}\right\} {% endequation %} - מה הגודל שלה? האינטואיציה שלנו אומרת שהגודל שלה הוא 3 כי יש בה שלושה איברים. האינטואיציה אומרת שלקבוצה הריקה {% equation %}\emptyset{% endequation %} יש 0 איברים ושלקבוצה {% equation %}\mathbb{N}=\left\{ 0,1,2,\ldots\right\} {% endequation %} יש {% equation %}\infty{% endequation %} ("אינסוף") איברים. אבל אנחנו רוצים לפרמל את האינטואיציה הזו כי זה מה שעושים במתמטיקה.

אם נותנים לנו קבוצה, איך בעצם אנחנו יודעים כמה איברים יש בה? אנחנו <strong>סופרים</strong> אותם. אני לוקח את האיבר {% equation %}\pi{% endequation %} ואומר "1", ואז אני לוקח את {% equation %}e{% endequation %} ואומר "2" ואז אני לוקח את {% equation %}\sqrt{2}{% endequation %} ואומר "3" ובכך זה נגמר כי לא נשארו איברים בקבוצה. את מה שעשיתי כאן אפשר לתאר פורמלית בעזרת <strong>פונקציה</strong>: אני הגדרתי פונקציה {% equation %}f:\left\{ \pi,e,\sqrt{2}\right\} \to\left\{ 1,2,3\right\} {% endequation %} כך ש-

{% equation %}f\left(\pi\right)=1{% endequation %}

{% equation %}f\left(e\right)=2{% endequation %}

{% equation %}f\left(\sqrt{2}\right)=3{% endequation %}

הייתי יכול, כמובן, גם לספור את האיברים בסדר שונה, ואז הייתי מקבל פונקציה אחרת, נאמר {% equation %}g:\left\{ \pi,e,\sqrt{2}\right\} \to\left\{ 1,2,3\right\} {% endequation %} שמוגדרת על ידי

{% equation %}g\left(\sqrt{2}\right)=1{% endequation %}

{% equation %}g\left(\pi\right)=2{% endequation %}

{% equation %}g\left(e\right)=3{% endequation %}

אבל זה לא משנה כלום - הפונקציה {% equation %}g{% endequation %} היא אינדיקציה לכך שהקבוצה היא מגודל 3 בדיוק כפי שהפונקציה {% equation %}f{% endequation %} היא אינדיקציה שכזו.

אם כן, אולי יש לנו הגדרה כללית? נאמר, הקבוצה {% equation %}A{% endequation %} היא מגודל 3 אם קיימת פונקציה {% equation %}f:A\to\left\{ 1,2,3\right\} {% endequation %}? די קל לראות שההגדרה הזו <strong>לא עובדת</strong> כמות שהיא. למשל, בואו ניקח את הקבוצה {% equation %}A=\left\{ e,\pi\right\} {% endequation %} שיש בה רק <strong>שני</strong> איברים, אז נביט בפונקציה {% equation %}f:\left\{ e,\pi\right\} \to\left\{ 1,2,3\right\} {% endequation %} שמוגדרת כך:

{% equation %}f\left(\pi\right)=1{% endequation %}

{% equation %}f\left(e\right)=2{% endequation %}

זו בעצם אותה פונקציה בדיוק כמו קודם, אז מה השתבש עכשיו? שהאיבר {% equation %}3{% endequation %} הוא "מיותר"; בכלל לא השתמשנו בו. באותה מידה יכלנו להגדיר {% equation %}f:\left\{ e,\pi\right\} \to\left\{ 1,2\right\} {% endequation %} וגם זה היה עובד. נראה די ברור איך אפשר לתקן את הבעיה הזו - צריך לדרוש ש<strong>כל</strong> האיברים של {% equation %}\left\{ 1,2,3\right\} {% endequation %} "יהיו בשימוש", או בניסוח מתמטי - הפונקציה {% equation %}f:A\to\left\{ 1,2,3\right\} {% endequation %} צריכה להיות <strong>על</strong>.

לרוע המזל, זה עדיין לא מספיק. הנה עוד דוגמא ששוברת את האינטואיציה שלנו, שתתבסס על קבוצה בת <strong>ארבעה </strong>איברים, {% equation %}\left\{ \pi,e,\sqrt{2},42\right\} {% endequation %}: נגדיר {% equation %}f:\left\{ \pi,e,\sqrt{2},42\right\} \to\left\{ 1,2,3\right\} {% endequation %} על ידי

{% equation %}f\left(\pi\right)=1{% endequation %}

{% equation %}f\left(e\right)=2{% endequation %}

{% equation %}f\left(\sqrt{2}\right)=3{% endequation %}

{% equation %}f\left(42\right)=3{% endequation %}

ושוב - זו אותה פונקציה כמו קודם, רק עם התוספת החדשה {% equation %}f\left(42\right)=3{% endequation %}. מה השתבש הפעם? כמובן, הפעם השתמשתי ב-3 <strong>יותר מדי</strong> פעמים: גם {% equation %}\sqrt{2}{% endequation %} וגם 42 הלכו אליו. אם הייתי מבצע ספירה בקול רם, מה שהיינו שומעים הוא "אחד, שתיים, שלוש, שלוש...". זו רמאות ברורה וגם הפתרון ברור - לאסור על {% equation %}f{% endequation %} להחזיר את אותו פלט לשני קלטים שונים. או בניסוח מתמטי: הפונקציה {% equation %}f:A\to\left\{ 1,2,3\right\} {% endequation %} צריכה להיות <strong>חד-חד-ערכית</strong>.

אפשר לעשות את זה טיפה יותר אלגנטי. <a href="http://gadial.net/2019/10/19/what_is_set_theory/">כזכור</a>, הגדרה אפשרית למספרים הטבעיים הלכה ככה: {% equation %}0{% endequation %} מוגדר להיות הקבוצה הריקה {% equation %}\emptyset{% endequation %}, {% equation %}1{% endequation %} מוגדר להיות הקבוצה {% equation %}\left\{ 0\right\} {% endequation %} וכן הלאה. באופן כללי, {% equation %}n{% endequation %} מוגדר להיות {% equation %}\left\{ 0,1,2,\ldots,n-1\right\} {% endequation %}. אז אם אני מתחיל את המספור שלי מ-0 במקום מ-1, אני יכול לומר ש-{% equation %}A{% endequation %} היא קבוצה מגודל 3 אם קיימת פונקציה חח"ע ועל {% equation %}f:A\to3{% endequation %} (כלומר, {% equation %}f:A\to\left\{ 0,1,2\right\} {% endequation %}). מכאן אפשר להגדיר קבוצות סופיות: קבוצה {% equation %}A{% endequation %} היא <strong>סופית</strong> אם קיים מספר טבעי {% equation %}n{% endequation %} כך שקיימת פונקציה חח"ע ועל {% equation %}f:A\to n{% endequation %}, ובמקרה זה מסמנים את <strong>הגודל</strong> של {% equation %}A{% endequation %} בתור {% equation %}\left|A\right|=n{% endequation %}.

ועכשיו אפשר להגדיר גם קבוצות אינסופיות, סוף כל סוף, וזו אחת ההגדרות האהובות עלי במתמטיקה! קבוצה היא <strong>אינסופית</strong> אם היא... לא סופית.

לא ראינו את זה בא, מה?

<h2>חלק שני, שבו אנחנו משווים עוצמות</h2>

בהגדרה שלי של קבוצה סופית הכלי שבו השתמשתי היה <strong>פונקציה חח"ע ועל</strong> מהקבוצה {% equation %}A{% endequation %} אל קבוצה ספציפית אחרת של מספרים טבעיים. אבל למה לעצור כאן? האינטואיציה היא שאם קיימת {% equation %}f:A\to B{% endequation %} חח"ע ועל עבור שתי קבוצות {% equation %}A,B{% endequation %} כלשהן, אז הגודל שלהן הוא שווה. הרי מה {% equation %}f{% endequation %} עושה בסך הכל? <strong>משנה את השמות</strong> של אברי {% equation %}A{% endequation %} כך שמתקבלים <strong>כל </strong>אברי {% equation %}B{% endequation %} (כולם, כי {% equation %}f{% endequation %} על), ושינוי השמות הזה לא "מאבד" איברים כי {% equation %}f{% endequation %} חח"ע ולכן שני איברים שונים לא "יתמזגו לאחד" אחרי שינוי השמות שלהם.

עבור קבוצות סופיות, ההגדרה הזו עובדת מצוין. בואו ניקח שתי קבוצות סופיות כלשהן, {% equation %}A,B{% endequation %}, כך ש-{% equation %}\left|A\right|=n{% endequation %} ו-{% equation %}\left|B\right|=m{% endequation %}. נניח עכשיו שקיימת פונקציה חח"ע ועל {% equation %}f:A\to B{% endequation %}. מכך ש-{% equation %}\left|A\right|=n{% endequation %} אפשר להסיק שקיימת {% equation %}g:n\to A{% endequation %} חח"ע ועל (ההגדרה אומרת שקיימת פונקציה מ-{% equation %}A{% endequation %} אל {% equation %}n{% endequation %}, אבל אפשר לקחת את ההופכי שלה) ומכך ש-{% equation %}\left|B\right|=m{% endequation %} אפשר להסיק שקיימת {% equation %}h:B\to m{% endequation %} חח"ע ועל. ההרכבה {% equation %}hfg:n\to m{% endequation %} נותנת לנו פונקציה חח"ע ועל בין {% equation %}n{% endequation %} ו-{% equation %}m{% endequation %}. אז אנחנו נשארים רק עם הצורך להוכיח שאם יש פונקציה חח"ע ועל {% equation %}f:n\to m{% endequation %} אז {% equation %}n=m{% endequation %}. בואו נניח בלי הגבלת הכלליות ש-{% equation %}n\le m{% endequation %} ונוכיח באינדוקציה על הגודל של {% equation %}n{% endequation %}.

אם {% equation %}n=0{% endequation %}, כלומר {% equation %}n=\emptyset{% endequation %}, אז הפונקציה {% equation %}f:n\to m{% endequation %} היחידה שקיימת היא הפונקציה הריקה (כלומר, פונקציה שפורמלית היא יחס שהוא הקבוצה הריקה). אם {% equation %}m\ne\emptyset{% endequation %} הפונקציה הזו לא תהיה על, ולכן {% equation %}m=\emptyset=n{% endequation %}.

נניח אם כן שעבור {% equation %}n{% endequation %} הטענה נכונה ונוכיח אותה עבור {% equation %}n+1{% endequation %}. כלומר, נניח שקיימת פונקציה {% equation %}f:n+1\to m{% endequation %} כך ש-{% equation %}n+1\le m{% endequation %} ונוכיח ש-{% equation %}n+1=m{% endequation %}. כזכור, {% equation %}n+1{% endequation %} זו פשוט הקבוצה {% equation %}\left\{ 0,1,\ldots,n\right\} {% endequation %} ואילו {% equation %}m{% endequation %} היא הקבוצה {% equation %}\left\{ 0,1,\ldots,m-1\right\} {% endequation %}.

מכיוון ש-{% equation %}f{% endequation %} היא על {% equation %}m{% endequation %}, קיים {% equation %}k\in\left\{ 0,1,\ldots,n\right\} {% endequation %} כך ש-{% equation %}f\left(k\right)=m-1{% endequation %}. בואו נבנה מ-{% equation %}f{% endequation %} הזו פונקציה {% equation %}g:n\to m-1{% endequation %} על ידי כך שניקח את {% equation %}f{% endequation %}, נתעלם מהפעולה שלה על {% equation %}n{% endequation %}, ואם צריך לתקן את מי ש-{% equation %}k{% endequation %} עבור אליו, נתקן כך:

{% equation %}g\left(x\right)=\begin{cases} f\left(n\right) & x=k\\ f\left(x\right) & x\ne k \end{cases}{% endequation %}

קיבלנו ש-{% equation %}g{% endequation %} הזו היא פונקציה חח"ע ועל מ-{% equation %}n{% endequation %} אל {% equation %}m-1{% endequation %} ומהנחת האינדוקציה נובע ש-{% equation %}n=m-1{% endequation %}, כלומר {% equation %}n+1=m{% endequation %} וזה מסיים את ההוכחה.

בואו נתפקס עכשיו על מה שהייתה המטרה שלנו פה - הוכחנו שאם קיימת {% equation %}f:A\to B{% endequation %} חח"ע ועל כאשר {% equation %}A,B{% endequation %} הן קבוצות סופיות, אז הגודל שלהן שווה. הנכונות הזו נותנת לנו אומץ לקפוץ אל השלב הבא ולתת הגדרה שהיא תמימה למראה וכמעט ריקה מאינפורמציה, אבל היא מה שינחה אותנו מכאן ואילך: אנחנו אומרים שאם קיימת {% equation %}f:A\to B{% endequation %} חח"ע ועל אז {% equation %}A,B{% endequation %} הן <strong>שוות עוצמה</strong> ומסמנים זאת {% equation %}\left|A\right|=\left|B\right|{% endequation %} או לפעמים סתם {% equation %}A\sim B{% endequation %}. שימו לב שכאן אני <strong>לא מניח</strong> ש-{% equation %}A,B{% endequation %} סופיות; במילים אחרות, נתתי הגדרה פורמלית לאופן שבו בודקים אם שתי קבוצות אינסופיות הן "מאותו גודל אינסופי".

נשמע הגיוני ומתבקש? <strong>זה לא צריך להיות הגיוני ומתבקש</strong> כי דברים מוזרים קורים פה. למעשה, דברים שהיו מוזרים מספיק כדי למשוך את תשומת לבו של גלילאו גלילאי. בספרו האחרון, "שני מדעים חדשים", הוא מביא (בצורה של דיאלוג, שאוותר עליה) את האבחנה הבאה, שנקראת לרוב "הפרדוקס של גלילאו" כי גלילאו עצמו התייחס אל זה בתור סיבה להפסיק לדבר על קבוצות אינסופיות: הקבוצות {% equation %}A=\left\{ 0,1,2,3,4,\ldots\right\} {% endequation %} של הטבעים ו-{% equation %}B=\left\{ 0,1,4,9,16,\ldots\right\} {% endequation %} של <strong>ריבועים</strong> של מספרים טבעיים הן שוות עוצמה - הפונקציה {% equation %}f:A\to B{% endequation %} המוגדרת בתור {% equation %}f\left(n\right)=n^{2}{% endequation %} היא בבירור חח"ע ועל. אבל מצד שני, {% equation %}B\subsetneq A{% endequation %} - קיימים ב-{% equation %}A{% endequation %} איברים שלא מופיעים ב-{% equation %}B{% endequation %}, כך שאינטואיטיבית, {% equation %}B{% endequation %} <strong>קטנה יותר</strong> מאשר {% equation %}A{% endequation %}. אז מה הולך כאן?

אני אוהב להתמודד עם הפרדוקס הזה באופן הבא: תשכחו לרגע מריבועים. נניח שאני מגדיר פונקציה {% equation %}f{% endequation %} שתחומה {% equation %}A{% endequation %} ופועלת כך: {% equation %}f\left(n\right)=n^{\prime}{% endequation %}. מה זה {% equation %}n^{\prime}{% endequation %}? זה פשוט המספר {% equation %}n{% endequation %} כשהוספתי איזה לכלוך ("תג") מעליו. זה לא מספר שונה, זו <strong>מחרוזת</strong> שונה. שיטת סימון שונה לאותו מספר. כך למשל {% equation %}f\left(15\right)=15^{\prime}{% endequation %}. מה הטווח של {% equation %}f{% endequation %}? בואו נכתוב את שתי הקבוצות זו מעל זו:

{% equation %}A=\left\{ 0,1,2,3,\ldots\right\} {% endequation %}

{% equation %}B=\left\{ 0^{\prime},1^{\prime},2^{\prime},3^{\prime},\ldots\right\} {% endequation %}

הקבוצה {% equation %}B{% endequation %} הזו היא בסך הכל "{% equation %}A{% endequation %} עם לכלוכים קטנים בקצה". האם יש הבדל מהותי? לא. סתם שיטת סימון משונה, אבל "ברור" שהגודל לא משתנה כתוצאה ממנה.

אה-הא! כעת, הבה ונחליף את הלכלוך הזה של תג בלכלוך שנראה טיפה שונה אבל גם הוא לכלוך: הספרה 2. נקבל:

{% equation %}B=\left\{ 0^{2},1^{2},2^{2},3^{2},\ldots\right\} {% endequation %}

ובעצם קיבלנו פה שוב את {% equation %}B{% endequation %} המקורית, רק עם שיטת כתיב טיפה שונה לאיברים. אז איפה הבעיה מתחילה? אולי הבעיה מתחילה כשמפסיקים להתייחס ל-{% equation %}2{% endequation %} בתור "לכלוך" ומתחילים להתייחס אליו בתור "הוראות הפעלה" של איך לחשב את הערכים של אברי {% equation %}B{% endequation %}? אבל למה שתהיה פה בעיה? הרי הערכים השונים שמתקבלים עקב כך לא מתנגשים.

אז זהו, שאני באמת לא רואה פה בעיה, וכל שאר הפוסטים שלי על תורת הקבוצות יתבססו על ההנחה שאין בעיה. אבל זה שאני חושב שאין בעיה לא אומר שצריך להיות תמימים לגבי הסיכוי לבעיה שכזו. אני תמיד אוהב להזכיר את <a href="https://gadial.net/2010/04/10/riemann_series_theorem/">משפט רימן לטורים</a>: אם תיקחו טור אינסופי שהוא מתכנס אבל לא מתכנס בהחלט, אז אפשר על ידי שינוי <strong>סדר הסכימה</strong> של האיברים שלו לגרום לו להתכנס לכל מספר שנרצה, או להתבדר, או להיות בעל ערך לא מוגדר. רק שינוי הסדר! אז גם אם משהו נראה לנו טבעי ומובן מאליו, לכו תדעו איזה מוקש מתחבא מתחתיו.

עדיין, הביטוי "{% equation %}A,B{% endequation %} הן שוות<strong> עוצמה</strong>" מאפשר לנו להתייחס לעניין בספקנות ההכרחית. מה זו "עוצמה" (Cardinality באנגלית)? זו מילה חדשה שהכנסנו לדיון בדיוק כדי שנוכל לדבר על "גדלים" של קבוצות אינסופיות. אין לנו מחוייבות לאינטואיציה שהמילה "גודל" נושאת איתה. מצד שני, עכשיו גם קצת פחות ברור על מה אנחנו מדברים - בזמן ש"גודל" הוא מספר טבעי, מה זו "עוצמה"? בינתיים הגדרתי רק מה זה אומר ששתי קבוצות הן <strong>בעלות אותה עוצמה</strong>, אבל לא מה זו ה"עוצמה" הזו מלכתחילה!

התשובה היא שיש למושג הזה הגדרה פורמלית לגמרי, אבל הוא לא יגיד לנו כלום כרגע; פורמלית זה "סודר שאינו שווה עוצמה לאף סודר קטן ממנו", אבל המילה <strong>סודר</strong> עוד לא מוכרת לנו. אז נחכה עם זה להמשך; לא צריך את זה כרגע.

דבר נחמד ושימושי במיוחד ששוויון עוצמה מקיים הוא התכונות של יחסי שקילות. כלומר:

<ul> <li>לכל קבוצה {% equation %}A{% endequation %} מתקיים {% equation %}A\sim A{% endequation %} (כאן {% equation %}f:A\to A{% endequation %} החח"ע ועל תהיה פונקציית הזהות)</li>


<li>אם {% equation %}A\sim B{% endequation %} אז {% equation %}B\sim A{% endequation %} (כי אם יש {% equation %}f:A\to B{% endequation %} חח"ע ועל אז {% equation %}f^{-1}:B\to A{% endequation %} היא חח"ע ועל)</li>


<li>אם {% equation %}A\sim B{% endequation %} וגם {% equation %}B\sim C{% endequation %} אז {% equation %}A\sim C{% endequation %} (כי אם יש {% equation %}f:A\to B{% endequation %} ו-{% equation %}g:B\to C{% endequation %} חח"ע ועל אז גם ההרכבה {% equation %}gf:A\to C{% endequation %} חח"ע ועל)</li>

</ul>

נשתמש בתכונות הללו בחופשיות מכאן ואילך.

<h2>חלק שלישי, שבו אנחנו מגלים עוד הגדרה לקבוצה אינסופית, ורואים מיהו האינסוף "הקטן ביותר"</h2>

בואו נחזור לרגע אל הפרדוקס של גלילאו. מה שהיה מוזר בו הוא שגילינו ש-{% equation %}A\sim B{% endequation %} עבור סיטואציה שבה {% equation %}B{% endequation %} היא תת-קבוצה <strong>ממש</strong> של {% equation %}A{% endequation %} - שכל איבר של {% equation %}B{% endequation %} שייך ל-{% equation %}A{% endequation %}, אבל חלק מהאיברים של {% equation %}A{% endequation %} <strong>חסרים</strong>. תופעה כזו לא יכולה להתרחש בקבוצות <strong>סופיות</strong> - כבר ראינו שאם ל-{% equation %}B{% endequation %} יש פחות איברים מ-{% equation %}A{% endequation %} כששתיהן סופיות, אז לא קיימת {% equation %}f:A\to B{% endequation %} שהיא חח"ע ועל. אם כן, נראה שיש פה דרך חדשה להגדיר קבוצה אינסופית: קבוצה {% equation %}A{% endequation %} היא אינסופית אם ורק אם קיימת לה תת-קבוצה ממש {% equation %}B\subsetneq A{% endequation %} כך ש-{% equation %}A\sim B{% endequation %}. ההגדרה הזו נקראת "אינסופיות דדקינד" על שם המתמטיקאי ריכארד דדקינד שהמציא אותה, והיא יפה כי היא בכלל לא מסתמכת על המספרים הטבעיים כדי להגדיר "גודל" של קבוצות.

אז אם הכל טוב, מה הבעיה? כי בטח הרגשתן שיש פה בעיה שאני חותר אליה. ובכן, הבעיה היא שהמושג הזה של אינסופיות הוא לא בדיוק שקול למושג הרגיל של אינסופיות - לא בלי הנחה נוספת. ההנחה הנוספת הזו היא <strong>אקסיומת הבחירה</strong> שהזכרתי בפוסט שלי על <a href="https://gadial.net/2020/06/20/general_cartesian_products/">מכפלות קרטזיות כלליות</a>.

בשביל לראות למה צריך את ההנחה הזו ומה זה בכלל אומר שצריכים אותה, בואו ננסה להוכיח שאינסופיות "רגילה" גוררת את אינסופיות דדקינד, וההפך. אם קבוצה {% equation %}A{% endequation %} היא אינסופית דדקינד, אז קיימת {% equation %}B\subsetneq A{% endequation %} כך ש-{% equation %}A\sim B{% endequation %}. עכשיו, אם {% equation %}A{% endequation %} סופית במובן הרגיל, כלומר {% equation %}A\sim n{% endequation %} עבור {% equation %}n{% endequation %} טבעי כלשהו, אז מה שקורה הוא ש-{% equation %}B\sim A\sim n{% endequation %}. מצד שני, אם ניקח את הפונקציה שמראה ש-{% equation %}A\sim n{% endequation %} ונצמצם את התחום שלה ל-{% equation %}B{% endequation %} נקבל התאמה חח"ע ועל בין {% equation %}B{% endequation %} ובין תת-קבוצה ממש של {% equation %}n{% endequation %} (זו תת-קבוצה <strong>ממש</strong> כי יש {% equation %}a\in A\backslash B{% endequation %} שאת התמונה שלו אף איבר ב-{% equation %}B{% endequation %} לא מקבל, אחרת ההתאמה שמראה ש-{% equation %}A\sim n{% endequation %} לא הייתה חח"ע). במילים אחרות, עברנו מלדבר על {% equation %}A,B{% endequation %} כלליות לדבר על כך שלא ייתכן ש-{% equation %}n{% endequation %} שוות עוצמה לתת-קבוצה ממש של עצמה. את זה אפשר להוכיח באינדוקציה על {% equation %}n{% endequation %} בצורה דומה למה שעשינו קודם.

אם כן, ראינו שאם קבוצה היא אינסופית-דדקינד אז היא גם אינסופית במובן הרגיל. אבל האם ההפך נכון? אני אוכיח את זה בדרך עקיפה, בעזרת טענה אחרת שהיא שימושית באופן כללי, ואותה אוכיח בנפנוף ידיים שמסתמך ברמה כלשהי על אקסיומת הבחירה: אם {% equation %}A{% endequation %} היא קבוצה אינסופית (במובן הרגיל) אז, אינטואיטיבית, היא מכילה "משהו שנראה כמו הטבעיים" ופורמלית: קיימת פונקציה {% equation %}f:\mathbb{N}\to A{% endequation %} שהיא חד-חד-ערכית (<strong>לא</strong> בהכרח על). לפונקציה כזו קוראים <strong>שיכון</strong>.

למה הטענה הזו מספיקה כדי להראות שאם {% equation %}A{% endequation %} אינסופית, אז היא אינסופית-דדקינד? כי אם {% equation %}A{% endequation %} אינסופית ו-{% equation %}f{% endequation %} כזו קיימת, אפשר לתאר את התמונה שלה בתור {% equation %}\left\{ a_{0},a_{1},a_{2},\ldots\right\} {% endequation %}, ואז אפשר לעשות את התעלול הבא: להגדיר פונקציה {% equation %}g:A\to A{% endequation %} על ידי

{% equation %}g\left(x\right)=\begin{cases} a_{k+1} & x=a_{k}\\ x & \text{else} \end{cases}{% endequation %}

כלומר, מה ש-{% equation %}g{% endequation %} עושה על אברי {% equation %}A{% endequation %} הוא זה: על רובם היא לא עושה כלום ומשאירה אותם ללא שינוי; אבל אם היא מקבלת איבר מתוך {% equation %}\left\{ a_{0},a_{1},a_{2},\ldots\right\} {% endequation %}, היא מחזירה את האיבר הבא בתור. קל לראות ש-{% equation %}g\left(A\right)=A\backslash\left\{ a_{0}\right\} {% endequation %} וש-{% equation %}g{% endequation %} היא חח"ע, ולכן קיבלנו תת-קבוצה ממש של {% equation %}A{% endequation %} (כל {% equation %}A{% endequation %} למעט {% equation %}a_{0}{% endequation %}) ששקולה ל-{% equation %}A{% endequation %} - אינסופיות-דדקינד בפעולה.

אוקיי, אז איך מוכיחים שאם {% equation %}A{% endequation %} אינסופית אפשר לשכן את {% equation %}\mathbb{N}{% endequation %} בתוכה? הנה הוכחה בנפנוף ידיים: מכיוון ש-{% equation %}A{% endequation %} לא ריקה, יש בה איבר, נקרא לו {% equation %}a_{0}{% endequation %}. אז נגדיר {% equation %}f\left(0\right)=a_{0}{% endequation %}. עכשיו, גם {% equation %}A\backslash\left\{ a_{0}\right\} {% endequation %} לא ריקה (כי {% equation %}A{% endequation %} אינסופית, לא ייתכן ש-{% equation %}a_{0}{% endequation %} היה האיבר היחיד בה) אז קיים איבר {% equation %}a_{1}\in A\backslash\left\{ a_{0}\right\} {% endequation %} ואפשר להגדיר {% equation %}f\left(1\right)=a_{1}{% endequation %}. ככה אפשר להמשיך: נניח שכבר הגדרתי את {% equation %}f{% endequation %} עד לערך {% equation %}n{% endequation %}, אז נתבונן ב-{% equation %}A\backslash\left\{ a_{0},\ldots,a_{n}\right\} {% endequation %}. זו קבוצה לא ריקה כי אם הייתה ריקה, {% equation %}A{% endequation %} הייתה שווה לקבוצה <strong>הסופית</strong> {% equation %}\left\{ a_{0},\ldots,a_{n}\right\} {% endequation %}, ולכן קיים בקבוצה הזו איבר {% equation %}a_{n+1}{% endequation %} ואפשר להגדיר {% equation %}f\left(n+1\right)=a_{n+1}{% endequation %}, וכך זה נמשך עד אינסוף.

נשמע סביר? בהחלט. אז למה זו הוכחה בנפנוף ידיים? כי כזכור, בתורת הקבוצות צריך לבנות דברים באופן מסודר, מתוך אקסיומות, ולא סתם לומר "אני יכול לתאר את זה ולכן זה קיים", מה שמביא עלינו זוועות כמו הפרדוקס של ראסל. כאן אני בונה פונקציה {% equation %}f{% endequation %}, שהיא בעצם קבוצה של זוגות סדורים מהצורה {% equation %}\left(n,a_{n}\right){% endequation %}. אנחנו יודעים לבנות זוגות סדורים, ועבור כל זוג סדור אנחנו גם יודעים לבנות את הקבוצה שהוא האיבר היחיד שלה, ואנחנו יודעים לאחד מספר <strong>סופי</strong> של קבוצות - אבל ב-{% equation %}f{% endequation %} צריך להיות מספר <strong>אינסופי</strong> של זוגות סדורים, ואת זה אנחנו כבר לא יודעים לעשות מהאקסיומות הבסיסיות.

בניה מחוכמת יותר, בעזרת אקסיומות מחוכמות יותר, כבר דורשת שנתבסס על משהו קיים. אני לא יכול סתם כך להגיד "{% equation %}A{% endequation %} לא ריקה אז יש בה איזה איבר ונקרא לו {% equation %}a_{0}{% endequation %}"; בשביל <strong>לבנות פורמלית</strong> את {% equation %}f{% endequation %} אני צריך משהו קיים ש<strong>נותן לי במפורש</strong> את {% equation %}a_{0}{% endequation %} ואני יכול להסתמך עליו. המשהו הזה הוא, ובכן, פונקציה: פונקציה {% equation %}g{% endequation %} שיודעת לקבל תת-קבוצות של {% equation %}A{% endequation %} ולהחזיר איברים שנמצאים בהן. זה <strong>בדיוק</strong> מה שאקסיומת הבחירה מדברת עליו. אקסיומת הבחירה אומרת במפורש את הדבר הזה: אם {% equation %}\left\{ A_{i}\right\} _{i\in\Lambda}{% endequation %} היא משפחה של קבוצות כך ש-{% equation %}A_{i}\ne\emptyset{% endequation %} לכל {% equation %}i\in\Lambda{% endequation %} אז קיימת {% equation %}g:\Lambda\to\bigcup_{i\in\Lambda}A_{i}{% endequation %} כך ש-{% equation %}g\left(i\right)\in A_{i}{% endequation %} לכל {% equation %}i\in\Lambda{% endequation %}. במקרה שלנו, משפחת הקבוצות היא פשוט {% equation %}\mathcal{P}\left(A\right)\backslash\left\{ \emptyset\right\} {% endequation %} - כל תתי-הקבוצות של {% equation %}A{% endequation %} למעט הקבוצה הריקה.

עכשיו, במקום לומר "{% equation %}A\backslash\left\{ a_{0},\ldots,a_{n}\right\} {% endequation %} לא ריקה אז קיים בה {% equation %}a_{n+1}{% endequation %} ולכן נגדיר {% equation %}f\left(n+1\right)=a_{n+1}{% endequation %}" אני יכול להגיד משהו פשוט יותר: "נגדיר {% equation %}f\left(a_{n+1}\right)=g\left(A\backslash\left\{ a_{0},\ldots,a_{n}\right\} \right){% endequation %}". זו כבר הגדרה מאוד קונקרטית שניתן לבצע - אבל בשביל זה צריך שהפונקציה {% equation %}g{% endequation %} תתקיים מלכתחילה.

אפשר היה לעשות את זה פשוט יותר. לא חייבים את אקסיומת הבחירה המלאה בכל עוצמתה - אפשר להחליף אותה במשהו שנקרא "אקסיומת הבחירה התלויה" (Axiom of dependent choice). לא אכנס לזה הפעם. אבל בלי סוג כלשהו של אקסיומת הבחירה, זה פשוט לא עובד. זה לא שאם אין לנו את אקסיומת הבחירה ו-{% equation %}A{% endequation %} אינסופית אז אין בה עותק של המספרים הטבעיים; זה שאם אין לנו את אקסיומת הבחירה אנחנו פשוט לא מסוגלים <strong>לבנות פורמלית</strong> את הפונקציה ש<strong>מראה לנו את השיכון הזה</strong>. גם בהגדרה של אינסופיות-דדקינד, מה ש"נשבר" ללא אקסיומת הבחירה הוא לא שלא <strong>קיימת</strong> תת-קבוצה {% equation %}B{% endequation %} שהיא "מאותו הגודל" של {% equation %}A{% endequation %}, אלא שאין לנו דרך <strong>לבנות פורמלית</strong> את הפונקציה שמראה לנו ש-{% equation %}A\sim B{% endequation %} (ובלי פונקציה כזו פשוט <strong>אין משמעות</strong> לאמירה ששתי הקבוצות הן "מאותו הגודל"; הרי מהגדרת "אותו הגודל" בהתבסס על קיום פונקציה שכזו התחלנו).

זה מקום טוב לעצור בו, אבל לפני כן, בואו נחדד עוד קצת את המשמעות של מה שהוכחנו. ראינו שאם {% equation %}A{% endequation %} היא קבוצה אינסופית <strong>כלשהי</strong>, אז היא מכילה עותק של {% equation %}\mathbb{N}{% endequation %}, כלומר אינטואיטיבית, {% equation %}A{% endequation %} גדולה "לפחות כמו" {% equation %}\mathbb{N}{% endequation %}. כלומר, אינטואטיבית, {% equation %}\mathbb{N}{% endequation %} היא הקבוצה האינסופית "הקטנה ביותר". איך מפרמלים את הרעיון הזה עד הסוף? את זה כבר כדאי לדחות לפעם הבאה. 