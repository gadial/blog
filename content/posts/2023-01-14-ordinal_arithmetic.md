---
title: "תורת הקבוצות - אריתמטיקה של סודרים"
layout: post
categories:
  - תורת הקבוצות
tags:
  - סודרים
image: "/assets/img/main/set_theory.png"
---


<h2>איך הסודרים נראים?</h2>

סדרת הפוסטים שלי על תורת הקבוצות הגיעה <a href="https://gadial.net/2023/01/12/ordinals/">בפוסט הקודם</a> אל ההגדרה של סודרים וראינו עליהם כל מני דברים מרתקים כמו זה שאפשר להשוות אותם, אבל דבר אחד לא באמת הסברתי - <strong>איך הם נראים</strong>. מלמלתי משהו על זה שהטבעיים הם סודרים, ויש איזה סודר שנקרא {% equation %}\omega=\left\{ 0,1,2,\ldots\right\} {% endequation %} והראיתי עוד כמה סודרים באמצעותו, אבל זה לא רציני. אם אנחנו מדברים על סודרים, בואו נבין איך <strong>כולם</strong> כולל כולם נראים. אבל איך נעשה את זה?

בואו נחשוב על מספרים טבעיים. יש כל מני דרכים לייצג מספרים טבעיים, אבל הדרך החביבה על האנושות בימינו היא <strong>הצגה עשרונית</strong>. בהצגה עשרונית אני כותב 572 וכולם מבינים שכתבתי מספר שמתקבל בתור מין תרגיל חשבוני: {% equation %}5\times10^{2}+7\times10^{1}+2\times10^{0}{% endequation %}. מה יש לנו פה? ביטוי שמערב שלוש פעולות חשבוניות: חיבור, כפל וחזקה; ומערב שלוש <strong>ספרות</strong>, במקרה הזה 5,7,2, שהן מספרים בין 0 ל-9; ומערב את המספר המיוחד 10 שמשמש בתור ה<strong>בסיס</strong> של הייצוג העשרוני.

האם יש משהו דומה עבור סודרים באופן כללי? למרבה השמחה, כן. כל סודר {% equation %}\alpha>0{% endequation %} אפשר לכתוב באופן הבא:

{% equation %}\alpha=\omega^{\beta_{1}}\cdot k_{1}+\ldots+\omega^{\beta_{n}}\cdot k_{n}{% endequation %}

כאשר {% equation %}\alpha\ge\beta_{1}\ge\ldots\ge\beta_{n}{% endequation %} הם סודרים ו-{% equation %}k_{1},\ldots,k_{n}{% endequation %} הם מספרים טבעיים. הייצוג הזה נקרא <strong>הצורה הנורמלית של קנטור</strong>.

לא תמיד הייצוג הזה עושה את החיים פשוטים יותר: למשל, יש סודרים שמקיימים {% equation %}\alpha=\omega^{\alpha}{% endequation %}, אז לא לגמרי ברור האם הייצוג הזה עוזר לנו להבין יותר טוב איך הם נראים; אבל לפחות יש לנו צורה אחידה לכולם שנראית סבירה יחסית.

<h2>איך מגדירים אריתמטיקה של סודרים?</h2>

כדי להבין איך הצורה הנורמלית הזו "עובדת", אנחנו צריכים להגדיר פעולות חשבון עבור סודרים - חיבור, כפל וחזקה, בדיוק כמו עבור טבעיים. ההגדרות די פשוטות; הן כמעט זהות למה שקורה עם טבעיים. אבל עם סיבוך אחד. אז בואו ניזכר קודם איך ההגדרות עובדות אצל הטבעיים.

הדבר הבסיסי שאנחנו מתחילים ממנו הוא קיום הפעולה {% equation %}n+1{% endequation %} - פעולת ה<strong>עוקב</strong>. ראינו איך היא מוגדרת פורמלית: {% equation %}n+1\triangleq n\cup\left\{ n\right\} {% endequation %}. ברגע שיש אותה, אפשר להגדיר חיבור כללי {% equation %}n+m{% endequation %} באופן הבא:

<ul> <li>{% equation %}n+0\triangleq n{% endequation %}</li>


<li>{% equation %}n+\left(m+1\right)\triangleq\left(n+m\right)+1{% endequation %}</li>

</ul>

במילים אחרות, עבור {% equation %}m=0{% endequation %} החיבור מוגדר בצורה כזו ש-0 הוא נייטרלי לחיבור - לא משנה את מה שמחברים אותו אליו. עבור חיבור עם כל מספר גדול מאפס, אנחנו מתבססים על כך שהמספר הזה הוא <strong>עוקב מיידי</strong> של מישהו: כלומר, ניתן לכתוב אותו בתור {% equation %}m+1{% endequation %} עבור {% equation %}m{% endequation %} טבעי כלשהו. מכיוון ש-{% equation %}m<m+1{% endequation %} אנחנו מניחים שכבר הגדרנו את {% equation %}n+m{% endequation %} עבורו, ואנחנו לוקחים את ה-{% equation %}n+m{% endequation %} הזה ומפעילים עליו את פעולת העוקב. זו דוגמא להגדרה <strong>רקורסיבית</strong>: אנחנו מגדירים משהו באמצעות מקרים פשוטים יותר שלו שכבר טיפלנו בהם.

באופן מאוד דומה אפשר להגדיר עכשיו כפל {% equation %}n\cdot m{% endequation %}, רק שעכשיו 0 לא יהיה נייטרלי אלא "בולעני", ואת מקום פעולת העוקב תחליף פעולת החיבור שכבר הגדרנו:

<ul> <li>{% equation %}n\cdot0\triangleq0{% endequation %}</li>


<li>{% equation %}n\cdot\left(m+1\right)\triangleq n\cdot m+n{% endequation %}</li>

</ul>

והגדרת חזקה {% equation %}n^{m}{% endequation %} ממשיכה באותה רוח:

<ul> <li>{% equation %}n^{0}\triangleq1{% endequation %}</li>


<li>{% equation %}n^{m+1}\triangleq n^{m}\cdot n{% endequation %}</li>

</ul>

את כל ההגדרות הללו אפשר להחיל גם על סודרים, אבל יש לנו סיבוך מהותי אחד: בהגדרה עבור טבעיים, ההנחה המובלעת שלנו הייתה שכל מספר שאיננו 0 הוא עוקב מיידי של מישהו. זה לא קורה עבור סודרים. למשל, {% equation %}\omega=\left\{ 0,1,2,\ldots\right\} {% endequation %} הוא לא עוקב מיידי של אף אחד. סודר כזה נקרא <strong>סודר גבולי</strong>. הסודר הגבולי הקטן ביותר הוא כאמור 0 שבו ההגדרות הקיימות כן מטפלות, אבל יש עוד אינספור נוספים, וצריך לטפל בכולם.

כדי לקבל אינטואיציה לגבי מה שנעשה עכשיו, בואו ניזכר לרגע באופן שבו מגדירים במספרים ממשיים את {% equation %}a^{\sqrt{2}}{% endequation %}. הרעיון הוא להתבסס על זה שאנחנו יודעים להגדיר חזקה שבה המעריך הוא מספר רציונלי: {% equation %}a^{\frac{n}{m}}=\sqrt[m]{a^{n}}{% endequation %}; ומה שאנחנו עושים עכשיו הוא לקחת סדרה של מספרים רציונליים שמתכנסת ל-{% equation %}\sqrt{2}{% endequation %} (תמיד יש כזו; זה מה שנקרא "הרציונליים צפופים בממשיים"): סדרה {% equation %}\left\{ r_{n}\right\} _{n=1}^{\infty}{% endequation %} כך ש-{% equation %}\lim_{n\to\infty}r_{n}=\sqrt{2}{% endequation %}, ואנחנו <strong>מגדירים</strong> {% equation %}a^{\sqrt{2}}=\lim_{n\to\infty}a^{r_{n}}{% endequation %}. צריך כמובן להוכיח שזה מוגדר היטב, במובן זה שכל סדרה של רציונליים שמתכנסת אל {% equation %}\sqrt{2}{% endequation %} תניב את אותו מספר, אבל זה עובד.

ההגדרה הזו הסתמכה על מושג ה<strong>גבול</strong> שקיים בחדו"א. עבור סודרים אין דבר כזה, אבל יש משהו דומה. ראשית, בואו נשים לב לכך שאם יש לנו קבוצה {% equation %}A{% endequation %} שכל האיברים שלה הם סודרים, אז {% equation %}\bigcup A{% endequation %} הוא סודר בעצמו. זה די ברור בקבוצה סופית, כי ראינו שלכל זוג סודרים, אחד מוכל בשני, כך שהאיחוד של כולם יהיה פשוט האיבר המקסימלי בקבוצה. אבל אם {% equation %}A{% endequation %} אינסופית זה מצריך הוכחה דומה לאלו של הפוסט הקודם. אני אסמן {% equation %}\alpha=\bigcup A{% endequation %} ואז כדי להראות שזו קבוצה טרנזיטיבית ניקח {% equation %}\gamma\in\alpha{% endequation %}. על פי הגדרת {% equation %}\alpha{% endequation %} זה אומר שקיים {% equation %}\beta\in A{% endequation %} כך ש-{% equation %}\gamma\in\beta{% endequation %}, ומכיוון ש-{% equation %}\beta{% endequation %} סודר אז {% equation %}\gamma\subseteq\beta\subseteq\bigcup A=\alpha{% endequation %} ולכן {% equation %}\gamma\subseteq\alpha{% endequation %} וקיבלנו ש-{% equation %}\alpha{% endequation %} טרנזיטיבי. עכשיו, האיברים של {% equation %}\alpha{% endequation %} כולם סודרים (כי האיברים של {% equation %}A{% endequation %} הם סודרים ולכן כל האיברים <strong>שלהם</strong> הם סודרים) וכבר ראינו שהם סדורים בסדר מלא על ידי {% equation %}\in{% endequation %}, כך ש-{% equation %}\alpha{% endequation %} הוא סודר.

אבחנה נוספת היא ש-{% equation %}\alpha=\sup A{% endequation %}, כלומר האיבר המינימלי של אוסף הסודרים שגדולים או שווים לכל אברי {% equation %}A{% endequation %}. איבר כזה בהחלט קיים כי {% equation %}\alpha{% endequation %} הוא סודר כזה, אז מספיק להסתכל על קבוצת כל הסודרים הקטנים או שווים אליו שמקיימים את התכונה הזו והיא סדורה היטב. בנוסף, מכיוון ש-{% equation %}\text{sup}A{% endequation %} גדול או שווה לכל איבר ב-{% equation %}A{% endequation %} הוא מכיל את כולם, ולכן מכיל את האיחוד שלהם שהוא {% equation %}\alpha{% endequation %}; והמינימליות שלו פירושה שהוא מוכל ב-{% equation %}\alpha{% endequation %}, כך שקיבלנו שהם שווים.

עכשיו אפשר להגדיר גבול, עבור מקרה ספציפי. ניקח סודר גבולי {% equation %}\alpha{% endequation %} וסדרה של סודרים שהאינדקסים שלה הם כל הסודרים עד ולא כולל {% equation %}\alpha{% endequation %}, כלומר {% equation %}\left\{ a_{\beta}\right\} _{\beta<\alpha}{% endequation %} (פורמלית, זו פונקציה מ-{% equation %}\alpha{% endequation %} אל קבוצה כלשהי של סודרים, כמו שסדרה רגילה היא פונקציה מ-{% equation %}\mathbb{N}{% endequation %} לקבוצה כלשהי). נניח שהסדרה עולה, כלומר אם {% equation %}\beta_{1}<\beta_{2}{% endequation %} אז {% equation %}a_{\beta_{1}}<a_{\beta_{2}}{% endequation %}, ועכשיו אפשר להגדיר את הגבול של הסדרה על ידי

{% equation %}\lim_{\beta\to\alpha}a_{\beta}=\sup\left\{ a_{\beta}\ |\ \beta<\alpha\right\} {% endequation %}

עם ההגדרה הזו אפשר להציג סוף סוף את ההגדרה הפורמלית של פעולות האריתמטיקה של סודרים.

חיבור מוגדר על ידי

<ul> <li>{% equation %}\alpha+0\triangleq\alpha{% endequation %}</li>


<li>{% equation %}\alpha+\left(\beta+1\right)\triangleq\left(\alpha+\beta\right)+1{% endequation %} לכל סודר {% equation %}\beta{% endequation %}</li>


<li>{% equation %}\alpha+\beta\triangleq\lim_{\gamma\to\beta}\left(\alpha+\gamma\right){% endequation %} לכל סודר גבולי {% equation %}\beta>0{% endequation %}</li>

</ul>

כפל מוגדר על ידי

<ul> <li>{% equation %}\alpha\cdot0\triangleq0{% endequation %}</li>


<li>{% equation %}\alpha\cdot\left(\beta+1\right)\triangleq\left(\alpha\cdot\beta\right)+\alpha{% endequation %} לכל סודר {% equation %}\beta{% endequation %}</li>


<li>{% equation %}\alpha\cdot\beta\triangleq\lim_{\gamma\to\beta}\left(\alpha\cdot\gamma\right){% endequation %} לכל סודר גבולי {% equation %}\beta>0{% endequation %}</li>

</ul>

חזקה מוגדרת על ידי

<ul> <li>{% equation %}\alpha^{0}\triangleq1{% endequation %}</li>


<li>{% equation %}\alpha^{\beta+1}\triangleq\alpha^{\beta}\cdot\alpha{% endequation %} לכל סודר {% equation %}\beta{% endequation %}</li>


<li>{% equation %}\alpha^{\beta}\triangleq\lim_{\gamma\to\beta}\alpha^{\gamma}{% endequation %} לכל סודר גבולי {% equation %}\beta>0{% endequation %}</li>

</ul>

זה מסיים את ההגדרה, אם כי אני כבר מציין שההגדרה הזו לא פורמלית מספיק; הגדרתי את הכל באופן רקורסיבי, אבל לא הסברתי למה בכלל אפשר להגדיר דברים באופן רקורסיבי. בגלל שהנושא הזה מביא איתו שלל סיבוכים משל עצמו, אני שומר אותו לפוסט הבא.

<h2>כמה דוגמאות ועוד דרך התבוננות על זה</h2>

עכשיו שיש לנו הגדרות פורמליות אפשר לראות כל מני דברים שאולי קצת לא אינטואיטיביים לנו, למשל ש-{% equation %}1+\omega\ne\omega+1{% endequation %}. למה? כי {% equation %}\omega+1=\left\{ 0,1,\ldots,\omega\right\} {% endequation %}, זה הסודר שבא מייד אחרי {% equation %}\omega{% endequation %}; לעומת זאת, אם ננסה למצוא מהו {% equation %}1+\omega{% endequation %} על פי הגדרה, נקבל

{% equation %}1+\omega=\lim_{n\to\omega}\left(1+n\right)=\sup\mathbb{N}=\omega{% endequation %}

זה בגלל שאם {% equation %}n<\omega{% endequation %} אז {% equation %}n{% endequation %} הוא מספר טבעי, ולכן {% equation %}1+n{% endequation %} גם הוא מספר טבעי, ואנחנו לוקחים את הסופרמום על קבוצת הטבעיים - לא קיבלנו שום דבר "חדש".

הבעיה עם התיאור הזה, לפחות שלי, היא שאני מרגיש שהעניינים הסתבכו בצורה משמעותית. קיבלנו הגדרה יפה ומועילה, אבל עכשיו אנחנו רואים שיש בה מוקשים סמויים שאין לנו אינטואיציה טובה לגביהם. אז אולי אפשר לתת עוד אינטואיציה מה זה בכלל חיבור סודרים? התשובה היא שכן, ולמרבה המזל היא די פשוטה.

בואו ניקח שתי קבוצות זרות {% equation %}A,B{% endequation %} שהן סדורות בסדרים מלאים, {% equation %}<_{A},<_{B}{% endequation %}, ונגדיר יחס סדר על {% equation %}A\cup B{% endequation %} שאפשר לתאר בתור "קודם {% equation %}A{% endequation %} ואז {% equation %}B{% endequation %}". כלומר:

<ul> <li>אם {% equation %}a\in A,b\in B{% endequation %} אז {% equation %}a<b{% endequation %}</li>


<li>אם {% equation %}a,b\in A{% endequation %} אז {% equation %}a<b{% endequation %} אם ורק אם {% equation %}a<_{A}b{% endequation %}</li>


<li>אם {% equation %}a,b\in B{% endequation %} אז {% equation %}a<b{% endequation %} אם ורק אם {% equation %}a<_{B}b{% endequation %}</li>

</ul>

ראינו כבר משהו כזה לא מזמן; <a href="https://gadial.net/2023/01/07/well_ordered_sets/">בפוסט שלי</a> על קבוצות סדורות היטב לקחתי את {% equation %}\mathbb{Z}{% endequation %} וחילקתי אותה לשני חלקים: {% equation %}\mathbb{Z}=A\cup B{% endequation %} כאשר {% equation %}A=\mathbb{N}{% endequation %} עם יחס הסדר הרגיל ו-{% equation %}B=\left\{ -1,-2,-3,\ldots\right\} {% endequation %} עם יחס הסדר על פי הערך המוחלט. מזה הסקתי יחס סדר חדש ולא סטנדרטי של {% equation %}\mathbb{Z}{% endequation %}, שסימנתי {% equation %}\mathbb{Z}=\left\{ 0,1,2,\ldots,-1,-2,\ldots\right\} {% endequation %}. עכשיו, כשעושים את זה על קבוצות סדורות היטב, התוצאה היא קבוצה סדורה היטב; ואם {% equation %}A\cong\alpha,B\cong\beta{% endequation %} מקבלים ש-{% equation %}A\cup B\cong\alpha+\beta{% endequation %} (בדוגמא שלנו קיבלנו ש-{% equation %}\mathbb{Z}{% endequation %} עם יחס הסדר המוזר איזומורפית ל-{% equation %}\omega+\omega{% endequation %}). זו הדרך הנוחה לחשוב על זה.

עכשיו אולי קצת יותר ברור עניין ה-{% equation %}1+\omega\ne\omega+1{% endequation %}. כי {% equation %}\omega+1{% endequation %} זה "לאינסוף... ומעבר לו!" - זו קבוצת הטבעיים {% equation %}\omega{% endequation %} כשאנחנו מוסיפים עוד איבר 1 (זה ה-{% equation %}+1{% endequation %}) "בסוף" שלה, אחרי כל הטבעיים. לעומת זאת, {% equation %}1+\omega{% endequation %} זו קבוצת הטבעיים כשאנחנו מוסיפים איבר חדש <strong>בהתחלה</strong>, כלומר למשל הקבוצה {% equation %}\left\{ -1,0,1,2,\ldots\right\} {% endequation %} עם יחס הסדר הרגיל, שאיזומורפית ל-{% equation %}\mathbb{N}{% endequation %} עם האיזומורפיזם {% equation %}x\mapsto x+1{% endequation %}.

מה עם כפל? אותו עניין: {% equation %}2\cdot\omega\ne\omega\cdot2{% endequation %}. כי {% equation %}2\cdot\omega=\lim_{n\to\omega}2\cdot n=\omega{% endequation %}, אבל {% equation %}\omega\cdot2=\left(\omega\cdot1\right)+\omega=\omega+\omega{% endequation %}. ושוב נשאלת השאלה האם אפשר לתת תיאור "קבוצתי" של זה, ואפשר! ניקח {% equation %}A,B{% endequation %} כמו קודם ונסתכל על {% equation %}A\times B{% endequation %}. על הקבוצה הזו נגדיר <strong>סדר לקסיקוגרפי</strong>, כלומר כזה שבו קודם כל משווים את האיברים ברכיב אחד, ורק אם הם זהים משווים ברכיב השני. כאן ספציפית משווים קודם את {% equation %}B{% endequation %} ורק אז את {% equation %}A{% endequation %}. כלומר, אם יש לנו את {% equation %}\left(a_{1},b_{1}\right),\left(a_{2},b_{2}\right)\in A\times B{% endequation %} אז {% equation %}\left(a_{1},b_{1}\right)<\left(a_{2},b_{2}\right){% endequation %} אם ורק אם

<ul> <li>{% equation %}b_{1}<b_{2}{% endequation %}, או:</li>


<li>{% equation %}b_{1}=b_{2}{% endequation %} וגם {% equation %}a_{1}<a_{2}{% endequation %}</li>

</ul>

וכמקודם, אם {% equation %}A\cong\alpha{% endequation %} ו-{% equation %}B\cong\beta{% endequation %} אז {% equation %}A\times B\cong\alpha\times\beta{% endequation %}. למשל, עבור {% equation %}\omega\cdot2{% endequation %} אפשר להסתכל על הקבוצה {% equation %}\mathbb{N}\times\left\{ 0,1\right\} {% endequation %}; אנחנו משווים איברים {% equation %}\left(n,b\right){% endequation %} קודם כל על פי ה"ביט" הימני, ואז על פי המספר השמאלי. אנחנו מקבלים שני עותקים של {% equation %}\mathbb{N}{% endequation %}: ראשית כל האיברים מהצורה {% equation %}\left(n,0\right){% endequation %} ולאחר מכן האיברים מהצורה {% equation %}\left(n,1\right){% endequation %}.

<h2>אז איך מגיעים לצורה הנורמלית?</h2>

כזכור, התחלנו את הפוסט מלדבר על זה שכל סודר ניתן להציג בצורה הנורמלית {% equation %}\alpha=\omega^{\beta_{1}}\cdot k_{1}+\ldots+\omega^{\beta_{n}}\cdot k_{n}{% endequation %}. איך מוכיחים את זה? התשובה היא - באינדוקציה. אבל כמו שהייתי זקוק לסוג מיוחד של רקורסיה כדי להגדיר את פעולות האריתמטיקה, אני צריך סוג מיוחד של אינדוקציה בשביל ההוכחה; אני אשמור את ההסבר הפורמלי עליה לפוסט הבא ובואו פשוט נזרום איתה כרגע.

הלב הטכני של ההוכחה הוא משפט ש... ניחשתן נכון... מכליל תוצאה דומה עבור מספרים טבעיים. ספציפית, בטבעיים אנחנו יודעים שאם {% equation %}a,b{% endequation %} הם טבעיים כך ש-{% equation %}b>0{% endequation %} אז קיימים {% equation %}q,r{% endequation %} יחידים כך ש-{% equation %}a=bq+r{% endequation %} ו-{% equation %}0\le r<a{% endequation %}. מה שנקרא, חילוק עם שארית. עבור סודרים קיים אותו דבר בדיוק: בהינתן {% equation %}\alpha,\beta{% endequation %} כך ש-{% equation %}\beta>0{% endequation %}, קיימים {% equation %}\gamma,\rho{% endequation %} כך ש-{% equation %}\alpha=\beta\cdot\gamma+\rho{% endequation %} ו-{% equation %}\rho<\alpha{% endequation %}. גם ההוכחה של זה דומה להוכחה עבור הטבעיים: לוקחים את {% equation %}\gamma{% endequation %} המקסימלי שעבורו {% equation %}\alpha\ge\beta\cdot\gamma{% endequation %} (קיים כזה כי {% equation %}\beta\cdot\left(\alpha+1\right)>\alpha{% endequation %}). עכשיו לוקחים את {% equation %}\rho{% endequation %} המקסימלי שעבורו {% equation %}\alpha\ge\beta\cdot\gamma+\rho{% endequation %} (קיים כזה כי {% equation %}\beta\cdot\gamma+\beta=\beta\cdot\left(\gamma+1\right)>\alpha{% endequation %}). קל לראות ש-{% equation %}\alpha=\beta\cdot\gamma+\rho{% endequation %} אחרת היינו מקבלים סתירה למקסימליות עם {% equation %}\beta\cdot\gamma+\rho+1{% endequation %}.

את המשפט המרכזי של הצורה הנורמלית מוכיחים באינדוקציה על {% equation %}\alpha{% endequation %}. עבור {% equation %}\alpha=1{% endequation %} בוחרים {% equation %}\beta=0{% endequation %} ומקבלים {% equation %}\alpha=\omega^{\beta}{% endequation %} כך ש-{% equation %}\alpha\ge\beta{% endequation %}. עבור {% equation %}\alpha>1{% endequation %} כלשהו, בוחרים את {% equation %}\beta{% endequation %} להיות הסודר הגדול ביותר כך ש-{% equation %}\alpha\ge\omega^{\beta}{% endequation %}. קיים כזה כי {% equation %}\alpha\le\omega^{\alpha}{% endequation %} (ההוכחה היא באינדוקציה; נראה אותה בפוסט הבא בתור דוגמא). על פי משפט החלוקה שראינו, קיימים {% equation %}\delta,\rho{% endequation %} כך ש-{% equation %}\rho<\omega^{\beta}{% endequation %} ומתקיים {% equation %}\alpha=\omega^{\beta}\cdot\delta+\rho{% endequation %}. עכשיו שמים לב ש-{% equation %}\delta{% endequation %} חייב להיות מספר טבעי (כי אם היה לפחות {% equation %}\omega{% endequation %} היינו מקבלים {% equation %}\omega^{\beta}\cdot\delta\ge\omega^{\beta}\cdot\omega=\omega^{\beta+1}{% endequation %} בסתירה למקסימליות של {% equation %}\beta{% endequation %}) ואפשר להמשיך באינדוקציה על {% equation %}\rho{% endequation %}.

זה מסיים את הפוסט הזה, אבל כמות נפנופי הידיים שהלכה פה היא לא זניחה, והיא תחמיר בהמשך אם לא נעצור כדי להבין מה הולך באינדוקציות והרקורסיות שאני משתמש בהן; בזה יעסוק הפוסט הבא. 