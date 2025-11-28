---
id: 3622
title: "כשחבורות ושדות מתנגשים"
date: 2018-05-07 23:06:42
layout: post
categories: 
  - אלגברה מופשטת
tags: 
  - תורת גלואה
---
סדרת הפוסטים שלי על אלגברה מופשטת מתקרבת אל אחת מנקודות השיא שלה - <strong>המשפט היסודי של תורת גלואה</strong>. זה לא מה שנעשה היום. מה שנעשה היום הוא את כל עבודת ההכנה שנדרשת עד שמגיעים למשפט הזה, ובפרט תהיה לנו הוכחה אחת שהיא הלב הטכני של כל הסיפור. יהיה בסדר; זו הוכחה טכנית אבל יש לה את האלגנטיות שלה ואפשר "להרגיש" באמצעותה למה הדברים עובדים. את ההוכחה עצמה אשמור לסוף, כי בעזרת המשפט שהיא מוכיחה נוכל לעשות דברים מעניינים שחבל להתאפק איתם. בפרט, נבין הרבה יותר טוב מה זו בכלל <strong>הרחבת גלואה </strong>שהזכרנו בחטף בפוסט הקודם.
<h2>מחבורה לשדה ומשדה לחבורה</h2>
בואו נזכיר על מה דיברנו בפעם הקודמת: הייתה לנו הרחבת שדות {% equation %}E/F{% endequation %} ודיברנו על {% equation %}\text{Aut}\left(E/F\right){% endequation %} - חבורת האוטומורפיזמים של {% equation %}E{% endequation %} ש<strong>משמרים</strong> את {% equation %}F{% endequation %}. כאן זה ש-{% equation %}\sigma\in\text{Aut}\left(E/F\right){% endequation %} "משמר" את {% equation %}F{% endequation %} פירושו ש-{% equation %}\sigma a=a{% endequation %} לכל {% equation %}a\in F{% endequation %} (להבדיל ממושג חלש יותר, {% equation %}\sigma\left(F\right)\subseteq F{% endequation %} שלא מונע מ-{% equation %}\sigma{% endequation %} לשנות איברים של {% equation %}F{% endequation %} אבל כן מונע ממנו להוציא דברים מגבולות {% equation %}F{% endequation %}). אמרנו גם ש-{% equation %}E/F{% endequation %} היא <strong>הרחבת גלואה</strong> אם {% equation %}\left[E:F\right]=\left|\text{Aut}\left(E/F\right)\right|{% endequation %} ובמקרה הזה אני מסמן את {% equation %}\text{Aut}\left(E/F\right){% endequation %} גם בסימון הנוסף {% equation %}\text{Gal}\left(E/F\right){% endequation %}.

דיברנו על התהליך שבו אנחנו מפיקים חבורה מתוך הרחבה. ליתר דיוק, בהינתן {% equation %}E{% endequation %}, אנחנו מפיקים תתי-חבורות של {% equation %}\text{Aut}\left(E\right){% endequation %} על ידי התבוננות על תתי-שדות של {% equation %}E{% endequation %}. מה שאנחנו רוצים לדבר עליו עכשיו הוא התהליך ההפוך: בהינתן תת-חבורה {% equation %}G{% endequation %} של {% equation %}\text{Aut}\left(E\right){% endequation %}, בואו נגדיר את {% equation %}F{% endequation %} להיות השדה שתת-החבורה הזו משמרת. כלומר, {% equation %}F\triangleq\left\{ a\in E\ |\ \sigma a=a,\forall\sigma\in G\right\} {% endequation %} (קל להוכיח שזה אכן שדה; זה נובע מכך ש-{% equation %}\sigma{% endequation %} הומומורפיזם של שדות). המשפט המרכזי לפוסט הזה, שאת ההוכחה שלו כאמור אני שומר לסוף הפוסט, הוא ש<strong>תמיד</strong> מתקיים {% equation %}\left[E:F\right]=\left|G\right|{% endequation %}. ה"תמיד" הזה עשוי להיות מבלבל; הרי ראינו שלא כל הרחבה היא הרחבת גלואה, אבל הכיוון השני "תמיד" עובד. ובכן, הנקודה היא שלא מובטח לנו ש<strong>כל</strong> תת-שדה של {% equation %}E{% endequation %} אכן יהיה בר הפקה בצורה שכזו; רק אם {% equation %}E/F{% endequation %} היא גלואה זה יעבוד.

בואו נראה מה המסקנות מהמשפט שהצגתי. ראשית, בואו נראה ש-{% equation %}\left|\text{Aut}\left(E/F\right)\right|\le\left[E:F\right]{% endequation %} תמיד, גם בהרחבה שאיננה גלואה. הרעיון הוא זה: אם {% equation %}G=\text{Aut}\left(E/F\right){% endequation %}, המשפט מבטיח לנו שמתקיים {% equation %}\left|G\right|=\left[E:K\right]{% endequation %} כאשר {% equation %}K{% endequation %} הוא השדה ש-{% equation %}G{% endequation %} משמרת. מה השדה הזה? ברור לנו שהוא <strong>מכיל</strong> את {% equation %}F{% endequation %}, מכיוון ש-{% equation %}G=\text{Aut}\left(E/F\right){% endequation %} ולכן על פי הגדרה משמרת את כל {% equation %}F{% endequation %}, אבל זה לא אומר שאין <strong>עוד</strong> איברים ש-{% equation %}G{% endequation %} משמרת. לכן באופן כללי {% equation %}F\subseteq K\subseteq E{% endequation %} ולכן

{% equation %}\left[E:F\right]=\left[E:K\right]\left[K:F\right]=\left|G\right|\left[K:F\right]{% endequation %} ומכאן ש-{% equation %}\left|\text{Aut}\left(E/F\right)\right|=\frac{\left[E:F\right]}{\left[K:F\right]}\le\left[E:F\right]{% endequation %} כמו שרצינו.

שנית, בואו נראה שכל הרחבה שמתקבלת מ-{% equation %}G{% endequation %} באופן שתיארתי היא <strong>כן</strong> הרחבת גלואה. כלומר: ניקח תת-חבורה {% equation %}G{% endequation %} של {% equation %}\text{Aut}\left(E\right){% endequation %}, ונגדיר את {% equation %}F{% endequation %} להיות השדה שהיא משמרת. אני טוען ש-{% equation %}\text{Aut}\left(E/F\right)=G{% endequation %}. אני כבר יודע כיוון אחד: {% equation %}G{% endequation %} בוודאי מוכלת ב-{% equation %}\text{Aut}\left(E/F\right){% endequation %}, כי היא חבורה של אוטומורפיזמים של {% equation %}E{% endequation %} שמשמרים את {% equation %}F{% endequation %}. השאלה היא למה אין אוטומורפיזמים כאלו גם מחוץ ל-{% equation %}G{% endequation %}. הנימוק הוא מאוד פשוט:

{% equation %}\left[E:F\right]=\left|G\right|\le\left|\text{Aut}\left(E/F\right)\right|\le\left[E:F\right]{% endequation %}

ולכן בפרט {% equation %}\left|G\right|=\left|\text{Aut}\left(E/F\right)\right|{% endequation %} . אינטואיטיבית, כל אוטומורפיזם של {% equation %}E{% endequation %} שמשמר את {% equation %}F{% endequation %} מכריח את המימד של {% equation %}E{% endequation %} מעל {% equation %}F{% endequation %} לגדול עוד ועוד; אבל המימד הזה חסום מלכתחילה על ידי הגודל של {% equation %}G{% endequation %} ש"יצרה" את {% equation %}F{% endequation %} מלכתחילה, על פי המשפט הקסום שאומר {% equation %}\left[E:F\right]=\left|G\right|{% endequation %}. מכיוון שקיבלנו פה ש-{% equation %}\left|\text{Aut}\left(E/F\right)\right|=\left[E:F\right]{% endequation %} המסקנה היא ש-{% equation %}E/F{% endequation %} היא הרחבת גלואה.

העסק הזה מבלבל, אז הנה תמצית:
<ul>
 	<li>אם נתונה לנו הרחבה {% equation %}E/F{% endequation %} ואנחנו מסיקים ממנה חבורת אוטומורפיזמים {% equation %}G{% endequation %} של {% equation %}E{% endequation %} שמשמרת את {% equation %}F{% endequation %}, זה <strong>לא</strong> מבטיח ש-{% equation %}E/F{% endequation %} גלואה.</li>
 	<li>אם נתונה לנו חבורת אוטומורפיזמים {% equation %}G{% endequation %} של {% equation %}E{% endequation %} ואנחנו מסיקים ממנה הרחבה {% equation %}E/F{% endequation %} כאשר {% equation %}F{% endequation %} השדה ש-{% equation %}G{% endequation %} משמרת, זה <strong>כן</strong> מבטיח ש-{% equation %}E/F{% endequation %} גלואה.</li>
</ul>
בפרט, הנקודה השניה נותנת לנו אפיון שקול חדש להרחבת גלואה: {% equation %}E/F{% endequation %} היא הרחבת גלואה אם ורק אם קיימת תת-חבורה של {% equation %}\text{Aut}\left(E\right){% endequation %} ש-{% equation %}F{% endequation %} הוא בדיוק השדה שהיא משמרת. אפשר אפילו לחדד את זה: {% equation %}E/F{% endequation %} גלואה אם ורק אם השדה שאותו {% equation %}\text{Aut}\left(E/F\right){% endequation %} משמרת הוא {% equation %}F{% endequation %}.

עכשיו, בואו נחזור למה ש<strong>עלול להיכשל</strong>. ראינו שייתכן שאני אקח הרחבה <strong>שאיננה גלואה</strong> {% equation %}E/F{% endequation %}, אגדיר {% equation %}G=\text{Aut}\left(E/F\right){% endequation %}, ואז אנסה "להפוך" את התהליך ולהגדיר את השדה ש-{% equation %}G{% endequation %} משמרת; באופן כללי אני עלול להיתקע עם שדה {% equation %}F\subseteq K\subseteq E{% endequation %} כך ש-{% equation %}F\ne K{% endequation %}. במילים אחרות, יוצא לנו ש-{% equation %}\text{Aut}\left(E/F\right)=\text{Aut}\left(E/K\right){% endequation %} למרות ש-{% equation %}F\ne K{% endequation %}; ההתאמה שלוקחת תת-שדה של {% equation %}E{% endequation %} ומחזירה חבורת אוטומורפיזמים איננה חד-חד-ערכית.

לעומת זאת, הכיוון ההפוך הוא <strong>כן</strong> חד-חד-ערכי. כלומר, אם {% equation %}G_{1}\ne G_{2}{% endequation %} הן שתי תת-חבורות שונות של {% equation %}\text{Aut}\left(E\right){% endequation %} ואנחנו בונים את {% equation %}F_{1},F_{2}{% endequation %} שהם השדות שהן משמרות, אז {% equation %}F_{1}\ne F_{2}{% endequation %}. למה? כי בואו נניח ש-{% equation %}F_{1}=F_{2}{% endequation %}. אז ממה שכבר ראינו: {% equation %}G_{1}=\text{Aut}\left(E/F_{1}\right)=\text{Aut}\left(E/F_{2}\right)=G_{2}{% endequation %}.

החד-חד ערכיות הזו היא הבסיס למשפט היסודי של תורת גלואה.
<h2>הרחבת גלואה ושדות פיצול של פולינומים ספרביליים</h2>
עכשיו אני רוצה לעבור למשפט שהוא התכל'ס של "מה זו הרחבת גלואה" - הרחבת גלואה היא שדה פיצול של פולינום ספרבילי. כזכור, פולינום ספרבילי הוא כזה שאין לו שורש מרובה, כלומר אפשר לכתוב אותו בתור {% equation %}\left(x-a_{1}\right)\left(x-a_{2}\right)\dots\left(x-a_{n}\right){% endequation %} כאשר כל ה-{% equation %}a_{i}{% endequation %}-ים שונים זה מזה - אלו הם ה<strong>שורשים</strong> של הפולינום. אז הרחבת גלואה היא מה שמתקבל כשלוקחים שדה, לוקחים פולינום תמים מעליו שהוא ספרבילי, ודוחפים לתוך השדה את <strong>כל</strong> השורשים שלו. בהכרח אלו יהיו כולם, ולא רק חלק; אם רק חלק מהשורשים התווספו לשדה, אז בהחלט ייתכן שלא יהיו לנו מספיק אוטומורפיזמים כדי שיתקיים הקריטריון של {% equation %}\left|\text{Aut}\left(E/F\right)\right|=\left[E:F\right]{% endequation %}. בשלב הזה כל הטענה הזו נשמעת מאוד חשודה; אני חושב שלראות את ההוכחה שלה, שכוללת רגע מפיל אסימון אחד לפחות, היא הדבר הכי מועיל לאינטואיציה כאן.

החלק ה<strong>פחות חשוד</strong> הוא הטענה ששדה הפיצול של פולינום ספרבילי הוא הרחבת גלואה. אני אציג את ההוכחה הזו בנפנוף ידיים כדי לעזור להתמקד ברעיון שלה; אל תלמדו אותה מהפוסט הזה ישירות למבחן אלא קחו ספר ושימו לב לנקודות העדינות בניסוח שלו שהן חשובות כשרוצים להוכיח פורמלית עד הסוף.

בואו ניקח {% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} שהוא ספרבילי ונגדיר את {% equation %}E{% endequation %} להיות שדה הפיצול שלו. אם {% equation %}E=F{% endequation %} אז סיימנו; {% equation %}\left|\text{Aut}\left(E/F\right)\right|=\left[E:F\right]=1{% endequation %}. אחרת, משדה הפיצול הזה ניקח איבר {% equation %}a\in E{% endequation %} כך ש-{% equation %}a\notin F{% endequation %} והוא שורש של {% equation %}p{% endequation %}: {% equation %}p\left(x\right)=0{% endequation %}, ונסתכל על ההרחבה {% equation %}F\left(a\right){% endequation %}. אנחנו יודעים ש-{% equation %}\left[E:F\right]=\left[E:F\left(a\right)\right]\left[F\left(a\right):F\right]{% endequation %}, ומכיוון ש-{% equation %}a\notin F{% endequation %} אני יודע ש-{% equation %}\left[F\left(a\right):F\right]&gt;1{% endequation %} כלומר {% equation %}\left[E:F\right]&lt;\left[E:F\left(a\right)\right]{% endequation %} וזה נותן לנו איזה שהוא פתח להוכחה אינדוקטיבית.

אנחנו יודעים ש-{% equation %}\left[F\left(a\right):F\right]{% endequation %} שווה למעלה של <strong>הפולינום המינימלי</strong> {% equation %}m_{a,F}\left(x\right){% endequation %} של {% equation %}a{% endequation %} מעל השדה {% equation %}F{% endequation %}; הפולינום הזה מחלק את {% equation %}p\left(x\right){% endequation %} שממנו התחלנו. זה פולינום שהמקדמים שלו כולם ב-{% equation %}F{% endequation %} ולכן כל אוטומורפיזם ב-{% equation %}\text{Aut}\left(E/F\right){% endequation %} מבצע פרמוטציה על השורשים שלו.

כמה שורשים יש לפולינום הזה? באופן כללי, לפולינום מעל שדה יש <strong>לכל היותר</strong> מספר שורשים ששווה למעלה שלו; במקרה שבו הפולינום ספרבילי מספר השורשים הוא <strong>בדיוק</strong> המעלה שלו. הפולינום המינימלי הוא ספרבילי כי הוא מחלק פולינום ספרבילי, ולכן זה מתקיים עבורו. כלומר, כשאני בא להגדיר אוטומורפיזם כלשהו ב-{% equation %}\text{Aut}\left(E/F\right){% endequation %} ואני ניצב בפני השאלה "לאן להעביר את {% equation %}a{% endequation %}?" יש לי בדיוק {% equation %}\text{deg}m_{a,F}=\left[F\left(a\right):F\right]{% endequation %} בחירות אפשריות.

מכיוון שכל איבר ב-{% equation %}F\left(a\right){% endequation %} ניתן לכתיבה בעזרת אברי {% equation %}F{% endequation %} ו-{% equation %}a{% endequation %}, הרי שמרגע שביצעתי את הבחירה לאן להעביר את {% equation %}a{% endequation %}, האוטומורפיזם שבניתי נקבע באופן יחיד על כל {% equation %}F\left(a\right){% endequation %}. עכשיו מגיע הרגע של נפנוף הידיים הפרוע: אני יכול להשתמש בהנחת האינדוקציה שלי (שלא ניסחתי במפורש כי כשננסה לנסח אותה במפורש נראה שהיא צריכה להיות קצת יותר מסובכת) כדי להראות ש-{% equation %}\left|\text{Aut}\left(E/F\left(a\right)\right)\right|=\left[E:F\left(a\right)\right]{% endequation %}. אפשר לחשוב על אוטומורפיזם שכזה על {% equation %}E{% endequation %} שמשמר את {% equation %}F\left(a\right){% endequation %} כאילו (נפנוף ידיים!) הוא ניתן להרחבה לאוטומורפיזם של {% equation %}E{% endequation %} שמשמר רק את {% equation %}F{% endequation %} על ידי כך שנגיד לאן {% equation %}a{% endequation %} צריך לעבור, ואנחנו יודעים שאנחנו יכולים להעביר את {% equation %}a{% endequation %} לכל שורש אחר של {% equation %}m_{a,F}{% endequation %} מבלי (נפנוף ידיים!) שיווצרו עם זה בעיות; כלומר, לכל אוטומורפיזם ב-{% equation %}\text{Aut}\left(E/F\left(a\right)\right){% endequation %} יש לנו {% equation %}\left[F\left(a\right):F\right]{% endequation %} דרכים שונות להרחיב אותו, ומכיוון ש-{% equation %}\left|\text{Aut}\left(E/F\left(a\right)\right)\right|=\left[E:F\left(a\right)\right]{% endequation %} אני אקבל ש-{% equation %}\left|\text{Aut}\left(E/F\right)\right|=\left[E:F\left(a\right)\right]\left[F\left(a\right):F\right]=\left[E:F\right]{% endequation %} כפי שרציתי.

ההוכחה הזו, אולי שמתם לב, קצת מנפנפת בידיים, אבל היא מציגה בדיוק את הסיבה שבגללה ההרחבה הופכת להיות גלואה: אפשר לחשוב על שדה פיצול בתור משהו שמתקבל באמצעות סדרה של הרחבות פשוטות. ה"קפיצה במימד של ההרחבה" שאני מקבל עם כל הרחבה פשוטה שכזו מתאימה בדיוק לחופש התמרון שיש לי כשאני בא להגדיר אוטומורפיזם וצריך להחליט מה לעשות עם האיבר שבאמצעותו הרחבתי את אותה הרחבה פשוטה. אי-ספרביליות מקלקלת את כל זה בכך שהיא מקטינה את חופש הבחירה הזה שלי (כי יש פחות שורשים לבחור מהם) למרות שהקפצה במימד של ההרחבה נותרת זהה (כי הקפיצה במימד של ההרחבה תמיד מתאימה למעלה של הפולינום המינימלי, גם אם הוא לא ספרבילי; זכרו שראינו בפוסט הקודם דוגמא מוזרה של פולינום אי פריק שאינו ספרבילי שדרשה מאיתנו ללכת לשדה אינסופי ממציין {% equation %}p{% endequation %} ).

עכשיו בואו נעבור לדבר על הכיוון השני של המשפט, שהוא מוזר יותר: אם {% equation %}E/F{% endequation %} הרחבת גלואה אז <strong>בודאות</strong> {% equation %}E/F{% endequation %} היא שדה פיצול של פולינום ספרבילי. מה זה פה? מאיפה בכלל מתחילים? איך מוצאים את הפולינום הזה?

ובכן, האינטואיציה של <strong>זה</strong> היא דווקא די קלה. אם {% equation %}E/F{% endequation %} היא הרחבת שדות סופית, אז אנחנו כבר יודעים ש-{% equation %}E=F\left(a_{1},\dots,a_{n}\right){% endequation %}; זה היה <a href="http://gadial.net/2018/04/09/simple_finite_algebraic_field_extensions/">אחד הדברים הראשונים שראינו</a> על הרחבת שדות. לכל {% equation %}a_{i}{% endequation %} כזה, אני מסמן את הפולינום המינימלי שלו מעל {% equation %}F{% endequation %} ב-{% equation %}m_{a_{i},F}\left(x\right){% endequation %}. אם אני אקח עכשיו את פולינום המכפלה {% equation %}\prod_{i=1}^{n}m_{a_{i},F}\left(x\right){% endequation %} אני אקבל פולינום יחיד ש-{% equation %}a_{1},\dots,a_{n}{% endequation %} נמנים על השורשים שלו, ואז אני אקח את שדה הפיצול שלו ואקבל בין היתר את {% equation %}a_{1},\dots,a_{n}{% endequation %} בפנים. אבל עם הרעיון הנחמד הזה יש שתי בעיות:
<ul>
 	<li>הפולינום שאקבל לא בהכרח יהיה ספרבילי.</li>
 	<li>לא ברור למה בשדה הפיצול שלו לא יהיו איברים <strong>נוספים</strong>, שאינם דווקא ב-{% equation %}E{% endequation %}.</li>
</ul>
הפתרון לשני אלו טמון במשפט המאוד מפתיע (לטעמי) הבא: אם {% equation %}E/F{% endequation %} היא הרחבת גלואה ו-{% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} הוא פולינום <strong>אי פריק</strong> מעל {% equation %}F{% endequation %} שיש לו שורש ב-{% equation %}E{% endequation %}, אז קורים שני דברים:
<ol>
 	<li>{% equation %}p\left(x\right){% endequation %} ספרבילי.</li>
 	<li>{% equation %}p\left(x\right){% endequation %} מתפרק מעל {% equation %}E{% endequation %} לגורמים לינאריים, כלומר <strong>כל</strong> השורשים של {% equation %}p\left(x\right){% endequation %} (ולא רק אחד) נמצאים ב-{% equation %}E{% endequation %}.</li>
</ol>
זו אולי התכונה שהכי מבהירה לי, אינטואיטיבית, מה ה"כוח" של הרחבת גלואה - אם פולינום כלשהו מעל {% equation %}F{% endequation %} שאין לו שורשים בכלל ב-{% equation %}F{% endequation %} מחליט לעשות לנו טובה ולתת לנו איזה שורש מסכן אחד ב-{% equation %}E{% endequation %}, אז זהו, המשחק נגמר - אוטומטית כולם יהיו ב-{% equation %}E{% endequation %}. הרחבת גלואה היא כזו שמבטיחה לנו ש"לא יהיו חסרים שורשים לאף פולינום". והאופן שבו אני אוכיח את זה יפיל לכולנו (בתקווה) את האסימון בנוגע לשאלה <strong>למה </strong>הקסם הזה קורה.

בואו נסמן {% equation %}G=\text{Gal}\left(E/F\right){% endequation %}. ניקח {% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} שהוא אי-פריק מעל {% equation %}F{% endequation %} אבל יש לו שורש {% equation %}a\in E{% endequation %}, ועכשיו נפעיל על השורש הזה את כל האיברים של {% equation %}G{% endequation %}, כלומר נסתכל על הקבוצה {% equation %}\left\{ \sigma a\ |\ \sigma\in G\right\} {% endequation %}. האיברים הללו נקראים <strong>צמודי הגלואה</strong> של {% equation %}a{% endequation %}. זו קבוצה של איברים של {% equation %}E{% endequation %} שכולם שורשים של {% equation %}p\left(x\right){% endequation %}; מן הסתם, מה שאנחנו מקווים להגיד הוא שאלו הם <strong>כל</strong> השורשים של {% equation %}p\left(x\right){% endequation %}. בואו נסמן את אברי הקבוצה הזו ב-{% equation %}a_{1},a_{2},\dots,a_{k}{% endequation %} (כשאנחנו כותבים כל איבר של הקבוצה רק פעם אחת, אפילו אם הוא התקבל בכמה דרכים שונות).

עכשיו בואו נגדיר פולינום <strong>חדש</strong> שהוא ספרבילי ואלו בדיוק השורשים שלו:

{% equation %}q\left(x\right)=\left(x-a_{1}\right)\left(x-a_{2}\right)\dots\left(x-a_{k}\right){% endequation %}

אני טוען ש-{% equation %}p\left(x\right)=q\left(x\right){% endequation %}. אבל למה? כאן מגיע השפן שאני שולף מהכובע - המהות של המהות של הסיבה שבגללה תורת גלואה עובדת לדעתי - ואפשר לתמצת למשפט המחץ <strong>כי מקדמים של פולינום מתוקן ספרבילי הם פונקציות סימטריות בשורשים שלו</strong>.

בואו נסביר את זה.

אם יש לנו פולינום ממעלה שניה עם השורשים {% equation %}a_{1},a_{2}{% endequation %} אז קל לבדוק, על ידי כך שפותחים סוגריים במפורש, ש-{% equation %}\left(x-a_{1}\right)\left(x-a_{2}\right)=x^{2}-\left(a_{1}+a_{2}\right)+a_{1}a_{2}{% endequation %}. כלומר, המקדם החופשי הוא מכפלה של השורשים והמקדם שאחריו הוא סכום שלהם. זה נקרא <strong>נוסחאות וייטה</strong>, אבל אפשר להפעיל אותן בצורה דומה על פולינום ממעלה כלשהי, עם מספר כלשהו של שורשים. השורה התחתונה תהיה תמיד זהה: המקדם שאחרי המקדם המוביל הוא מינוס של סכום כל השורשים; המקדם שאחריו הוא סכום כל המכפלות של שני שורשים, זה שאחריו הוא מינוס הסכום של כל המכפלות של שלושה שורשים וכן הלאה. הנה דוגמא עבור פולינום ממעלה שלישית עם שורשים {% equation %}a_{1},a_{2},a_{3}{% endequation %}:

{% equation %}x^{3}-\left(a_{1}+a_{2}+a_{3}\right)+\left(a_{1}a_{2}+a_{1}a_{3}+a_{2}a_{3}\right)-a_{1}a_{2}a_{3}{% endequation %}

מה זו "פונקציה סימטרית"? {% equation %}f\left(x_{1},\dots,x_{n}\right){% endequation %} היא סימטרית אם לכל זוג אינדקסים {% equation %}i\ne j{% endequation %}, והשמה לפונקציה, אם נחליף את הערכים שבמקומות {% equation %}i,j{% endequation %} הפלט של הפונקציה לא ישתנה. כלומר, {% equation %}f\left(a_{1},\dots,a_{i},\dots,a_{j},\dots,a_{n}\right)=f\left(a_{1},\dots,a_{j},\dots,a_{i},\dots,a_{n}\right){% endequation %}. אם אפשר להחליף ערכים עבור <strong>זוג</strong> אינדקסים וששום דבר לא ישתנה, אפשר לעשות את זה כמה פעמים שרוצים, ומכיוון שכל תמורה ניתן להציג בתור הרכבה של חילופים של זוגות של איברים, נקבל שפונקציה סימטרית היא כזו שהפלט שלה נשאר קבוע תחת תמורות של אברי הקלט; במילים אחרות, הפלט תלוי רק בזהות של הקלטים, לא בסדר שלהם.

קל לראות שמקדמי הפולינום שלנו הם פונקציות סימטריות שכאלו בשורשים. מה שאומר שאם אנחנו מפעילים תמורה {% equation %}\sigma{% endequation %} כלשהי על השורשים, זה לא משנה את המקדמים של הפולינום. מה זה אומר? שלכל {% equation %}\sigma\in\text{Gal}\left(E/F\right){% endequation %}, המקדמים של {% equation %}q\left(x\right){% endequation %} משתמרים על ידי {% equation %}\sigma{% endequation %}. אבל מה המשמעות של זה ש-{% equation %}E/F{% endequation %} היא הרחבת גלואה? שאם איבר כלשהו משתמר על ידי <strong>כל</strong> האיברים של {% equation %}\text{Gal}\left(E/F\right){% endequation %}, זה אומר שהוא שייך ל-{% equation %}F{% endequation %}. לכן <strong>כל</strong> המקדמים של {% equation %}q\left(x\right){% endequation %} שייכים ל-{% equation %}F{% endequation %} ולכן {% equation %}q\left(x\right)\in F\left[x\right]{% endequation %}.

עכשיו, מה קורה? {% equation %}p\left(x\right){% endequation %} היה פולינום אי-פריק, אבל מצד שני כל שורש של {% equation %}q\left(x\right){% endequation %} הוא גם שורש שלו, ולכן {% equation %}q\left(x\right){% endequation %} מחלק אותו בלי שארית, מה שמכריח את {% equation %}q\left(x\right)=p\left(x\right){% endequation %}. קיבלנו ש-{% equation %}p\left(x\right){% endequation %} הוא פולינום ספרבילי (כי בנינו את {% equation %}q\left(x\right){% endequation %} להיות ספרבילי) שכל השורשים שלו הם ב-{% equation %}E{% endequation %} (כי בנינו את {% equation %}q\left(x\right){% endequation %} רק מהשורשים של {% equation %}p\left(x\right){% endequation %} שהיו שייכים ל-{% equation %}E{% endequation %}). זה מסיים את הטענה המרכזית שלי כאן.

אם כן, ראינו שאם {% equation %}E/F{% endequation %} גלואה ו-{% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} אי-פריק מעל {% equation %}F{% endequation %} ועם שורש אחד ב-{% equation %}E{% endequation %} אז כל השורשים שלו ב-{% equation %}E{% endequation %} והוא ספרבילי. עם הידע הזה בואו נחזור לכך ש-{% equation %}E=F\left(a_{1},\dots,a_{n}\right){% endequation %} ואני רוצה להציג את {% equation %}E{% endequation %} כשדה פיצול של פולינום ספרבילי מעל {% equation %}F{% endequation %}. אני לוקח את הפולינומים המינימליים {% equation %}m_{a_{i},F}\left(x\right){% endequation %} של היוצרים של {% equation %}E{% endequation %}. הם אי-פריקים מעל {% equation %}F{% endequation %} כי פולינום מינימלי הוא תמיד אי-פריק. כמו כן, יש להם שורש ב-{% equation %}E{% endequation %} כי לכל {% equation %}i{% endequation %} אנחנו יודעים ש-{% equation %}a_{i}\in E{% endequation %} הוא שורש של {% equation %}m_{F,a_{i}}{% endequation %} (זו המהות של הפולינום הזה). לכן כל השורשים של הפולינום המינימלי הזה שייכים ל-{% equation %}E{% endequation %}. לכן אם נגדיר פולינום שהוא המכפלה של כל הפולינומים המינימליים הללו, שדה הפיצול שלו יהיה בדיוק {% equation %}E{% endequation %}.

הבעיה היחידה שנותרה היא שהמכפלה הזו לאו דווקא תהיה ספרבילית. מכיוון שכל הפולינומים המינימליים ספרביליים (כי כאמור - ראינו שאי פריק מעל {% equation %}F{% endequation %} ובעל שורש ב-{% equation %}E{% endequation %} גורר ספרבילי) הדרך היחידה שבה המכפלה לא תהיה ספרבילית היא אם יש שני פולינומים מינימליים שיש להם שורש משותף. אבל ראינו לפני רגע איך שורש אחד <strong>כלשהו</strong> של הפולינומים הללו קובע אותם במפורש (בהינתן השורש הזה, הפולינום שהוא קובע הוא זה ששורשיו הם בדיוק צמודי הגלואה של השורש). לכן אם יש לשני פולינומים מינימליים שורש משותף הם זהים, ואפשר פשוט לא לקחת אחד מהם למכפלה. בצורה הזו מובטח שנקבל פולינום ספרבילי ששדה הפיצול שלו הוא {% equation %}E{% endequation %}.

ראינו פה שתי תכונות חדשות ומעניינות של פולינומים אי-פריקים בהרחבת גלואה. התכונות הללו הן מוטביציה לשתי הגדרות של תכונות כלליות של הרחבות:
<ul>
 	<li>הרחבה {% equation %}E/F{% endequation %} היא <strong>נורמלית</strong> אם לכל פולינום אי-פריק {% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} או שאין לו שורש ב-{% equation %}E{% endequation %}, או שכל השורשים שלו הם ב-{% equation %}E{% endequation %}.</li>
 	<li>הרחבה {% equation %}E/F{% endequation %} היא <strong>ספרבילית</strong> אם לכל {% equation %}a\in E{% endequation %}, הפולינום המינימלי של {% equation %}a{% endequation %} מעל {% equation %}F{% endequation %} הוא ספרבילי.</li>
</ul>
ראינו זה עתה שהרחבת גלואה היא נורמלית וספרבילית - אלו התכונות שניצלנו כדי להוכיח שהרחבת גלואה היא שדה פיצול של פולינום ספרבילי. אם כן, יש לנו שרשרת של גרירות: "גלואה" גורר "נורמלית וספרבילית" וזה גורר "שדה פיצול של פולינום ספרבילי" שגורר, כפי שראינו קודם, "גלואה". לכן כל אלו שקולים. נוסיף לזה את הטענה שראינו קודם על השדה ש-{% equation %}\text{Aut}\left(E/F\right){% endequation %} משמרת, וקיבלנו ארבע הגדרות שקולות ל"מתי {% equation %}E/F{% endequation %} היא הרחבת גלואה"
<ol>
 	<li>אם {% equation %}\left[E:F\right]=\left|\text{Aut}\left(E/F\right)\right|{% endequation %}.</li>
 	<li>אם השדה ש-{% equation %}\text{Aut}\left(E/F\right){% endequation %} משמרת הוא {% equation %}F{% endequation %}.</li>
 	<li>אם {% equation %}E/F{% endequation %} הרחבה נורמלית וספרבילית.</li>
 	<li>אם {% equation %}E{% endequation %} הוא שדה פיצול של פולינום ספרבילי מעל {% equation %}F{% endequation %}.</li>
</ol>
<h2>הוכחת המשפט ה"קשה"</h2>
חזרה אל החוב שלי מתחילת הפוסט. כזכור, אני רוצה להוכיח שאם {% equation %}E{% endequation %} שדה ו-{% equation %}G{% endequation %} תת-חבורה של {% equation %}\text{Aut}\left(E\right){% endequation %} ואני מגדיר את {% equation %}F{% endequation %} להיות השדה ש-{% equation %}G{% endequation %} משמרת, אז {% equation %}\left[E:F\right]=\left|G\right|{% endequation %}. את ההוכחה אפשר לחלק לשני חלקים ששניהם דומים באופיים: מניחים ש-{% equation %}\left[E:F\right]{% endequation %} גדול או קטן מ-{% equation %}\left|G\right|{% endequation %}, ובכל אחד מהמקרים הללו משתמשים באלגברה לינארית בסיסית ובתכונות הנחמדות של אוטומורפיזמים כדי ליצור איבר שהוא "טוב מכדי להתקיים". התכונה הרלוונטית לי מאלגברה לינארית היא זו: אם יש לי מערכת הומוגנית של {% equation %}k{% endequation %} משוואות לינאריות ב-{% equation %}n{% endequation %} נעלמים כך ש-{% equation %}k&lt;n{% endequation %}, אז תמיד קיים לה פתרון לא טריוויאלי ("מערכת הומוגנית" היא מערכת מהצורה {% equation %}Ax=0{% endequation %}, ו"פתרון לא טריוויאלי" הוא כזה שבו לא כל המשתנים מקבלים 0).

עוד תכונה שאזדקק לה היא שאוטומורפיזמים של {% equation %}E{% endequation %} הם <strong>בלתי תלויים לינארית</strong> מעל {% equation %}E{% endequation %}. למה אני מתכוון? אם {% equation %}\sigma_{1},\dots,\sigma_{n}{% endequation %} הם אוטומורפיזמים כלשהם של {% equation %}E{% endequation %} אז לא קיים צירוף לינארי לא טריוויאלי שלהם שהוא פונקציית האפס, כלומר אם {% equation %}a_{1}\sigma_{1}\left(x\right)+\dots+a_{n}\sigma_{n}\left(x\right)=0{% endequation %} לכל {% equation %}x\in E{% endequation %}, אז {% equation %}a_{1}=\dots=a_{n}{% endequation %}.

כדי להוכיח את התכונה הזו נניח בשלילה שיש צירוף לינארי לא טריוויאלי שכזה. בלי הגבלת הכלליות אפשר להניח ש-{% equation %}a_{1},\dots,a_{m}{% endequation %} הם המקדמים ששונים מאפס ופשוט לשכוח מהאחרים. יותר מכך - אפשר להניח ש-{% equation %}m{% endequation %} הוא המספר המינימלי שעבורו קיים צירוף לינארי לא טריוויאלי שכזה, וש-{% equation %}m&gt;1{% endequation %} (כי {% equation %}a_{1}\sigma_{1}{% endequation %} הוא אוטומורפיזם ולכן בוודאי שלא פונקציית האפס). התעלול עכשיו יהיה לייצר צירוף לינארי לא טריוויאלי מתאפס <strong>קטן יותר</strong>. אני אקח את

{% equation %}a_{1}\sigma_{1}\left(x\right)+\dots+a_{m}\sigma_{m}\left(x\right)=0{% endequation %}

ועכשיו אני רוצה "למחוק" מהצירוף הזה את {% equation %}\sigma_{m}{% endequation %} תוך שאני משאיר לכל הפחות את {% equation %}\sigma_{1}{% endequation %}. לשם כך אני צריך איכשהו להבדיל בין שני אלו; מכיוון שהם פונקציות, אז העובדה שהם שונים מעידה על כך שקיים לפחות {% equation %}x_{0}{% endequation %} אחד כך ש-{% equation %}\sigma_{1}\left(x_{0}\right)\ne\sigma_{m}\left(x_{0}\right){% endequation %}. בהכרח {% equation %}x_{0}\ne0{% endequation %} אחרת שניהם היו מחזירים עליו 0. אם הצירוף הלינארי שלעיל נכון לכל {% equation %}x\in E{% endequation %}, הוא נכון בפרט עבור {% equation %}x_{0}\cdot y{% endequation %} כאשר {% equation %}y\in E{% endequation %} איבר כלשהו. לכן אפשר לכתוב:

{% equation %}a_{1}\sigma_{1}\left(x_{0}y\right)+\dots+a_{m}\sigma_{m}\left(x_{0}y\right)=0{% endequation %}

ותוך שימוש בכך שה-{% equation %}\sigma{% endequation %}-ות הן הומומורפיזמים:

{% equation %}a_{1}\sigma_{1}\left(x_{0}\right)\sigma_{1}\left(y\right)+\dots+a_{m}\sigma_{m}\left(x_{0}\right)\sigma_{m}\left(y\right)=0{% endequation %}

עכשיו ניקח את המשוואה שהתחלנו ממנה, ונכפול את כולה ב-{% equation %}\sigma_{m}\left(x_{0}\right){% endequation %}. נקבל:

{% equation %}a_{1}\sigma_{m}\left(x_{0}\right)\sigma_{1}\left(y\right)+\dots+a_{m}\sigma_{m}\left(x_{0}\right)\sigma_{m}\left(y\right)=0{% endequation %}

ועכשיו נחסר את המשוואה הזו שקיבלנו מהמשוואה שקיבלנו לפני רגע. נקבל:

{% equation %}a_{1}\left(\sigma_{1}\left(x_{0}\right)-\sigma_{m}\left(x_{0}\right)\right)\sigma_{1}\left(y\right)+\dots+a_{m-1}\left(\sigma_{m-1}\left(x_{0}\right)-\sigma_{m}\left(x_{0}\right)\right)\sigma_{m-1}\left(y\right)=0{% endequation %}

מה קיבלנו פה? צירוף לינארי של {% equation %}m-1{% endequation %} איברים לכל היותר ששווה גם הוא אפס לכל {% equation %}y\in E{% endequation %}. לא כל המקדמים של הצירוף הזה הם אפס, כי {% equation %}a_{1}\left(\sigma_{1}\left(x_{0}\right)-\sigma_{m}\left(x_{0}\right)\right)\ne0{% endequation %}. זו סתירה להנחה שלנו ש-{% equation %}m{% endequation %} היה מינימלי, מה שמוכיח שכל ה-{% equation %}\sigma{% endequation %}-ות הן בלתי תלויות לינארית מעל {% equation %}E{% endequation %}.

עכשיו, משאני מצוייד בידע הזה, אפשר סוף סוף להוכיח ש-{% equation %}\left[E:F\right]=\left|G\right|{% endequation %}. נסמן {% equation %}\left|G\right|=n{% endequation %} (כלומר {% equation %}G=\left\{ \sigma_{1},\sigma_{2},\dots,\sigma_{n}\right\} {% endequation %}), ונטפל בנפרד במקרים של {% equation %}\left[E:F\right]&lt;n{% endequation %} ו-{% equation %}\left[E:F\right]&gt;n{% endequation %}. נתחיל מהראשון. במקרה הראשון, אסמן {% equation %}k=\left[E:F\right]{% endequation %} וניקח בסיס {% equation %}a_{1},\dots,a_{k}\in E{% endequation %} ל-{% equation %}E{% endequation %} מעל {% equation %}F{% endequation %}. עכשיו אשתמש בדברים הללו כדי ליצור מערכת משוואות לינארית הומוגנית של {% equation %}k{% endequation %} משוואות ב-{% equation %}n{% endequation %} נעלמים - ומכיוון ש-{% equation %}k&lt;n{% endequation %} אז כפי שאמרתי לעיל, יהיה לה פתרון לא טריוויאלי:

{% equation %}\sigma_{1}\left(a_{1}\right)x_{1}+\dots+\sigma_{n}\left(a_{1}\right)x_{n}=0{% endequation %}

{% equation %}\vdots{% endequation %}

{% equation %}\sigma_{1}\left(a_{k}\right)x_{1}+\dots+\sigma_{n}\left(a_{k}\right)x_{n}=0{% endequation %}

בואו נסמן את הפתרון הזה ב-{% equation %}\beta_{1},\dots,\beta_{n}\in E{% endequation %}. אני ארצה להוכיח שמתקיים {% equation %}\beta_{1}\sigma_{1}+\dots+\beta_{n}\sigma_{n}=0{% endequation %}, מה שעומד בסתירה לכך שראינו שאוטומורפיזמים הם בלתי תלויים לינארית.

כדי להראות את השוויון הזה, אני צריך איכשהו להראות ש-

{% equation %}\beta_{1}\sigma_{1}\left(\alpha\right)+\dots+\beta_{n}\sigma_{n}\left(\alpha\right)=0{% endequation %}

<strong>לכל</strong> {% equation %}\alpha\in E{% endequation %}. כרגע יש לי את השוויון הזה, אבל לא לכל {% equation %}\alpha{% endequation %} אלא רק לאיברים {% equation %}a_{1},\dots,a_{n}{% endequation %}. מצד אחד, זה לא מספיק; מצד שני, אלו לא איברים שרירותיים של {% equation %}E{% endequation %} אלא <strong>בסיס</strong> ל-{% equation %}E{% endequation %}, מה שאומר שאני יכול לכתוב

{% equation %}\alpha=\lambda_{1}a_{1}+\dots+\lambda_{k}a_{k}{% endequation %}

עבור {% equation %}\lambda_{1},\dots,\lambda_{k}\in F{% endequation %}. כאן נכנס לתמונה הקלף המנצח שלי: המקדמים הללו לא סתם שייכים ל-{% equation %}E{% endequation %} אלא ל-{% equation %}F{% endequation %}. מי זה {% equation %}F{% endequation %}? אולי הלכנו לאיבוד בסבך המשוואות, אבל {% equation %}F{% endequation %} <strong>הוגדר</strong> בתור מה שכל אברי החבורה {% equation %}G{% endequation %} משמרים. כלומר, {% equation %}\sigma_{i}\left(\lambda_{j}\right)=\lambda_{j}{% endequation %} לכל {% equation %}1\le i\le n{% endequation %} ו-{% equation %}1\le j\le k{% endequation %}.

על כן, אם אכפול את המשוואה הראשונה ב-{% equation %}\lambda_{1}{% endequation %}, את השניה ב-{% equation %}\lambda_{2}{% endequation %} וכן הלאה, אני אקבל:

{% equation %}\sigma_{1}\left(\lambda_{1}a_{1}\right)\beta_{1}+\dots+\sigma_{n}\left(\lambda_{1}a_{1}\right)\beta_{n}=0{% endequation %}

{% equation %}\vdots{% endequation %}

{% equation %}\sigma_{1}\left(\lambda_{k}a_{k}\right)\beta_{1}+\dots+\sigma_{n}\left(\lambda_{k}a_{k}\right)\beta_{n}=0{% endequation %}

ועכשיו נחבר את כל המשוואות יחד, ונקבל את {% equation %}\beta_{1}\sigma_{1}\left(\alpha\right)+\dots+\beta_{n}\sigma_{n}\left(\alpha\right)=0{% endequation %} שלנו. הגענו לסתירה עבור המקרה {% equation %}\left[E:F\right]&lt;n{% endequation %}, תוך שאנו מסתמכים חזק על כך ש-{% equation %}F{% endequation %} הוא השדה ש-{% equation %}G{% endequation %} משמרת וש-{% equation %}G{% endequation %} היא קבוצת אוטומורפיזמים. עם זאת, שימו לב ש<strong>לא</strong> השתמשתי עדיין בכלל בכך ש-{% equation %}G{% endequation %} חבורה.

אם כן, קדימה אל המקרה {% equation %}\left[E:F\right]&gt;n{% endequation %} שאיתו נסיים!

במקרה הזה פחות חשוב לנו מה המימד המדויק {% equation %}\left[E:F\right]{% endequation %} אלא רק שאנחנו מסוגלים למצוא {% equation %}n+1{% endequation %} איברים של {% equation %}E{% endequation %} שהם בלתי תלויים לינארית מעל {% equation %}F{% endequation %}. נסמן אותם {% equation %}a_{1},\dots,a_{n+1}{% endequation %}. נבנה עכשיו מערכת של {% equation %}n{% endequation %} משוואות ב-{% equation %}n+1{% endequation %} נעלמים, בצורה טיפה שונה ממה שהיה קודם:

{% equation %}\sigma_{1}\left(a_{1}\right)x_{1}+\dots+\sigma_{1}\left(a_{n+1}\right)x_{n+1}{% endequation %}

{% equation %}\vdots{% endequation %}

{% equation %}\sigma_{n}\left(a_{1}\right)x_{1}+\dots+\sigma_{n}\left(a_{n+1}\right)x_{n+1}{% endequation %}

קודם כל משוואה הוקדשה ל<strong>איבר בסיס</strong> אחד; הפעם כל משוואה מוקדשת ל<strong>אוטומורפיזם</strong> אחד. כמקודם, המסקנה היא אותה מסקנה: יש לנו {% equation %}\beta_{1},\dots,\beta_{n+1}{% endequation %} מעל {% equation %}E{% endequation %} שהם פתרון לא טריוויאלי של המשוואה. אבל מה הסתירה שננסה להגיע אליה עכשיו?

כמו שהיה במקרה של אי-התלות של האוטומורפיזמים, גם כאן אני רוצה להגיע לסתירה מסוג "נתחיל עם צירוף לינארי עם מספר מינימלי של מקדמים שונה מאפס, ואז נקטין את מספר המקדמים באחד". כאן המקדמים הם ה-{% equation %}\beta{% endequation %}-ים. לא סתם ניקח פתרון אקראי של המשוואה, אלא נבחר אותו בחוכמה כך שמספר ה-{% equation %}\beta{% endequation %}-ים השונים מאפס בפתרון הוא מינימלי. אפשר גם להניח שה-{% equation %}\beta{% endequation %}-ים השונים מאפס הם {% equation %}\beta_{1},\dots,\beta_{k}{% endequation %} (אולי צריך למספר מחדש איברים בשביל זה). וחוץ מזה, אפשר גם לחלק את כל המשוואות ב-{% equation %}\beta_{k}{% endequation %}, אז אפשר להניח ש-{% equation %}\beta_{k}=1{% endequation %}. <strong>וחוץ מזה</strong> (תאמינו לי שהכל הכרחי) אני גם יודע בודאות שאחד מה-{% equation %}\beta{% endequation %}-ים לא שייך ל-{% equation %}F{% endequation %}. קחו שניה ותנסו לחשוב למה. אסביר בשורה הבאה.

מכיוון ש-{% equation %}G{% endequation %} חבורה, היא כוללת את אוטומורפיזם הזהות. אז אחת מהמשוואות שראינו היא פשוט המשוואה {% equation %}a_{1}\beta_{1}+\dots+a_{n+1}\beta_{n+1}=0{% endequation %}. אם כל ה-{% equation %}\beta{% endequation %}-ים היו שייכים ל-{% equation %}F{% endequation %}, אז היינו מקבלים צירוף לינארי לא טריוויאלי של האיברים הבלתי תלויים לינארית {% equation %}a_{1},\dots,a_{n+1}{% endequation %}. המסקנה אם כן היא ש-{% equation %}\beta{% endequation %} כלשהו אינו ב-{% equation %}F{% endequation %}, וזה הדבר המרכזי שנשחק עליו. את ה-{% equation %}\beta{% endequation %} בר המזל נסמן ב-{% equation %}\beta_{1}{% endequation %} - שוב, אפשר למספר מחדש כדי להבטיח את זה.

וכעת, לאקשן.

כל משוואה לעיל הוקדשה לאוטומורפיזם אחר. אחרי שנציב את ה-{% equation %}\beta{% endequation %}-ים, נקבל משוואות שנראות ככה:

{% equation %}\sigma_{i}\left(a_{1}\right)\beta_{1}+\dots+\sigma_{i}\left(a_{k-1}\right)\beta_{k-1}+\sigma_{i}\left(a_{k}\right)=0{% endequation %}

מכיוון ש-{% equation %}\beta_{1}\notin F{% endequation %} הרי ש<strong>בהכרח </strong>קיים {% equation %}\sigma\in G{% endequation %} כך ש-{% equation %}\sigma\left(\beta_{1}\right)\ne\beta_{1}{% endequation %}. אם לא היה קיים {% equation %}\sigma{% endequation %} כזה, אז היינו מקבלים {% equation %}\beta_{1}\in F{% endequation %}. מה נעשה עם {% equation %}\sigma{% endequation %}? פשוט מאוד - נפעיל אותו על כל אחת מהמשוואות, ונשתמש בכך שהוא אוטומורפיזם כדי לקבל

{% equation %}\sigma\sigma_{i}\left(a_{1}\right)\sigma\left(\beta_{1}\right)+\dots+\sigma\sigma_{i}\left(a_{k-1}\right)\sigma\left(\beta_{k-1}\right)+\sigma\sigma_{i}\left(a_{k}\right)=0{% endequation %}

מה קיבלנו פה? קודם הייתה לנו משוואה שאמרה "הנה צירוף לינארי של הפעלת האוטומורפיזם {% equation %}\sigma_{i}{% endequation %} על האיברים {% equation %}a_{1},\dots,a_{k}{% endequation %} ששווה אפס". עכשיו קיבלנו משוואה שאומרת "הנה צירוף לינארי <strong>עם מקדמים אחרים</strong> של הפעלת האוטומורפיזם {% equation %}\sigma\sigma_{i}{% endequation %} על האיברים {% equation %}a_{1},\dots,a_{k}{% endequation %} ששווה אפס". כאן נכנסת לתמונה העובדה ש-{% equation %}G{% endequation %} היא <strong>חבורה</strong>. בחבורה, כפל באיבר כלשהו של כל אברי החבורה בסך הכל מבצע תמורה שלהם. כלומר, {% equation %}\left\{ \sigma_{1},\dots,\sigma_{n}\right\} {% endequation %} היא אותה קבוצה בדיוק כמו {% equation %}\left\{ \sigma\sigma_{1},\dots,\sigma\sigma_{n}\right\} {% endequation %}. מכאן שלכל {% equation %}\sigma_{i}{% endequation %}, קיבלנו בסופו של דבר את המשוואה

{% equation %}\sigma_{i}\left(a_{1}\right)\sigma\left(\beta_{1}\right)+\dots+\sigma_{i}\left(a_{k-1}\right)\sigma\left(\beta_{k-1}\right)+\sigma_{i}\left(a_{k}\right)=0{% endequation %}

נפחית מהמשוואה הזו את המשוואה של {% equation %}\sigma_{i}{% endequation %} שהייתה לנו קודם, כלומר את

{% equation %}\sigma_{i}\left(a_{1}\right)\beta_{1}+\dots+\sigma_{i}\left(a_{k-1}\right)\beta_{k-1}+\sigma_{i}\left(a_{k}\right)=0{% endequation %}

ונקבל:

{% equation %}\sigma_{i}\left(a_{1}\right)\left(\beta_{1}-\sigma\left(\beta_{1}\right)\right)+\dots+\sigma_{i}\left(a_{k-1}\right)\left(\beta_{k-1}-\sigma\left(\beta_{k-1}\right)\right)=0{% endequation %}

שימו לב שהחיסור <strong>העלים את האיבר האחרון</strong> בסכום; זאת מכיוון שהאיבר האחרון הזה היה עבור {% equation %}\beta_{k}=1{% endequation %}, וזה איבר ש-{% equation %}\sigma{% endequation %} <strong>בודאות כן משמרת</strong>. באותו אופן, בחרנו את {% equation %}\sigma{% endequation %} מלכתחילה כדי ש- {% equation %}\beta_{1}{% endequation %} יהיה איבר ש-{% equation %}\sigma{% endequation %} <strong>בודאות לא משמרת</strong>, ולכן {% equation %}\beta_{1}\ne\sigma\left(\beta_{1}\right){% endequation %}, כלומר {% equation %}\beta_{1}-\sigma\left(\beta_{1}\right)\ne0{% endequation %}, כלומר המקדם הראשון בצירוף הלינארי שקיבלנו אינו אפס.

מה קרה? קיבלנו <strong>פתרון חדש</strong> למערכת המשוואות שממנה התחלנו. פתרון שבו יש רק {% equation %}k-1{% endequation %} איברים שונים מאפס, בסתירה להנחה שלנו ש-{% equation %}k{% endequation %} הוא המספר המינימלי של איברים שונים מאפס בפתרון לא טריוויאלי <strong>כלשהו</strong> למערכת המשוואות הזו. זה מסיים את ההוכחה.

האם זה היה טכני? כן, במידה מסויימת.

האם זה היה קשה? כן, במידה מסויימת, אם כי כל המעברים פה פשוטים למדי.

האם זה עוזר לנו להבין <strong>למה </strong>תורת גלואה עובדת? כן, במידה מסויימת: כל המרכיבים החשובים של תורת גלואה (בסיס של שדה אחד מעל אחר, חבורת אוטומורפיזמים, שימור של השדה הקטן) באים כאן לידי ביטוי. לכן אני חושב שלמרות שההוכחה היא טכנית למדי, היא עדיין אלגנטית ויפה מאוד, ויש חשיבות גדולה ל"להרגיש אותה בידיים" כדי להבין מה בעצם הולך בתורת גלואה.
