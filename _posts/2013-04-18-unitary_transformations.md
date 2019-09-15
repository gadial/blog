---
id: 2503
title: "טרנספורמציות אוניטריות"
date: 2013-04-18 21:12:34
layout: post
categories: 
  - אלגברה לינארית
tags: 
  - טרנספורמציות אוניטריות
  - מרחבי מכפלה פנימית
---
אני חוזר לסדרת הפוסטים שלי על אלגברה לינארית, ש<a href="http://www.gadial.net/2012/04/29/inner_product_space_adjoint/">נעצרה</a> במרחבי מכפלה פנימית ובסוג מעניין אחד של אופרטורים לינאריים עליהם - אופרטורים צמודים לעצמם ("הרמיטיים"). הפעם אני רוצה לדבר על סוג מעניין אחר של אופרטורים, שנקראים <strong>אופרטורים אוניטריים</strong>; בהמשך נראה איך הכל מתחבר.

בואו ניזכר מה זו בכלל טרנספורמציה לינארית. אם יש לנו שני מרחבים וקטוריים {% equation %}V,W{% endequation %} אז טרנספורמציה לינארית היא פונקציה {% equation %}T:V\to W{% endequation %} ש<strong>משמרת את המבנה</strong> של המרחבים הלינאריים. מבנה של מרחב לינארי מתבטא ב<strong>פעולות חשבוניות</strong> שמוגדרות עליו - חיבור של שני איברים, וכפל בסקלר של איבר. {% equation %}T\left(v+u\right)=T\left(v\right)+T\left(u\right){% endequation %} פירושו שבהינתן שני וקטורים {% equation %}v,u{% endequation %} זה לא משנה אם קודם נחבר אותם ואז נפעיל עליהם את {% equation %}T{% endequation %} או אם קודם נפעיל עליהם את {% equation %}T{% endequation %} ואז נחבר אותם - בכל מקרה נקבל את אותה התוצאה בסוף (את הרעיון הזה מתארים לפעמים בעזרת <strong>דיאגרמה קומוטטיבית</strong> והוא חזק למדי, אבל אלו דברים שיחכו לפוסט אחר). אותו הדבר עם כפל בסקלר: {% equation %}T\left(\lambda v\right)=\lambda T\left(v\right){% endequation %} פירושו שלא משנה אם קודם נכפול את {% equation %}v{% endequation %} בסקלר {% equation %}\lambda{% endequation %} ואז נפעיל עליו את {% equation %}T{% endequation %} או שקודם נפעיל עליו את {% equation %}T{% endequation %} ואז נכפול ב-{% equation %}\lambda{% endequation %} - בכל מקרה נקבל את אותה התוצאה.

עכשיו, מהו מרחב מכפלה פנימית? הוא מרחב וקטורי שהוספנו לו עוד <strong>מבנה</strong>, שמתבטא בפונקציה של <strong>מכפלה פנימית</strong>, שהיא פונקציה שמקבלת שני וקטורים ומחזירה סקלר, {% equation %}\left\langle v,u\right\rangle :V\times V\to\mathbb{C}{% endequation %}. אם נמשיך את קו המחשבה של שתי הדוגמאות הקודמות, אנחנו רואים שמחלקה מעניינת של טרנספורמציות לינאריות תהיה המחלקה של הטרנספורמציות ש<strong>משמרות את המכפלה הפנימית</strong>. כלומר, אם {% equation %}V,W{% endequation %} הם שני מרחבי מכפלה פנימית ו-{% equation %}T:V\to W{% endequation %}, מעניין אותנו אם אפשר קודם להפעיל את {% equation %}T{% endequation %} על זוג וקטורים ואז לכפול אותם, או קודם לכפול אותם ואז להפעיל עליהם את {% equation %}T{% endequation %}... רגע, רגע, רגע, משהו לא מסתדר פה!

הנקודה שצריך לתת עליה את הדעת היא שמכפלה פנימית "מוציאה" אותנו מהמרחב {% equation %}V{% endequation %}. בניגוד לחיבור, שקיבל זוג וקטורים ב-{% equation %}V{% endequation %} והחזיר וקטור ב-{% equation %}V{% endequation %}, מכפלה פנימית מעבירה אותנו מ-{% equation %}V{% endequation %} אל {% equation %}\mathbb{C}{% endequation %} ולכן כל עניין ה"התחלפות" שתיארתי לא עובד. עדיין, זו אינטואיציה טובה לדרישה שאני כן הולך לדרוש: שהמכפלה הפנימית של זוג וקטורים <strong>לא תשתנה</strong> אם נפעיל עליהם את {% equation %}T{% endequation %}, ובאופן פורמלי, {% equation %}\left\langle v,u\right\rangle =\left\langle T\left(v\right),T\left(u\right)\right\rangle {% endequation %}. שימו לב שהמכפלה הפנימית באגף שמאל היא המכפלה הפנימית של {% equation %}V{% endequation %} ואילו זו באגף ימין היא המכפלה הפנימית של {% equation %}W{% endequation %}. לטרנספורמציה לינארית שמקיימת את התכונה הזו אקרא <strong>אוניטרית</strong>. דוגמאות מיידיות לטרנספורמציות כאלו הן גאומטריות באופיין: חשבו על {% equation %}\mathbb{R}^{2}{% endequation %} עם המכפלה הפנימית הרגילה ועל הפעולות של סיבוב בזווית כלשהי סביב הראשית או של שיקוף ביחס לציר העובר דרך הראשית. אינטואיטיבית ברור למדי שאם מסובבים שני וקטורים באותה זווית גם האורכים שלהם והזווית ביניהם נשמרת, וב-{% equation %}\mathbb{R}^{2}{% endequation %} עם המכפלה הפנימית הרגילה, המכפלה הפנימית של זוג וקטורים היא מכפלת האורכים שלהם בקוסינוס הזווית ביניהם, כך שברור שהיא תשתמר. יש עוד הרבה דוגמאות אך לא אציג אותן כרגע. תחת זאת, בואו ננסה להבין אילו עוד תכונות טרנספורמציות אוניטריות מקיימות.

ראשית כל, מכפלה פנימית הייתה קשורה בקשר הדוק לפונקציה דומה שנקראה <strong>נורמה</strong>: {% equation %}\|v\|=\left\langle v,v\right\rangle {% endequation %}. בבירור אם {% equation %}T{% endequation %} אוניטרית אז {% equation %}\|T\left(v\right)\|=\left\langle T\left(v\right),T\left(v\right)\right\rangle =\left\langle v,v\right\rangle =\|v\|{% endequation %}, כלומר {% equation %}T{% endequation %} משמרת גם את הנורמה של איברים (פורמלית: את הנורמה הספציפית שמושרית על המרחבים מהמכפלה הפנימית שביחס אליהם {% equation %}T{% endequation %} אוניטרית). גם ההפך נכון - אם {% equation %}T{% endequation %} משמרת נורמה, אז היא אוניטרית; זה נובע מכך שאם נורמה מושרית ממכפלה פנימית כלשהי, אז אפשר לכתוב את המכפלה הפנימית בתור נוסחה כלשהי שמערבת את הנורמה - <strong>זהות הפולריזציה</strong> שהראיתי <a href="http://www.gadial.net/2012/03/01/inner_product_spaces_geometry/">בפוסט קודם</a>. מכאן שכדי להראות שטרנספורמציה היא אוניטרית יספיק לי לפעמים להראות שהיא משמרת נורמה.

עכשיו קופץ משהו אחר לעיניים: כזכור, {% equation %}\|v\|=0{% endequation %} אם ורק אם {% equation %}v=0{% endequation %} (וקטור האפס), ולכן אם {% equation %}T\left(v\right)=0{% endequation %} עבור {% equation %}v{% endequation %} כלשהו, הרי ש-{% equation %}\|v\|=\|T\left(v\right)\|=\|0\|=0{% endequation %} ומכאן נובע שגם {% equation %}v=0{% endequation %}. במילים אחרות, {% equation %}T{% endequation %} מעבירה לוקטור האפס רק את וקטור האפס; מכך נובע ש-{% equation %}T{% endequation %} <strong>הפיכה </strong>("לא סינגולרית"). אם כן, כל טרנספורמציה אוניטרית היא גם הפיכה; אם {% equation %}T:V\to W{% endequation %} היא אוניטרית ו-{% equation %}V,W{% endequation %} הם מאותו מימד סופי (כרגיל, מכאן ואילך נדבר רק על מרחבים ממימד סופי) אז נובע מכך ש-{% equation %}T{% endequation %} היא <strong>איזומורפיזם</strong> של {% equation %}V,W{% endequation %} שגם משמרת את המכפלה הפנימית שלהם. בלשון פחות פורמלית זה אומר ש-{% equation %}V,W{% endequation %} "הם אותו מרחב עד כדי שינוי שמות האיברים" וש-{% equation %}T{% endequation %} היא בדיוק מה שמבצע את השינוי של שמות האיברים הללו.

דבר אחד ש<a href="http://www.gadial.net/2012/02/06/inner_products_intro/">הוכחנו בעבר</a> הוא שאם {% equation %}V{% endequation %} הוא מרחב מכפלה פנימית ממימד סופי, אז קיים לו בסיס אורתונורמלי {% equation %}\left\{ b_{1},\dots,b_{n}\right\} {% endequation %}. עכשיו, אם {% equation %}W{% endequation %} הוא מרחב מאותו מימד כמו {% equation %}V{% endequation %}, מה נקבל כשנפעיל טרנספורמציה אוניטרית {% equation %}T:V\to W{% endequation %} על אברי הבסיס? נקבל קבוצה {% equation %}\left\{ T\left(b_{1}\right),\dots,T\left(b_{n}\right)\right\} {% endequation %} שהיא בבירור בסיס ל-{% equation %}W{% endequation %} כי היא קבוצה בלתי תלויה לינארית ב-{% equation %}W{% endequation %} עם מספר וקטורים ששווה למימד של {% equation %}W{% endequation %} (למה היא בלתי תלויה? כי {% equation %}T{% endequation %} הפיכה - נסו להוכיח!). כפי שאתם ודאי מנחשים, הבסיס שקיבלנו לא יהיה "סתם" בסיס, אלא בסיס אורתונורמלי, ובכך צצה לה תכונה נוספת של טרנספורמציות אוניטריות: הן מעבירות בסיסים אורתונורמליים לבסיסים אורתונורמליים.

העובדה שהבסיס החדש אורתונורמלי די מיידית. בסיס הוא אורתונורמלי אם לכל זוג איברים בו מתקיים {% equation %}\left\langle b_{i},b_{j}\right\rangle =\delta_{ij}{% endequation %} (כאשר {% equation %}\delta_{ij}=\begin{cases}1 &amp; i=j\\0 &amp; i\ne j\end{cases}{% endequation %} נקראת <strong>הדלתא של קרונקר</strong>), ובבירור {% equation %}\left\langle T\left(b_{i}\right),T\left(b_{j}\right)\right\rangle =\left\langle b_{i},b_{j}\right\rangle =\delta_{ij}{% endequation %} כי {% equation %}T{% endequation %} אוניטרית וה-{% equation %}b{% endequation %}-ים שייכים לבסיס אורתונורמלי. מה שיותר מעניין הוא שהטענה הזו עובדת גם בכיוון השני, ואפילו בגרסה יותר חזקה: אם {% equation %}T:V\to W{% endequation %} היא טרנספורמציה לינארית כלשהי כך שקיים בסיס אורתונורמלי <strong>אחד</strong> {% equation %}\left\{ b_{1},\dots,b_{n}\right\} {% endequation %} של {% equation %}V{% endequation %} בעל התכונה ש-{% equation %}\left\{ T\left(b_{1}\right),\dots,T\left(b_{n}\right)\right\} {% endequation %} הוא בסיס אורתונורמלי של {% equation %}T{% endequation %}, אז {% equation %}T{% endequation %} אוניטרית. ההוכחה, כרגיל במרחבי מכפלה פנימית, תעבור דרך העובדה שאנו בדיוק איך להציג כל איבר במרחב כצירוף לינארי של איברי הבסיס האורתונורמלי: אם {% equation %}v\in V{% endequation %} אז {% equation %}v=\sum\left\langle v,b_{i}\right\rangle b_{i}{% endequation %}. זה גם מאפשר לנו לדעת איך {% equation %}T\left(v\right){% endequation %} ייראה: {% equation %}T\left(v\right)=\sum\left\langle v,b_{i}\right\rangle T\left(b_{i}\right){% endequation %}.

בואו ניקח שני וקטורים {% equation %}v,u\in V{% endequation %}. אנו רוצים להראות ש-{% equation %}\left\langle v,u\right\rangle =\left\langle T\left(v\right),T\left(u\right)\right\rangle {% endequation %}. את החישוב של {% equation %}\left\langle v,u\right\rangle {% endequation %} כבר עשיתי <a href="http://www.gadial.net/2012/04/29/inner_product_space_adjoint/">בפוסט קודם</a>: מקבלים {% equation %}\left\langle v,u\right\rangle =\sum\left\langle v,b_{i}\right\rangle \overline{\left\langle u,b_{i}\right\rangle }{% endequation %}. עכשיו, אם נציב ב-{% equation %}\left\langle T\left(v\right),T\left(u\right)\right\rangle {% endequation %} את הביטוי ל-{% equation %}T\left(v\right){% endequation %} ו-{% equation %}T\left(u\right){% endequation %} שמצאנו קודם, נקבל:

{% equation %}\left\langle T\left(v\right),T\left(u\right)\right\rangle =\left\langle \sum_{i}\left\langle v,b_{i}\right\rangle T\left(b_{i}\right),\sum_{j}\left\langle u,b_{j}\right\rangle T\left(b_{j}\right)\right\rangle =\sum_{i,j}\left\langle v,b_{i}\right\rangle \overline{\left\langle u,b_{j}\right\rangle }\left\langle T\left(b_{i}\right),T\left(b_{j}\right)\right\rangle {% endequation %}

{% equation %}=\sum_{i,j}\left\langle v,b_{i}\right\rangle \overline{\left\langle u,b_{j}\right\rangle }\delta_{ij}=\sum_{i}\left\langle v,b_{i}\right\rangle \overline{\left\langle u,b_{i}\right\rangle }=\left\langle v,u\right\rangle {% endequation %}

מה שמסיים את ההוכחה. עכשיו יש לנו שלושה קריטריונים שקולים לכך שטרנספורמציה היא אוניטרית: היא משמרת מכפלה פנימית, היא משמרת נורמה, והיא מעבירה בסיס אורתונורמלי לבסיס אורתונורמלי.

הבנו איך טרנספורמציה אוניטרית מתנהגת "ברמת הוקטורים". עכשיו בואו ננסה להבין מה המבנה של אוסף כל הטרנספורמציות האוניטריות. נניח ש-{% equation %}T,S{% endequation %} הן שתי טרנספורמציות אוניטריות, מה בדבר ההרכבה, {% equation %}TS{% endequation %}? די בבירור גם היא אוניטרית, כי {% equation %}\|TS\left(v\right)\|=\|T\left(S\left(v\right)\right)\|=\|S\left(v\right)\|=\|v\|{% endequation %}. כמו כן, אם {% equation %}T{% endequation %} היא אוניטרית ראינו שהיא הפיכה; אני טוען שגם {% equation %}T^{-1}{% endequation %} אוניטרית, כי {% equation %}\|T^{-1}\left(v\right)\|=\|T\left(T^{-1}\left(v\right)\right)\|=\|v\|{% endequation %} (למי שלא ברור לו מה הלך פה, סמנו {% equation %}u=T^{-1}\left(v\right){% endequation %} ושימו לב לכך ש-{% equation %}\|u\|=\|T\left(u\right)\|{% endequation %} כי {% equation %}T{% endequation %} אוניטרית).

- בואו ננסה עכשיו להבין אותה לאור מה שדיברנו עליו <a href="http://www.gadial.net/2012/04/29/inner_product_space_adjoint/">בפוסט הקודם</a> על טרנספורמציות מעל מרחבי מכפלה פנימית - פעולת ההצמדה. כזכור, אם {% equation %}T:V\to V{% endequation %} הייתה אופרטור לינארי (המילה "אופרטור" כאן באה לתאר טרנספורמציות ממרחב כלשהו אל עצמו, להבדיל מ"סתם" טרנספורמציה שיכולה להיות בין שני מרחבים שונים), הוכחנו שקיים ויחיד אופרטור {% equation %}T^{*}{% endequation %} - ה<strong>צמוד</strong> של {% equation %}T{% endequation %}, כך שמתקיים {% equation %}\left\langle T\left(v\right),u\right\rangle =\left\langle v,T^{*}\left(u\right)\right\rangle {% endequation %} לכל זוג וקטורים {% equation %}v,u\in V{% endequation %}. אם {% equation %}T{% endequation %} אוניטרית, האם יש לצמוד עוד תכונות מעניינות?

ובכן, זכרו שכבר ראינו כי {% equation %}T{% endequation %} הפיך, כלומר קיים אופרטור שהוא בעצמו אוניטרי {% equation %}T^{-1}{% endequation %} כך ש-{% equation %}TT^{-1}=T^{-1}T=I{% endequation %}. אני טוען שההופכי הוא גם הצמוד של {% equation %}T{% endequation %}; בואו ונראה למה:

{% equation %}\left\langle T\left(v\right),u\right\rangle =\left\langle T^{-1}T\left(v\right),T^{-1}\left(u\right)\right\rangle =\left\langle v,T^{-1}\left(u\right)\right\rangle {% endequation %}

זה היה פשוט, לא? (איפה השתמשתי בכך ש-{% equation %}T^{-1}{% endequation %} אוניטרי?)

סיימתי להגיד את כל מה שאני רוצה להגיד כרגע על טרנספורמציות אוניטריות לבדן. העניין הוא שבאלגברה לינארית יש לטרנספורמציות לינאריות בנות זוג הדוקות - מטריצות. בפוסט הבא ננסה להבין איך מטריצות נכנסות לכל עניין הטרנספורמציות צמודות-צמודות לעצמן-אוניטריות.