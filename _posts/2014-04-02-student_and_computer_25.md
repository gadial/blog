---
id: 3087
title: "פרוייקט \"התלמיד והמחשב\", בעיה 25"
date: 2014-04-02 18:18:48
layout: post
categories: 
  - אלגברה לינארית
  - תכנות
tags: 
  - משוואות דיופנטיות
  - פרוייקט "התלמיד והמחשב"
  - צורת סמית
---
סוף סוף הגענו אל בעיה עם בשר אמיתי, וכזו שתיתן לנו תירוץ להזכיר קצת מתמטיקה, ברמה יותר גבוהה מזו שהוזכרה בספר. נתחיל מהבעיה עצמה, שהיא פשוטה למדי לניסוח ולמרבה הצער, מנוסחת בלשון צבאית: בפלוגה כלשהי יש לנו 100 חיילים. מהם חלק הם טוראים, חלק הם סמלים וחלק הם קצינים. משכורתו של טוראי היא 1 ש"ח, משכורתו של סמל היא 10 ש"ח ומשכורתו של קצין היא 50 ש"ח. ידוע שסכום המשכורות של כל החיילים הוא 500 ש"ח. מה מספר הטוראים, מה מספר הסמלים ומה מספר הקצינים בפלוגה?

למי שהניסוח הצבאי מעצבן אותו אפשר להשתמש בשלל סיפורי רקע אחרים. למשל, תערובת כימית שכוללת 100 אטומים של מימן (פרוטון אחד), נאון (10 פרוטונים) ובדיל (50 פרוטונים) וידוע שיש בה סה"כ 500 פרוטונים. נשאלת השאלה כמה אטומים יש מכל סוג (למעשה, שאלות מסוג זה הן אכן נפוצות הרבה יותר בהקשר של תערובות ותרכובות כימיות מאשר בהקשר הצבאי). בסופו של דבר אנחנו מקבלים את אותו פורמליזם מתמטי - מערכת משוואות לינארית שנראית כך:

{% equation %}\array{x+y+z&=&100\\x+10y+50z&=&500}{% endequation %}

זו <strong>מערכת</strong> של משוואות כי היא כוללת שתי משוואות ולא אחת; וזו מערכת <strong>לינארית</strong> כי כל המשתנים שלנו - {% equation %}x,y,z{% endequation %} - מופיעים בה כשהחזקה שלהם היא 1, ולא מפעילים עליהם פונקציות מוזרות כמו סינוס. הנה דוגמה למשוואות לא לינאריות: {% equation %}x^2+x+1=0{% endequation %}  אינה לינארית כי ה-{% equation %}x{% endequation %} הוא בריבוע, ו-{% equation %}\sin(x)=x{% endequation %} אינה לינארית כי {% equation %}x{% endequation %} מופיע פעם אחת כשמפעילים עליו את סינוס.

הסיבה שאנחנו טורחים לתת שם מיוחד למשוואות לינאריות היא שהמשוואות הללו <strong>פשוטות במיוחד</strong>. לפתור משוואות לא לינאריות בצורה מדוייקת זה לרוב קשה; אבל עבור משוואות לינאריות התיאוריה מאוד מפותחת ויש לנו שיטות פתרון נקיות ופשוטות למדי. לעתים קרובות האופן שבו מתמודדים עם מערכת משוואות לא לינאריות היא באמצעות קירוב שלהן בעזרת מערכת משוואות לינאריות שאותה אנחנו יודעים לפתור.

במקרה הפשוט ביותר, המערכת היא מעל <strong>שדה</strong>, כלומר אפשר לבצע על המספרים שלנו פעולות של חיבור, חיסור, כפל וחילוק. במקרה הזה אפשר להפעיל את מה שנקרא "חילוץ גאוסי" - אולי אחד הדברים הראשונים שסטודנטים למתמטיקה לומדים (בקורס אלגברה לינארית) שמוצא את כל הפתרונות למערכת, אם קיימים כאלו. צריך לשים דגש על המילה "פתרונות" - כבר בבית הספר לומדים שלמערכת עם שלושה נעלמים ושתי משוואות, כמו אצלנו, יכול להיות יותר מפתרון אחד.

אז מה הבעיה? הבעיה היא שלפעמים יש עוד <strong>אילוצים</strong> על הפתרונות, וכך גם אצלנו. ראשית, אנחנו מצפים שהפתרונות יהיו <strong>מספרים שלמים</strong>, מה שאומר שאם נפעיל את שיטת גאוס ונקבל פתרונות שהם שבר זה לא יהיה מספיק טוב. למשוואה שבה הפתרונות צריכים להיות שלמים קוראים <strong>משוואה דיופנטית</strong>, אז מה שיותר מדויק לומר הוא שאנחנו פותרים פה מערכת של משוואות דיופנטיות לינאריות. באופן כללי משוואות דיופנטיות הן דבר קשה ביותר לפתרון - כתבתי בשעתו <a href="http://www.gadial.net/2012/08/27/hilbert_tenth_intro/">סדרת פוסטים</a> שמוכיחה שלא קיים אלגוריתם שפותר מערכת משוואות דיופנטית כללית. אבל במערכת כזו יכולות להיות חזקות גדולות מ-1 של המשתנים, ואילו אצלנו מערכת המשוואות הדיופנטיות היא לינארית, ותמיד ניתן לפתור מערכת כזו ואסביר את הרעיון הכללי בהמשך.

עדיין, יש לנו עוד הגבלה על המערכת - כל הפתרונות צריכים להיות מספרים <strong>חיוביים</strong>. המגבלות הללו הן לא סוף העולם ואפשר להשתמש באלגוריתמים הכלליים לפתרון מערכות של משוואות; אבל צריך להבין ששימוש בהם עדיין לא יהיה סוף הסיפור. השיטות הכלליות יתנו לנו המון פתרונות אפשריים, ונצטרך לחפש בתוכם את הפתרון ה"נכון". השיטות הכלליות גם יהיו קצת מסובכות מבחינת התיאוריה שמאחוריהן ואני לא מצפה שכל הקוראים יבינו אותן וישרדו עד הסוף.

על כן, לפני שניגש לפתרונות הכלליים, בואו נראה את הפתרון שיש בספר, שהוא פתרון "ברוטלי" למדי אבל לפעמים הוא גם הכי מתאים - פשוט נחפש בכוח שלשה של מספרים שהיא פתרון. אבל גם פתרון כוח גס שכזה צריך לדעת לממש. הנה דוגמה למימוש <strong>לא טוב</strong>:

<div class="code-block">
{% highlight ruby %}
A = 1
B = 10
C = 50
NUM = 100
SUM = 500

for x in (0..NUM) do
  for y in (0..NUM) do
    for z in (0..NUM) do
      if (x+y+z == NUM and A*x+B*y+C*z == SUM)
	puts &quot;x = #{x}, y = #{y}, z = #{z}&quot;
      end
    end
  end
end
{% endhighlight %}
</div>

הפתרון הזה לא טוב לא בגלל שהוא לא עובד; הוא עובד, ועוצר תוך שניה ומחזיר את הפתרון הנכון (x = 60, y = 39, z = 1). הוא לא טוב כי הוא עושה עבודה מיותרת ולא עובר בצורה חכמה על המשתנים שלנו. ראשית, אין שום סיבה בעולם להשתמש ב<strong>שלוש</strong> לולאות for אחת בתוך השניה; אפשר להיעזר בכך שאנחנו יודעים ש-{% equation %}x+y+z=100{% endequation %} ולכן אם כבר קבענו מי יהיו {% equation %}x,y{% endequation %} אז אפשר להגדיר את {% equation %}z{% endequation %} להיות 100 פחות שניהם:

<div class="code-block">
{% highlight ruby %}
for x in (0..NUM) do
  for y in (0..NUM) do
    z = NUM - (x+y)
    if (z &gt;= 0 and A*x+B*y+C*z == SUM)
      puts &quot;x = #{x}, y = #{y}, z = #{z}&quot;
    end
  end
end
{% endhighlight %}
</div>

שימו לב שעכשיו אני נאלץ לבדוק אם z הוא חיובי כי הוא עלול לצאת שלילי. הסיבה לכך היא שלא הייתי חכם ואני נותן ל-y להיות כל מספר מ-0 ועד 100, גם אם הסכום של x ו-y יעבור את 100. אז בואו נגביל את y:

<div class="code-block">
{% highlight ruby %}
for x in (0..NUM) do
  for y in (0..(NUM-x)) do
    z = NUM - (x+y)
    if (A*x+B*y+C*z == SUM)
      puts &quot;x = #{x}, y = #{y}, z = #{z}&quot;
    end
  end
end
{% endhighlight %}
</div>

עד כאן הכל די ברור. האופטימיזציה הבאה היא טיפה יותר חכמה, וכנראה הדבר הכי חשוב מבין כל האופטמיזציות שאני מראה פה. האבחנה היא שיש לי מגבלה נוספת ברורה על הגודל המקסימלי של x,y,z - המשוואה השניה. המשוואה השניה אומרת לי, למשל, ש-z חייב להיות בין 0 ל-10, אחרת כבר 50z לבדו יהיה גדול מ-500. לכן, במקום לרוץ על כל ערכי x מ-0 ועד 100, עדיף להתחיל דווקא מלרוץ על ערכי z, אחר כך לרוץ על ערכי y, ואת x כבר לקבוע מתוך שניהם. זה מוביל לפתרון הכי טוב שלי:

<div class="code-block">
{% highlight ruby %}
for z in (0..SUM/C) do
  for y in (0..(SUM-C*z)/10) do
    x = NUM - (y+z)
    if (A*x+B*y+C*z == SUM)
      puts &quot;x = #{x}, y = #{y}, z = #{z}&quot;
    end
  end
end
{% endhighlight %}
</div>

הפתרון הזה פחות קריא מהקודמים, אבל בהחלט יותר יעיל. עד כמה שאפשר לדבר על "יעילות" בהקשר הזה, שבו כל אחד מהסקריפטים שהצגתי מסיים לרוץ כהרף עין.

אז זה פתרון הכוח הגס. מה על פתרונות חכמים יותר, שמשתמשים בשיטות מתמטיות כלליות? ובכן, אפשר לממש את השיטות הללו באופן עצמאי, אבל זה לא רעיון טוב במיוחד - עבור רוב שפות התכנות יש ספריות מתמטיות שמומשו עם דגש על יעילות, ועדיף להשתמש בהן. למרבה הצער, רובי היא אחת מאותן שפות שבהן זה <strong>לא</strong> המצב. הספריה המתמטית שלה אינה מפותחת מספיק, ולמרות שעושים מאמצים בכיוון, אני מעדיף לנצל את ההזדמנות הזו ולקפוץ לרגע הצידה, אל האחות של רובי - פייתון.

בשורה התחתונה, פייתון ורובי הן שפות די דומות - שתיהן שפות סקריפטינג עם תחביר קליל יחסית (ודומה יחסית) ושתיהן רבות עוצמה ומאפשרות לעשות דברים מורכבים בפשטות יחסית, תוך תשלום של מחיר כלשהו בזמן הריצה. מצד שני, לפייתון יש יתרון מרכזי אחד על רובי - כמות גדולה יותר של משתמשים, ולכן קהילה גדולה יותר, סיכוי גדול יותר לקבל תמיכה אם נתקלים בבעיה, והכי חשוב - הרבה יותר ספריות. אפשר לומר בצחוק שיש ספריית פייתון לכל דבר בערך, וזה לא יהיה רחוק כל כך מהמציאות. הנה מה שהיה לרנדל מונרו מ-xkcd לומר כשהוא גילה את פייתון:

<a href="{{site.baseurl}}{{site.post_images}}/2014/03/python.png"><img src="{{site.baseurl}}{{site.post_images}}/2014/03/python.png" alt="python" width="518" height="588" class="alignnone size-full wp-image-3088" /></a>

בפרט, לפייתון יש תמיכה יפה מאוד בספריות מתמטיות. בואו נתחיל מלדבר על SymPy - ספריה למתמטיקה סימבולית, שזה בדיוק מה שאנחנו צריכים - פתרון משוואות אלגבריות עם נעלמים הוא סוג של מתמטיקה סימבולית. בואו נראה תוכנית בפייתון שפותרת את הבעיה שלנו עם התבססות על חילוץ גאוסי, ואסביר אותה שורה שורה:

<div class="code-block">
{% highlight python %}
from sympy import *
x, y, z = symbols('x y z')
sol = solve([x + y + z - 100, x + 10*y + 50*z - 500], x, y, z)
for z_val in range(11):
  x_val = sol[x].subs(z,z_val)
  y_val = sol[y].subs(z,z_val)
  if x_val.q == 1 and y_val.q == 1:
    print &quot;x = %d, y = %d, z = %d&quot; % (x_val, y_val, z_val)
{% endhighlight %}
</div>

התחביר דומה מספיק לזה של רובי כדי שלא אבזבז זמן על הסברים שלו - אני מניח שגם מה שלא זהה הוא די ברור. בשורה 1 אני אומר לפייתון להשתמש בספריה של SymPy. בשורה 2 אני מגדיר שלושה סימבולים, x,y,z, ומציב אותם בתוך המשתנים שנקראים באותו שם (למרות שהם לא חייבים). שימו לב ש"סימבול" כאן הוא משהו שונה מסיבול של רובי - כאן סימבול הוא אובייקט של הספריה SymPy ולא קשור לסימבולים של רובי בשום צורה.

בשורה השלישית מתבצעת המתמטיקה - אני קורא לפונקציה solve שמקבלת כקלט מערך הכולל שתי משוואות. ההנחה הסמויה של SymPy הוא שאם אני כותב ביטוי כמו "x + y + z - 100" בלי שוויון בתוכו, אני מתכוון שהוא יהיה שווה ל-0. לכן הביטוי הזה מקודד את המשוואה "x + y + z = 100". בדומה,  "x + 10*y + 50*z - 500" מקודד את המשוואה "x + 10*y + 50*z = 500". מה ש-SymPy עושה הוא לזהות בעצמו שמדובר על משוואה לינארית ולקרוא למימוש שלו של האלגוריתם הגאוסי שמחזיר פתרון כללי למשוואה הזו מעל הרציונליים. ואם נסתכל מה הערך של sol בשלב הזה, זה מה שנראה:

<div class="code-block">
{% highlight python %}
{x: 40*z/9 + 500/9, y: -49*z/9 + 400/9}
{% endhighlight %}
</div>

מה שיש לנו כאן הוא Hash שמכיל שני מפתחות: את הערך של x כפונקציה של z, ואת הערך של y כפונקציה של z. הנקודה פה היא שלכל ערך של z שרק נבחר, קיים פתרון (יחיד) למערכת המשוואות, ואם נציב את z בפונקציות שמגדירות את x,y נקבל את הערכים שלהם. למשל, אם נבחר z=1 נקבל {% equation %}x=\frac{40+500}{9}=60{% endequation %} ו-{% equation %}y=\frac{-49+400}{9}=39{% endequation %}. זה, במקרה ממוזל, גם הפתרון הנכון של המשוואה - קיבלנו רק מספרים שלמים חיוביים.

באופן כללי הפתרונות הם מספרים רציונליים, ולכן כדי למצוא פתרון שכולל רק שלמים יש את שורות 4-7, שבהן אני עובר על כל הערכים האפשריים של z (זוכרים שאני יכול להגביל אותם להיות בין 0 ל-10? פקודת ה-range שם יוצרת את הטווח הזה) ולכל אחד מהם מחשב את הערכים של x,y עבור הערך הזה של z, באמצעות פקודת subs (שאומרת "בביטוי הסימבולי הנוכחי שכולל את z, הצב כך-וכך במקום z ונראה מה תקבל"). לבסוף אני בודק שקיבלתי מספרים שלמים, על ידי כך שאני לוקח את המשתנים ומסתכל על הערך של המכנה (q) שלהם.

זה בוודאי נראה קצת מסורבל ביחס לפתרון הקודם שלי, אבל שימו לב שעכשיו יש לי רק לולאה אחת - על הערכים האפשריים של z. זה היה שיפור משמעותי בזמן הריצה, אם הבעיה הזו הייתה מסדרי גודל שבהם זה היה בכלל חשוב (וכמובן, גם שלב ה-solve דורש זמן לא טריוויאלי, אבל לרוב הוא יהיה יחסית מהיר).

האם אפשר היה לוותר על הלולאה הזו? כלומר, האם יש דרך חכמה מבחינה מתמטית למצוא z שמבטיח שנקבל מספרים שלמים? התשובה היא כן, והיא מתבססת על פתרון של <a href="http://www.gadial.net/2013/05/13/modular_arithmetic/">משוואות מודולריות</a>, אבל נעזוב את זה להפעם כי זה ייקח אותי רחוק מדי והפוסט כבר כך ארוך.

בואו נעבור לראות פתרון כללי עוד יותר, שעשוי להיראות כאן מסורבל שלא לצורך ולא יעיל במיוחד, אבל הוא המעניין ביותר מבחינה מתמטית, לדעתי. המטרה שלי היא לקבל את הפתרון הכללי למערכת המשוואות הדיופנטית הלינארית - כלומר, לקבל ביטוי סימבולי כלשהו שיש בו משתנים, ולכל ערך שלם שאני מציב במשתנים הללו אני מקבל פתרון של המערכת, וכל הפתרונות של המערכת מתקבלים כך. הדרך שבה אשתמש כדי למצוא אותו היא באמצעות מה שמכונה <strong>צורת סמית</strong> של מטריצה. מה שאומר שההמשך יהיה ברור רק למי שמכיר מטריצות, ועם הסליחה ממי שעדיין לא מכיר.

סטודנטים למתמטיקה ייתקלו בצורת סמית בהקשר של משפט המבנה של מודולים נוצרים סופית מעל תחום ראשי (או בהקשר של מקרה פרטי שלו - משפט המבנה של חבורות אבליות נוצרות סופית). זה משפט נפלא ונהדר, שממנו נובע לא רק המשפט הפשוט יותר עבור חבורות אלא גם צורת ז'ורדן והצורה הרציונלית של מטריצות. אבל זו מתמטיקה לא טריוויאלית שאין לי כוונה להיכנס אליה בפוסט, ולכן אסתפק בניסוח הכי יבש שרק אפשר. הרעיון הוא זה: נניח ש-{% equation %}A{% endequation %} היא מטריצה, לאו דווקא ריבועית אלא מסדר {% equation %}n\times m{% endequation %}. אז <strong>תמיד</strong> אפשר למצוא שתי מטריצות <strong>הפיכות</strong>, {% equation %}L,R{% endequation %} (מלשון Left ו-Right) מסדרים {% equation %}n\times n{% endequation %} ו-{% equation %}m\times m{% endequation %}, כך ש-{% equation %}D=LAR{% endequation %} היא מטריצה "אלכסונית בערך". מה זה אומר? זו עדיין מטריצה מסדר {% equation %}n\times m{% endequation %} ולכן אולי לא ריבועית בכלל, אבל הכניסות היחידות שלה שעשויות להיות שונות מאפס הן הכניסות {% equation %}D_{11},D_{22},\dots{% endequation %}, והכניסות הללו גם מחלקות כל אחת את הבאה אחריה. והמשפט הזה נכון מעל שדות, כמו הרציונליים למשל, אבל גם מעל <strong>תחומים ראשיים</strong> כלליים - ולמי שלא מכיר, לא חשוב; מה שחשוב הוא רק שהשלמים הם תחום ראשי ולכן המשפט תקף לגביו. {% equation %}D{% endequation %} הזו נקראת "צורת סמית" של {% equation %}A{% endequation %}.

איך זה עוזר לנו לפתור משוואות? פשוט מאוד. נניח שאנחנו רוצים לפתור את מערכת המשוואות שמוגדרת על ידי {% equation %}Ax=b{% endequation %}. אז זה תרגיל קל מאוד באלגברה לינארית להוכיח שאם נגדיר {% equation %}c=Lb{% endequation %} ונמצא פתרון למערכת המשוואות {% equation %}Dy=c{% endequation %}, אז פתרון למערכת המקורית נתון על ידי {% equation %}x=Ry{% endequation %}. נסו להוכיח! כעת, מכיוון ש-D כל כך פשוטה, אפשר בלי קושי למצוא את הפתרון עבורה, ואז לחזור ולקבל פתרון למערכת המקורית. עכשיו, אם יש לנו מערכת שיש לה יותר מפתרון אחד, אפשר למצוא <strong>פתרון כללי</strong> למערכת ש-D מגדירה, ולקבל ממנו בחזרה פתרון כללי למערכת ש-A מגדירה.

רק בעיה "קטנה" נותרה - איך מוצאים את צורת סמית של מטריצה? ובכן, אם היינו פוסט אלגוריתמי, הייתי אומר שזה מסובך ולא טריוויאלי (אבל גם לא אסון). אבל אנחנו לא - אנחנו פוסט על "איך פותרים תרגילים בעזרת מחשב" ואני בכוונה רוצה להציג כלים חזקים, אז בואו נדבר על הכלי שאני בדרך כלל משתמש בו לחישובים מתמטיים - <a href="http://www.sagemath.org/">Sage</a>. אם SymPy שהזכרתי קודם היא ספריה קטנה ונחמדה, Sage היא לוויתן כחול אדיר. היא ערב-רב של ספריות מתמטיות מסוגים שונים ומשונים שחברו להם יחדיו, ומוחבאים כולם מאחורי ממשק משותף ונוח ביותר, שהוא בבסיסו פייתון עם טיפ-טיפה שיפורים. זה אומר שמדובר על הורדה יחסית כבדה (כמעט ג'יגה) ושקשה לשלב את Sage בתוך תוכנות קלילות שאתם רוצים לכתוב, אבל לשימוש שנועד לעמוד בפני עצמו, או סתם לשימוש בהתמודדות עם בעיה מורכבת, אני נוהג להשתמש ב-Sage.

יש בעולם הגדול עוד כלים דומים, כמובן; כמה שמות מיידיים הם מתמטיקה, מייפל ומטלאב. היתרון המיידי של Sage עליהם הוא שהיא חופשית לשימוש (ואם השמטתי אזכור לכלי חופשי לשימוש נוסף - למשל Maxima - קרוב לודאי שזה כי Sage משתמשת בו).

טוב, אז איך נראה פתרון ב-Sage לבעיה הזו? הוא יהיה מורכב משני חלקים, שאני מפריד ביניהם ברווח. בחלק הראשון מוצאים פתרון כללי למערכת, ובחלק השני שוב עושים חיפוש כוח גס מטופש אחרי הפתרון שאנחנו רוצים, סתם כי לא היה לי כוח לכתוב משהו אלגנטי יותר:

<div class="code-block">
{% highlight python %}
t = var('t')
A = matrix(ZZ, [[1,1,1],[1,10,50]])
b = matrix(ZZ, [[100,500]]).transpose()
(D, L, R) = A.smith_form()
x = R*(D.solve_right(L*b) + matrix([[0,0,t]]).transpose())

val = 0
while true:
  ((a,),(b,),(c,)) = x.subs(t=val)
  if a &gt; 0 and b &gt; 0 and c &gt; 0:
    print &quot;x = %d, y = %d, z = %d&quot; % (a,b,c)
    break
  val *= -1
  if val &gt;= 0:
    val += 1
    {% endhighlight %}
</div>

החלק הראשון הוא המעניין כאן. אם נסתכל על x בסופו, זה מה שנראה:

<div class="code-block">
{% highlight python %}
[ 40*t - 3500]
[-49*t + 4400]
[   9*t - 800]
{% endhighlight %}
</div>

וזה בעצם הפתרון הכללי למערכת. מה עשיתי כדי למצוא אותו? פשוט מאוד. בשורה 1 הגדרתי את המשתנה שבו אשתמש בתור פרמטר, כמו שהגדרתי בצורה דומה משתנים ב-SymPy. בשורה השניה והשלישית הגדרתי את מערכת המשוואות שלי בעזרת מטריצות (גם וקטור עמודה הוא מטריצה). ה-ZZ שמופיע שם אומר שמדובר על מטריצות מעל השלמים. בשורה 4 מצאתי את צורת סמית (הפונקציה מחזירה גם את D וגם את L,R, כמובן). רק בשורה 5 יש סוג של קסם. מה שקורה פה הוא שקודם כל אני פותר את המשוואה {% equation %}Dy=Lb{% endequation %} שתיארתי קודם; עכשיו, בגלל הצורה של D, הפתרון של המשוואה הזו יהיה וקטור שהכניסה האחרונה בו היא 0, אבל בעצם גם כל ערך אחר בכניסה הזו היה עובד (למה? זו אולי השאלה הכי מאתגרת אליכם בפוסט; חשבו על ההגדרה של צורת סמית שנתתי קודם). לכן אני דוחף לשם את t, ואז כופל את הכל ב-R כדי לקבל את הפתרון הכללי למערכת המקורית.

מכאן רק נותר לי לחפש ערך של {% equation %}t{% endequation %} שנותן ערכים חיוביים הן ל-x, הן ל-y והן ל-z, אבל שימו לב שכל ערך שלם שאציב ב-t יתן לי פתרון שלם של המשוואה - בעצם מצאתי את כל הפתרונות השלמים, והשיטה הזו תעבוד גם באופן כללי. אני משאיר לכם לחשוב איך אפשר למצוא יותר ביעילות ערך של {% equation %}t{% endequation %} שיתן ערך חיובי לשלושת המשתנים - זה לא קשה וממש לא חייבים לערוך חיפוש ממצה אחריו כמו שאני עשיתי.

אם כן, הפוסט הזה היה קצת חריג - הרשיתי לעצמי להציג את פייתון ו-Sage, פשוט כי הם הכלים הראשונים שהייתי משתמש בהם כדי לפתור את הבעיה הזו; כלומר, אם לא היה אפשר לכתוב פתרון כוח גס ברובי שיעבוד. כלל האצבע שלי פשוט - אני תמיד כותב קודם כל פתרון כוח גס ברובי, ורק אם הוא נכשל בצורה מביכה (קורה הרבה, אבל לא הרבה כפי שאפשר היה לצפות) אני מאפטמז.