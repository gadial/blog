---
title: "ריבוע הקסם של פרס-מרמין - איך זה עובד?"
layout: post
categories:
  - פיזיקה
  - חישוב קוונטי
tags:
  - חישוב קוונטי
---


<h2>חלק ראשון, ובו אנחנו נזכרים בריבוע הקסם של פרס ומרמין</h2>

<a href="https://gadial.net/2020/01/31/mermin_peres_magic_square/">לא מזמן</a> כתבתי פוסט שמציג את "ריבוע הקסם" של פרס-מרמין. ריבוע הקסם הזה הוא המחשה לאתגר כלשהו שחישוב קוונטי מאפשר לנו לפתור בזמן שחישוב "קלאסי" לא מסוגל לפתור אותו. לא נכנסתי לפרטים הטכניים של הפתרון הקוונטי כי היו חסרים לי היסודות של חישוב קוונטי שבהם משתמשים כאן (והפוסט על ריבוע הקסם נכתב בתור תירוץ לתת אותם). עכשיו <a href="https://gadial.net/2020/02/28/what_is_a_qubit/">כתבתי פוסטים</a> על היסודות הללו ואפשר לגשת חזרה אל ריבוע הקסם ולהסביר בדיוק איך ולמה זה עובד.

אני אנסה לנקוט פה גישה הדרגתית - להתחיל מלהסביר את הרעיון הכללי, ולאט לאט לפרוט אותו לפרוטות ולהסביר איך זה עובד ברמה הטכנית ביותר. גם אם לא מחזיקים מעמד יותר רחוק מתחילת הפוסט, אני מקווה שזה כבר מספיק כדי להבין מה הולך פה ואיך עובד הקסם.

נתחיל עם תזכורת למשחק ריבוע הקסם. זה משחק לשני שחקנים - אליס ובוב. הם מקבלים לוח משחק שנראה כך:

<img src="{{site.baseurl}}{{site.post_images}}/2020/01/magic_square1.PNG" alt=""/>

ניתנת לאליס ובוב ההזדמנות לתאם ביניהם עניינים, ואז מכניסים אותם לחדרים נפרדים ואין להם יותר דרכי תקשורת "קלאסיות" (הם לא יכולים לדבר, אין להם חיבור אינטרנט וכו')

אחרי שאליס נכנסת לחדר נותנים לה מספר שנבחר באקראי (בהתפלגות אחידה) בין 1 ל-3 והיא צריכה לצבוע את <strong>השורה</strong> שזה המספר שלה, כך שבשורה יהיה <strong>מספר זוגי</strong> של משבצות אדומות, כלומר משבצות עם {% equation %}-1{% endequation %} (או 0 או 2). גם בוב מקבל מספר אקראי בין 1 ל-3 והוא צריך לצבוע את <strong>העמודה</strong> שזה המספר שלה, כך שבעמודה יהיה <strong>מספר אי זוגי</strong> של משבצות אדומות. והנה האתגר: לא משנה איזה שורה ועמודה אליס ובוב קיבלו, תהיה בדיוק משבצת אחת שמשותפת לשניהם. הם צריכים לצבוע את הצביעות שלהם כך שאותה משבצת נצבעת <strong>באותו הצבע</strong>. אם הם הצליחו - הם מנצחים. אם הם נכשלו - הם מפסידים.

הנה דוגמא למשחק שהסתדר טוב מבחינת אליס ובוב:

<img src="{{site.baseurl}}{{site.post_images}}/2020/01/magic_square2.PNG" alt=""/>

עכשיו, כל עוד אנחנו מתבססים על חישוב "קלאסי" לא משנה כמה תיאום אליס ובוב יעשו מראש, הם עדיין עלולים להפסיד במשחק הזה. זה בגלל שאי אפשר למצוא צביעה של הלוח שבה התנאי של אליס ובוב מתקיים תמיד. הנה נסיון אחד שנכשל:

<img src="{{site.baseurl}}{{site.post_images}}/2020/01/magic_square3.PNG" alt=""/>

המשבצת {% equation %}\left(3,3\right){% endequation %} צריכה להיצבע באדום ({% equation %}-1{% endequation %}) כדי שהקריטריון של אליס יתקיים; היא צריכה להיצבע בירוק ({% equation %}+1{% endequation %}) כדי שהקריטריון של בוב יתקיים. אם אליס ובוב יוכנסו לחדרים נפרדים וההגרלה תיתן לשניהם את שורה/עמודה 3 והם ינסו לצבוע על פי הטבלה שלהלן, הם יפסידו כי הם ייאלצו לצבוע את המשבצת {% equation %}\left(3,3\right){% endequation %} בצורה לא עקבית.

אז איך חישוב קוונטי עוזר לאליס ובוב? או, טוב ששאלתם.

<h2>חלק שני, ובו אנחנו שוזרים קיוביטים</h2>

לפני שמכניסים אותם לחדרים, אליס ובוב הולכים לחלוק ביניהם שני קיוביטים שזורים, כלומר לשתף את המצב הקוונטי {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %}. אליס תקבל את הקיוביט השמאלי ובוב יקבל את הקיוביט הימני. בצורה הזו הם "מרמים את המערכת" - אסור להם לתקשר אינפורמציה כלשהי, אבל אם אליס מודדת את הקיוביט שלה, תוצאת המדידה תשפיע על הקיוביט של בוב: אם אליס מודדת בבסיס {% equation %}Z{% endequation %} ומקבלת {% equation %}\left|0\right\rangle {% endequation %} גם הקיוביט של בוב יקרוס למצב {% equation %}\left|0\right\rangle {% endequation %}; אם היא מקבלת {% equation %}\left|1\right\rangle {% endequation %} גם הקיוביט של בוב יקרוס ל-{% equation %}\left|1\right\rangle {% endequation %}. בצורה הזו אליס ובוב הולכים לייצר ביניהם את התיאום שנדרש כדי שהתשובה שיתנו למשבצת המשותפת שלהם תהיה זהה.

הפסקה שלעיל נועדה לא רק להסביר מה הולך כאן אלא לשמש בתור סוג של "שומר סף" - אם קראתם אותה ולא הבנתם מה אני רוצה מהחיים שלכם, זה אומר שכדאי לכם לחזור קודם על הרקע הבסיסי של חישוב קוונטי שהצגתי בפוסטים הקודמים; בהמשך הפוסט אני אניח שהמושגים שהשתמשתי בהם שם הם מוכרים מספיק כדי שנוכל להתחיל לעבוד איתם.

הכל בסדר עכשיו? יפה, אז בואו נסבך את הסיפור <strong>טיפה</strong>: מה שאליס ובוב הולכים לחלוק הוא לא זוג שזור אחד, אלא <strong>שני</strong> זוגות שזורים. כלומר, לאליס יש שני קיוביטים ולבוב יש שני קיוביטים ואיכשהו הקיוביטים של אליס יכולים להשפיע על הקיוביטים של בוב. בפרט, המערכת הקוונטית הכוללת שעליה אנחנו מדברים כאן היא מערכת בת <strong>ארבעה</strong> קיוביטים; אבל רוב הזמן אני אתייחס רק לזוג הקיוביטים של אליס או בוב ואתעלם מקיום הזוג השני, כי זה שומר את ההצגה המתמטית פשוטה יותר.

כדי לשמור את המתמטיקה יפה, אני איעזר בסימונים סטנדרטיים: המצב הקוונטי {% equation %}\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %}, של קיוביט בודד בסופרפוזיציה אחידה, מסומן בתור {% equation %}\left|+\right\rangle \triangleq\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %}. אליס מתחילה את המשחק עם <strong>שני</strong> קיוביטים כאלו, שאין קשר בין שניהם; הדרך שבה משלבים שני קיוביטים לא קשורים כאלו למערכת אחת היא בעזרת <strong>מכפלה טנזורית</strong>, {% equation %}\left|+\right\rangle \otimes\left|+\right\rangle {% endequation %}, וכדי לשמור את הסימון פשוט אנחנו כותבים {% equation %}\left|++\right\rangle {% endequation %} בשביל לתאר את המערכת הזו.

עכשיו אליס מקבלת את מספר השורה שעליה לסמן. היא פועלת בצורה שונה בהתאם למספר השורה שקיבלה:

<ol> <li>אליס מודדת את המצב הקוונטי שלה בבסיס {% equation %}Z{% endequation %}.</li>


<li>אליס מודדת את המצב הקוונטי שלה בבסיס {% equation %}X{% endequation %}.</li>


<li>אליס מודדת את המצב הקוונטי שלה בבסיס מסובך יותר, שאסביר עוד מעט מהו.</li>

</ol>

המדידות הללו מחזירות <strong>במובן מסויים</strong> מצב בסיס קוונטי כלשהו. השאלה "איזה מצב בסיס" תלויה בבסיס המדידה, כלומר מה שאפשר לקבל בשורה הראשונה שונה ממה שאפשר לקבל בשורה השניה. אחרי שאליס קיבלה מצב בסיס, היא מחשבת מתוכו לכל תא בשורה שקיבלה האם להציב בו {% equation %}+1{% endequation %} או {% equation %}-1{% endequation %}. פורמלית, על ידי הפעלת אופרטורים מסויימים על מצב הבסיס הזה ובדיקה אם הוא וקטור עצמי שלהם עם הערך העצמי {% equation %}+1{% endequation %} או {% equation %}-1{% endequation %}.

זה הכל.

בוב עושה את אותו הדבר בדיוק, אבל עם עמודות במקום עם שורות, ועם כללי המדידה הבאים בהתאם למספר העמודה:

<ol> <li>בוב מודד את הקיוביט הראשון שלו בבסיס {% equation %}X{% endequation %} ואת השני בבסיס {% equation %}Z{% endequation %}.</li>


<li>בוב מודד את הקיוביט הראשון שלו בבסיס {% equation %}Z{% endequation %} ואת השני בבסיס {% equation %}X{% endequation %}.</li>


<li>בוב מודד את המצב הקוונטי שלו בבסיס מסובך יותר, שאני עדיין מבטיח שאסביר עוד מעט מהו.</li>

</ol>

הנה הטבלה שאומרת בדיוק איך לחשב את הערך עבור כל משבצת:

<table>
<tr>
<td>{% equation %}Z\otimes Z{% endequation %}</td>
<td>{% equation %}Z\otimes I{% endequation %}</td>
<td>{% equation %}I\otimes Z{% endequation %}</td>
</tr>
<tr>
<td>{% equation %}X\otimes X{% endequation %}</td>
<td>{% equation %}I\otimes X{% endequation %}</td>
<td>{% equation %}X\otimes I{% endequation %}</td>
</tr>
<tr>
<td>{% equation %}Y\otimes Y{% endequation %}</td>
<td>{% equation %}-Z\otimes X{% endequation %}</td>
<td>{% equation %}-X\otimes Z{% endequation %}</td>
</tr>
</table>

עוד לפני שאני נכנס לעובי הפרטים הטכניים של למה זה עובד, בואו נראה דוגמא קונקרטית כדי לראות שזה עובד. נניח שאליס קיבלה את שורה מס' 2 ואילו בוב קיבל את עמודה מס' 1. נניח גם שאליס הייתה זריזה יותר מבוב ומדדה את הקיוביטים שלה קודם. מה קרה?

ובכן, אסביר בהמשך יותר לעומק למה אני מתכוון כאן ב"מדידה בבסיס {% equation %}X{% endequation %}" אבל כשאליס מודדת את {% equation %}\left|++\right\rangle {% endequation %} בבסיס {% equation %}X{% endequation %}, המצב שיימדד הוא בודאות של 100 אחוזים {% equation %}\left|++\right\rangle {% endequation %}. עכשיו אליס מפעילה את האופרטורים {% equation %}X\otimes I{% endequation %}, {% equation %}I\otimes X{% endequation %} ו-{% equation %}X\otimes X{% endequation %} על {% equation %}\left|++\right\rangle {% endequation %} ובודקת מה הערכים העצמיים שמתקבלים.

כזכור מהפוסטים הקודמים, {% equation %}X\left|+\right\rangle =\left|+\right\rangle {% endequation %}, ולכן <strong>כל</strong> האופרטורים הנ"ל פשוט יחזירו את {% equation %}\left|++\right\rangle {% endequation %} ולכן אליס תמלא את השורה שלה ב-{% equation %}+1,+1,+1{% endequation %}. זה בסדר גמור: מספר הערכים השליליים הוא 0, כלומר זוגי.

מה קורה עם בוב? המדידה של אליס לא שינתה את הקיוביטים שלה, ולכן לא שינתה גם את שלו - גם הוא עדיין במצב {% equation %}\left|++\right\rangle {% endequation %}. הוא קיבל את העמודה הראשונה, ולכן הוא מודד את הקיוביטים שלו בצורה הבאה: את הקיוביט הראשון הוא מודד בבסיס {% equation %}X{% endequation %}, ומכיווון שהקיוביט היה {% equation %}\left|+\right\rangle {% endequation %} הוא מקבל {% equation %}\left|+\right\rangle {% endequation %}; ואת הקיוביט השני הוא מודד בבסיס {% equation %}Z{% endequation %}, מה שיכול לתת שתי תוצאות, כל אחת בהסתברות {% equation %}\frac{1}{2}{% endequation %}: או {% equation %}\left|0\right\rangle {% endequation %} או {% equation %}\left|1\right\rangle {% endequation %}. כלומר, אחרי שתי המדידות הללו המצב הקוונטי שיש לבוב ביד הוא או {% equation %}\left|+0\right\rangle {% endequation %} או {% equation %}\left|+1\right\rangle {% endequation %} (לא להתבלבל! {% equation %}\left|+1\right\rangle {% endequation %} לא אומר "המצב שערכו הוא אחד" אלא "המצב שמורכב משני קיוביטים שהראשון מהם הוא מה שכיניתי {% equation %}+{% endequation %} שהוא סופרפוזיציה אחידה של 0 ו-1 ואילו השני הוא 1").

עכשיו בוב מפעיל על המצב שקיבל את האופרטורים {% equation %}I\otimes Z,X\otimes I,-X\otimes Z{% endequation %}. בואו נראה מה קורה בכל אחד משני המקרים האפשריים.

במקרה הראשון, שבו בוב קיבל {% equation %}\left|+0\right\rangle {% endequation %}, מתקיים {% equation %}I\otimes Z\left|+0\right\rangle =\left|+0\right\rangle {% endequation %} ו-{% equation %}X\otimes I\left|+0\right\rangle =\left|+0\right\rangle {% endequation %} פשוט מהגדרת {% equation %}X,Z{% endequation %}. כמו כן {% equation %}-X\otimes Z\left|+0\right\rangle =-\left|+0\right\rangle {% endequation %} פשוט כי יש מינוס לפני האופרטור הזה. לכן במקרה הזה, בוב מסמן את העמודה שלו ב-{% equation %}+1,+1,-1{% endequation %} שזה גם מתאים לקריטריון שלו (מספר אי-זוגי של {% equation %}-1{% endequation %}-ים) וגם עקבי עם הבחירה של אליס (שעבור המשבצת של {% equation %}X\otimes I{% endequation %} בחרה את {% equation %}+1{% endequation %}).

במקרה השני, שבו בוב קיבל {% equation %}\left|+1\right\rangle {% endequation %}, סוף סוף יש קצת אקשן: מכיוון ש-{% equation %}Z\left|1\right\rangle =-\left|1\right\rangle {% endequation %}, נקבל {% equation %}I\otimes Z\left|+1\right\rangle =-\left|+1\right\rangle {% endequation %} ו-{% equation %}-X\otimes Z\left|+1\right\rangle =\left|+1\right\rangle {% endequation %}. לעומת זאת, {% equation %}X\otimes I\left|+1\right\rangle =\left|+1\right\rangle {% endequation %} ולכן עדיין נקבל {% equation %}+1{% endequation %} למשבצת האמצעית. בסך הכל בוב יקבל את הסימון {% equation %}-1,+1,+1{% endequation %} לשורה שלו - עדיין עונה על הקריטריון, עדיין עקבי עם מה שאליס סימנה.

ככה זה יעבוד <strong>לכל בחירה של שורות ועמודות</strong>, ו<strong>לכל תוצאה של המדידות</strong> ו<strong>בלי תלות בשאלה אם אליס או בוב מודדים קודם</strong>. כולל סיטואציות מופרעות כמו "אליס מודדת את הקיוביט הראשון שלה ואז בוב מודד את הראשון שלו ואז אליס את השני שלה ואז בוב את השני שלו. זה פשוט יעבוד תמיד. אפשר לבדוק את זה על ידי מעבר על כל האפשרויות סדרתית תוך היווכחות שזה עובד; ואפשר כמובן להסתכל על כל הסיפור קצת יותר ממעוף הציפור, כדי שאפשר יהיה להוכיח שהכל עובד בלי ללכלך עד כדי כך את הידיים.

בואו נעשה את זה.

<h2>חלק שלישי, שבו אנחנו מנסים להסתכל על הכל ממעוף הציפור</h2>

תיארתי את מה שאליס עושה בתור "מודדת בבסיס כלשהו ואז מפעילה אופרטורים על התוצאה ובודקת מה יצא הערך העצמי של תוצאת המדידה עבור כל אחד מהאופרטורים". זה תיאור נכון מתמטית אבל אולי אפשר לתת לו הסבר קצת יותר ברור.

הנה הרעיון בקצה המזלג: בכל שורה ועמודה יש לנו <strong>שלושה</strong> אופרטורי מדידה <strong>שונים</strong>, אבל יש להם תכונה יפה: הם <strong>מתחלפים בכפל</strong>. התחלפות בכפל של אופרטורים לינאריים לכסינים גוררת את זה שהם <a href="https://gadial.net/2011/12/24/simultaneous_diagonalization/">לכסינים סימולטנית</a>. לכסון סימולטני שכזה פירושו שאפשר למצוא למרחב (במקרה שלנו, מרחב המצבים הקוונטיים על שני קיוביטים, שזה המרחב {% equation %}\mathbb{C}^{4}{% endequation %}) בסיס שמורכב כולו מוקטורים עצמיים <strong>של כל האופרטורים בו זמנית</strong>. כלומר: כל איבר בבסיס הוא וקטור עצמי של כל אחד מהאופרטורים שמתחלפים בכפל; מה שכן, ייתכן שעבור אופרטורים שונים הוא יתאים לערכים עצמיים שונים.

מנקודת מבט פיזיקלית, אם יש לנו אופרטורים שהם לכסינים סימולטונית שמגדירים מדידות, האינטואיציה היא שאפשר לבצע את המדידות הללו "ביחד". המתמטיקה של הביצוע המשותף של המדידות הללו היא בדיוק "לבחור באקראי את אחד מהוקטורים העצמיים ואז לכפול בו את האופרטורים ולבדוק איזה ערך עצמי יצא", אבל יש עוד דרך התבוננות שקולה שאציג עוד מעט.

בואו נראה את הדוגמא הפשוטה ביותר: השורה הראשונה של המטריצה, עם אופרטורי המדידה {% equation %}I\otimes Z,Z\otimes I{% endequation %} ו-{% equation %}Z\otimes Z{% endequation %}. האופרטור {% equation %}Z\otimes I{% endequation %} הוא מה שאנחנו מכירים בתור "מדידה של הקיוביט הראשון". מדידה כזו מחזירה {% equation %}+1{% endequation %} או {% equation %}-1{% endequation %} ומקבעת את הקיוביט הראשון להיות {% equation %}\left|0\right\rangle {% endequation %} או {% equation %}\left|1\right\rangle {% endequation %}, עם או בלי השפעה על הקיוביט השני. בדומה, {% equation %}I\otimes Z{% endequation %} היא "מדידה לפי הקיוביט השני". לעומת זאת, {% equation %}Z\otimes Z{% endequation %} היא <strong>ממש לא</strong> "מדידה של שני הקיוביטים ביחד". מדידה של שני הקיוביטים ביחד אמורה להניב לי <strong>זוג</strong> של תוצאות שכל אחת מהן היא {% equation %}\pm1{% endequation %}. היא מה שקורה אם מודדים לפי {% equation %}I\otimes Z{% endequation %} ואז לפי {% equation %}Z\otimes I{% endequation %} (או ההפך). האופרטור {% equation %}Z\otimes Z{% endequation %} מתאר מדידה שונה, פשטנית יותר, שמחזירה לי רק שני ערכים מספריים אפשריים: או {% equation %}+1{% endequation %} או {% equation %}-1{% endequation %}, ולא בהכרח מעבירה את הקיוביטים למצב קונקרטי כמו {% equation %}\left|01\right\rangle {% endequation %}.

אם זה נשמע חשוד, בואו נראה את המתמטיקה של העניין. כשאני מפעיל את {% equation %}Z\otimes Z{% endequation %} על מצב קוונטי, אני מפעיל {% equation %}Z{% endequation %} על כל קיוביט לחוד ואם קיבלתי את אותו קיוביט מוכפל בסקלר כלשהו, אני מוציא את הסקלר החוצה (זו התכונה {% equation %}\lambda v\otimes\tau u=\left(\lambda\tau\right)\left(v\otimes u\right){% endequation %} של מכפלות טנזוריות). לכן אני הולך לקבל

<ul> <li>{% equation %}Z\otimes Z\left|00\right\rangle =\left|00\right\rangle {% endequation %}</li>


<li>{% equation %}Z\otimes Z\left|01\right\rangle =-\left|01\right\rangle {% endequation %}</li>


<li>{% equation %}Z\otimes Z\left|10\right\rangle =-\left|10\right\rangle {% endequation %}</li>


<li>{% equation %}Z\otimes Z\left|11\right\rangle =\left|11\right\rangle {% endequation %}</li>

</ul>

כאשר השוויון האחרון נובע מכך שהוצאנו החוצה <strong>פעמיים</strong> את הסקלר {% equation %}-1{% endequation %} והרי {% equation %}\left(-1\right)\left(-1\right)=1{% endequation %}.

עכשיו אפשר לראות שהפירוק הספקטרלי של {% equation %}Z\otimes Z{% endequation %} הוא

{% equation %}Z\otimes Z=\left(\left|00\right\rangle \left\langle 00\right|+\left|11\right\rangle \left\langle 11\right|\right)-\left(\left|01\right\rangle \left\langle 01\right|+\left|10\right\rangle \left\langle 10\right|\right){% endequation %}

כלומר, למדוד לפי {% equation %}Z\otimes Z{% endequation %} דורש לבצע הטלה לפי אחד משני האופרטורים שבסכום - זו הטלה על מרחב שבו ייתכן שהקיוביטים <strong>שזורים</strong>, גם אם קודם הם לא היו כאלו! בקיצור, אל תחשבו על {% equation %}Z\otimes Z{% endequation %} בתור "מדידה של שני הקיוביטים", זה ממש לא נכון.

אחרי כל הדיון הזה, אני מקווה שכבר ברור שיש לנו בסיס משותף של וקטורים עצמיים עבור כל שלושת האופרטורים: הבסיס ה"סטנדרטי", {% equation %}\left\{ \left|00\right\rangle ,\left|01\right\rangle ,\left|10\right\rangle ,\left|11\right\rangle \right\} {% endequation %}. הוקטור {% equation %}\left|11\right\rangle {% endequation %} הוא דוגמא לוקטור שמתאים לערכים עצמיים שונים עבור אופרטורים שונים: עבור {% equation %}I\otimes Z{% endequation %} ו-{% equation %}Z\otimes I{% endequation %} הוא מתאים לערך העצמי {% equation %}-1{% endequation %} ואילו עבור {% equation %}Z\otimes Z{% endequation %} הוא מתאים לערך העצמי {% equation %}+1{% endequation %}. לכן אפשר לחשוב על מדידה סימולטנית של שלושת האופרטורים הללו בתור בחירה של אחד מאברי הבסיס הללו ואז חישוב הערכים העצמיים שמתאימים לו, כפי שכבר תיארתי למעלה.

אם יש לנו מצב קוונטי כללי {% equation %}\left|\psi\right\rangle {% endequation %}, אין נדע באיזו הסתברות לבחור איבר בסיס כלשהו? ובכן, זה העיקרון הכללי שראינו בפוסט הקודם: נכתוב {% equation %}\left|\psi\right\rangle =\sum_{x\in\left\{ 0,1\right\} ^{2}}\alpha_{x}\left|x\right\rangle {% endequation %} ואז ההסתברות ש-{% equation %}\left|x\right\rangle {% endequation %} יעלה בגורל היא {% equation %}\left|\alpha_{x}\right|^{2}{% endequation %}.

עם זאת, אני רוצה שנראה עוד דרך התבוננות על הסיפור הזה ששקולה מתמטית. למעלה תיארתי את מה שעושים בשורה הראשונה בתור "קודם מודדים את הקיוביט הראשון ואז את השני", כלומר קודם מבצעים מדידה לפי האופרטור {% equation %}Z\otimes I{% endequation %} ואז לפי {% equation %}I\otimes Z{% endequation %}. די ברור שהמדידות הללו אכן יניבו מצב קוונטי שהוא מהצורה {% equation %}\left|b_{1}b_{2}\right\rangle {% endequation %} כאשר {% equation %}b_{1},b_{2}\in\left\{ 0,1\right\} {% endequation %} - המדידה על פי {% equation %}Z\otimes I{% endequation %} "מכריחה" את הקיוביט הראשון להיות 0 או 1 והמדידה על פי {% equation %}I\otimes Z{% endequation %} "מכריחה" את השני. אבל יש בדרך ההצגה הזו שבירת סימטריה מעצבנת כי {% equation %}Z\otimes Z{% endequation %} המסכן נאלץ לחכות בצד בזמן ש-{% equation %}Z\otimes I{% endequation %} ו-{% equation %}I\otimes Z{% endequation %} עושים חיים, ובפועל בכלל לא "מודדים" אותו אלא מסיקים מה הערך שלו מתוך שני הערכים האחרים שהתקבלו. אבל האם באמת יקרה משהו שונה אם נכניס פנימה גם מדידה לפי {% equation %}Z\otimes Z{% endequation %}?

ובכן, נניח שמדדנו קודם לפי {% equation %}Z\otimes Z{% endequation %}. המצב הקוונטי שלנו בהתחלה הוא {% equation %}\left|++\right\rangle {% endequation %}, ואם קשה לנו לעבוד עם מצב שנראה ככה, זכרו שזה בסך הכל דרך אחרת לכתוב {% equation %}\frac{\left|00\right\rangle +\left|01\right\rangle +\left|10\right\rangle +\left|11\right\rangle }{2}{% endequation %}. כעת, נניח שהערך העצמי {% equation %}-1{% endequation %} הוא זה שעלה בגורל, כדי שיהיה לנו מעניין. זה אומר שאנחנו מפעילים את האופרטור {% equation %}\left|01\right\rangle \left\langle 01\right|+\left|10\right\rangle \left\langle 10\right|{% endequation %} על המצב הקוונטי {% equation %}\left|++\right\rangle {% endequation %} שלנו כדי לראות מה יהיה מצב המערכת אחרי המדידה הזו, ואז מנרמלים את התוצאה. אם תעשו את החשבון, תראו שנקבל {% equation %}\frac{\left|01\right\rangle +\left|10\right\rangle }{\sqrt{2}}{% endequation %} (שזו תוצאה צפויה גם בלי לעשות חשבון בגלל הסימטריה של העסק, אבל טוב לעשות את החשבון ולראות שאנחנו לא מרמים את עצמנו).

עכשיו, את התוצאה הזו נמדוד לפי האופרטור {% equation %}Z\otimes I{% endequation %}. נניח בשביל האקשן שקיבלנו הפעם דווקא {% equation %}+1{% endequation %}. זה אומר שההטלה שעלתה בגורל היא {% equation %}\left|00\right\rangle \left\langle 00\right|+\left|01\right\rangle \left\langle 01\right|{% endequation %}, והיא מעבירה אותנו אחרי נירמול למצב {% equation %}\left|01\right\rangle {% endequation %}. וזה... אחד מהוקטורים העצמיים בבסיס הוקטורים העצמיים המשותפים! כפי שהבטחתי! ואם נסתכל עכשיו על האופרטור {% equation %}I\otimes Z{% endequation %} שלא השתתף במדידות, הערך העצמי של {% equation %}\left|01\right\rangle {% endequation %} עבור האופרטור הזה הוא {% equation %}-1{% endequation %}, כך שאנחנו מקבלים את תוצאות המדידות {% equation %}+1,-1,-1{% endequation %} וזו תוצאה חוקית עבור אליס.

סיימנו עם הדוגמא הזו? יפה, עכשיו בואו נעבור להבין את המקרה הכללי.

<h2>חלק רביעי, שבו הציפור הארורה הזאתי אמורה כבר להתחיל לטוס</h2>

אחרי שהבנו איך עובדת השורה הראשונה, כדאי להסביר איך עובדות שאר השורות והעמודות, אבל לפני זה בואו נוכיח שני דברים באופן כללי: שבכל שורה ועמודה כל האופרטורים <strong>מתחלפים בכפל</strong> (ולכן יש להם בסיס משותף של וקטורים עצמיים), ושתוצאות המדידה של כל שורה ועמודה הן בעלות קורלציה כזו שמתאימה לחוקים של אליס/בוב.

התחלפות בכפל נובעת מהתכונות הנחמדות של אופרטורי פאולי, {% equation %}\left\{ I,X,Y,Z\right\} {% endequation %}. ראשית, {% equation %}I{% endequation %} היא בסך הכל מטריצת הזהות ולכן מתחלפת בכפל עם כל דבר, וכמו כן כל מטריצה מתחלפת עם עצמה בכפל, כמובן; שנית, כל זוג מטריצות אחר מתחלף בכפל עד כדי סימן, כלומר:

<ul> <li>{% equation %}XY=-YX{% endequation %}</li>


<li>{% equation %}XZ=-ZX{% endequation %}</li>


<li>{% equation %}YZ=-ZY{% endequation %}</li>

</ul>

את זה אפשר לבדוק על ידי חישוב ישיר.

עם החוקים הללו, בדיקה שכל זוג אופרטורים הוא מתחל, היא פשוטה. בשתי השורות והעמודות הראשונות כל מכפלה מערבת רק כפל מטריצה ב-{% equation %}I{% endequation %} או כפל מטריצה בעצמה, כך שההתחלפות טרויוויאלית; עבור השורה השלישית והעמודה השלישית, כל מכפלה מערבת החלפה בין שתי מטריצות שונות <strong>בשני הרכיבים</strong> כך שהתוצאה תוכפל ב-{% equation %}-1{% endequation %} פעמיים, ולכן נקבל התחלפות גם במקרה הזה (קשה להאמין? תבדקו!)

עכשיו, למה תוצאות המדידות של כל שורה ועמודה מקיימות את הדרישות מאליס ובוב? כאן גישת ה"אופרטורים שמופעלים על וקטור עצמי משותף" מאוד עוזרת לנו. בואו נניח לרגע באופן כללי ש-{% equation %}A,B,C{% endequation %} הם אופרטורים כלשהם עם וקטור עצמי משותף {% equation %}v{% endequation %}, כלומר

{% equation %}Av=\lambda_{A}v{% endequation %}

{% equation %}Bv=\lambda_{B}v{% endequation %}

{% equation %}Cv=\lambda_{C}v{% endequation %}

אז {% equation %}\left(CBA\right)v=\lambda_{A}\lambda_{B}\lambda_{C}v{% endequation %}. כלומר, אנחנו יכולים לדעת את <strong>המכפלה</strong> של הערכים העצמיים אם נסתכל על פעולת <strong>המכפלה</strong> של האופרטורים על הוקטור העצמי.

הנה מה שיקרה: לכל <strong>שורה</strong>, המכפלה הולכת לצאת האופרטור {% equation %}I\otimes I{% endequation %}, שיש לו את הערך העצמי {% equation %}+1{% endequation %} עבור <strong>כל</strong> וקטור. זה אומר שמכפלת שלושת התאים שאליס ממלאת בשורה תצא {% equation %}+1{% endequation %}, כלומר מספר התאים שבהם כתוב {% equation %}-1{% endequation %} הוא <strong>זוגי</strong>. לעומת זאת, עבור בוב המכפלה של האופרטורים בכל עמודה תצא {% equation %}-I\otimes I{% endequation %}, מה שאומר שמספר התאים בעמודה שלו שבו יוצא {% equation %}-1{% endequation %} הוא <strong>אי זוגי</strong>. האלגנטיות המתמטית הזו היא הסיבה שבגללה מלכתחילה דיברתי על {% equation %}+1,-1{% endequation %} בתאים של ריבוע הקסם ולא על {% equation %}0,1{% endequation %} שנראו טבעיים יותר בשעתו.

כדי לראות שהמכפלות יוצאות מה שאני מבטיח יש לנו תרגיל קליל באלגברה של מטריצות פאולי. הנה שתי התכונות שיהיו רלוונטיות לנו בנוסף לאלו שכבר ראינו:

<ol> <li>{% equation %}X^{2}=Y^{2}=Z^{2}=I{% endequation %}</li>


<li>{% equation %}XYZ=i\cdot I{% endequation %}</li>

</ol>

כפל האופרטורים בשורה הראשונה יוצא לנו {% equation %}\left(I\otimes Z\right)\cdot\left(Z\otimes I\right)\cdot\left(Z\otimes Z\right)=\left(Z^{2}\otimes Z^{2}\right)=I\otimes I{% endequation %}. אותו דבר בדיוק קורה בשורה השניה רק עם {% equation %}X{% endequation %} במקום {% equation %}Y{% endequation %}. השורה השלישית יותר מעניינת: כפל נותן לנו {% equation %}\left(-X\otimes Z\right)\cdot\left(-Z\otimes X\right)\cdot\left(Y\otimes Y\right)=\left(XZY\otimes ZXY\right){% endequation %}. את שני הביטויים הללו - {% equation %}XZY{% endequation %} ו-{% equation %}ZXY{% endequation %} אפשר להעביר לצורה {% equation %}XYZ{% endequation %} על ידי החלפות של זוגות סמוכים וכפל במינוס 1. נקבל {% equation %}XZY=-XYZ=-i\cdot I{% endequation %} ו-{% equation %}ZXY=\left(-1\right)\left(-1\right)XYZ=i\cdot I{% endequation %}. לכן נקבל {% equation %}\left(XZY\otimes ZXY\right)=-i^{2}\left(I\otimes I\right)=I\otimes I{% endequation %}. כפי שאתם רואים, זה לא "מזל" שהכל עובד; המטריצה מהונדסת בקפידה כדי שכל האלמנטים בה ישחקו יפה.

הבדיקה עבור העמודות דומה; עבור שתי העמודות הראשונות מה שקורה הוא כמעט אותו דבר ורק המינוס שמוצמד לאופרטורים בשורה השלישית מבטיח שנקבל תוצאה שהיא מינוס במקום פלוס. העמודה השלישית נותנת לנו {% equation %}XYZ\otimes XYZ=i^{2}\left(I\otimes I\right)=-I\otimes I{% endequation %}. זה מסיים את החלק הזה של הסיפור.

מה שקרה כרגע היה אולי לב-לבו של כל הסיפור, ואני רוצה להדגיש אותו כדי שהאלגנטיות המתמטית לא תתפספס. מה שכבר ראינו הוא ש<strong>לא ניתן</strong> למלא טבלה של {% equation %}3\times3{% endequation %} עם המספרים {% equation %}+1,-1{% endequation %} כך שהמכפלה של כל שורה תהיה 1 והמכפלה של כל עמודה תהיה {% equation %}-1{% endequation %}; אבל <strong>כן אפשר</strong> למלא אותה באיברים שהם <strong>אופרטורים</strong> כך שהמכפלה של כל שורה תהיה האופרטור שמתאים ל-{% equation %}+1{% endequation %} והמכפלה של כל עמודה תהיה האופרטור שמתאים ל-{% equation %}-1{% endequation %}. בניסוח עוד יותר מתמטי: לא ניתן למלא את הטבלה באיברים של החבורה הכפלית {% equation %}\mathbb{Z}_{2}=\left\{ 1,-1\right\} {% endequation %} כך שמכפלת כל שורה היא {% equation %}1{% endequation %} ומכפלת כל עמודה היא {% equation %}-1{% endequation %}, אבל כן ניתן למלא אותה באברי <strong>חבורת פאולי על שני קיוביטים</strong>, שהיא חבורה "עשירה" יותר ש-{% equation %}1,-1{% endequation %} הם איברים שלה (כלומר, {% equation %}\mathbb{Z}_{2}{% endequation %} היא תת-חבורה שלה) כך שתכונת הכפליות הזו כן מתקיימת. זה תרגיל נחמד לחשוב איפה ההוכחה שלא קיים ריבוע קסם עם {% equation %}\left\{ 1,-1\right\} {% endequation %} "נשברת"; מהר מאוד רואים שה<strong>קומוטטיביות</strong> של {% equation %}\left\{ 1,-1\right\} {% endequation %} משחקת כאן תפקיד מרכזי, ולכן ה"קסם" של חבורת פאולי הוא בחוסר הקומוטטיביות שלה, <a href="https://gadial.net/2017/08/13/finite_simple_groups/">שכידוע</a> מייצר חבורות מורכזות ומתוחכמות יותר.

<h2>חלק חמישי, שבו סוף סוף נבין מה הולך בשורה ועמודה מס' 3 הזו</h2>

אם לסכם מה ראינו בינתיים: ראינו שאם מודדים סימולטנית את כל האופרטורים שבשורה כלשהי, מקבלים מילוי של השורה שחוקי על פי אליס, ואם מודדים סימולטנית את כל האופרטורים בעמודה כלשהי מקבלים מילוי של העמודה שחוקי על פי בוב. ראינו גם איך בדיוק מודדים את השורה הראשונה; מה עם היתר?

ובכן, השורה השניה זהה לראשונה, רק עם מדידה בבסיס {% equation %}X{% endequation %} ולא בבסיס {% equation %}Z{% endequation %}. הסברתי בפוסט הקודם מהי מדידה בבסיס {% equation %}X{% endequation %}, אבל הרעיון הוא פשוט: כזכור, {% equation %}\left|+\right\rangle {% endequation %} מתאר את המצב הקוונטי {% equation %}\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %} ו-{% equation %}\left|-\right\rangle {% endequation %} מתאר את המצב הקוונטי {% equation %}\frac{\left|0\right\rangle -\left|1\right\rangle }{2}{% endequation %}. כעת, מדידה בבסיס {% equation %}X{% endequation %} של קיוביט בודד היא פשוט מדידה על פי הבסיס האורתונורמלי {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %}. כדי למדוד את כל השורה, משתמשים בבסיס המשותף של הוקטורים העצמיים על שני קיוביטים: {% equation %}\left\{ \left|++\right\rangle ,\left|+-\right\rangle ,\left|-+\right\rangle ,\left|--\right\rangle \right\} {% endequation %}. המתמטיקה זהה באופיה לזו של המדידה על בסיס {% equation %}Z{% endequation %}.

שתי <strong>העמודות</strong> הראשונות הן קצת יותר טריקיות, אבל לא יותר מדי - מה שקורה בהן הוא שמודדים את אחד הקיוביטים בבסיס {% equation %}\left\{ \left|0\right\rangle ,\left|1\right\rangle \right\} {% endequation %} ואת השני בבסיס {% equation %}\left\{ \left|+\right\rangle ,\left|-\right\rangle \right\} {% endequation %}. אפשר לחשוב על זה בתור מדידה בבסיס "מעורב" שכזה של שני קיוביטים: עבור העמודה הראשונה, שבה {% equation %}X{% endequation %} הוא השמאלי ו-{% equation %}Z{% endequation %} הוא הימני, נמדוד בבסיס {% equation %}\left\{ \left|+0\right\rangle ,\left|+1\right\rangle ,\left|-0\right\rangle ,\left|-1\right\rangle \right\} {% endequation %}; עבור העמודה השניה נמדוד בבסיס {% equation %}\left\{ \left|0+\right\rangle ,\left|1+\right\rangle ,\left|0-\right\rangle ,\left|1-\right\rangle \right\} {% endequation %}.

מה שמביא אותנו לשורה ועמודה מס' 3. נתחיל עם השורה. האופרטורים בה הם {% equation %}-X\otimes Z,-Z\otimes X,Y\otimes Y{% endequation %}, מה שאומר שאנחנו בסיטואציה קצת יותר מורכבת מקודם - אי אפשר להסתכל על אף אחד מהאופרטורים הללו בתור מדידה של קיוביט אחד בלבד; זה כמו {% equation %}Z\otimes Z{% endequation %} מהשורה הראשונה שבהחלט <strong>לא</strong> היה זהה ל"מודדים את הקיוביט הראשון ואז את השני". אבל לא נורא - כל עוד אנחנו יודעים למצוא בסיס משותף של וקטורים עצמיים, הכל טוב. הבסיס פה הולך לצאת טיפה טריקי, אבל המתמטיקה לא ממש קשה.

נתחיל עם האופרטור {% equation %}Y\otimes Y{% endequation %}. עדיין לא היה לנו {% equation %}Y{% endequation %}, אז בואו נזכור מה הוא עושה - הוא פועל כמו מין שילוב של {% equation %}X{% endequation %} ושל {% equation %}Z{% endequation %} עם מרוכבים:

{% equation %}Y\left|0\right\rangle =i\left|1\right\rangle {% endequation %}

{% equation %}Y\left|1\right\rangle =-i\left|0\right\rangle {% endequation %}

לכן, אם נפעיל את {% equation %}Y\otimes Y{% endequation %} על שני קיוביטים, נקבל:

{% equation %}Y\otimes Y\left|00\right\rangle =-\left|11\right\rangle {% endequation %}

{% equation %}Y\otimes Y\left|01\right\rangle =\left|10\right\rangle {% endequation %}

{% equation %}Y\otimes Y\left|10\right\rangle =\left|01\right\rangle {% endequation %}

{% equation %}Y\otimes Y\left|11\right\rangle =-\left|00\right\rangle {% endequation %}

ה-{% equation %}i{% endequation %} המרוכב נעלם - בגלל שיש שני {% equation %}Y{% endequation %}-ים הוא מוכפל בעצמו והופך ל-{% equation %}-1{% endequation %} הזה שיש לחלק מהמצבים.

בעזרת הנוסחאות הללו קל למדי לנחש מה יהיו הוקטורים העצמיים, אם מתעצלים לעבוד "לפי הספר" ופשוט לפתור מערכת של משוואות: {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} יהיה וקטור עצמי עם הערך העצמי {% equation %}-1{% endequation %}, ואילו {% equation %}\frac{\left|00\right\rangle -\left|11\right\rangle }{\sqrt{2}}{% endequation %} יהיה עם הערך העצמי 1; ובדומה, {% equation %}\frac{\left|01\right\rangle +\left|10\right\rangle }{\sqrt{2}}{% endequation %} יהיה עם הערך העצמי {% equation %}1{% endequation %} ואילו {% equation %}\frac{\left|01\right\rangle -\left|10\right\rangle }{\sqrt{2}}{% endequation %} יהיה עם הערך העצמי {% equation %}-1{% endequation %}. המצבים הללו כל כך שימושיים שהגיע הזמן לתת גם להם סימון מיוחד:

<ul> <li>{% equation %}\left|\Phi^{+}\right\rangle =\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %}</li>


<li>{% equation %}\left|\Phi^{-}\right\rangle =\frac{\left|00\right\rangle -\left|11\right\rangle }{\sqrt{2}}{% endequation %}</li>


<li>{% equation %}\left|\Psi^{+}\right\rangle =\frac{\left|01\right\rangle +\left|10\right\rangle }{\sqrt{2}}{% endequation %}</li>


<li>{% equation %}\left|\Psi^{-}\right\rangle =\frac{\left|01\right\rangle -\left|10\right\rangle }{\sqrt{2}}{% endequation %}</li>

</ul>

שהסימונים לא יבלבלו אתכם: {% equation %}\left|\Phi^{+}\right\rangle {% endequation %} הוא וקטור עצמי של הערך העצמי <strong>השלילי</strong> {% equation %}-1{% endequation %} של {% equation %}Y\otimes Y{% endequation %}, וגם {% equation %}\left|\Psi^{-}\right\rangle {% endequation %} מתאים לערך העצמי הזה, ואילו {% equation %}\left|\Phi^{-}\right\rangle {% endequation %} ו-{% equation %}\left|\Psi^{+}\right\rangle {% endequation %} מתאימים לערך העצמי 1.

איך הוקטורים הללו משחקים עם שני האופרטורים האחרים בשורה?

ובכן, נסתכל לרגע על {% equation %}-X\otimes Z{% endequation %}. אנחנו יודעים ש-{% equation %}X{% endequation %} פועל כך:

{% equation %}X\left|0\right\rangle =\left|1\right\rangle {% endequation %}

{% equation %}X\left|1\right\rangle =\left|0\right\rangle {% endequation %}

ולכן:

{% equation %}-X\otimes Z\left|00\right\rangle =-\left|10\right\rangle {% endequation %}

{% equation %}-X\otimes Z\left|11\right\rangle =\left|01\right\rangle {% endequation %}

ולכן אם נפעיל את {% equation %}-X\otimes Z{% endequation %} על הוקטור {% equation %}\left|\Phi^{+}\right\rangle {% endequation %} נקבל... {% equation %}\frac{\left|01\right\rangle -\left|10\right\rangle }{\sqrt{2}}=\left|\Psi^{-}\right\rangle {% endequation %}. וזה אומר ש-{% equation %}\left|\Phi^{+}\right\rangle {% endequation %} הוא בכלל לא וקטור עצמי של {% equation %}-X\otimes Z{% endequation %}...? איך זה ייתכן? הוקטורים העצמיים לא אמורים להיות משותפים?! האם המתמטיקה קורסת?!

ובכן, כמובן שלא. אם אופרטורים לכסינים הם מתחלפים בכפל זה אומר ש<strong>יש </strong>להם בסיס משותף של וקטורים עצמיים, לא ש<strong>כל</strong> בסיס של וקטורים עצמיים לאחד האופרטורים יהיה כזה גם עבור השני. צריך לפעול בחוכמה כדי למצוא את הבסיס המשותף. אם תסתכלו בפוסט שלי על לכסון סימולטני זה מוסבר שם, אבל למה לא להסביר את זה שוב עבור המקרה הקונקרטי שלנו.

קודם ראינו ש-{% equation %}\left|\Phi^{+}\right\rangle ,\left|\Psi^{-}\right\rangle {% endequation %} הם הוקטורים העצמיים של {% equation %}Y\otimes Y{% endequation %} שפורשים את המרחב העצמי שמתאים ל-{% equation %}-1{% endequation %}. מה שאפשר לומר בודאות הוא שהמרחב הזה הוא תת-מרחב שמור של {% equation %}-X\otimes Z{% endequation %} (זה נובע מההתחלפות בכפל) - כלומר, שאם מפעילים את האופרטור הזה על איבר בתוך תת-המרחב, הפלט גם הוא שייך לתת-המרחב. ואכן, הפעלת {% equation %}-X\otimes Z{% endequation %} על {% equation %}\left|\Phi^{+}\right\rangle {% endequation %} החזירה את {% equation %}\left|\Psi^{-}\right\rangle {% endequation %} ששייך לתת-המרחב, והפעלה שלו על {% equation %}\left|\Psi^{-}\right\rangle {% endequation %} תחזיר את {% equation %}\left|\Phi^{+}\right\rangle {% endequation %}. לכן השאלה היא - איזה וקטור ששייך למרחב הזה הוא גם וקטור עצמי של {% equation %}-X\otimes Z{% endequation %}?

ובכן, אפשר לפתור את זה בשיטה הרגילה של פתרון מערכת משוואות, אבל יותר קל לשים לב לכך שהאופרטור מחליף בין {% equation %}\left|\Phi^{+}\right\rangle {% endequation %} ובין {% equation %}\left|\Psi^{-}\right\rangle {% endequation %} ולכן הסכום שלהם {% equation %}\frac{\left|\Phi^{+}\right\rangle +\left|\Psi^{-}\right\rangle }{\sqrt{2}}{% endequation %} יהיה וקטור עצמי של האופרטור, עם הערך העצמי 1. הסכום הזה הוא שייך למרחב העצמי של {% equation %}Y\otimes Y{% endequation %} ולכן הוא גם וקטור עצמי של האופרטור הזה - הנה לכם הוקטור העצמי המשותף שחיפשנו. פורמלית, הוקטור הזה שווה ל-

{% equation %}\frac{\left|\Phi^{+}\right\rangle +\left|\Psi^{-}\right\rangle }{\sqrt{2}}=\frac{\left|00\right\rangle +\left|01\right\rangle -\left|10\right\rangle +\left|11\right\rangle }{2}{% endequation %}

שלושת הוקטורים העצמיים המשותפים האחרים דומים במבנה שלהם - רק מחליפים את זהות האיבר שיש לו מינוס. כלומר הם יהיו

<ul> <li>{% equation %}\frac{-\left|00\right\rangle +\left|01\right\rangle +\left|10\right\rangle +\left|11\right\rangle }{2}{% endequation %}</li>


<li>{% equation %}\frac{\left|00\right\rangle -\left|01\right\rangle +\left|10\right\rangle +\left|11\right\rangle }{2}{% endequation %}</li>


<li>{% equation %}\frac{\left|00\right\rangle +\left|01\right\rangle +\left|10\right\rangle -\left|11\right\rangle }{2}{% endequation %}</li>

</ul>

וזה מסיים את הסיפור גם במקרה הזה - עכשיו אנחנו יודעים מהם אברי הבסיס שצריך למדוד בשביל לטפל בשורה השלישית.

נשאר רק להבין את העמודה השלישית, עם האופרטורים {% equation %}Z\otimes Z{% endequation %}, {% equation %}X\otimes X{% endequation %} ו-{% equation %}Y\otimes Y{% endequation %}. כאן המצב עוד יותר קל: הבסיס {% equation %}\left\{ \left|\Phi^{+}\right\rangle ,\left|\Phi^{-}\right\rangle ,\left|\Psi^{+}\right\rangle ,\left|\Psi^{-}\right\rangle \right\} {% endequation %} (שנקרא לפעמים "בסיס בל") הוא עצמו הבסיס המשותף - נסו להפעיל את {% equation %}Z\otimes Z{% endequation %} או {% equation %}X\otimes X{% endequation %} על המצבים הללו ולראות מה קורה.

אז מה נשאר לנו?

<h2>פרק שישי, שבו אנחנו סוף סוף חוזרים אל עניין השזירה ההוא</h2>

כל מה שעשינו עד כה נועד לתאר בפרוטרוט את מה שאליס ובוב עושים לבדם - שניהם עושים משהו עם הקיוביטים שלהם, מקבלים תוצאה וממלאים את הריבוע לפיה. הוכחנו שזה מייצר מילוי חוקי על פי הכללים של אליס ובוב, אבל עוד לא הוכחנו את הדבר הכי חשוב - שמה שאליס ובוב עושים הוא <strong>עקבי</strong>, כלומר שהם ממלאים באותה צורה את המשבצת שמשותפת לשניהם. כאן נכנסת לפעולה העובדה שהקיוביטים שעליהם הם פעלו מלכתחילה היו שזורים.

כזכור, אנחנו מתחילים את הסיפור כשלאליס ובוב יש זוג קיוביטים שנמצאים יחד במצב {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %}. למעשה, יש להם <strong>שני</strong> זוגות כאלו (זוגות שבהם לאליס יש קיוביט אחד ולבוב את השני). המצב הקוונטי הזה כל כך מעניין שנתתי לו סימון: {% equation %}\left|\Phi^{+}\right\rangle {% endequation %}. עכשיו, לכתוב את המצב הזה בתור {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} זה קצת מטעה כי זה נותן את הרושם השגוי שיש איזו חשיבות מיוחדת ל-{% equation %}\left|0\right\rangle {% endequation %} ו-{% equation %}\left|1\right\rangle {% endequation %}, אבל אין להם: באותה מידה בדיוק אפשר לכתוב {% equation %}\left|\Phi^{+}\right\rangle =\frac{\left|++\right\rangle +\left|--\right\rangle }{\sqrt{2}}{% endequation %}. וגם לבסיס {% equation %}\left\{ \left|+\right\rangle ,\left|-\right\rangle \right\} {% endequation %} אין פה חשיבות מיוחדת. הנה תיאור כללי שיהיה קריטי עבורנו כדי להבין למה הקסם של אליס ובוב עובד: אם {% equation %}\left|\psi_{1}\right\rangle ,\left|\psi_{2}\right\rangle {% endequation %} הוא <strong>בסיס אורתונורמלי</strong> כלשהו של המרחב שנפרש בידי {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %}, ואם נכתוב

{% equation %}\left|\psi_{1}\right\rangle =\alpha_{1}\left|0\right\rangle +\beta_{1}\left|1\right\rangle {% endequation %}

{% equation %}\left|\psi_{2}\right\rangle =\alpha_{2}\left|0\right\rangle +\beta_{2}\left|1\right\rangle {% endequation %}

ועכשיו נגדיר בסיס אורתונורמלי חדש על ידי <strong>הצמדה</strong> של המקדמים, כלומר נגדיר

{% equation %}\left|\phi_{1}\right\rangle =\alpha_{1}^{\dagger}\left|0\right\rangle +\beta_{1}^{\dagger}\left|1\right\rangle {% endequation %}

{% equation %}\left|\phi_{2}\right\rangle =\alpha_{2}^{\dagger}\left|0\right\rangle +\beta_{2}^{\dagger}\left|1\right\rangle {% endequation %}

אז מתקיים הדבר הבא: {% equation %}\left|\Phi^{+}\right\rangle =\frac{\left|\psi_{1}\phi_{1}\right\rangle +\left|\psi_{2}\phi_{2}\right\rangle }{\sqrt{2}}{% endequation %}

כדי לראות שזה קורה, אפשר פשוט "לפתוח" את הביטויים {% equation %}\left|\psi_{1}\phi_{1}\right\rangle {% endequation %} ו-{% equation %}\left|\psi_{2}\phi_{2}\right\rangle {% endequation %} ולייצג אותם בעזרת אברי הבסיס {% equation %}\left\{ \left|00\right\rangle ,\left|01\right\rangle ,\left|10\right\rangle ,\left|11\right\rangle \right\} {% endequation %} ואז לראות אילו מקדמים מתאפסים ואילו יוצאים שווים ל-1:

{% equation %}\left|\psi_{1}\phi_{1}\right\rangle =\left|\alpha_{1}\right|^{2}\left|00\right\rangle +\alpha_{1}\beta_{1}^{\dagger}\left|01\right\rangle +\left(\alpha_{1}\beta_{1}^{\dagger}\right)^{\dagger}\left|10\right\rangle +\left|\beta_{1}\right|^{2}\left|11\right\rangle {% endequation %}

{% equation %}\left|\psi_{2}\phi_{2}\right\rangle =\left|\alpha_{2}\right|^{2}\left|00\right\rangle +\alpha_{2}\beta_{2}^{\dagger}\left|01\right\rangle +\left(\alpha_{2}\beta_{2}\right)^{\dagger}\left|10\right\rangle +\left|\beta_{2}\right|^{2}\left|11\right\rangle {% endequation %}

ולכן, אחרי חיבור, נראה שאנחנו בעצם רוצים שיתקיים

<ul> <li>{% equation %}\left|\alpha_{1}\right|^{2}+\left|\alpha_{2}\right|^{2}=1{% endequation %}</li>


<li>{% equation %}\left|\beta_{1}\right|^{2}+\left|\beta_{2}\right|^{2}=1{% endequation %}</li>


<li>{% equation %}\alpha_{1}\beta_{1}^{\dagger}+\alpha_{2}\beta_{2}^{\dagger}=0{% endequation %}</li>

</ul>

זה נובע מהאורתונורמליות של {% equation %}\left\{ \left|\psi_{1}\right\rangle ,\left|\psi_{2}\right\rangle \right\} {% endequation %}, אבל קצת טריקי לראות את זה. אם נרשום מטריצה שבה האיברים הללו הם הוקטורים:

{% equation %}U=\left(\begin{array}{cc} \alpha_{1} & \alpha_{2}\\ \beta_{1} & \beta_{2} \end{array}\right){% endequation %}

אז האורתונורמליות של הבסיס פירושה ש-{% equation %}U^{\dagger}U=I{% endequation %}, כלומר {% equation %}U^{\dagger}=U^{-1}{% endequation %} (אומרים על זה ש-{% equation %}U{% endequation %} היא <strong>מטריצה אוניטרית</strong>). מכיוון שמטריצה מתחלפת בכפל עם ההופכית שלה (זה משפט לא לגמרי טריוויאלי אבל אני מרשה לעצמי לחפף פה) אז {% equation %}UU^{\dagger}=I{% endequation %} וזה נותן לנו בדיוק את השוויונות שרציתי למעלה (נסו לכפול את המטריצות ולראות מה קורה).

יפה, אז לסיכום, ראינו שאפשר לכתוב את {% equation %}\left|\Phi^{+}\right\rangle {% endequation %} בצורות רבות ושונות. איך זה עוזר לנו? ובכן, בואו נזכור למה {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} היה מצב מעניין מלכתחילה: כי אם אנחנו מודדים <strong>את הקיוביט הראשון</strong> לפי הבסיס הסטנדרטי ומקבלים {% equation %}\left|0\right\rangle {% endequation %} זה "הכריח" גם את הקיוביט השני להיות {% equation %}\left|0\right\rangle {% endequation %}. באותו אופן, אם היינו מודדים את הקיוביט הראשון של {% equation %}\left|\Phi^{+}\right\rangle =\frac{\left|++\right\rangle +\left|--\right\rangle }{\sqrt{2}}{% endequation %} לפי בסיס {% equation %}X{% endequation %} ומקבלים {% equation %}\left|+\right\rangle {% endequation %} זה היה "מכריח" את הקיוביט השני להיות {% equation %}\left|+\right\rangle {% endequation %}. ועכשיו בכללי: נניח שיש לנו את המצב {% equation %}\left|\Phi^{+}\right\rangle {% endequation %} ואנחנו מודדים את <strong>הקיוביט הראשון</strong> לפי בסיס מדידה אורתונורמלי <strong>כלשהו</strong>, {% equation %}\left\{ \left|\psi_{1}\right\rangle ,\left|\psi_{2}\right\rangle \right\} {% endequation %}. אז אם הקיוביט הראשון יצא {% equation %}\left|\psi_{1}\right\rangle {% endequation %} זה מכריח את הקיוביט השני להיות {% equation %}\left|\phi_{1}\right\rangle {% endequation %}, ואם הוא יצא {% equation %}\left|\psi_{2}\right\rangle {% endequation %} זה מכריח את הקיוביט השני להיות {% equation %}\left|\phi_{2}\right\rangle {% endequation %}. זו המהות האמיתית של "שזירה" כאן. וזה רלוונטי לנו כי אליס ובוב מודדים את הקיוביטים שלהם בבסיסים שונים ומשונים, בהתאם לשורה והעמודה שלהם.

המערכת של אליס ובוב מורכבת מארבעה קיוביטים ולא משניים, אבל המתמטיקה שהצגתי למעלה ניתנת להכללה די בקלות. אם {% equation %}\left\{ \left|\psi_{1}\right\rangle ,\left|\psi_{2}\right\rangle ,\left|\psi_{3}\right\rangle ,\left|\psi_{4}\right\rangle \right\} {% endequation %} הוא בסיס אורתונורמלי למרחב של שני קיוביטים ו-{% equation %}\left\{ \left|\phi_{1}\right\rangle ,\left|\phi_{2}\right\rangle ,\left|\phi_{3}\right\rangle ,\left|\phi_{4}\right\rangle \right\} {% endequation %} מתקבל ממנו על ידי הצמדת המקדמים, אז את המצב הקוונטי שמתקבל משני הזוגות השזורים של הקיוביטים אפשר לתאר בתור {% equation %}\frac{1}{2}\sum_{i=1}^{4}\left|\psi_{i}\phi_{i}\right\rangle {% endequation %}, ולכן שוב: אם אליס מודדת את הקיוביטים שלה לפני בוב, אז הקיוביטים של בוב יקרסו לאותו מצב בסיס <strong>בדיוק</strong> כמו זה שאליס קיבלה; ואם בוב ימדוד קודם, אז הקיוביטים של אליס יקרסו למצב הבסיס שבוב קיבל.

האם זה מסיים את הסיפור? עוד לא! אבל כמעט. בואו נניח שאליס מדדה את הקיוביטים שלה קודם ונבין למה זה מבטיח שהיא תיתן את אותה תוצאה כמו בוב על המשבצת המשותפת שלהם. כרגיל, הכי קל לראות דוגמא. נניח שאליס מודדת את השורה הראשונה שלה ובוב את העמודה השלישית, ואליס מדדה קודם. השורה הראשונה נמדדת לפי הבסיס {% equation %}\left\{ \left|00\right\rangle ,\left|01\right\rangle ,\left|10\right\rangle ,\left|11\right\rangle \right\} {% endequation %}. בואו נניח שאליס קיבלה את הוקטור העצמי {% equation %}\left|10\right\rangle {% endequation %}. הערך העצמי שמתאים לוקטור הזה ביחס לאופרטור {% equation %}Z\otimes Z{% endequation %} הוא {% equation %}-1{% endequation %} ולכן אליס כתבה {% equation %}-1{% endequation %} במשבצת הימנית ביותר בשורה שלה. זה גם מה שבוב אמור לכתוב.

עכשיו בוב מגיע שמח וטוב לב למדוד את הקיוביטים שלו. אולי הוא עוד מאמין בלב שהמצב הקוונטי שיש לו ביד הוא {% equation %}\left|++\right\rangle {% endequation %}. מה חבל! אנחנו כבר יודעים שהוא טועה ומה שיש לו ביד הוא בעצם את המצב הקוונטי {% equation %}\left|10\right\rangle {% endequation %}. עכשיו, בוב מודד את העמודה השלישית שלו על פי מה שקראתי לו "בסיס בל": {% equation %}\left\{ \left|\Phi^{+}\right\rangle ,\left|\Phi^{-}\right\rangle ,\left|\Psi^{+}\right\rangle ,\left|\Psi^{-}\right\rangle \right\} {% endequation %}. אנחנו יודעים שהוא יקבל את אחד מהוקטורים הללו בתור תוצאה - זה לא מושפע ממה שאליס עשתה. מה שכן השתנה הוא <strong>ההסתברויות</strong> שלו לקבל את המצבים הללו; את חלקם פשוט אין לו סיכוי לקבל עכשיו.

כזכור, מדידה על פי בסיס אורתונורמלי פירושה לקחת את המצב הנוכחי שלנו, לכתוב אותו בתור <strong>צירוף לינארי</strong> של אברי הבסיס האורתונורמלי, ואז ההסתברות לקבל איבר בסיס כלשהו כתוצאת המדידה מחושבת איכשהו מתוך המקדם. אם המקדם הוא 0, אז אין סיכוי לקבל את האיבר הזה. עכשיו, עבור הדוגמא {% equation %}\left|10\right\rangle {% endequation %} קל למצוא את ההצגה שלה כצירוף אורתונורמלי של אברי הבסיס: {% equation %}\left|10\right\rangle =\frac{\left|\Psi^{+}\right\rangle -\left|\Psi^{-}\right\rangle }{\sqrt{2}}{% endequation %}. כלומר, אחרי המדידה של בוב הוא יקבל את {% equation %}\left|\Psi^{+}\right\rangle {% endequation %} או את {% equation %}\left|\Psi^{-}\right\rangle {% endequation %}. שני המצבים הללו הם וקטורים עצמיים של {% equation %}Z\otimes Z{% endequation %} עם הערך העצמי {% equation %}-1{% endequation %}, ולכן זה מה שבוב יגיד - בהסכמה מלאה עם מה שאליס אמרה. קסם!

באופן כללי, אחרי המדידה של אליס המצב של בוב נמצא בוקטור ששייך <strong>למרחב העצמי</strong> של האופרטור של המשבצת המשותפת של של בוב ואליס. אחר כך בוב מודד את המצב שלו על פי בסיס אורתונורמלי שמורכב מאברי הבסיס של המרחב העצמי הזה, ואברי בסיס של מרחב עצמי אחר. מכיוון שהמצב של בוב כבר שייך למרחב עצמי, המדידה תשאיר אותו שם; הוא מלכתחילה צירוף לינארי של וקטורים עצמיים של המרחב הזה ותו לא. זה מסיים את הסיפור כולו.

<h2>פרק שביעי, שבו דברי סיכום ופרידה</h2>

סיימנו! הגענו לסוף הסאגה של ריבוע הקסם של פרס ומרמין, ואני די מבועת מכמה שהפוסט הזה יצא לי ארוך. בהצגות פופולריות של הנושא ההסבר לוקח בדרך כלל עמוד או שניים; כאן רציתי להיכנס למתמטיקה עד הסוף (כי גם אני לא ממש הבנתי אותה עד הסוף) והאורך הוא התוצאה של זה, אבל אני מקווה שבדרך למדנו הרבה על דברים מעניינים בקוונטים ואלגברה לינארית ואנחנו כבר לא מרגישים שיש מסתורין בסיפור הזה.

כדי לסכם אני רוצה להצביע על שתי הנקודות שבהן תורת הקוונטים מאפשרת את הקסם שמתרחש פה:

ראשית, השזירה הקוונטית יוצרת סוג של "תקשורת" בין אליס ובוב למרות שהם לכאורה לא מסוגלים לתקשר. צריך להיות זהירים מאוד כאן - זו לא באמת תקשורת. אליס לא מסוגלת לספר לבוב מה הערך המספרי שהיא ממלאת במשבצת שלה. כל מה שהיא יכולה לעשות הוא <strong>להטות את ההגרלה</strong> שבוב מבצע. ההטיה הזו לא קובעת באופן דטרמיניסטי מה בוב יעשה; אבל היא כן מבטיחה שעל משבצת אחת ויחידה הערך שלו יהיה זהה לערך שלה. כשרואים את זה בצורה הזו קל להבין איך שזירה קוונטית יכולה להיות יתרון <strong>אבל גם חיסרון</strong> עבור מי שמבצעים חישוב קוונטי - זה גורם לבוב לבצע חישובים שהם מוטים בצורה שאין לו איך לשלוט עליה. זה לא משפיע לרעה במקרה של פרס ומרמין, אבל זה נהיה רלוונטי כשמדברים על תוצאה כמו {% equation %}\text{MIP}^{*}=\text{RE}{% endequation %} שמתבססת על כך שמוודא יכול "להכריח" מוכיחים שזורים קוונטית להתנהל בצורה שמקשה עליהם לרמות אותו (בשביל זה הוא צריך גם להיות מסוגל להכריח אותם בכלל להשתמש בקיוביטים השזורים שלהם; זה כבר סיפור אחר שאולי יסופר בפעם אחרת).

שנית, ראינו שהמבנה של חבורת פאולי הוא "עשיר" מספיק כדי להחביא בתוכו מילוי חוקי של כל ריבוע הקסם בעזרת אופרטורים, בזמן שסתם מילוי של הריבוע עם {% equation %}+1{% endequation %} ו-{% equation %}-1{% endequation %} לא היה עובד. זו המחשה לסוג המעניין של מתמטיקה שחישוב קוונטי מאפשר לנו לעשות; אני מקווה שזה נותן תחושה כלשהי של הסיבות לכך שחישוב קוונטי הוא דבר יעיל, וגם (ואולי בעיקר) של הסיבות לכך שהוא עניין ממש לא פשוט גם מהבחינה התיאורטית.

וכמובן, אני מקווה שזה היה ממש מגניב. 
