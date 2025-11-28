---
id: 3562
title: "תחומים אוקלידיים ותחומים ראשיים"
date: 2018-03-01 16:12:37
layout: post
categories: 
  - אלגברה מופשטת
tags: 
  - תחום אוקלידי
  - תחום פריקות יחידה
  - תחום ראשי
---
<a href="http://gadial.net/2018/02/14/unique_factorization_domains/">הפוסט הקודם שלי</a> דיבר על <strong>תחומי פריקות יחידה</strong> - תחומי שלמות שבהם מתקיימת גרסה מתאימה של המשפט היסודי של האריתמטיקה. בזמן שניסינו להבין למה {% equation %}\mathbb{Z}{% endequation %} הוא תחום פריקות יחידה שכזה, ראינו שצריך להפריד בין שני האתגרים השונים שמציב המשפט:
<ul>
 	<li>היה צריך להוכיח שלכל איבר בחוג שאיננו אפס או הפיך <strong>קיים</strong> פירוק לגורמים אי-פריקים.</li>
 	<li>היה צריך להוכיח שהפירוק הזה הוא <strong>יחיד</strong>.</li>
</ul>
האתגר השני היה, במפתיע, קל; כל מה שנזקקנו לו היה האבחנה ש"איבר אי פריק הוא ראשוני", שהתבררה כנכונה לא רק עבור {% equation %}\mathbb{Z}{% endequation %} אלא עבור כל תחום שלמות שבו כל אידאל הוא ראשי, כלומר נוצר על ידי איבר בודד: חוג כזה נקרא <strong>תחום ראשי</strong>. דווקא החלק של ה"קיים פירוק" היה קצת קשה; האינטואיציה של "אם המספר אי-פריק, סיימנו, אחרת ניקח פירוק שלו ונפעל באינדוקציה על הגורמים בפירוק" לא הסבירה למה התהליך הזה של לפרק ולפרק ולפרק יסתיים לבסוף. בשביל שזה יעבוד הכנסתי מושג של <strong>נורמה</strong> שאיפשר לנו לבצע סוג של אינדוקציה. אבל בתחום ראשי כללי אין לנו דבר כזה, אז מה עושים?
<h2>קיום פירוק לגורמים בתחום ראשי</h2>
כזכור, איבר לא הפיך {% equation %}a\in R{% endequation %} הוא <strong>אי-פריק</strong> אם לא קיימים {% equation %}b,c{% endequation %} שהם עצמם לא הפיכים כך ש-{% equation %}a=bc{% endequation %}. זה אומר שאם {% equation %}a{% endequation %} <strong>כן</strong> פריק, אז בפרט קיים {% equation %}b{% endequation %} לא הפיך שמחלק אותו. ואם אותו {% equation %}b{% endequation %} גם הוא פריק אז קיים {% equation %}c{% endequation %} שמפרק אותו, וכן הלאה. אינטואיטיבית אנחנו מצפים שהתהליך הזה שבו אנחנו לוקחים איבר, מוצאים גורם פריק שלו, ומוצאים גורם פריק של הגורם ההוא וכן הלאה - התהליך הזה צריך להסתיים מתישהו.

פורמלית, בואו ניקח {% equation %}a\in R{% endequation %} לא הפיך. אם {% equation %}a{% endequation %} אי-פריק, סיימנו. אחרת יש {% equation %}a_{1},a_{2}\in R{% endequation %} שהם לא הפיכים כך ש-{% equation %}a=a_{1}a_{2}{% endequation %}. אם שניהם אי-פריקים, סיימנו. אחרת, נרצה להראות שקיים פירוק לאי-פריקים של כל אחד מהם. נניח ש-{% equation %}a_{1}{% endequation %} הוא פריק בעצמו, אז אפשר לכתוב {% equation %}a_{1}=a_{11}a_{12}{% endequation %} ולהמשיך באותו האופן. בסופו של דבר יקרה אחד משניים: או שנגיע לפירוק מלא לאי-פריקים, או שנקבל שרשרת שאסמן את איבריה ב-{% equation %}b_{0},b_{1},b_{2},b_{3},\dots{% endequation %} של איברים שכולם פריקים ומתקיים {% equation %}b_{1}|b_{0}{% endequation %} ו-{% equation %}b_{2}|b_{1}{% endequation %} וכן הלאה. יותר קל לנסח את זה בלשון אידאלים: {% equation %}\left\langle b_{0}\right\rangle \subset\left\langle b_{1}\right\rangle \subset\left\langle b_{2}\right\rangle \subset\dots{% endequation %} כשההכלה כאן היא <strong>הכלה ממש</strong>. עכשיו מגיע התעלול: נגדיר {% equation %}I=\bigcup_{i=0}^{\infty}\left\langle b_{i}\right\rangle {% endequation %}. קל לראות שהקבוצה הזו היא אידאל,ישירות על פי ההגדרה; ומכיוון שאנחנו בתחום ראשי אז קיים {% equation %}b\in I{% endequation %} כך ש-{% equation %}I=\left\langle b\right\rangle {% endequation %}. מצד שני, מכיוון ש-{% equation %}I{% endequation %} הוא בסך הכל איחוד של קבוצות, קיים {% equation %}\left\langle b_{n}\right\rangle {% endequation %} כך ש-{% equation %}b\in\left\langle b_{n}\right\rangle {% endequation %}, כלומר {% equation %}I\subseteq\left\langle b_{n}\right\rangle {% endequation %}. קיבלנו סתירה: {% equation %}I\subseteq\left\langle b_{n}\right\rangle \subset\left\langle b_{n+1}\right\rangle \subseteq I{% endequation %} - ה"הכלה ממש" לא יכולה להתקיים. זה מסיים את ההוכחה.

אם המצב כל כך פשוט, למה ההוכחה הזו "בעייתית"? ובכן, זה תלוי למה אתם קוראים בעייתי. יש בהוכחה הזו שימוש ב<strong>אקסיומת הבחירה</strong>, שאין בה משהו פסול לכשעצמו, אבל בהחלט אפשר לתהות אם ומתי אפשר להסתדר גם בלעדיה. אתם רואים את השימוש הזה? כרגיל בעניינים הללו, זה מתרחש במקום שבו אני מנפנף בידיים בזריזות ועושה משהו שנראה לכולנו טבעי. במקרה הנוכחי, ההנחה שהסדרה {% equation %}b_{0},b_{1},b_{2},b_{3},\dots{% endequation %} קיימת בכלל. הרי לא הוכחתי ממש את קיומה; הצגתי <strong>תהליך</strong> שבהינתן {% equation %}b_{n}{% endequation %} יודע לייצר את {% equation %}b_{n+1}{% endequation %}. זה בפני עצמו טוב ויפה אבל זה לא מבטיח שאני אוכל לייצר את האובייקט המלא {% equation %}b_{0},b_{1},b_{2},\dots{% endequation %} בעזרת התהליך הזה. אם אתם עדיין לא משוכנעים, בסדר גמור; זה הרי לא פוסט על אקסיומת הבחירה והדקויות שלה.
<h2>מחלק משותף מקסימלי</h2>
עכשיו בואו נראה איך נורמה עוזרת לנו להתחמק מהשימוש הזה באקסיומת הבחירה.

הזכרתי את "יסודות" של אוקלידס בפוסט הקודם, כי שם נמצאת ההוכחה המוקדמת ביותר למשפט היסודי של האריתמטיקה; זה נמצא בספר 7, שהוא הראשון שעוסק בתורת המספרים. הספר הזה <strong>נפתח</strong> עם יישום כפול של מה שנקרא כיום <strong>האלגוריתם האוקלידי</strong> והוא ככל הנראה המושג החשוב ביותר בתורת המספרים האלמנטרית. <a href="http://gadial.net/2011/09/12/euclidean_algorithm_and_rings/">יש לי כבר פוסט בנושא</a>, אבל מן הסתם נדבר על זה מחדש. הרעיון מאחורי האלגוריתם האוקלידי הוא לתת שיטה למציאת <strong>מחלק משותף מקסימלי</strong> של זוג מספרים. מה זה מחלק משותף מקסימלי? אם {% equation %}a,b{% endequation %} הם שני מספרים טבעיים, אז המחלק המשותף המקסימלי שלהם, שמסומן {% equation %}\text{gcd}\left(a,b\right){% endequation %} הוא מספר טבעי {% equation %}d{% endequation %} שמחלק את שניהם, והוא הגדול ביותר מבין כל המספרים שמחלקים את שניהם. למשל, {% equation %}\text{gcd}\left(12,8\right)=4{% endequation %}.

רק מה, אנחנו מתעסקים פה בחוגים, והטבעיים הם בכלל לא חוג. אז אנחנו רוצים להגדיר מחלק משותף מקסימלי עבור חוגים כלליים. בחוגים כלליים אין לנו עדיין מושג של "גודל", כך שקשה לדבר על "הגדול ביותר מבין כל המספרים שמחלקים את שניהם", אבל יש קריטריון טבעי אחר - חלוקה. כזכור, אני מסמן {% equation %}a|b{% endequation %} כדי לומר ש-{% equation %}a{% endequation %} <strong>מחלק</strong> את {% equation %}b{% endequation %}, כלומר שקיים {% equation %}c{% endequation %} כך ש-{% equation %}b=ac{% endequation %}.

בהגדרה הכללית, {% equation %}d{% endequation %} הוא מחלק משותף מקסימלי של {% equation %}a,b{% endequation %} אם {% equation %}d|a{% endequation %} וגם {% equation %}d|b{% endequation %}, ובנוסף לכך אם יש איבר כלשהו {% equation %}e{% endequation %} שגם הוא מחלק משותף של {% equation %}a,b{% endequation %}, כלומר מקיים {% equation %}e|a{% endequation %} וגם {% equation %}e|b{% endequation %} אז בהכרח {% equation %}e|d{% endequation %}. במילים: {% equation %}d{% endequation %} הוא מחלק משותף מקסימלי של {% equation %}a,b{% endequation %} אם הוא מתחלק בכל מחלק משותף של {% equation %}a,b{% endequation %}. תחת ההגדרה הזו, מחלק משותף מקסימלי הוא לא יחיד: ל-12 ול-8 מהדוגמא הקודמת יש עכשיו את המחלקים המשותפים המקסימליים {% equation %}4{% endequation %} וגם {% equation %}-4{% endequation %}. לא קשה לראות מההגדרה שכל שני מחלקים משותפים מקסימליים חייבים לחלק זה את זה, ומכך נובע חיש קל שהם <strong>ידידים</strong>, כלומר זהים עד כדי כפל באיבר הפיך, כך שזה לא מקרי שבדוגמא שלנו קיבלנו את אותו מספר עד כדי סימן. זו הסיבה שבגללה למרות שאין מחלק משותף מקסימלי יחיד עדיין הסימון {% equation %}\text{gcd}\left(a,b\right){% endequation %} הוא כמעט מוגדר היטב ועדיין משתמשים בו.

יתרון אחד של ההגדרה באמצעות חלוקה היא שהיא מאפשרת לנו לעבור לדבר על אידאלים. בפוסט הקודם ראינו את היתרון שבגישה הזו - היא איפשרה לנו להוכיח בקלות שאי-פריק בתחום ראשי הוא ראשוני. במקרה שלנו, {% equation %}d{% endequation %} הוא מחלק משותף מקסימלי של {% equation %}a,b{% endequation %} אם {% equation %}a,b\in\left\langle d\right\rangle {% endequation %}, ובנוסף לכך אם {% equation %}a,b\in\left\langle e\right\rangle {% endequation %} אז גם {% equation %}d\in\left\langle e\right\rangle {% endequation %}, כלומר {% equation %}\left\langle d\right\rangle \subseteq\left\langle e\right\rangle {% endequation %}. כלומר, המחלק המשותף <strong>הגדול ביותר</strong> דווקא יוצר את האידאל <strong>הקטן ביותר</strong> שמכיל את {% equation %}a,b{% endequation %}.

ובכן, שתי שאלות על היצור הזה:
<ul>
 	<li>האם בהינתן {% equation %}a,b{% endequation %} כלשהם שאינם אפס, בהכרח <strong>קיים</strong> להם מחלק משותף מקסימלי?</li>
 	<li>בהינתן שקיים כזה, האם יש לנו דרך למצוא אותו?</li>
</ul>
אם אנחנו בתחום פריקות יחידה, אז התשובה לשתי השאלות היא חיובית. בואו נניח ש-{% equation %}R{% endequation %} הוא תחום פריקות יחידה ו-{% equation %}a,b\in R{% endequation %} הם איברים שונים מאפס כלשהם (אם אחד מהם הוא אפס אז אפס הוא מחלק משותף מקסימלי שלהם). נסתכל על הפירוק לגורמים היחיד שלהם (זכרו ש"יחיד" זה עד כי החלפה של איברים במכפלה בידידים שלהם, כלומר כפל שלהם בהפיך):

{% equation %}a=r_{1}r_{2}\cdots r_{k}{% endequation %}

{% equation %}b=s_{1}s_{2}\dots s_{t}{% endequation %}

כאן ישתלם לי לעשות את הדבר הבא: ראשית, להציג בפירוקים הללו כל גורם אי-פריק בדיוק פעם אחת, אבל עם חזקה טבעית חיובית כלשהי שסופרת כמה פעמים הוא הופיע במכפלה; ושנית, להציג גם גורמים אי-פריקים שיש בפירוק של המספר השני, פשוט עם חזקת אפס. הנה דוגמא פשוטה עבור מספרים שלמים. אם

{% equation %}60=2\cdot2\cdot3\cdot5{% endequation %}

{% equation %}126=2\cdot3\cdot3\cdot7{% endequation %}

אז אכתוב:

{% equation %}60=2^{2}\cdot3^{1}\cdot5^{1}\cdot7^{0}{% endequation %}

{% equation %}126=2^{1}\cdot3^{2}\cdot5^{0}\cdot7^{1}{% endequation %}

ובאופן כללי:

{% equation %}a=p_{1}^{a_{1}}\cdots p_{n}^{a_{n}}{% endequation %}

{% equation %}b=p_{1}^{b_{1}}\cdots p_{n}^{b_{n}}{% endequation %}

וכעת מחלק משותף מקסימלי לשני אלו נתון על ידי

{% equation %}\text{gcd}\left(a,b\right)=p_{1}^{\min\left\{ a_{1},b_{1}\right\} }p_{2}^{\min\left\{ a_{2},b_{2}\right\} }\cdots p_{n}^{\min\left\{ a_{n},b_{n}\right\} }{% endequation %}

ובדוגמא שלנו:

{% equation %}\text{gcd}\left(60,126\right)=2^{\min\left\{ 2,1\right\} }\cdot3^{\min\left\{ 1,2\right\} }\cdot5^{\min\left\{ 1,0\right\} }\cdot7^{\min\left\{ 0,1\right\} }=2^{1}\cdot3^{1}\cdot5^{0}\cdot7^{0}=6{% endequation %}

לכאורה סיימנו עם כל נושא המחלק המשותף המקסימלי: גם הוכחנו שיש כזה וגם הראינו איך מוצאים אותו. אבל העניין הוא שהאלגוריתם שמוצא אותו הוא <strong>קשה לביצוע</strong>. למצוא פירוק לגורמים אי-פריקים של איברים? זה קשה. האבחנה המדהימה של אוקלידס (או מי שזה לא יהיה שהמציא את מה שאוקלידס העלה על הכתב) הייתה שבמספרים השלמים<strong> לא צריך </strong>את הפירוק לגורמים כדי למצוא את המחלק המשותף המקסימלי - אפשר להשתמש בשיטה שעוקפת את זה והיא הרבה יותר יעילה.

עד כמה זו אבחנה מדהימה? ובכן, האלגוריתם האוקלידי הוא אבן יסוד ברוב האלגוריתמים היעילים בתורת המספרים; מצד שני, עד היום אין לנו אלגוריתם יעיל לפירוק לגורמים. בלי האלגוריתם האוקלידי, תורת המספרים האלגוריתמית כפי שאנחנו מכירים אותה <strong>לא הייתה מתקיימת</strong>. למרות שאם אני רוצה להיות הגון היסטורית, עיקר השימושיות האלגוריתמית של האלגוריתם האוקלידי היא בהרבה שלו, שמאפשרת לנו למצוא {% equation %}x,y{% endequation %} כך ש-שווה ל-{% equation %}\text{gcd}\left(a,b\right)=ax+by{% endequation %} .

איך עושים את הקסם הזה? ובכן, התשובה טמונה במשהו שאנחנו יודעים לעשות עם מספרים שלמים עוד מבית הספר היסודי: <strong>חלוקה עם שארית</strong>. אם {% equation %}a,b{% endequation %} הם מספרים שלמים אז קיימים {% equation %}q,r{% endequation %} כך ש-{% equation %}a=qb+r{% endequation %}: {% equation %}q{% endequation %} הוא <strong>המנה</strong> של חלוקת {% equation %}a{% endequation %} ב-{% equation %}b{% endequation %} ואילו {% equation %}r{% endequation %} הוא ה<strong>שארית</strong>. כדי שזה יהיה מעניין, אנחנו רוצים על פי רוב שהשארית תהיה <strong>קטנה ככל הניתן</strong>, כלומר {% equation %}0\le r&lt;\left|b\right|{% endequation %} (כלומר, {% equation %}13=2\cdot5+3{% endequation %} הוא הדרך ה"נכונה" לחלק את 13 ב-5 עם שארית, ולא, למשל, {% equation %}13=1\cdot5+8{% endequation %}).

לא קשה לראות שאם {% equation %}a=qb+r{% endequation %} אז {% equation %}\text{gcd}\left(a,b\right)=\text{gcd}\left(b,r\right){% endequation %}, והאבחנה הזו היא המפתח לאלגוריתם האוקלידי: פשוט מחלקים את {% equation %}a{% endequation %} ב-{% equation %}b{% endequation %}. אם השארית היא 0, אז {% equation %}\text{gcd}\left(a,b\right)=b{% endequation %}, ואחרת ממשיכים רקורסיבית למצוא את {% equation %}\text{gcd}\left(b,r\right){% endequation %}. <a href="http://gadial.net/2011/09/12/euclidean_algorithm_and_rings/">בפוסט שלי</a> על הנושא יש את הפירוט המלא, כולל קוד. לעת עתה בואו נתמקד בסיבה שבגללה האלגוריתם עובד ואיך אפשר להכליל את זה. האלגוריתם עובד בדיוק בגלל התכונה הזו שהשארית "יותר קטנה" ממה שמחלקים בו, מה שמבטיח שהאלגוריתם יעצור בסופו של דבר, ואפילו די מהר. לכן, אם אנחנו רוצים להשתמש בו בחוגים כלליים, אנחנו צריכים מושג של "חלוקה עם שארית" ומושג של "גודל" שיאפשר לנו לקבוע שהשארית קטנה יותר ממה שמחלקים בו.
<h2>תחומים אוקלידיים</h2>
בפוסט הקודם ראינו את המושג של <strong>נורמה</strong>. כמקודם, אם {% equation %}R{% endequation %} הוא חוג, אז נורמה תהיה פונקציה {% equation %}N:R\to\mathbb{N}{% endequation %}. בפוסט הקודם דרשתי משהו בסגנון {% equation %}N\left(a\right)N\left(b\right)=N\left(ab\right){% endequation %}, אבל כרגע אני <strong>עדיין לא</strong> אעשה שום דבר כזה. הדרישה היחידה שלי מהנורמה היא זו: שלכל {% equation %}a,b\in R{% endequation %} כך ש-{% equation %}b\ne0{% endequation %} יהיו קיימים (ולאו דווקא יחידים) {% equation %}q,r\in R{% endequation %} כך ש-{% equation %}a=qb+r{% endequation %} ו-{% equation %}N\left(r\right)&lt;N\left(b\right){% endequation %} או ש-{% equation %}r=0{% endequation %} (למה אני דורש במפורש את האפשרות {% equation %}r=0{% endequation %}? כי ההגדרה שלי לא פוסלת את האפשרות של איברים שונים מאפס עם נורמה 0).

אם בחוג שלנו יש דבר כזה, מיידית קיבלנו את קיום האלגוריתם האוקלידי, והחוג נקרא <strong>תחום אוקלידי</strong>. בואו ונראה את זה. ראשית, אני רוצה להוכיח שאם {% equation %}R{% endequation %} הוא תחום אוקלידי אז הוא בפרט תחום ראשי, כלומר שכל אידאל נוצר על ידי איבר יחיד. ניקח אידאל {% equation %}I\ne\left\{ 0\right\} {% endequation %} שכזה. לכל איבר בו יש נורמה; בואו ניקח איבר שונה מ-{% equation %}0{% endequation %} שהנורמה שלו היא <strong>מינימלית</strong> (אולי יש כמה כאלו, אז נבחר אחד באופן שרירותי). הקיום של מינימום כזה מובטח מכך שהטווח של הנורמה הוא {% equation %}\mathbb{N}{% endequation %}, וזו קבוצה סדורה היטב (כלומר, לכל תת-קבוצה שלה יש איבר מינימלי). נסמן את האיבר הזה ב-{% equation %}d{% endequation %}. ברור ש-{% equation %}\left\langle d\right\rangle \subseteq I{% endequation %}, אבל צריך להוכיח את הכיוון השני - להראות ש-{% equation %}I\subseteq\left\langle d\right\rangle {% endequation %} שזו דרך אחרת לומר שלכל {% equation %}a\in I{% endequation %} מתקיים ש-{% equation %}d|a{% endequation %}.

ובכן, מכיוון שאנחנו בתחום אוקלידי, אפשר לחלק את {% equation %}a{% endequation %} ב-{% equation %}d{% endequation %} ולקבל {% equation %}a=qd+r{% endequation %} עם {% equation %}N\left(r\right)&lt;N\left(d\right){% endequation %}. על ידי העברת אגף נקבל ש-{% equation %}r=a-qd\in I{% endequation %} (כי {% equation %}d\in I{% endequation %} ולכן {% equation %}qd\in I{% endequation %} ולכן גם {% equation %}a-qd\in I{% endequation %} - אלו תכונות הסגירות הרגילות של אידאלים). מצד שני, הנורמה של {% equation %}r{% endequation %} <strong>קטנה ממש</strong> מזו של {% equation %}d{% endequation %}, והרי בחרנו את {% equation %}d{% endequation %} להיות האיבר בעל הנורמה המינימלית מבין כל האיברים <strong>השונים מאפס</strong> ב-{% equation %}I{% endequation %}, ולכן בהכרח {% equation %}r=0{% endequation %}, כלומר {% equation %}a=dq{% endequation %} ולכן {% equation %}a\in\left\langle d\right\rangle {% endequation %}. הופס, זה היה קל עד להפתיע.

טריק "העברת האגף" הזה שבו מחלקים {% equation %}a{% endequation %} ב-{% equation %}b{% endequation %}, מקבלים {% equation %}a=qb+r{% endequation %} ואז מעבירים אגף ומקבלים {% equation %}r=a-qb{% endequation %} הוא גם מה שמראה שאם {% equation %}d{% endequation %} הוא מחלק משותף של {% equation %}a,b{% endequation %} אז הוא מחלק גם את {% equation %}r{% endequation %} (פשוט מאוד: הוא מחלק את אגף ימין של {% equation %}r=a-qb{% endequation %} ולכן את אגף שמאל) ומכאן כבר קל להראות שאם {% equation %}d{% endequation %} הוא המחלק המשותף המקסימלי של {% equation %}a,b{% endequation %} אז כך גם עבור {% equation %}b,r{% endequation %}, והאלגוריתם האוקלידי עובד.

מכיוון שהראיתי שכל תחום אוקלידי הוא תחום ראשי, אז יחד עם מה שהראיתי בפוסט הקודם ראינו שבכל תחום אוקלידי אם קיים פירוק לגורמים אז הוא יחיד. עכשיו אני רוצה להראות שאכן קיים פירוק לגורמים. כזכור, בפוסט הקודם הראיתי שאם יש לנו על החוג נורמה <strong>כפלית</strong>, כלומר כזו שמקיימת {% equation %}N\left(a\right)N\left(b\right)=N\left(ab\right){% endequation %}, זה מספיק כדי להוכיח בקלות קיום של פירוק לגורמים.

רק מה, בתחום אוקלידי אמנם יש נורמה, אבל שום דבר לא מבטיח שהיא כפלית שכזו. למרבה המזל, אם יש לנו תחום אוקלידי, תמיד אפשר <strong>לתקן</strong> את הנורמה שלו כך שבנוסף לתכונת החלוקה הנחמדה שלה היא תיתן לנו את מה שצריך בשביל להוכיח פירוק יחיד. לשם כך בואו נקל טיפה על הדרישות שלנו: אני אראה שמספיק לי שתתקיים התכונה {% equation %}N\left(a\right)\le N\left(ab\right){% endequation %} לכל {% equation %}b\ne0{% endequation %} כדי להשיג את כל הטוב של הפוסט הקודם. איך נבנה נורמה כזו?

התעלול הוא פשוט: נניח ש-{% equation %}N:R\to\mathbb{N}{% endequation %} היא נורמה אוקלידית על {% equation %}R{% endequation %}. כלומר, לכל {% equation %}a,b\in R{% endequation %} כך ש-{% equation %}b\ne0{% endequation %} קיימים {% equation %}q,r{% endequation %} כך ש-{% equation %}a=bq+r{% endequation %} ו-{% equation %}N\left(r\right)&lt;N\left(b\right){% endequation %} או ש-{% equation %}r=0{% endequation %}. עכשיו בואו ניקח פטיש ונרביץ ממש ממש חזק ל-{% equation %}N{% endequation %} עד שתתעקם לצורה שאנחנו צריכים. לנורמה החדשה שלנו נקרא {% equation %}\overline{N}{% endequation %}.

קודם כל, שום דבר לא מונע מאיתנו להגדיר {% equation %}\overline{N}\left(0\right)=0{% endequation %}, אז שיהיה (הרי השימוש היחיד שלנו בנורמה הוא בבדיקה {% equation %}N\left(r\right)&lt;N\left(b\right){% endequation %} שלא אמורה בכלל להתבצע אם {% equation %}r{% endequation %} או {% equation %}b{% endequation %} הם 0; לפעמים בספרות פשוט אומרים מראש שהנורמה לא מוגדרת עבור 0).

עכשיו, אנחנו רוצים להגדיר את {% equation %}\overline{N}\left(a\right){% endequation %} עבור {% equation %}a\ne0{% endequation %} כלשהו. מצד אחד, אנחנו רוצים שזה יתבצע בעזרת {% equation %}N{% endequation %}, כי אין לנו שום דבר אחר להיאחז בו; מצד שני, אנחנו <strong>חייבים</strong> שיתקיים {% equation %}\overline{N}\left(a\right)\le\overline{N}\left(ab\right){% endequation %} לכל {% equation %}b\ne0{% endequation %} אפשרי. אז בואו נגדיר את {% equation %}\overline{N}\left(a\right){% endequation %} להיות הדבר הכי גדול שאפשר, במסגרת המגבלה הזו: {% equation %}\overline{N}\left(a\right)\triangleq\min_{b\ne0}N\left(ab\right){% endequation %}. מכיוון שגם {% equation %}b=1{% endequation %} נכלל בהגדרה הזו, אנחנו מקבלים {% equation %}\overline{N}\left(a\right)\le N\left(a\right){% endequation %}, כלומר הנורמה החדשה שלנו יכולה רק להיות קטנה או שווה לישנה, ולכן מה שאנחנו עושים כאן הוא לטפל באיברים שהנורמה שלהם הייתה "מנופחת יותר מדי".

אנחנו צריכים קודם כל לוודא שאכן מתקיימת התכונה שלשמה התכנסנו: {% equation %}\overline{N}\left(a\right)\le\overline{N}\left(ab\right){% endequation %} לכל {% equation %}b\ne0{% endequation %}. הרעיון מאוד פשוט: {% equation %}\overline{N}\left(ab\right)=N\left(ab\cdot c\right){% endequation %} עבור {% equation %}c{% endequation %} כלשהו (ה-{% equation %}c{% endequation %} שעבורו מתקבל מינימום על פני כל הערכים {% equation %}N\left(ab\cdot c\right){% endequation %}). מאסוציאטיביות הכפל של החוג נקבל שהערך הזה שווה ל-{% equation %}N\left(a\cdot bc\right){% endequation %}. כלומר, זה ערך מהערכים שהופיעו בחישוב של {% equation %}\overline{N}\left(a\right){% endequation %} (כי {% equation %}bc\ne0{% endequation %}, שהרי אנחנו בתחום שלמות). ולכן {% equation %}\overline{N}\left(a\right)\le N\left(a\cdot bc\right)=\overline{N}\left(ab\right){% endequation %}.

מסקנה אחת שאפשר להסיק ממה שכבר עשינו היא ש-{% equation %}\overline{N}\left(1\right)\le\overline{N}\left(1\cdot b\right)=\overline{N}\left(b\right){% endequation %} לכל {% equation %}b\ne0{% endequation %} בחוג. שימו לב שזה לא אומר ש-{% equation %}\overline{N}\left(1\right)=1{% endequation %}; רק שזה הערך המינימלי ש-{% equation %}\overline{N}{% endequation %} יכולה לקבל בכלל על קלט שאיננו אפס.

עכשיו צריך להראות שלא הרסנו את הנורמה שלנו בתהליך היצירה שלה - שעדיין, לכל {% equation %}a,b{% endequation %} קיימים {% equation %}q,r{% endequation %} כך ש-{% equation %}a=bq+r{% endequation %} ו-{% equation %}\overline{N}\left(r\right)&lt;\overline{N}\left(b\right){% endequation %} או ש-{% equation %}r=0{% endequation %}. מה החשש? שאולי בתהליך היצירה של {% equation %}\overline{N}{% endequation %} היה {% equation %}b{% endequation %} שהקטנו פלאים את גודל הנורמה שלו ביחס לזו של שאר האיברים בחוג, ופתאום מי שיכלו לשמש בתור "שאריות" בחלוקה ב-{% equation %}b{% endequation %} כבר לא טובות לתפקיד. זו בעיה אמיתית שצריך להתמודד איתה, והנה הדרך לעשות את זה: קודם כל, {% equation %}\overline{N}\left(b\right)=N\left(bc\right){% endequation %} עבור {% equation %}c\in R{% endequation %} שונה מאפס כלשהו. כעת, אפשר לחלק את {% equation %}a{% endequation %} ב-{% equation %}bc{% endequation %} על פי הנורמה {% equation %}N{% endequation %}, ולקבל ש-{% equation %}a=\left(bc\right)q+r{% endequation %} כך ש-{% equation %}N\left(r\right)&lt;N\left(bc\right){% endequation %} או ש-{% equation %}r=0{% endequation %}. מהדברים שכבר ראינו נסיק שאם {% equation %}r\ne0{% endequation %} אז {% equation %}\overline{N}\left(r\right)\le N\left(r\right)&lt;N\left(bc\right)=\overline{N}\left(b\right){% endequation %}, כך שיחד עם המשוואה {% equation %}a=b\left(cq\right)+r{% endequation %} קיבלנו בדיוק את מה שרצינו.

זה מסיים את מה שרציתי לומר לעת עתה על תחומים אוקלידיים מבחינה תיאורטית. ראינו בדיוק איך הם מקיימים את תכונת הפירוק היחיד לגורמים ואיך אפשר להשתעשע קצת עם הנורמה שלהם; אבל צריך לראות גם כמה דוגמאות.
<h2>דוגמאות לתחומים אוקלידיים</h2>
הדוגמא הראשונה היא כמובן {% equation %}\mathbb{Z}{% endequation %} עם הנורמה שהיא ערך מוחלט, אבל יש דוגמא אחרת שהיא חשובה לא פחות: פולינומים מעל שדה. אני אכתוב פוסט ייעודי על פולינומים ודומיהם בהמשך, אז בינתיים אסתפק בלהזכיר שפולינום מעל חוג {% equation %}R{% endequation %} הוא יצור שנראה ככה: {% equation %}p\left(x\right)=a_{n}x^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}{% endequation %} כאשר {% equation %}a_{0},\dots,a_{n}\in R{% endequation %}, {% equation %}a_{n}\ne0{% endequation %} אלא אם {% equation %}n=0{% endequation %} (כלומר, האיבר של החזקה הגבוהה ביותר של הפולינום איננו מיותר) ו-{% equation %}n{% endequation %} הוא מספר טבעי כלשהו שנקרא <strong>הדרגה</strong> של הפולינום ומסומן בתור {% equation %}\deg\left(p\right){% endequation %} . למשל, {% equation %}p\left(x\right)=5x^{2}+\pi x+-\frac{7}{2}{% endequation %} הוא פולינום מעל החוג {% equation %}\mathbb{R}{% endequation %} עם {% equation %}\deg\left(p\right)=2{% endequation %}.

כאשר {% equation %}R{% endequation %} הוא שדה, כמו מה שנדבר עליו עכשיו, יותר נפוץ לסמן אותו באות {% equation %}F{% endequation %}, ואת חוג הפולינומים מעל {% equation %}F{% endequation %} ב-{% equation %}F\left[x\right]{% endequation %}. למה חשוב לי לדבר על שדות? תכף נראה. כזכור, שדה הוא חוג קומוטטיבי שבו לכל איבר יש הפיך; ההפיכות הזו היא התכונה החשובה ביותר כאן.

מה שיפה בפולינומים הוא שיש להם חלוקה-עם-שארית כמו שיש למספרים השלמים. בשביל לדבר על זה צריך להגיד מה תהיה הנורמה שלהם; הדרגה של הפולינום נותנת לנו נורמה באופן טבעי. פשוט מגדירים {% equation %}N\left(p\right)=\deg\left(p\right){% endequation %}. הנורמה הזו היא לא כפלית, אבל שימו לב מה כן קורה: מתקיים {% equation %}\deg\left(ab\right)=\deg\left(a\right)+\deg\left(b\right){% endequation %} אלא אם אחד מהפולינומים הוא 0 (ולכן לפעמים מגדירים {% equation %}\deg\left(0\right)=-\infty{% endequation %}, כדי שהשוויון הזה "ימשיך להתקיים"). האם זה מזכיר לכם משהו? זה מה שקורה בחזקות: {% equation %}2^{a+b}=2^{a}\cdot2^{b}{% endequation %}. בשל כך, אם רוצים לקבל נורמה כפלית אפשר להגדיר {% equation %}N\left(p\right)=2^{\deg\left(p\right)}{% endequation %} ואז מקבלים ש-

{% equation %}N\left(ab\right)=2^{\deg\left(ab\right)}=2^{\deg\left(a\right)+\deg\left(b\right)}=2^{\deg\left(a\right)}2^{\deg\left(b\right)}=N\left(a\right)N\left(b\right){% endequation %}

אבל אני לא אזדקק לזה כאן אז נדבוק בנורמה שהיא פשוט הדרגה של הפולינום ונראה איך יחד איתה אנחנו מקבלים תחום אוקלידי. אני אדגים על מקרה קונקרטי פשוט. נסתכל בחוג {% equation %}\mathbb{R}\left[x\right]{% endequation %} על הפולינומים {% equation %}a\left(x\right)=x^{3}+2x^{2}+7{% endequation %} ו-{% equation %}b\left(x\right)=x+3{% endequation %}. אני רוצה למצוא {% equation %}q\left(x\right),r\left(x\right){% endequation %} כך ש-{% equation %}a\left(x\right)=b\left(x\right)q\left(x\right)+r\left(x\right){% endequation %} ו-{% equation %}\deg\left(r\right)&lt;\deg\left(b\right){% endequation %}. קודם כל אני רוצה "להיפטר" מהאיבר {% equation %}x^{3}{% endequation %} של {% equation %}a\left(x\right){% endequation %}. אז אני לוקח את כל {% equation %}b\left(x\right){% endequation %}, רואה שהאיבר המוביל שלו הוא {% equation %}x{% endequation %}, וכופל את הכל ב-{% equation %}-x^{2}{% endequation %}. עכשיו אני מקבל {% equation %}-x^{3}-3x^{2}{% endequation %}, וזה פולינום שכאשר אני מחבר אותו ל-{% equation %}a\left(x\right){% endequation %} אני מוחק לגמרי את האיבר בחזקה שלישית של {% equation %}a{% endequation %} ונשאר עם:

{% equation %}a\left(x\right)-x^{2}b\left(x\right)=-x^{2}+7{% endequation %}

עכשיו אני רוצה להיפטר מה-{% equation %}-x^{2}{% endequation %} של התוצאה. אז אני כופל <strong>שוב</strong> את {% equation %}b\left(x\right){% endequation %} במשהו מתאים, הפעם ב-{% equation %}x{% endequation %}, ומקבל:

{% equation %}a\left(x\right)-x^{2}b\left(x\right)+xb\left(x\right)=\left(-x^{2}+7\right)+\left(x^{2}+3x\right)=3x+7{% endequation %}

ועכשיו - להיפטר מה-{% equation %}3x{% endequation %} על ידי כפל ב-{% equation %}-3{% endequation %}!

{% equation %}a-x^{2}b+xb-3b=\left(3x+7\right)-\left(3x+9\right)=-2{% endequation %}

עכשיו אפשר <strong>להוציא גורם משותף</strong> באגף שמאל - מוציאים את {% equation %}b{% endequation %} החוצה מכל המכפלות שבהן הוא משתתף, ומקבלים:

{% equation %}a\left(x\right)-b\left(x\right)\left(x^{2}-x+3\right)=-2{% endequation %}

או במילים אחרות

{% equation %}a\left(x\right)=b\left(x\right)\left(x^{2}-3x+3\right)-2{% endequation %}

קיבלנו {% equation %}q\left(x\right)=x^{2}-3x+3{% endequation %} ו-{% equation %}r\left(x\right)=-2{% endequation %}, ואכן {% equation %}\deg\left(r\right)=0&lt;1=\deg\left(b\right){% endequation %}.

את התעלול הזה שבו מחסרים שוב ושוב "משהו כפול {% equation %}b{% endequation %}" מ-{% equation %}a{% endequation %} ומוחקים כל חזקה שגדולה או שווה לזו של המקדם המוביל של {% equation %}b{% endequation %} אפשר לעשות תמיד, אבל רק מכיוון שאנחנו מעל שדה. למשל, אם {% equation %}a\left(x\right)=x^{2}+1{% endequation %} ו-{% equation %}b\left(x\right)=2x{% endequation %} נהיה חייבים לכפול את {% equation %}b{% endequation %} ב-{% equation %}-\frac{1}{2}{% endequation %} כדי לנטרל את החזקה {% equation %}x^{2}{% endequation %} של {% equation %}a{% endequation %}; אם היינו מעל {% equation %}\mathbb{Z}{% endequation %} לא היינו מסוגלים לעשות משהו כזה וכל האוקלידיות הייתה הולכת לנו לאיבוד.

העובדה שבפולינומים יש חילוק עם שארית שכזה אומרת שכל האלגוריתם האוקלידי שהכרנו למספרים שלמים עובר יפה גם אליהם, ולכן גם לא מעט מתורת המספרים ניתנת לתרגום בצורה זו או אחרת לפולינומים, ויש אפילו דברים שהם יותר קלים לפולינומים (למשל, פירוק לגורמים). לא אכנס לזה כאן. דבר אחד שכן שווה לדבר עליו הוא המסקנה המיידית מכך שהפולינומים הם תחום אוקלידי: לכל פולינום יש פירוק יחיד לגורמים <strong>אי-פריקים</strong>. הגורמים האי-פריקים הללו הולכים לשחק תפקיד משמעותי מאוד כשנתחיל לדבר על תורת השדות.

עוד דוגמא לחוג אוקלידי הוא השלמים הגאוסיים, {% equation %}\mathbb{Z}\left[i\right]{% endequation %}. אני לא הולך להוכיח את זה כאן כי <a href="http://gadial.net/2011/09/12/euclidean_algorithm_and_rings/">כבר הוכחתי את זה</a> בפוסט הקודם שלי בנושא, ואם לצטט את עצמי - "ההוכחה הזו <strong>מגעילה</strong>". מה שכדאי לקחת מההוכחה הזו הוא ש<strong>קשה</strong> להוכיח שחוגים הם אוקלידיים, ואפילו די אד-הוקי; ממש לא כל חוג חביב הוא אוקלידי. בפרט, אם לוקחים את השדה {% equation %}\mathbb{Q}\left(\sqrt{-d}\right){% endequation %} ומסתכלים על חוג השלמים שלו (שיהיה לרוב {% equation %}\mathbb{Z}\left[\sqrt{-d}\right]{% endequation %} אבל לא תמיד, ואני מעדיף לא להיכנס עכשיו לפרטים) אז מקבלים חוג שהוא תחום פריקות יחידה רק במקרים הבאים: {% equation %}d=1,2,3,7,11,19,43,67,163{% endequation %}. בכל יתר המקרים אין פריקות יחידה, ובפרט החוג לא יהיה אוקלידי. כך שתחומים אוקלידיים הם דבר נפוץ הרבה פחות מאשר נראה (לפחות לי) במבט ראשון.

זהו, סיימנו את ענייני הפריקות היחידה. לאן כדאי ללכת מכאן? ובכן, קיבלנו רק טעימה קטנה של מהם פולינומים, וכנראה שכדאי לכתוב פוסט רציני יותר בנושא; זה יהיה שימושי מאוד ביעד שאליו אנחנו חותרים, שהוא תורת השדות.
