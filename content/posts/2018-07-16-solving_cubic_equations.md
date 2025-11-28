---
id: 3645
title: "אז איך פותרים משוואה ממעלה שלישית?"
date: 2018-07-16 22:40:28
layout: post
categories: 
  - אלגברה מופשטת
tags: 
  - משוואה ממעלה שלישית
  - תורת גלואה
---
סדרת הפוסטים שלי על תורת גלואה הגיעה <a href="https://gadial.net/2018/07/12/insolvability_of_the_quintic/">בפוסט הקודם</a> אל נקודת השיא שלה, שבה הוכחתי שאין נוסחה כללית לפתרון משוואות (פולינומיות, כשהפתרון הוא בעזרת רדיקלים) ממעלה 5 ומעלה. ליתר דיוק, מה שהוכחתי הוא זה:
<ul>
 	<li>פולינום הוא פתיר באמצעות רדיקלים אם ורק אם חבורת הגלואה שלו היא פתירה.</li>
 	<li>חבורת הגלואה של "פולינום כללי" ממעלה {% equation %}n{% endequation %} מעל שדה {% equation %}F{% endequation %} שכולל גם את <strong>המקדמים</strong> של הפולינום היא {% equation %}S_{n}{% endequation %}.</li>
 	<li>{% equation %}S_{n}{% endequation %} לא פתירה עבור {% equation %}n\ge5{% endequation %} וכן פתירה עבור {% equation %}n\le4{% endequation %}.</li>
</ul>
מה שעניין אותי עד כה היה ה-"{% equation %}S_{n}{% endequation %} לא פתירה עבור {% equation %}n\ge5{% endequation %}", אבל עכשיו היוצרות מתהפכות ואני מנסה להבין איך המשפט של גלואה "מגלה לנו" את הפתרונות עבור המקרים {% equation %}n=2,3,4{% endequation %}. זו גישה קצת אנכרוניסטית כי היא הופכת את הסדר - הנוסחאות לפתרון משוואות ממעלה רביעית ומטה היו ידועות היטב בימיו של גלואה והתגלו מאות שנים לפני כן. לא "צריך" את תורת גלואה בשבילן, אבל אני חושב שתורת גלואה עוזרת להבין מה בעצם הולך בהן, וזו גם הזדמנות טובה להראות את הצד ה"חיובי" של תורת גלואה בפעולה - זה שאשכרה יודע לפתור משוואות ולא רק להגיד שתשכחו מזה.
<h2>הדיסקרימיננטה</h2>
כזכור או לא, שיטת העבודה שגלואה הציע היא זו: אם {% equation %}E/F{% endequation %} היא ההרחבה שבה {% equation %}E{% endequation %} הוא שדה הפיצול של הפולינום מעל {% equation %}F{% endequation %} שאנחנו רוצים לפתור, ואם {% equation %}G=\text{Gal}\left(E/F\right){% endequation %} היא פתירה, אז זה נותן לנו סדרה של תת-חבורות {% equation %}G=G_{0}\supset G_{1}\supset\dots\supset G_{k}=\left\{ e\right\} {% endequation %} כך ש-{% equation %}G_{i}/G_{i+1}{% endequation %} היא ציקלית לכל {% equation %}0\le i&lt;k{% endequation %}. תת-החבורות הללו נותנות לנו סדרה של שדות, שהם שדות השבת שלהן: {% equation %}F=E_{0}\subset E_{1}\subset\dots\subset E_{k}=E{% endequation %}. הטוויסט של גלואה עכשיו הוא שאפשר לקבל כל {% equation %}E_{i+1}{% endequation %} כזו מתוך {% equation %}E_{i}{% endequation %} על ידי הוצאת שורש מסדר כלשהו לאיבר ב-{% equation %}E_{i}{% endequation %} (בתנאי שב-{% equation %}E_{i}{% endequation %} כבר יש את שורשי היחידה המתאימים, אחרת תוקעים הרחבה נוספת בין {% equation %}E_{i}{% endequation %} ו-{% equation %}E_{i+1}{% endequation %} שמוסיפה אותם, גם כן על ידי הוצאת שורש).

כעת נשאלת השאלה איך מבצעים בפועל כל צעד בסדרת הצעדים הזו. כלומר, אם {% equation %}E/F{% endequation %} הרחבה כך ש-{% equation %}\text{Gal}\left(E/F\right){% endequation %} ציקלית מסדר {% equation %}n{% endequation %} ויש ב-{% equation %}F{% endequation %} כבר את שורשי היחידה מסדר {% equation %}n{% endequation %}, מה עושים כדי למצוא את האיבר שצריך להרחיב באמצעות שורש שלו את {% equation %}F{% endequation %} כדי לקבל את {% equation %}E{% endequation %}? אם נסתכל <a href="http://בהוכחה שהראיתי">בהוכחה שהראיתי</a>, אז נראה שהפתרון עובר דרך מה שנקרא <strong>הרזולבנטה של לגראנז'</strong>. הרעיון הוא זה: אם {% equation %}\text{Gal}\left(E/F\right){% endequation %} ציקלית עם יוצר {% equation %}\sigma{% endequation %}, ואם {% equation %}\omega{% endequation %} הוא שורש יחידה פרימיטיבי מסדר {% equation %}n{% endequation %}, ואם {% equation %}\alpha\in E{% endequation %} הוא איבר כלשהו, אז מגדירים את הרזולבנטה כך:

{% equation %}\left(\alpha,\omega\right)=\alpha+\omega\sigma\left(\alpha\right)+\omega^{2}\sigma^{2}\left(\alpha\right)+\dots+\omega^{n-1}\sigma^{n-1}\left(\alpha\right){% endequation %}

כלומר, הרזולבנטה של {% equation %}\alpha,\omega{% endequation %} היא איבר של {% equation %}E{% endequation %} שנבנה בתור איזה סכום מתוחכם של דברים שמתקבלים מ-{% equation %}\alpha,\omega{% endequation %} וחבורת הגלואה. מה שהוכחנו כבר הוא שהחזקה ה-{% equation %}n{% endequation %}-ית של האיבר הזה שייכת ל-{% equation %}F{% endequation %}, ושאם האיבר הזה שונה מאפס אז הוא לא שייך לאף שדה ביניים של {% equation %}E{% endequation %}, כלומר הוספה שלו ל-{% equation %}F{% endequation %} תייצר בהכרח את {% equation %}E{% endequation %}. מה שעושים עכשיו הוא לסמן {% equation %}a\triangleq\left(\alpha,\omega\right)^{n}{% endequation %} ולקבל {% equation %}E=F\left(\sqrt[n]{a}\right){% endequation %} (כאשר כאמור {% equation %}a\in F{% endequation %} כי זה הקסם שרזולבנטה עושה).

בואו נתחיל מלראות דוגמא למה קורה במקרה הפשוט של הרחבה ממימד 2. נסתכל על המקרה הקונקרטי של <strong>יחס הזהב</strong> {% equation %}\varphi{% endequation %} שהוא שורש של הפולינום {% equation %}x^{2}-x-1{% endequation %}, שקל לראות שהוא אי-פריק מעל {% equation %}\mathbb{Q}{% endequation %} ולכן ההרחבה {% equation %}\mathbb{Q}\left(\varphi\right)/\mathbb{Q}{% endequation %} היא ממימד 2. כרגע לא ברור שהיא רדיקלית כי {% equation %}\varphi{% endequation %} <strong>אינו</strong> שורש של אף איבר ב-{% equation %}\mathbb{Q}{% endequation %}. השאלה היא "לאיזה איבר של {% equation %}\mathbb{Q}{% endequation %} ישתלם לנו עכשיו להוציא שורש כדי לקבל את {% equation %}\mathbb{Q}\left(\varphi\right){% endequation %}".

מכיוון שההרחבה {% equation %}\mathbb{Q}\left(\varphi\right)/\mathbb{Q}{% endequation %} היא ממימד 2, חבורת הגלואה המתאימה היא בת שני איברים, היחידה ו-{% equation %}\sigma{% endequation %}, כאשר {% equation %}\sigma{% endequation %} מחליפה בין {% equation %}\varphi{% endequation %} לבין הפתרון השני של המשוואה שמסומן לעתים כ-{% equation %}\varphi_{-}{% endequation %}. במקרה של חבורה ממימד 2, שורש היחידה שצריך בשביל הרזולבנטה הוא פשוט {% equation %}\omega=-1{% endequation %}, והרזולבנטה של איבר כלשהו תצא {% equation %}\left(\alpha,\omega\right)=\alpha-\sigma\left(\alpha\right){% endequation %}. מה שאנחנו מחפשים, אם כן, הוא איבר של {% equation %}\mathbb{Q}\left(\varphi\right){% endequation %} שהרזולבנטה שלו לא תהיה 0, ואז הרזולבנטה הזו תהיה יוצרת של {% equation %}\mathbb{Q}\left(\varphi\right){% endequation %} והריבוע שלה יהיה שייך ל-{% equation %}\mathbb{Q}{% endequation %}.

את מי ניקח כדי לייצר את הרזולבנטה הזו? למה לא את {% equation %}\varphi{% endequation %} עצמו? {% equation %}\varphi\ne\sigma\left(\varphi\right){% endequation %} (לא מאמינים? פשוט תבדקו ש-{% equation %}x^{2}-x-1{% endequation %} ספרבילי על ידי גזירה שלו) ולכן {% equation %}\varphi-\varphi_{-}{% endequation %} הוא האיבר שאנחנו מחפשים. אבל מי הוא בעצם? אם פותרים את {% equation %}x^{2}-x-1{% endequation %} בעזרת נוסחת השורשים רואים ש-{% equation %}\varphi=\frac{1+\sqrt{5}}{2}{% endequation %} ואילו {% equation %}\varphi_{-}=\frac{1-\sqrt{5}}{2}{% endequation %}; כלומר, הרזולבנטה היא {% equation %}\left(\frac{1+\sqrt{5}}{2}\right)-\left(\frac{1-\sqrt{5}}{2}\right)=\sqrt{5}{% endequation %}. טה-דה! ההוכחה של גלואה הראתה לנו את מה שהיה ברור לנו אינטואיטיבית מראש - שאם מסתכלים על {% equation %}\frac{1+\sqrt{5}}{2}{% endequation %}, אז "החלק החשוב" פה הוא {% equation %}\sqrt{5}{% endequation %}; ש-{% equation %}\mathbb{Q}\left(\sqrt{5}\right){% endequation %} היא הדרך ה"רדיקלית" להציג את ההרחבה שלנו. עדיין, זה לא אומר שמה שהולך פה לא היה חמוד - אני מקווה שזה הזכיר לכם את האופן שבו כדי לבודד את החלק <strong>המדומה</strong> מתוך מספר מרוכב {% equation %}a+bi{% endequation %}, <strong>מחסרים</strong> ממנו את הצמוד שלו; זה בדיוק הסיפור כאן.

עכשיו בואו נדבר על מה קורה במקרה של "פולינום כללי". בפוסט הקודם הצגתי שתי שיטות סימון לפולינום כללי, אחת שמציגה אותו בעזרת המקדמים שלו (שההנחה היא שהם בלתי תלויים אלגברית) ואחרת שמציגה אותו באמצעות השורשים שלו (שגם עליהם יש את ההנחה הזו). ההצגה באמצעות מקדמים נראית קצת מוזרה במבט ראשון אבל ראינו למה היא עדיפה על הכתיב היותר אינטואיטיבי בפוסט הקודם:

{% equation %}p\left(x\right)=x^{n}-s_{1}x^{n-1}+s_{2}x^{n-2}+\dots+\left(-1\right)^{n-1}s_{n-1}x+\left(-1\right)^{n}s_{n}{% endequation %}

ההצגה באמצעות שורשים היא זו:

{% equation %}p\left(x\right)=\left(x-\alpha_{1}\right)\left(x-\alpha_{2}\right)\cdots\left(x-\alpha_{n}\right){% endequation %}

וההרחבה הרלוונטית שאנחנו רוצים להראות שהיא רדיקלית היא {% equation %}F\left(\alpha_{1},\dots,\alpha_{n}\right)/F\left(s_{1},\dots,s_{n}\right){% endequation %}, כאשר {% equation %}F{% endequation %} הוא שדה כלשהו ממציין 0 אבל בדרך כלל אנחנו חושבים עליו בתור {% equation %}\mathbb{Q}{% endequation %} (הוא בוודאי <strong>מכיל</strong> את {% equation %}\mathbb{Q}{% endequation %}, ואנחנו לא משתמשים בהנחות נוספות לגביו).

בפוסט הקודם ראינו שחבורת הגלואה של ההרחבה הזו היא {% equation %}S_{n}{% endequation %}; עבור כל {% equation %}\sigma\in S_{n}{% endequation %}, האוטומורפיזם של {% equation %}F\left(\alpha_{1},\dots,\alpha_{n}\right){% endequation %} ש-{% equation %}\sigma{% endequation %} מתארת הוא זה שמבצע פרמוטציה על השורשים {% equation %}\alpha_{1},\dots,\alpha_{n}{% endequation %} כמו ש-{% equation %}\sigma{% endequation %} מבצעת פרמוטציה על {% equation %}\left\{ 1,2,\dots,n\right\} {% endequation %}, כלומר אם משתמשים ב-Abuse of notation ומשתמשים ב-{% equation %}\sigma{% endequation %} גם כדי לתאר את האוטומורפיזם, זה האוטומורפיזם שמבצע {% equation %}\sigma\left(\alpha_{i}\right)=\alpha_{\sigma\left(i\right)}{% endequation %}. על אברי {% equation %}F{% endequation %} האוטומורפזים {% equation %}\sigma{% endequation %} פועל כמו הזהות, ולכן הוא הזהות על כל {% equation %}F\left(s_{1},\dots,s_{n}\right){% endequation %}, כי כל {% equation %}s_{i}{% endequation %} כזה הוא <strong>פונקציה סימטרית</strong> בשורשים {% equation %}\alpha_{1},\dots,\alpha_{n}{% endequation %} ולכן משתמר על ידי פרמוטציות שלהם.

בואו נסתכל שוב על המקרה של פולינום ממעלה שניה, הפעם פולינום כללי {% equation %}p\left(x\right)=x^{2}-bx+c{% endequation %}. אם אסמן את שורשי הפולינום ב-{% equation %}\alpha,\beta{% endequation %} נקבל את שתי המשוואות

{% equation %}b=\alpha+\beta{% endequation %}

{% equation %}c=\alpha\beta{% endequation %}

במקרה הזה, חבורת הגלואה שלנו כוללת שני איברים, הזהות ו-{% equation %}\sigma{% endequation %} שמקיימת {% equation %}\sigma\left(\alpha\right)=\beta{% endequation %} ו-{% equation %}\sigma\left(\beta\right)=\alpha{% endequation %}. אז אם ניקח את {% equation %}\alpha{% endequation %} בתור יוצר אפשרי של רזולבנטה מועילה, נקבל את הרזולבנטה {% equation %}\alpha-\sigma\left(\alpha\right)=\alpha-\beta{% endequation %}. אם ניקח את הריבוע שלה, נקבל {% equation %}\left(\alpha-\beta\right)^{2}=\alpha^{2}-2\alpha\beta+\beta^{2}{% endequation %} ש<strong>אמור</strong> להיות איבר של {% equation %}\mathbb{Q}\left(b,c\right){% endequation %}. איך אני יודע שזה יעבוד? כי {% equation %}\alpha^{2}-2\alpha\beta+\beta^{2}{% endequation %} היא פונקציה סימטרית, ולכן ניתנת להצגה בתור צירוף של פונקציות סימטריות פרימיטיביות. עכשיו, לא התעסקתי באלגוריתם שתמיד מוצא ייצוג כזה, אבל אפשר עם תעלול קטן להצליח פה בקלות: פשוט שמים לב לכך ש-

{% equation %}b^{2}=\left(\alpha+\beta\right)^{2}=\alpha^{2}+2\alpha\beta+\beta^{2}{% endequation %}

שזה כמעט אותו דבר כמו מה שאנחנו רוצים, רק צריך להפוך את הסימן של ה-{% equation %}2\alpha\beta{% endequation %} שבאמצע - ואת זה אפשר לעשות בעזרת {% equation %}c=\alpha\beta{% endequation %}. נקבל:

{% equation %}b^{2}-4c=\left(\alpha-\beta\right)^{2}{% endequation %}

ולכן {% equation %}\sqrt{b^{2}-4c}=\left(\alpha-\beta\right){% endequation %} הוא האיבר שאם נרחיב את {% equation %}\mathbb{Q}{% endequation %} באמצעותו נגיע לשדה שבו נמצאים {% equation %}\alpha,\beta{% endequation %}: {% equation %}\mathbb{Q}\left(\alpha,\beta\right)=\mathbb{Q}\left(\sqrt{b^{2}-4c}\right){% endequation %}. הביטוי {% equation %}b^{2}-4c{% endequation %} בוודאי מוכר לכם - הוא מופיע בנוסחה הכללית לפתרון משוואה ממעלה שניה, ואולי שמעתם את השם <strong>דיסקרימיננטה</strong> שבא לתאר אותו. אנחנו מכירים את הדיסקרימיננטה בתור כלי שבא לספר לנו משהו על הפתרונות: אם {% equation %}b^{2}-4c&gt;0{% endequation %} אז יש לנוסחה שני פתרונות ממשיים, אם {% equation %}b^{2}-4c=0{% endequation %} אז יש פתרון ממשי יחיד ואם {% equation %}b^{2}-4c&lt;0{% endequation %} אז יש שני פתרונות מרוכבים. עם זאת, זה לא יהיה ההיבט שיעניין אותי עכשיו (אבל שימו לב שאם {% equation %}b^{2}-4c=0{% endequation %} אז אכן, אין הרחבה; הפתרון למשוואה במקרה הזה הוא איבר <strong>יחיד</strong> שכבר שייך ל-{% equation %}\mathbb{Q}{% endequation %}).

עכשיו השאלה היא מה קורה במקרה של פולינום כללי ממעלות גבוהות יותר. התשובה היא שתמיד ניתן להגדיר דיסקרימיננטה, והוספה שלה היא תמיד הצעד הראשון החיובי שאפשר לנקוט בו. אבל מה ההגדרה הנכונה לדיסקרימיננטה כללית? בשביל להבין את זה בואו ננסה להבין את הפרטים המלוכלכים שהיה קל לטאטא מתחת לשטיח במקרה של מימד 2. בואו נסמן ב-{% equation %}E{% endequation %} את שדה השבת של {% equation %}A_{n}{% endequation %} בתוך {% equation %}F\left(\alpha_{1},\dots,\alpha_{n}\right){% endequation %}, אז מה שאנחנו יודעים הוא שחבורת הגלואה של {% equation %}E/F\left(s_{1},\dots,s_{n}\right){% endequation %} איזומורפית ל-{% equation %}\mathbb{Z}_{2}{% endequation %}, ואנחנו מנסים למצוא דרך לייצר את {% equation %}E{% endequation %}. הבעיה היא שלא ברור מי הוא {% equation %}E{% endequation %} במקרה הכללי; במקרה של מימד 2, זה היה פשוט {% equation %}F\left(\alpha,\beta\right){% endequation %} עצמו.

אם כן, השאלה שלנו היא זו: בהינתן {% equation %}\sigma\in A_{n}{% endequation %}, מי האיברים שמשתמרים על ידי כל {% equation %}\sigma{% endequation %} שכזו?מה שדה הביניים של {% equation %}F\left(\alpha_{1},\dots,\alpha_{n}\right){% endequation %} שמתאים ל-{% equation %}A_{n}{% endequation %}? בשביל לענות לשאלה הזו כדאי לחזור לפוסט שבו <a href="https://gadial.net/2017/03/14/permutation_groups/">הגדרתי לראשונה</a> את {% equation %}A_{n}{% endequation %}. ההגדרה שלי הייתה מוזרה במבט ראשון - הגדרתי את {% equation %}A_{n}{% endequation %} בתור <strong>גרעין של הומומורפיזם</strong> של פונקציה שעשתה את הדבר הבא: הסתכלה על הפולינום {% equation %}\Delta=\prod_{1\le i&lt;j\le n}\left(x_{i}-x_{j}\right){% endequation %} ולכל {% equation %}\sigma{% endequation %} התאימה את {% equation %}\frac{\sigma\left(\Delta\right)}{\Delta}{% endequation %}, כאשר {% equation %}\sigma{% endequation %} פעל על {% equation %}\Delta{% endequation %} בדרך ה"צפויה": {% equation %}\sigma\left(x_{i}\right)=x_{\sigma\left(i\right)}{% endequation %}. לא קשה להוכיח שזה הומומורפיזם שמחזיר או 1 או {% equation %}-1{% endequation %}, ו-{% equation %}A_{n}{% endequation %} הוגדרה להיות הגרעין שלו. כלומר כל התמורות {% equation %}\sigma{% endequation %} שמקיימות {% equation %}\sigma\left(\Delta\right)=\Delta{% endequation %}. עכשיו, מה זה אומר לנו? אם במקום לדבר על {% equation %}x_{i}{% endequation %}-ים נדבר על {% equation %}\alpha_{i}{% endequation %}-ים, מה שאנחנו רואים הוא ש-{% equation %}\Delta{% endequation %} הוא איבר ששייך <strong>לשדה השבת</strong> של כל אברי {% equation %}A_{n}{% endequation %}, אבל מכיוון שיש איברים ב-{% equation %}S_{n}{% endequation %} שמחזירים עליו {% equation %}-1{% endequation %}, הוא בוודאי לא שייך לשדה השבת של {% equation %}S_{n}{% endequation %}, כלומר הוא לא שייך ל-{% equation %}F\left(s_{1},\dots,s_{n}\right){% endequation %}.

עכשיו, מהי הרזולבנטה של {% equation %}\Delta{% endequation %}? מכיוון ש-{% equation %}S_{n}/A_{n}\cong\mathbb{Z}_{2}{% endequation %} הסיטואציה דומה לזו שהייתה קודם - הרזולבנטה תהיה {% equation %}\Delta-\sigma\left(\Delta\right){% endequation %}, אבל צריך להיות קצת זהירים לגבי מהי {% equation %}\sigma{% endequation %} הזו. הרי האיברים של {% equation %}S_{n}/A_{n}{% endequation %} הם <strong>קוסטים</strong> של {% equation %}S_{n}{% endequation %}. מה זה אומר במקרה שלנו? אנחנו לא יכולים להפעיל קוסט על {% equation %}\Delta{% endequation %}!

ובכן, אם נחזור למה שעשינו בהוכחת המשפט היסודי של תורת גלואה נראה שהרעיון הכללי היה זה: אם {% equation %}F\subseteq K\subseteq E{% endequation %} היא מגדל של הרחבות כך ש-{% equation %}\text{Gal}\left(E/F\right)=G{% endequation %} ו-{% equation %}\text{Gal}\left(E/K\right)=H{% endequation %} אז {% equation %}\text{Gal}\left(K/F\right)\cong G/H{% endequation %}, אבל צריך להבין שזה רק איזומורפיזם; זה לא שוויון ממש של חבורות. האיברים של {% equation %}\text{Gal}\left(K/F\right){% endequation %} הם אוטומורפיזמים של {% equation %}K{% endequation %}, לא קוסטים של {% equation %}G/H{% endequation %}, כלומר קבוצות של אוטומורפיזמים של {% equation %}G{% endequation %}. הנקודה הייתה שאם {% equation %}\sigma\in\text{Gal}\left(K/F\right){% endequation %} היא אוטומורפיזם של {% equation %}K{% endequation %} אז ניתן <strong>להרחיב</strong> את {% equation %}\sigma{% endequation %} לאוטומורפיזם של {% equation %}G{% endequation %} בשלל דרכים שונות, והדרכים הללו יניבו בדיוק את האיברים של {% equation %}G/H{% endequation %}. במילים אחרות, אם אני רוצה להבין מה {% equation %}\sigma{% endequation %} עושה לאיברים של {% equation %}K{% endequation %}, אני יכול לקחת איבר <strong>כלשהו</strong> של הקוסט המתאים ב-{% equation %}G/H{% endequation %} ולהפעיל אותו על אברי {% equation %}K{% endequation %}, ומובטח לי שלא משנה איזה איבר אני אקח מהקוסט אני אקבל את אותה התוצאה.

במקרה שלנו, כדי להבין מה {% equation %}\sigma\in S_{n}/A_{n}{% endequation %} עושה ל-{% equation %}\Delta{% endequation %} אני יכול לבחור {% equation %}\sigma\in S_{n}{% endequation %} <strong>כלשהו</strong> ששייך לקוסט הלא טריוויאלי ב-{% equation %}S_{n}/A_{n}{% endequation %}; כלומר, {% equation %}\sigma{% endequation %} היא בדיוק תמורה אי-זוגית <strong>כלשהי</strong>. העניין הוא שכפי שכבר ראינו, הפעולה של כל התמורות האי זוגיות על {% equation %}\Delta{% endequation %} היא זהה: {% equation %}\sigma\left(\Delta\right)=-\Delta{% endequation %}. מכאן שהרזולבנטה של {% equation %}\Delta{% endequation %} תהיה {% equation %}\left(\Delta,-1\right)=\Delta-\sigma\left(\Delta\right)=\Delta+\Delta=2\Delta{% endequation %}. כלומר, עד כדי הקבוע חסר המשמעות של 2, הרזולבנטה של {% equation %}\Delta{% endequation %} זו היא עצמה, מה שאומר ש-{% equation %}\Delta^{2}\in F\left(s_{1},\dots,s_{n}\right){% endequation %}. כמובן, אין כאן משהו מפתיע במיוחד: נסמן {% equation %}D=\Delta^{2}{% endequation %} אז קל לראות ש-{% equation %}D=\prod_{1\le i&lt;j\le n}\left(\alpha_{i}-\alpha_{j}\right)^{2}=\prod_{i\ne j}\left(\alpha_{i}-\alpha_{j}\right){% endequation %} היא פולינום סימטרי ולכן בוודאי שניתן לכתיבה באמצעות {% equation %}s_{1},\dots,s_{n}{% endequation %}. ה-{% equation %}D{% endequation %} הזה נקרא <strong>הדיסקרימיננטה</strong> של הפולינום; לכל פולינום עם שורשים {% equation %}\alpha_{1},\dots,\alpha_{n}{% endequation %} הדיסקרימיננטה מוגדרת כ-{% equation %}\prod_{1\le i&lt;j\le n}\left(\alpha_{i}-\alpha_{j}\right)^{2}{% endequation %}, גם אם זה לא פולינום גנרי ואפילו אם שורש כלשהו חוזר על עצמו (ולכן {% equation %}D=0{% endequation %} במקרה הזה).

לסיכום: אם אנחנו רוצים לפתור משוואה פולינומית כלשהי באמצעות רדיקלים, הצעד הראשון שכדאי שננקוט בו הוא להוסיף לשדה שלנו את {% equation %}\sqrt{D}{% endequation %} - השורש הריבועי של הדיסקרימיננטה של המשוואה. במשוואות ממעלה שניה זה מסיים את הסיפור. ובמשוואה ממעלה שלישית? ובכן, כאן הסיטואציה מסובכת יותר.
<h2>איך פותרים משוואה ממעלה שלישית, שלב א': מציאת הדיסקרימיננטה</h2>
נתחיל במילה זריזה למי שבאים לפה בתקווה למצוא נוסחה פשוטה כמו עבור משוואות למעלה שניה - <strong>תשכחו מזה</strong>. לא סתם הייתה מהומה שלמה סביב פתרון משוואות כאלו, ואני מקווה לכתוב פוסט מפורט בנושא בעתיד. אבל, וזה אבל גדול, עכשיו משאנחנו מצויידים בידע מתורת גלואה, מה שהולך פה לא יראה כמו מהומה אקראית אלא יש סדר והגיון כלשהו במה שנעשה.

השלב הראשון הוא <strong>פישוט</strong> של המשוואה שאנחנו רוצים לפתור, על ידי החלפת משתנים. <a href="https://gadial.net/2018/07/07/galois_theory_and_radical_extensions/">לא מזמן הצגתי</a> שיטה פשוטה למציאת הנוסחה של משוואה ממעלה שניה; התעלול המרכזי שם היה לפשט את {% equation %}x^{2}+ax+b{% endequation %} על ידי ההחלפה {% equation %}y=x+\frac{a}{2}{% endequation %}. זה "מחק" לגמרי את המקדם של {% equation %}x{% endequation %} במשוואה, ונותרה לנו משוואה עם מקדם חופשי מסובך.

במשוואה ממעלה שלישית ננקוט בתעלול דומה, אבל זה לא יסיים את הסיפור עבורנו אלא רק יעלים את אחד מהגורמים במשוואה, ובכך יפשט את מצב העניינים. אם המשוואה שלנו היא {% equation %}x^{3}+ax^{2}+bx+c{% endequation %}, אז נשתמש בהחלפה {% equation %}y=x+\frac{a}{3}{% endequation %}. כלומר, {% equation %}x=y-\frac{a}{3}{% endequation %}. עכשיו אפשר לבצע חישוב ארוך וכואב ולבדוק עם מה אנחנו נשארים:

{% equation %}x^{3}=\left(y-\frac{a}{3}\right)^{3}=y^{3}-y^{2}a+\frac{ya^{2}}{3}-\frac{a^{3}}{27}{% endequation %}

{% equation %}ax^{2}=a\left(y-\frac{a}{3}\right)^{2}=ay^{2}-\frac{2ya^{2}}{3}+\frac{a^{3}}{9}{% endequation %}

{% equation %}bx=by-\frac{ba}{3}{% endequation %}

שימו לב ל-{% equation %}-y^{2}a{% endequation %} בשורה של {% equation %}x^{3}{% endequation %} ול-{% equation %}ay^{2}{% endequation %} בשורה של {% equation %}ax^{2}{% endequation %} - הם מבטלים זה את זה, ולכן אנחנו הולכים להישאר עם משוואה מהצורה

{% equation %}y^{3}+py+q{% endequation %}

החישוב המדויק של {% equation %}p,q{% endequation %} לא כל כך חשוב לנו כי מכאן ואילך אני הולך לפתור רק את המשוואה הזו ולא אטרח בסוף לחזור למשוואה המקורית, אבל למי שזה חשוב לו, אפשר לבצע את החישוב הזה בקלות, הוא פשוט לא יפה:

{% equation %}p=\frac{a^{2}}{3}-2\frac{a^{2}}{3}+b=b-\frac{a^{2}}{3}=\frac{1}{3}\left(3b-a^{2}\right){% endequation %}

{% equation %}q=-\frac{a^{3}}{27}+\frac{a^{3}}{9}-\frac{ba}{3}+c=\frac{1}{27}\left(2a^{3}-9ab+27c\right){% endequation %}

זהו, מעכשיו אני רוצה להתמקד בשאלה איך פותרים את המשוואה הבאה:

{% equation %}x^{3}+px+q{% endequation %}

אם הולכים על פי השיטה של תורת גלואה, הצעד הראשון הוא להוסיף את {% equation %}\sqrt{D}{% endequation %} לשדה שלנו, מה שאומר שנצטרך לחשב את הדיסקרימיננטה (בגלל הפישוט של המשוואה, גם הדיסקרימיננטה תצא פשוטה). השלב השני הוא להמשיך את שרשרת התת-חבורות שלנו: האיבר הנוכחי בשרשרת הוא {% equation %}A_{3}{% endequation %}, שהוא פשוט החבורה הציקלית {% equation %}\mathbb{Z}_{3}{% endequation %}. זה אומר שאם אנחנו כרגע בשדה {% equation %}E{% endequation %}, אז ההרחבה שאנחנו צריכים כדי להגיע אל הפתרונות של המשוואה היא זו: קודם כל להוסיף ל-{% equation %}E{% endequation %} את שורשי היחידה מסדר 3, ואחר כך להוסיף ל-{% equation %}E{% endequation %} רזולבנטה שונה מאפס של איבר כלשהו משדה הפיצול.

אני אגלה מראש שהדיסקרימיננטה שנקבל תהיה {% equation %}D=-4p^{3}-27q^{2}{% endequation %}, אבל כדי לקבל אותה נצטרך לעשות קצת להטוטים.

בואו נסמן את השורשים של המשוואה ב-{% equation %}\alpha,\beta,\gamma{% endequation %}. מה שאנחנו מחפשים הוא דרך לתאר ב-{% equation %}\mathbb{Q}\left(p,q\right){% endequation %} את

{% equation %}\left(\alpha-\beta\right)^{2}\left(\alpha-\gamma\right)^{2}\left(\beta-\gamma\right)^{2}{% endequation %}

אפשר פשוט לפתוח את הסוגריים ולקבץ איברים, אבל זה יהיה איבר מפלצתי בגודלו. הנה תעלול שיכול לפשט מאוד את העניינים: בואו נכתוב את {% equation %}g\left(x\right)=x^{3}+px+q{% endequation %} במפורש בעזרת השורשים:

{% equation %}g\left(x\right)=\left(x-\alpha\right)\left(x-\beta\right)\left(x-\gamma\right){% endequation %}

עכשיו, מצד אחד קל לנו לגזור את {% equation %}g\left(x\right){% endequation %} כשהוא מוצג עם {% equation %}p,q{% endequation %}:

{% equation %}g^{\prime}\left(x\right)=3x^{2}+p{% endequation %}

אם נגזור את {% equation %}g\left(x\right){% endequation %} בצורה הכפלית שלה, על פי כללי הגזירה הרגילים, נקבל:

{% equation %}g^{\prime}\left(x\right)=\left(x-\beta\right)\left(x-\gamma\right)+\left(x-\alpha\right)\left(x-\gamma\right)+\left(x-\alpha\right)\left(x-\beta\right){% endequation %}

עכשיו ננקוט בתעלול ונציב בתוך {% equation %}g^{\prime}{% endequation %} הזו כל אחד משלושת השורשים. זה תמיד יאפס שניים מהמחוברים, כך שנקבל:

{% equation %}g^{\prime}\left(\alpha\right)=\left(\alpha-\beta\right)\left(\alpha-\gamma\right){% endequation %}

{% equation %}g^{\prime}\left(\beta\right)=\left(\beta-\alpha\right)\left(\beta-\gamma\right){% endequation %}

{% equation %}g^{\prime}\left(\gamma\right)=\left(\gamma-\beta\right)\left(\gamma-\alpha\right){% endequation %}

ועכשיו תראו איזה קסם קרה! המכפלה של כל שלושת הביטויים הללו היא בדיוק {% equation %}D{% endequation %}, עד כדי סימן!

{% equation %}D=-g^{\prime}\left(\alpha\right)g^{\prime}\left(\beta\right)g^{\prime}\left(\gamma\right)=-\left(3\alpha^{2}+p\right)\left(3\beta^{2}+p\right)\left(3\gamma^{2}+p\right){% endequation %}

הבעיה היא שעכשיו הכיף נגמר - עדיין יש לי ביטוי מסובך שצריך לפשט, ואין לי ברירה אלא לפתוח את הסוגריים. זה כאילו עברתי לדבר על פולינום אחר, שהמשתנה שלו הוא {% equation %}p{% endequation %} והשורשים שלו הם {% equation %}-3\alpha^{2},-3\beta^{2},-3\gamma^{2}{% endequation %}. לכן ברור שכשאני אפתח את הסוגריים אני אקבל פונקציות סימטריות בשורשים; הכי פשוט יהיה לכתוב את זה ולגמור עם זה:

{% equation %}-D=p^{3}+3\left(\alpha^{2}+\beta^{2}+\gamma^{2}\right)p^{2}+9\left(\alpha^{2}\beta^{2}+\alpha^{2}\gamma^{2}+\beta^{2}\gamma^{2}\right)p+27\left(\alpha^{2}\beta^{2}\gamma^{2}\right){% endequation %}

אנחנו יודעים שכל פונקציה סימטרית ב-{% equation %}\alpha,\beta,\gamma{% endequation %} ניתנת לכתיבה בתור צירוף כלשהו של {% equation %}p,q{% endequation %} (כי כל פונקציה סימטרית בשורשים של פולינום ניתנת לכתיבה בתור צירוף של המקדמים). זה לא חוסך מאיתנו את הצורך המעיק למצוא את הצירוף הזה.

מה אנחנו יודעים על הקשר בין המקדמים והשורשים?
<ul>
 	<li>{% equation %}\alpha+\beta+\gamma=0{% endequation %} (זה המקדם של {% equation %}x^{2}{% endequation %})</li>
 	<li>{% equation %}p=\alpha\beta+\alpha\gamma+\beta\gamma{% endequation %}</li>
 	<li>{% equation %}q=-\alpha\beta\gamma{% endequation %}</li>
</ul>
אם כן, מייד אנחנו רואים ש-{% equation %}\alpha^{2}\beta^{2}\gamma^{2}=q^{2}{% endequation %} וזה כבר טיפל לנו באחת משלוש הפונקציות הסימטריות שיש למעלה. בואו נמשיך אל הבאות בתור.

אם נעלה בריבוע את {% equation %}\alpha+\beta+\gamma{% endequation %} נקבל:

{% equation %}0=\left(\alpha^{2}+\beta^{2}+\gamma^{2}\right)+2\left(\alpha\beta+\alpha\gamma+\beta\gamma\right)=\left(\alpha^{2}+\beta^{2}+\gamma^{2}\right)+2p{% endequation %}

כך שיש לנו עוד מקדם: המקדם של {% equation %}p^{2}{% endequation %} בדיסקרימיננטה הוא פשוט {% equation %}-2p{% endequation %}.

התעלול האחרון יהיה להעלות בריבוע את {% equation %}p{% endequation %} עצמו. נקבל:

{% equation %}p^{2}=\left(\alpha^{2}\beta^{2}+\alpha^{2}\gamma^{2}+\beta^{2}\gamma^{2}\right)+2\left(\alpha^{2}\beta\gamma+\alpha\beta^{2}\gamma+\alpha\beta\gamma^{2}\right){% endequation %}

המחובר הימני יעלים את עצמו:

{% equation %}\alpha^{2}\beta\gamma+\alpha\beta^{2}\gamma+\alpha\beta\gamma^{2}=q\left(\alpha+\beta+\gamma\right)=0{% endequation %}

כך שקיבלנו:

{% equation %}p^{2}=\left(\alpha^{2}\beta^{2}+\alpha^{2}\gamma^{2}+\beta^{2}\gamma^{2}\right){% endequation %}

וכשנציב הכל בביטוי של הדיסקרימיננטה נקבל:

{% equation %}-D=p^{3}+3\left(-2p\right)p^{2}+9\left(p^{2}\right)p+27\left(q^{2}\right)=4p^{3}+27q^{2}{% endequation %}

בדיוק כמו שהבטחתי למעלה.
<h2>איך פותרים משוואה ממעלה שלישית, שלב ב' - שובן של הרזולבנטות</h2>
סיכום ביניים קצר: התחלנו מ-{% equation %}\mathbb{Q}\left(p,q\right){% endequation %} ועברנו אל {% equation %}\mathbb{Q}\left(p,q,\sqrt{D}\right){% endequation %} כאשר {% equation %}D=-4p^{3}-27q^{2}{% endequation %}. עכשיו, אומרת תורת גלואה, נא להרחיב את השדה עם שורש יחידה פרימיטיבי מסדר 3. אוקיי, נסמן את השורש הזה ב-{% equation %}\omega\triangleq e^{\frac{2\pi i}{3}}{% endequation %}. אנחנו עכשיו מעל השדה {% equation %}\mathbb{Q}\left(p,q,\sqrt{D},\omega\right){% endequation %}. ועכשיו? עכשיו אנחנו מחפשים איבר שעדיין אין לנו, שחזקת 3 שלו כן נמצאת איתנו. איבר כזה יכול להתקבל בתור הרזולבנטה של משהו, בתנאי שהרזולבנטה הזו תהיה שונה מאפס.

איך נראית רזולבנטה במקרה שלנו? היא יותר מסובכת ממה שהיה קודם - קודם התעסקנו עם שורש היחידה הפרימיטיבי מסדר 2 ואילו עכשיו יש לנו את {% equation %}\omega{% endequation %}. חבורת הגלואה הרלוונטית היא {% equation %}A_{3}{% endequation %} שאפשר לכתוב הכי במפורש בעולם: {% equation %}A_{3}=\left\{ e,\left(1\ 2\ 3\right),\left(1\ 3\ 2\right)\right\} {% endequation %}. אז אני אסמן {% equation %}\sigma=\left(1\ 2\ 3\right){% endequation %}. באופן מפורש, זו הפונקציה שמבצעת

{% equation %}\sigma\left(\alpha\right)=\beta{% endequation %}

{% equation %}\sigma\left(\beta\right)=\gamma{% endequation %}

{% equation %}\sigma\left(\gamma\right)=\alpha{% endequation %}

ולכן:

{% equation %}\sigma^{2}\left(\alpha\right)=\gamma{% endequation %}

{% equation %}\sigma^{2}\left(\beta\right)=\alpha{% endequation %}

{% equation %}\sigma^{2}\left(\gamma\right)=\beta{% endequation %}

מה שנעשה עכשיו הוא להסתכל על <strong>כל</strong> הרזולבנטות של השורש {% equation %}\alpha{% endequation %}, עבור כל אחד משלושת שורשי היחידה האפשריים, {% equation %}1,\omega,\omega^{2}{% endequation %}:

{% equation %}\left(\alpha,1\right)=\alpha+\sigma\left(\alpha\right)=\sigma^{2}\left(\alpha\right)=\alpha+\beta+\gamma=0{% endequation %}

{% equation %}\left(\alpha,\omega\right)=\alpha+\sigma\left(\alpha\right)\omega=\sigma^{2}\left(\alpha\right)\omega^{2}=\alpha+\beta\omega+\gamma\omega^{2}=\theta_{1}{% endequation %}

{% equation %}\left(\alpha,\omega^{2}\right)=\alpha+\sigma\left(\alpha\right)\omega^{2}=\sigma^{2}\left(\alpha\right)\omega=\alpha+\beta\omega^{2}+\gamma\omega=\theta_{2}{% endequation %}

השילוב של שלוש הרזולבנטות הללו ביחד יכול לחלץ את {% equation %}\alpha{% endequation %} כמעט מייד באופן הבא: בואו נחבר את שלושתן ונקבל

{% equation %}0+\theta_{1}+\theta_{2}=3\alpha+\left(1+\omega+\omega^{2}\right)\beta+\left(1+\omega^{2}+\omega\right)\gamma{% endequation %}

העניין הוא ש-{% equation %}1+\omega+\omega^{2}=0{% endequation %}. אין כאן קסם מיוחד - זה כך לכל סכום של <strong>כל</strong> שורשי היחידה מסדר מסוים, ונובע פשוט מכך ש-

{% equation %}1+\omega+\omega^{2}+\dots+\omega^{n-1}=\frac{\omega^{n}-1}{\omega-1}=\frac{1-1}{\omega-1}=0{% endequation %}

לכן קיבלנו:

{% equation %}\alpha=\frac{\theta_{1}+\theta_{2}}{3}{% endequation %}

כאשר <strong>מובטח לנו</strong> ש-{% equation %}\theta_{1}^{3},\theta_{2}^{3}{% endequation %} כבר שייכים לשדה שאנחנו עובדים מעליו. כל מה שנשאר לנו לעשות הוא למצוא הצגה מפורשת שלהם. זה יהיה, אולי שלא במפתיע, החלק הכי טכני פה.

איך אני אחשב את {% equation %}\theta_{1}^{3}{% endequation %}? ובכן, במפורש. זה סכום של שלושה איברים, ולכן כשאעלה אותו בחזקה שלישית אני אקבל סכום של 27 איברים וזה לא נעים בכלל, אבל נתמודד עם זה. תהיה הרבה סימטריה.

הנוסחה הכללית שרלוונטית לנו היא זו:

{% equation %}\left(x+y+z\right)^{3}=\left(x^{3}+y^{3}+z^{3}\right)+3x^{2}\left(y+z\right)+3y^{2}\left(x+z\right)+3z^{2}\left(x+y\right)+6xyz{% endequation %}

הרעיון פה הוא כמו <a href="https://gadial.net/2010/06/22/newton_binom/">הבינום של ניוטון</a>: כל מונום בפיתוח הוא תוצאה של בחירה של איבר מכל אחד משלושת המוכפלים. {% equation %}x^{3}{% endequation %} למשל מתאים לסיטואציה שבה בחרנו את {% equation %}x{% endequation %} מכולם, ויש רק דרך אחת לעשות זאת; לעומת זאת, {% equation %}x^{2}y{% endequation %} פירושו שבחרנו {% equation %}x{% endequation %} משני מוכפלים ו-{% equation %}y{% endequation %} מהשלישי, ויש 3 דרכים לעשות זאת (אנחנו בוחרים מאיזה מהמוכפלים ניקח את {% equation %}y{% endequation %}). ה-{% equation %}6xyz{% endequation %} בסיום מגיע מכך שיש 6 פרמוטציות אפשריות על 1,2,3 וכל פרמוטציה אומרת לנו "מהמוכפל ה-{% equation %}i{% endequation %} קח את האיבר ה-{% equation %}\sigma\left(i\right){% endequation %}-י".

עכשיו אני מציב:

{% equation %}x=\alpha{% endequation %}

{% equation %}y=\beta\omega{% endequation %}

{% equation %}z=\gamma\omega^{2}{% endequation %}

ומקבל:

{% equation %}\left(\alpha^{3}+\beta^{3}+\gamma^{3}\right)+{% endequation %}

{% equation %}3\alpha^{2}\left(\beta\omega+\gamma\omega^{2}\right)+3\beta^{2}\omega^{2}\left(\alpha+\gamma\omega^{2}\right)+3\gamma^{2}\omega\left(\alpha+\omega\beta\right)+{% endequation %}

{% equation %}6\alpha\beta\gamma{% endequation %}

המחובר התחתון הוא פשוט מאוד: זה {% equation %}-6q{% endequation %} ידידינו משכבר הימים.

המחובר העליון גם כן לא מסובך. בואו נציב את {% equation %}\alpha,\beta,\gamma{% endequation %} בביטוי ל-{% equation %}\left(x+y+z\right)^{3}{% endequation %} שהראיתי קודם - אנחנו הרי יודעים ש-{% equation %}\alpha+\beta+\gamma=0{% endequation %} וזה יעזור לנו פעמיים: זה אומר לנו ש-{% equation %}\left(x+y+z\right)^{3}=0{% endequation %} במקרה הזה, וזה מחליף גורם כמו {% equation %}3x^{2}\left(y+z\right){% endequation %} בגורם הידידותי יותר {% equation %}-3x^{3}{% endequation %}, כך שבסופו של דבר נקבל:

{% equation %}0=-2\left(\alpha^{3}+\beta^{3}+\gamma^{3}\right)+6\alpha\beta\gamma{% endequation %}

כלומר

{% equation %}\alpha^{3}+\beta^{3}+\gamma^{3}=-3q{% endequation %}

עיקר המהומה נמצאת בגורם האמצעי; יותר קל להבין מה קורה איתו אם מקבצים אותו לפי חזקות של {% equation %}\omega{% endequation %}. אנחנו נקבל:

{% equation %}3\omega\left(\alpha^{2}\beta+\beta^{2}\gamma+\gamma^{2}\alpha\right)+3\omega^{2}\left(\alpha^{2}\gamma+\beta^{2}\alpha+\gamma^{2}\beta\right){% endequation %}

שזה, למען האמת, ביטוי די סימטרי ונחמד! אבל די קשה להרגיש את זה מבלי שתהיו חייבים לכתוב את כל זה בעצמכם (ובואו לא נשלה את עצמנו - אני כותב את הפוסט ברמת הפירוט הזו בדיוק בגלל שאני רוצה להבין את הסיפור הזה פעם אחת ולתמיד). אבל "די סימטרי ונחמד" לא עוזר לי - אני צריך משהו שחי בשדה {% equation %}\mathbb{Q}\left(p,q,\sqrt{D},\omega\right){% endequation %}. אז בואו אני אוכיח לכם שהמקדם של {% equation %}3\omega{% endequation %} שווה ל-{% equation %}\frac{3q+\sqrt{D}}{2}{% endequation %} והמקדם של {% equation %}3\omega^{2}{% endequation %} שווה ל-{% equation %}\frac{3q-\sqrt{D}}{2}{% endequation %}.

בשביל זה צריך לחזור קודם כל להגדרה של {% equation %}\sqrt{D}{% endequation %}:

{% equation %}\sqrt{D}=\left(\alpha-\beta\right)\left(\alpha-\gamma\right)\left(\beta-\gamma\right){% endequation %}

מכפלות כאלו כבר קטנות עלינו; בואו נפתח את הסוגריים ונקבל

{% equation %}\sqrt{D}=\left(\alpha^{2}\beta+\beta^{2}\gamma+\gamma^{2}\alpha\right)-\left(\alpha^{2}\gamma+\beta^{2}\alpha+\gamma^{2}\beta\right){% endequation %}

בואו ניקח את אותו ביטוי בדיוק רק עם פלוס במקום מינוס באמצע:

{% equation %}S=\left(\alpha^{2}\beta+\beta^{2}\gamma+\gamma^{2}\alpha\right)+\left(\alpha^{2}\gamma+\beta^{2}\alpha+\gamma^{2}\beta\right){% endequation %}

אז ברור ש-

{% equation %}\frac{S+\sqrt{D}}{2}=\left(\alpha^{2}\beta+\beta^{2}\gamma+\gamma^{2}\alpha\right){% endequation %} (זה המקדם של {% equation %}3\omega{% endequation %})

{% equation %}\frac{S-\sqrt{D}}{2}=\left(\alpha^{2}\gamma+\beta^{2}\alpha+\gamma^{2}\beta\right){% endequation %} (זה המקדם של {% equation %}3\omega^{2}{% endequation %})

נשאר רק להבין את {% equation %}S{% endequation %} עצמו, אבל זה בדיוק הביטוי שצץ במהלך הפיתוח של {% equation %}\left(\alpha+\beta+\gamma\right)^{3}{% endequation %}:

{% equation %}0=\left(\alpha+\beta+\gamma\right)^{3}=\left(\alpha^{3}+\beta^{3}+\gamma^{3}\right)+3S+6\alpha\beta\gamma=-3q+3S-6q{% endequation %}

כלומר, נקבל {% equation %}S=3q{% endequation %}, כפי שהבטחתי.

בזאת סיימנו! סיימנו את החישוב של {% equation %}\theta_{1}^{3}{% endequation %}:

{% equation %}\theta_{1}^{3}=-3q+\frac{3}{2}\omega\left(3q+\sqrt{D}\right)+\frac{3}{2}\omega^{2}\left(3q-\sqrt{D}\right)-6q{% endequation %}

האם אפשר לפשט את הביטוי הזה עוד יותר? ובכן, כן, אם רוצים להיפטר משורשי היחידה. ראשית, {% equation %}\omega+\omega^{2}=-1{% endequation %}, אז מביטוי כמו זה קל להיפטר. שנית, וזה פחות טריוויאלי, {% equation %}\omega-\omega^{2}=\sqrt{-3}{% endequation %}. כדי לראות את הדבר השני בואו נזכור ש-{% equation %}\omega{% endequation %} הוא שורש של הפולינום הציקלוטומי {% equation %}x^{2}+x+1{% endequation %} ובעזרת הנוסחה לפתרון משוואה ממעלה שניה נקבל {% equation %}\omega=\frac{1+\sqrt{-3}}{2}{% endequation %} ו-{% equation %}\omega^{2}=\frac{1-\sqrt{-3}}{2}{% endequation %} ומהם זה מיידי.

עכשיו הפישוט ברור: נקבל איבר מהצורה {% equation %}\frac{9q}{2}\left(\omega+\omega^{2}\right){% endequation %} ואיבר מהצורה {% equation %}\frac{3\sqrt{D}}{2}\left(\omega-\omega^{2}\right){% endequation %}, ובסך הכל נקבל:

{% equation %}\theta_{1}^{3}=-9q-\frac{9q}{2}+\frac{3\sqrt{D}}{2}\sqrt{-3}{% endequation %}

ולכן:

{% equation %}\theta_{1}^{3}=-\frac{27}{2}q+\frac{3}{2}\sqrt{-3D}{% endequation %}

שזה... די פשוט, חייבים להודות!

אוקיי, ומה עם {% equation %}\theta_{2}^{3}{% endequation %}? זה מזעזע, אבל גם אותו צריך לחשב!

אבל... אם עוצרים וחושבים רגע, מה ההבדל בין שניהם? בואו ניזכר איך הם הוגדרו:

{% equation %}\theta_{1}=\alpha+\beta\omega+\gamma\omega^{2}{% endequation %}

{% equation %}\theta_{2}=\alpha+\gamma\omega+\beta\omega^{2}{% endequation %}

כל מה שהשתנה הוא החלפת התפקידים של {% equation %}\beta{% endequation %} ו-{% equation %}\gamma{% endequation %}, אבל למה שזה ישפיע על משהו מהמשך החישוב? כל מה שקורה הוא סימטרי לחלוטין ביחס ל-{% equation %}\beta{% endequation %} ו-{% equation %}\gamma{% endequation %} ו... רגע, לא, לא נכון. יש דבר אחד שבמובהק שובר את הסימטריה: {% equation %}\sqrt{D}{% endequation %}. אולי כבר שכחנו, אבל זו הייתה <strong>כל הפואנטה</strong> של {% equation %}\sqrt{D}{% endequation %}; שזה איבר שלא נמצא בשדה השבת של {% equation %}S_{3}{% endequation %}; הגענו לכך שחילוף בודד מעביר את {% equation %}\sqrt{D}{% endequation %} אל {% equation %}-\sqrt{D}{% endequation %}. זה בדיוק מה שיקרה כאן - הביטוי שנקבל ל-{% equation %}\theta_{2}^{3}{% endequation %} זהה לביטוי של {% equation %}\theta_{1}^{3}{% endequation %} למעט זה שצריך להחליף את {% equation %}\sqrt{D}{% endequation %} ב-{% equation %}-\sqrt{D}{% endequation %}, ונקבל:

{% equation %}\theta_{2}^{3}=-\frac{27}{2}q-\frac{3}{2}\sqrt{-3D}{% endequation %}
<h2>איך פותרים משוואה ממעלה שלישית, שלב ג' - נוסחאות קרדנו</h2>
בואו נעשה סיכום ביניים של מה שיש לנו. מצאנו איברים {% equation %}\theta_{1},\theta_{2}{% endequation %} שנותנים לנו את השורש {% equation %}\alpha{% endequation %} של הפולינום {% equation %}x^{3}+px+q{% endequation %} באופן הבא:

{% equation %}\alpha=\frac{\theta_{1}+\theta_{2}}{3}{% endequation %}

{% equation %}\theta_{1}^{3}=-\frac{27}{2}q+\frac{3}{2}\sqrt{-3D}{% endequation %}

{% equation %}\theta_{2}^{3}=-\frac{27}{2}q-\frac{3}{2}\sqrt{-3D}{% endequation %}

מפתה מאוד לכתוב עכשיו משהו בסגנון הזה:

{% equation %}\alpha=\frac{1}{3}\left(\sqrt[3]{-\frac{27}{2}q+\frac{3}{2}\sqrt{-3D}}+\sqrt[3]{-\frac{27}{2}q-\frac{3}{2}\sqrt{-3D}}\right){% endequation %}

אבל למרות שזה מפתה, צריך להיזהר פה. לכתוב {% equation %}\sqrt[3]{a}{% endequation %} אומר "קחו את אחד מהשורשים השלישיים של {% equation %}a{% endequation %}, לא חשוב איזה". עכשיו, זה נכון שאפשר לקבל את {% equation %}\theta_{1}{% endequation %} על ידי בחירת שורש שלישי כלשהו של {% equation %}-\frac{27}{2}q+\frac{3}{2}\sqrt{-3D}{% endequation %} באופן שרירותי (עבור בחירה שונה של שורש נקבל בסוף גם שורש שונה מבין שלושת השורשים של הפולינום), אבל מרגע שבחרנו את {% equation %}\theta_{1}{% endequation %} אנחנו כבר לא יכולים לבחור בשרירותיות את {% equation %}\theta_{2}{% endequation %}; הוא תלוי אלגברית ב-{% equation %}\theta_{1}{% endequation %}. לכן, אם אנחנו רוצים לסיים את הסיפור סופית, אנחנו צריכים למצוא את הקשר האלגברי בין שניהם. הקשר הזה הוא די פשוט: {% equation %}\theta_{1}\theta_{2}=-3p{% endequation %}. איך רואים את זה? ובכן, בואו נעשה עוד חשבון ארוך וכואב, בפעם האחרונה:

{% equation %}\theta_{1}\theta_{2}=\left(\alpha+\beta\omega+\gamma\omega^{2}\right)\left(\alpha+\gamma\omega+\beta\omega^{2}\right)={% endequation %}

{% equation %}\left(\alpha^{2}+\beta^{2}+\gamma^{2}\right)+\left(\alpha\beta+\alpha\gamma+\gamma\beta\right)\left(\omega+\omega^{2}\right)={% endequation %}

{% equation %}-2p-p=-3p{% endequation %}

כאשר אני מתבסס על החישובים שכבר ביצעתי קודם. זה מסיים את הסיפור כמעט לגמרי, למעט העובדה שבינתיים הראיתי איך למצוא שורש <strong>אחד</strong> של המשוואה; איך מוצאים את כולם?

ובכן, זה החלק הפשוט בסיפור. בואו ניזכר שוב בשלושת האיברים שמככבים פה:

{% equation %}0=\alpha+\beta+\gamma{% endequation %}

{% equation %}\theta_{1}=\alpha+\beta\omega+\gamma\omega^{2}{% endequation %}

{% equation %}\theta_{2}=\alpha+\beta\omega^{2}+\gamma\omega{% endequation %}

הגעתי לנוסחה הקודמת על ידי כך שחיברתי את שלושת האיברים הללו. הפואנטה הייתה שהמקדם של {% equation %}\alpha{% endequation %} היה זהה בשלושתם, ועבור שאר השורשים המקדמים היו שונים בין שלושתם. אפשר לנסות להשיג אפקט דומה עבור {% equation %}\beta,\gamma{% endequation %} על ידי כפל של המשוואות ב-{% equation %}\omega{% endequation %} ו-{% equation %}\omega^{2}{% endequation %}. למשל, כדי לבודד את {% equation %}\beta{% endequation %} אפשר לכפול את {% equation %}\theta_{1}{% endequation %} ב-{% equation %}\omega^{2}{% endequation %} ואת {% equation %}\theta_{2}{% endequation %} ב-{% equation %}\omega{% endequation %} ולקבל:

עכשיו, בואו נכפול את {% equation %}\theta_{2}{% endequation %} ואת {% equation %}0{% endequation %} ב-{% equation %}\omega{% endequation %} ורק אז נחבר:

{% equation %}0=\alpha+\beta+\gamma{% endequation %}

{% equation %}\omega^{2}\theta_{1}=\alpha\omega^{2}+\beta+\gamma\omega{% endequation %}

{% equation %}\omega\theta_{2}=\alpha\omega+\beta+\gamma\omega^{2}{% endequation %}

ועכשיו נקבל {% equation %}\beta=\frac{\omega^{2}\theta_{1}+\omega\theta_{2}}{3}{% endequation %}

ובאותו אופן נקבל {% equation %}\gamma=\frac{\omega\theta_{1}+\omega^{2}\theta_{2}}{3}{% endequation %}

וזה כבר מסיים לחלוטין את הפתרון, ונותן את הנוסחה שמוכרת בתור <strong>נוסחת קרדנו</strong>. הנה הניסוח ה"נקי", שלא מצריך את ההבנה של מה שהלך פה:

בהינתן פולינום {% equation %}x^{3}+px+q{% endequation %}, נגדיר

{% equation %}D=-4p^{3}-27q^{2}{% endequation %}

{% equation %}A=\sqrt[3]{-\frac{27}{2}q+\frac{3}{2}\sqrt{-3D}}{% endequation %}

{% equation %}B=\sqrt[3]{-\frac{27}{2}q-\frac{3}{2}\sqrt{-3D}}{% endequation %}

כאשר {% equation %}B{% endequation %} נבחר באופן כזה ש-{% equation %}AB=-3p{% endequation %}, וכעת השורשים של הפולינום נתונים על ידי

{% equation %}x_{1}=\frac{A+B}{3}{% endequation %}

{% equation %}x_{2}=\frac{\omega A+\omega^{2}B}{3}{% endequation %}

{% equation %}x_{3}=\frac{\omega^{2}A+\omega B}{3}{% endequation %}

ביחס לטירוף שעברנו כדי להגיע אל הנוסחה הזו, אני מרגיש שהתוצאה הסופית היא דווקא אלגנטית למדי.
