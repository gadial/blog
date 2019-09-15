---
id: 177
title: "הרחבה קלה על הרחבת שדות"
date: 2009-01-06 14:00:49
layout: post
categories: 
  - אלגברה מופשטת
---
(אזהרה - פוסט טכני יחסית)

<a href="http://www.gadial.net/?p=176">בפוסט הקודם</a> הראיתי שניתן לחשוב על בניות בסרגל ומחוגה בתור "משחק" אלגברי לגמרי - מתחילים מהמספר 1, וכעת ניתן "לבנות" מספרים נוספים, כאשר הפעולות המותרות לנו הן <a href="http://he.wikipedia.org/wiki/%D7%90%D7%A8%D7%91%D7%A2_%D7%A4%D7%A2%D7%95%D7%9C%D7%95%D7%AA_%D7%94%D7%97%D7%A9%D7%91%D7%95%D7%9F">ארבע פעולות החשבון</a> - חיבור, חיסור, כפל וחילוק, ובנוסף לכך אנחנו מסוגלים להוציא <a href="http://he.wikipedia.org/wiki/%D7%A9%D7%95%D7%A8%D7%A9_%D7%A8%D7%99%D7%91%D7%95%D7%A2%D7%99">שורש ריבועי</a> למספרים חיוביים. השאלה המעניינת אותנו היא מה המספרים שניתנים לבנייה בדרך הזו (וזה אכן שמם הפורמלי "<a href="http://en.wikipedia.org/wiki/Constructible_number">מספרים ניתנים לבניה</a>"). הסיבה לכך שהבעיות הגאומטריות של היוונים הקדמונים שהזכרתי בפוסט הקודם אינן פתירות היא בדיוק מכיוון שפתרון שלהם מערב בהכרח בניה של מספר שאינו ניתן לבניה.

הדרך הפורמלית לטפל בבעיה הזו היא באמצעות המושג המתמטי הכללי של <strong>שדה</strong>, ובפרט באמצעות התחום שעוסק ב<a href="http://he.wikipedia.org/wiki/%D7%94%D7%A8%D7%97%D7%91%D7%AA_%D7%A9%D7%93%D7%95%D7%AA"><strong>הרחבת שדות</strong></a>, שעליו אדבר בפוסט הזה.

בצורה לא פורמלית (אך בכל זאת מדוייקת למדי) אפשר לומר ששדה הוא קבוצת איברים שניתן להגדיר עבורם את ארבע פעולות החשבון (<strong>ללא</strong> הוצאת שורש) באופן שהתכונות של ארבע פעולות החשבון "המקוריות" יתקיימו גם עבורם. התכונות הללו הן, למשל:
<ol>
	<li>חוק הקיבוץ: {% equation %}(x+y)+z=x+(y+z){% endequation %} (וכמו כן עבור כפל)</li>
	<li>חוק החילוף: {% equation %}x+y=y+x{% endequation %} (וכמו כן עבור כפל)</li>
	<li>חוק הפילוג: {% equation %}x(y+z)=xy+xz{% endequation %}</li>
</ol>
פרט לכך, יש איבר שמסומן ב-0 שמשמש בתור "נייטרלי לחיבור", כלומר כשמחברים את 0 עם x מקבלים x; ויש איבר שמסומן ב-1 ומשמש בתור נייטרלי לכפל - כשכופלים בו את x, מקבלים x. לכל איבר x יש איבר נגדי, מינוס x, כך שהסכום של שניהם הוא 0 (ולמעשה, את החיסור ניתן להגדיר בתור "חיבור עם הנגדי של"), ובדומה לכל איבר x שאינו 0 יש הופכי, {% equation %}\frac{1}{x}{% endequation %}, כך שהמכפלה של שניהם נותנת 1 (ואז מגדירים חילוק בתור "כפל עם ההופכי"). ל-0 אין הופכי מכיוון שאפס כפול כל דבר הוא אפס (נסו להוכיח זאת - התכונה המרכזית שצריך היא את חוק הפילוג).

תחת הגדרות מסויימות של פעולת החיבור מתקיימת תכונה שנראית מוזרה ממבט ראשון - אם מחברים את 1 לעצמו מספיק פעמים, מקבלים 0. זה קורה כאשר פעולת החיבור שלנו היא מודולו מספר כלשהו n (כלומר, אחרי שמחברים מחלקים ב-n והתוצאה הסופית היא השארית), אך בכל שאר הפוסט אניח שזה לא קורה. שדה שבו זה לא קורה, כלומר אפשר לחבר את 1 עם עצמו כמה פעמים שרק נרצה ולא נקבל אפס, נקרא "שדה ממציין 0".

הדוגמה הקלאסית לשדה היא<a href="http://he.wikipedia.org/wiki/%D7%A9%D7%93%D7%94_%D7%94%D7%9E%D7%A1%D7%A4%D7%A8%D7%99%D7%9D_%D7%94%D7%A8%D7%A6%D7%99%D7%95%D7%A0%D7%9C%D7%99%D7%99%D7%9D"> שדה המספרים הרציונליים</a>, אך הוא יותר מאשר דוגמה קלאסית "סתם" - הוא השדה הקטן ביותר ממציין 0, במובן זה ש<strong>כל</strong> שדה ממציין 0 יכיל בתוכו את המספרים הרציונליים (ליתר דיוק, שדה ש"נראה בדיוק כמו" המספרים הרציונליים). זאת מכיוון שאם יש לנו את 1 בשדה (ויש, על פי ההנחה) וכל מה שמתקבל על ידי ארבע פעולות החשבון גם נמצא בשדה, אפשר לבנות בקלות כל שני מספרים שלמים a,b, ולכן גם את המנה שלהם a/b - וזהו מספר רציונלי כללי.

בפרט, אוסף המספרים הניתנים לבנייה כולל את כל המספרים הרציונליים. אלא שהוא כולל עוד דברים - למשל, שורש 2. אם כן, הוא שדה גדול יותר, ש<strong>מכיל</strong> את המספרים הרציונליים כתת שדה. בניסוח אחר, שדה המספרים הניתנים לבנייה <strong>מרחיב</strong> את שדה המספרים הרציונליים. ובאופן כללי, אם F,E הם שני שדות כך ש-E מכיל את F, אומרים ש-E הוא שדה הרחבה של F. מסמנים את זה על ידי {% equation %}E/F{% endequation %}.

הדרך הפשוטה ביותר להרחיב שדה היא להוסיף לו איבר אחד שלא היה שייך לו קודם, ואז "לסגור" את השדה עבור האיבר הזה, כלומר להוסיף כל איבר אחר שחייבים להוסיף כדי שפעולות החשבון ימשיכו לתת איברים מהקבוצה. למשל, אם F הוא שדה הרציונליים ואנחנו מוסיפים לו את {% equation %}\sqrt{2}{% endequation %}, עלינו להוסיף עוד איברים כמו {% equation %}\sqrt{2}+1,\frac{\sqrt{2}}{2}{% endequation %} וכדומה. באופן כללי, אם מוסיפים לשדה F איבר {% equation %}\theta{% endequation %}, אז מסגירות לכפל גם כל החזקות שלו צריכות להיות שייכות לשדה - {% equation %}\theta, \theta^2,\theta^3,\dots{% endequation %}. במקרה של שורש 2 זה קל, כי שורש 2 בריבוע בחזקת 2 כבר שייך לשדה.

ייתכן שאתם שואלים את עצמכם "אם {% equation %}\theta{% endequation %} לא היה שייך ל-F, מאיפה הוא הגיע?" באופן כללי זו שאלה מצויינת, שדורשת הצדקה פורמלית. יש כזו, וזו בדיוק ההצדקה הפורמלית להוספת המספר המדומה i למספרים הממשיים, אך לא אעסוק בה כעת אלא בעתיד. לעת עתה, בהקשר של המספרים הניתנים לבנייה, כל מה שאדבר עליו הוא הרחבות של המספרים הרציונליים על ידי הוספת מספרים אי רציונליים אליהם - ומאיפה מגיעים המספרים האי רציונליים אנחנו יודעים (<a href="http://www.gadial.net/?p=29">כתבתי</a> פעם פוסט אחד או שניים בנושא).

חזרה לענייננו. בהינתן שהוספנו לשדה את {% equation %}\theta{% endequation %}, אז גם כל {% equation %}\theta^n{% endequation %} לכל n טבעי, צריך להיות בשדה, וגם כפל של דבר כזה באיבר שכבר עתה היה בשדה - {% equation %}a\theta^n{% endequation %} - צריך להיות בשדה, וגם סכומים של דברים כאלו צריכים להיות בשדה. בשורה התחתונה נובע מכך שאחרי הוספת {% equation %}\theta{% endequation %} לשדה וביצוע ה"סגירה" שלו, השדה מורכב כולו מביטויים מהצורה {% equation %}\sum_{i=0}^n a_i\theta^i{% endequation %}, כאשר n הוא טבעי כלשהו ואילו {% equation %}a_i{% endequation %} הם איברים השייכים לשדה המקורי. דרך אחרת לומר זאת היא שהשדה המתקבל מההרחבה של {% equation %}F{% endequation %} על ידי {% equation %}\theta{% endequation %} מכיל את כל ה<a href="http://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%9C%D7%99%D7%A0%D7%95%D7%9D">פולינומים</a> עם מקדמים מתוך {% equation %}F{% endequation %}, לאחר שהציבו בהם את {% equation %}\theta{% endequation %}.

טוב ויפה, אבל כפי שראינו, האיבר {% equation %}(\sqrt{2})^2{% endequation %} (שהוא פולינום מדרגה שנייה שהציבו בו את שורש 2) הוא בעצם האיבר {% equation %}2{% endequation %} (שהוא פולינום מדרגה 0 שהציבו בו את שורש 2 - כלומר, שורש 2 בכלל לא מופיע בו). אם כן, האם יש דרך הצגה פשוטה יותר לאברי השדה המורחב, שמבטיחה שכל איבר ייוצג פעם אחת?

התשובה חיובית, ותלויה בשאלה האם {% equation %}\theta{% endequation %} הוא מה שנקרא "אלגברי מעל F". איבר הוא אלגברי מעל F אם קיים פולינום שכל מקדמיו ב-F שמאפס את {% equation %}\theta{% endequation %}, כלומר {% equation %}\sum_{i=0}^n a_i\theta^i=0{% endequation %} עבורו. נניח שקיים פולינום כזה, אז בפרט אפשר לבחור אחד בעל דרגה מינימלית; הדרגה המינימלית של פולינום מעל F שמאפס את {% equation %}\theta{% endequation %} נקראת "הדרגה של {% equation %}\theta{% endequation %}", וניתן להוכיח שמכך ינבע שההרחבה של F באמצעות {% equation %}\theta{% endequation %} ניתנת לתיאור כאוסף כל הפולינומים מעל F מדרגה <strong>קטנה</strong> מ-n שהוצב בהם {% equation %}\theta{% endequation %}.

התכונה הזו, של דרגה של איבר, היא התכונה המרכזית שנזדקק לה כאשר נעסוק בבניות בסרגל ומחוגה. מכיוון שהיא קשורה בקשר אמיץ למושג בסיסי וחשוב מאוד מ<a href="http://he.wikipedia.org/wiki/%D7%90%D7%9C%D7%92%D7%91%D7%A8%D7%94_%D7%9C%D7%99%D7%A0%D7%90%D7%A8%D7%99%D7%AA">אלגברה לינארית</a> - מושג המימד. אקח כאן הפסקה קלה ואקדיש את הפוסט הבא למושג הזה - שבתקווה, ישפוך אור נוסף על מושג הדרגה במובנו הכללי והרחב יותר - דרגה של הרחבה.