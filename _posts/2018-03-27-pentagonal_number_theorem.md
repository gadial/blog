---
id: 3571
title: "משפט המספרים המחומשים"
date: 2018-03-27 14:51:55
layout: post
categories: 
  - קומבינטוריקה
  - תורת המספרים
tags: 
  - חלוקות
  - משפט המספרים המחומשים
---
בפוסט הזה אני רוצה להוכיח את מה שנקרא <strong>משפט המספרים המחומשים</strong>. במבט ראשון המשפט נראה מוזר ולא ברור למה הוא מעניין במיוחד, ולכן <a href="http://gadial.net/2018/03/11/partition_function_and_pentagonal_numbers/">הפוסט הקודם</a> הוקדש לשימוש מעניין שלו - מציאת נוסחת נסיגה עבור פונקציית החלוקה. עם זאת, המטרה של הפוסט הנוכחי היא לעמוד בפני עצמו, כי המתמטיקה של הפוסט הקודם היא טכנית למדי ולא דומה כל כך למה שנדבר עליו הפעם, כך שחבל לוותר רק בגלל זה.

ראשית, מה זה מספר מחומש? זה מספר מהצורה {% equation %}\frac{k\left(3k-1\right)}{2}{% endequation %} כאשר {% equation %}k{% endequation %} הוא מספר טבעי חיובי. השם "מספר מחומש" מגיע מכך שצורה מוזרה שבה אפשר לקבל את המספרים היא לצייר סדרה של {% equation %}k{% endequation %} מחומשים אחד בתוך השני, כשבמחומש ה-{% equation %}k{% endequation %} יש בדיוק {% equation %}k{% endequation %} נקודות על כל צלע, ואז לספור כמה נקודות יש בסך הכל. המחומש הראשון, זה עם נקודה אחת על כל צלע, הוא "מנוון" ונראה כמו נקודה בודדת:

<img class="alignnone size-medium wp-image-3572" src="{{site.baseurl}}{{site.post_images}}/2018/03/pengaton_numbers.jpg" alt="" width="300" height="138" />

זו דרך די מוזרה להגדיר סדרת מספרים, ואני אכן לא אחזור אליה בכלל. יותר מכך - אני אדבר גם על המספרים שמתקבלים כשמציבים בתוך {% equation %}k{% endequation %} ערכים <strong>שליליים</strong>; גם במקרה הזה מקבלים מספרים חיוביים. השיטה היא להציב מספר טבעי ואז את המינוס שלו, ואז את המספר הטבעי הבא וכן הלאה. הצבות של {% equation %}k=1,-1,2,-2,\dots{% endequation %} מניבות את סדרת המספרים {% equation %}1,2,5,7,12,15,22,26,\dots{% endequation %}.

הסיבה שהסדרה הזו מעניינת היא הנוסחה הבאה, שנקראת <strong>משפט המספרים המחומשים</strong> ובמבט ראשון ממש לא ברור מה היא אומרת בכלל:

{% equation %}\prod_{n=1}^{\infty}\left(1-x^{n}\right)=\sum_{k=-\infty}^{\infty}\left(-1\right)^{k+1}x^{\frac{k\left(3k-1\right)}{2}}{% endequation %}

כפי שהצהרתי בפוסט הקודם, לטעמי זו אחת מהנוסחאות היפות במתמטיקה, אבל אין שום סיבה להתעמק בפרטים שלה כאן (את זה עשיתי בפוסט הקודם) - במקום זה אפשר לנסח את המשפט בצורה שקולה לגמרי שהרבה יותר קל להבין, ותהיה הרבה יותר רלוונטית לאופן שבו אוכיח את המשפט בפועל. בהינתן מספר טבעי {% equation %}n{% endequation %}, אפשר לדבר על הדרכים השונות להציג אותו בתור סכום של מספרים טבעיים חיוביים כך שאין מספר שמופיע פעמיים. בפוסט הזה אני אקרא בשם <strong>חלוקה</strong> להצגה כזו (באופן כללי "חלוקות" מתייחס גם למקרה שבו מספר יכול להופיע פעמיים). למשל, ל-4 יש שתי חלוקות: {% equation %}4{% endequation %} עצמו, ו-{% equation %}1+3{% endequation %}. ה"חלוקה" {% equation %}2+2{% endequation %} לא נחשבת כי המספר 2 מופיע בה פעמיים.

אפשר לתאר חלוקות בדרך ציורית בעזרת <strong>טבלת יאנג</strong>. טבלת יאנג כוללת בסך הכל כמה שורות של ריבועים, כשכל שורה לא ארוכה יותר מאלו שבאות מתחתיה. סכום הריבועים הכולל בטבלה הוא {% equation %}n{% endequation %}, והאורך של כל שורה מייצג את אחד מהאיברים בפירוק. הנה דוגמא עבור הפירוקים של 4:

<strong><img class="alignnone size-medium wp-image-3573" src="{{site.baseurl}}{{site.post_images}}/2018/03/young1.png" alt="" width="300" height="81" /></strong>

הכלל הנוסף של "אותו מספר לא מופיע פעמיים בפירוק" מתורגם אצלנו ל"בטבלת יאנג, כל שורה קצרה יותר מזו שמתחתיה". לכן הטבלה הזו לא חוקית מבחינתנו:

<img class="alignnone wp-image-3574 size-thumbnail" src="{{site.baseurl}}{{site.post_images}}/2018/03/young2.png" alt="" width="150" height="150" />

מספר החלוקות של {% equation %}n{% endequation %} הוא מספר טבלאות היאנג החוקיות שקיימות עבורו. עכשיו בואו נבדיל בין שני סוגי טבלאות: כאלו עם מספר <strong>זוגי</strong> של שורות, מה שאקרא לו "חלוקה זוגית", וכאלו עם מספר <strong>אי-זוגי</strong> של שורות - "חלוקה אי-זוגית". אסמן ב-{% equation %}p_{\text{odd}}\left(n\right){% endequation %} את מספר החלוקות האי-זוגיות של {% equation %}n{% endequation %} וב-{% equation %}p_{\text{even}}\left(n\right){% endequation %} את מספר החלוקות הזוגיות. אנחנו יודעים ש-{% equation %}p_{\text{odd}}\left(n\right)+p_{\text{even}}\left(n\right){% endequation %} שווה למספר החלוקות של {% equation %}n{% endequation %} בסך הכל; אבל למה שווה ההפרש, {% equation %}p_{\text{odd}}\left(n\right)-p_{\text{even}}\left(n\right){% endequation %}? ובכן, זה בדיוק התוכן של משפט המספרים המחומשים: הוא אומר שכמעט תמיד מספר החלוקות הזוגיות יהיה שווה למספר החלוקות האי-זוגיות, כלומר ההפרש ביניהם יהיה 0; המקרים היחידים שבהם זה לא יהיה כך יהיו עבור {% equation %}n{% endequation %} שהוא מספר מחומש, ובמקרה הזה ההפרש יהיה פלוס-מינוס 1, כשהפלוס-או-מינוס נקבע על פי זוגיות ה-{% equation %}k{% endequation %} שמגדיר את המספר. בכתיבה פורמלית:

{% equation %}p_{\text{odd}}\left(n\right)-p_{\text{even}}\left(n\right)=\begin{cases} 1 & n=\frac{k\left(3k-1\right)}{2},k\text{ odd}\\ -1 & n=\frac{k\left(3k-1\right)}{2},k\text{ even}\\ 0 & \text{else} \end{cases}{% endequation %}

הנה דוגמאות לכל המקרים הללו. ראשית, 2. זה מספר מחומש שמתקבל על ידי {% equation %}k=1{% endequation %} האי-זוגי והפירוק היחיד שלו הוא 2; הפירוק {% equation %}1+1{% endequation %} אינו חוקי כי 1 מופיע פעמיים. לכן מספר הפירוקים האי-זוגיים גדול ב-1 ממספר הפירוקים הזוגיים. כעת אל 7. זה מספר מחומש שמתקבל על ידי {% equation %}k=-2{% endequation %} הזוגי, כך שאנחנו מצפים שמספר הפירוקים הזוגיים שלו יהיה גדול ב-1 ממספר הפירוקים האי-זוגיים שלו. הנה כל הפירוקים:

{% equation %}7,1+6,2+5,3+4,1+2+4{% endequation %}

יש לנו פה שלושה פירוקים זוגיים ושניים אי-זוגיים - כמו שהמשפט מבטיח.

עכשיו אל 8 שאיננו מספר מחומש בכלל ולכן אנחנו מצפים למספר שווה. הנה הפירוקים לכל גודל:

1: {% equation %}8{% endequation %}

{% equation %}2{% endequation %}: {% equation %}1+7,2+6,3+5{% endequation %}

3: {% equation %}1+2+5,1+3+4{% endequation %}

יש לנו פה פירוק אחד מגודל 1 ושניים מגודל 3 - סה"כ שלושה מגודל אי זוגי, מה שמתקזז עם שלושה מגודל 2 הזוגי.

הרעיון ברור, אבל איך מוכיחים את המשפט? ההוכחה שאראה פה תהיה קומבינטורית ותיעזר בטבלאות יאנג; זו לא ההוכחה המקורית של אוילר אלא הוכחה שהתגלתה לקראת סוף המאה ה-19 על ידי פרנקלין האמריקאי (לא, לא פרנקלין הזה). הטריק הוא לסדר פירוקים זוגיים ואי זוגיים בזוגות, כשלכל היותר פירוק אחד נותר בודד. נעשה את זה על ידי הגדרת פונקציה שלוקחת פירוק ובונה ממנו פירוק חדש, עם מספר מחוברים שונה ב-1, כך שהפעלה נוספת של הפונקציה "מתקנת" את ההפעלה הקודמת וחוזרת לאיבר שממנו התחלנו. במילים אחרות, הפונקציה שלנו היא ההופכית של עצמה; מקיימת {% equation %}f\left(f\left(x\right)\right)=x{% endequation %} לכל קלט. לפונקציה כזו קוראים <strong>אינבולוציה</strong>.

האינטואיציה של הבניה קלה להדהים כשמסתכלים עליה ציורית עם טבלאות יאנג. בואו נביט על טבלת היאנג של הפירוק {% equation %}4+6+8+9+10{% endequation %} של {% equation %}37{% endequation %}:

<strong><img class="alignnone wp-image-3576 size-medium" src="{{site.baseurl}}{{site.post_images}}/2018/03/young3.png" alt="" width="300" height="150" /></strong>

אנחנו רוצים לבנות מהטבלה הזו טבלה שמייצגת מספר שונה ב-1 של מחוברים. כל מחובר מתאים ל<strong>שורה</strong> בטבלת היאנג, כך ששתי דרכי הפעולה הטבעיות ביותר הן: או <strong>להוסיף שורה</strong> מעל השורה העליונה, שתיבנה מקוביות שניקח מהשורות האחרות; או <strong>להסיר</strong> את השורה העליונה ולחלק אותה לשורות האחרות. ואנחנו רוצים שהכלל שמכתיב לנו באיזו משתי הדרכים כדאי לנקוט יהיה כזה ש"הופך את עצמו" אחרי שימוש אחד. אז הנה הטריק: בואו נמספר ב-{% equation %}r{% endequation %} את מספר הקוביות בשורה העליונה ("המחובר הקטן ביותר בסכום") וב-{% equation %}s{% endequation %} נמספר את האורך של <strong>האלכסון</strong> בצד ימין למטה של הטבלה. באיור אצבע את השורה העליונה בירוק ואת האלכסון באדום:

<strong> <img class="alignnone size-medium wp-image-3577" src="{{site.baseurl}}{{site.post_images}}/2018/03/young4.png" alt="" width="300" height="150" /></strong>

הגדרה פורמלית יותר של {% equation %}s{% endequation %} היא זו: אורך הסדרה של המחוברים בסכום שמתחילה במחובר הגדול ביותר, עוברת עליהם מהגדול לקטן, ומסתיימת לפני האיבר הראשון ששונה מקודמו לפחות ב-2. והנה ניסוח עוד יותר פורמלי: אם נסמן חלוקה {% equation %}\lambda{% endequation %} בתור {% equation %}\lambda=\left(\lambda_{1},\lambda_{2},\dots,\lambda_{k}\right){% endequation %} כך ש-{% equation %}\lambda_{1}&gt;\lambda_{2}&gt;\dots&gt;\lambda_{k}{% endequation %} אז {% equation %}r=\lambda_{k}{% endequation %} ו-{% equation %}s{% endequation %} הוא המספר הגדול ביותר עבורו מתקיים {% equation %}\left(\lambda_{1},\dots,\lambda_{s}\right)=\left(\lambda_{1},\lambda_{1}-1,\dots,\lambda_{1}-\left(s-1\right)\right){% endequation %}.

ומה האינבולוציה עושה? אם {% equation %}r&gt;s{% endequation %} אז אנחנו מפרקים את האלכסון ובונים ממנו שורה חדשה מעל השורה העליונה; בגלל ש-{% equation %}r&gt;s{% endequation %} מובטח לנו שהשורה הזו תהיה קצרה מזו שמתחתיה, כדרוש. אם לעומת זאת {% equation %}r&lt;s{% endequation %} אנחנו מפרקים את השורה העליונה ובונים ממנה אלכסון חדש, כלומר מוסיפים קוביה אחת לכל {% equation %}r{% endequation %} השורות הראשונות; מכיוון ש-{% equation %}r&lt;s{% endequation %} אנחנו יודעים שיש מספיק שורות כאלו.

<strong><img class="alignnone size-medium wp-image-3578" src="{{site.baseurl}}{{site.post_images}}/2018/03/young5.png" alt="" width="300" height="200" /></strong>

מתי <strong>עשויה</strong> להיות בעיה? במקרה שבו {% equation %}r=s{% endequation %}. כאן העסק עלול להתקלקל אבל לא <strong>חייב</strong> להתקלקל. בואו נראה דוגמא, שמתאימה ל-{% equation %}3+6+8+9+10{% endequation %} של {% equation %}36{% endequation %}:

<strong><img class="alignnone size-medium wp-image-3579" src="{{site.baseurl}}{{site.post_images}}/2018/03/young6.png" alt="" width="300" height="150" /></strong>

ברור שבמקרה הזה אי אפשר לייצר שורה חדשה, כי היא תהיה באותה אורך כמו זו שמתחתיה; חייבים לפרק את השורה הקיימת, ואז מקבלים את הפירוק {% equation %}6+9+10+11{% endequation %}:

<strong><img class="alignnone size-medium wp-image-3580" src="{{site.baseurl}}{{site.post_images}}/2018/03/young7.png" alt="" width="300" height="110" /></strong>

הפירוק הזה תקין לגמרי, וכשנפעיל עליו את האינבולוציה נחזור לסיטואציה המקורית והכל טוב. מתי כן הייתה עלולה לצוץ בעיה? רק אם לא היו לנו {% equation %}r{% endequation %} שורות לחלק את הקוביות של השורה העליונה אליהן. מתי זה עלול לקרות? אנחנו הרי יודעים שיש לפחות {% equation %}s{% endequation %} שורות, ואת המספר הכולל של השורות סימנתי ב-{% equation %}k{% endequation %}. כלומר {% equation %}r=s\le k{% endequation %}; לכן כדי שתוכל להיווצר בעיה, הכרחי שיתקיים {% equation %}s=k{% endequation %}: במצב הזה מכיוון שאנחנו <strong>מפרקים</strong> את השורה העליונה, אנחנו נשארים בסוף עם קוביה בודדת שאין לנו שורה להכניס אותה אליה.

איך נראית טבלה שבה {% equation %}s=k{% endequation %}? היא תואמת כל חלוקה שבה הפער בין <strong>כל</strong> המחוברים הסמוכים הוא 1. למשל {% equation %}1+2+3+4{% endequation %}:

<strong><img class="alignnone wp-image-3582 size-medium" src="{{site.baseurl}}{{site.post_images}}/2018/03/young8.png" alt="" width="300" height="300" /></strong>

אבל כאן, כמובן, אין בעיה, כי {% equation %}r&lt;s{% endequation %} ולכן אפשר לפרק את השורה העליונה. לכן המקרה <strong>היחיד</strong> שבו יכולה להיות בעיה הוא זה שבו {% equation %}s=r=k{% endequation %}. למשל, הטבלה הזו:

<strong><img class="alignnone size-medium wp-image-3584" src="{{site.baseurl}}{{site.post_images}}/2018/03/young9-1.png" alt="" width="300" height="180" /></strong>

וכאן אנחנו אכן מקבלים מספר מחומש, {% equation %}12{% endequation %}. ובאופן כללי?

אם {% equation %}s=r=k{% endequation %} אז החלוקה שלנו היא בהכרח מהצורה הבאה: {% equation %}\left(k,k+1,k+2,\dots,k+\left(k-1\right)\right){% endequation %}. זה טור חשבוני פשוט במיוחד שאפשר לסכום "בשיטה של גאוס" - לשים לב שהסכום של המחובר הראשון והאחרון הוא {% equation %}3k-1{% endequation %}, וגם הסכום של המחובר השני והלפני אחרון, וכן הלאה, ויש בסך הכל {% equation %}k{% endequation %} מחוברים ולכן {% equation %}\frac{k}{2}{% endequation %} זוגות של מחוברים, ולכן הסכום הכולל הוא {% equation %}\frac{k\left(3k-1\right)}{2}{% endequation %} - והופס, קיבלנו מספר מחומש! אבל שימו לב, רק עבור המקרה שבו {% equation %}k{% endequation %} הוא חיובי, בינתיים. עכשיו גם ברור למה כאשר {% equation %}k{% endequation %} אי-זוגי אז יש יותר חלוקות אי זוגיות מזוגיות, ואחרת ההפך; כי {% equation %}k{% endequation %} הוא מספר השורות בטבלה, כלומר הזוגיות של {% equation %}k{% endequation %} קובעת האם החלוקה שאין לה בת זוג היא זוגית או אי זוגית.

אז רגע, מה פספסנו? איך ערכים שליליים של {% equation %}k{% endequation %} נכנסים לתמונה? ובכן, רימיתי אתכם קודם והשמטתי עוד מקרה קצה אחד. האם עליתם על הרמאות שלי? הבעיה היא במקרה שבו {% equation %}r&gt;s{% endequation %}. במקרה הזה, כזכור, הרעיון הוא לפרק את האלכסון ולדחוף את האיברים שלו בשורה מעל העליונה; אבל כאן עלולה להיווצר בעיה אם <strong>גם השורה העליונה השתתפה באלכסון</strong>, כי אז כשאני מפרק את האלכסון אני מסיר ממנה איבר אחד. הנה מקרה שבו זה קורה:

<strong><img class="alignnone wp-image-3587 size-medium" src="{{site.baseurl}}{{site.post_images}}/2018/03/young10.png" alt="" width="300" height="151" /></strong>

כאן האלכסון הוא מגודל 3 ולכאורה אין עם זה בעיה כי השורה העליונה היא מגודל 4, אבל כמובן - אחרי שנסיר את אברי האלכסון ניוותר עם שורה מגודל 3. לכן יכולה להיווצר בעיה בדיוק במקרה שבו {% equation %}r=s+1{% endequation %} ו-{% equation %}s=k{% endequation %} (כי {% equation %}s=k{% endequation %} פירושו "גם השורה העליונה משתתפת באלכסון). במקרה הזה, החלוקה היא מהצורה {% equation %}\left(k+1,k+2,\dots,k+k\right){% endequation %} והסכום יוצא {% equation %}\frac{k\left(3k+1\right)}{2}{% endequation %}. זה כמובן לא מתאים לנוסחה שלנו של מספר מחומש, אז אם רוצים לקבל את האחידות היפה בנוסחה שיש לנו, בואו נשים לב לכך ש-{% equation %}t\left(3t-1\right)=3t^{2}-t{% endequation %} ולכן אם נגדיר {% equation %}t=-k{% endequation %} נקבל

{% equation %}\frac{t\left(3t-1\right)}{2}=\frac{3t^{2}-t}{2}=\frac{3k^{2}+k}{2}=\frac{k\left(3k+1\right)}{2}{% endequation %}. זה מסביר את עניין המינוס ומסיים את ההוכחה.

נסכם מה הלך פה: הגדרתי אינבולוציה על קבוצת כל טבלאות יאנג הקיימות, למעט כמה מקרי קצה. האינבולוציה לא משנה את ה<strong>גודל</strong> של הטבלה (מספר הריבועים שלה, ששווה לגודל המספר שאת החלוקה שלו הטבלה מייצגת) אבל היא כן משנה בדיוק ב-1 את <strong>מספר השורות</strong> שלה (מספר המחוברים בחלוקה). בצורה הזו אנחנו מקבלים התאמה חח"ע ועל בין החלוקות הזוגיות של מספר והחלוקות האי-זוגיות שלו, למעט במקרים שבהם לפחות אחת מטבלאות היאנג שלו משתייכת אל מקרי הקצה שהאינבולוציה לא יודעת לטפל בהם. ראינו שמקרי הקצה הללו מתרחשים בדיוק עבור מספרים מהצורה {% equation %}\frac{k\left(3k-1\right)}{2}{% endequation %} עבור ערכים שלמים של {% equation %}k{% endequation %}; בפרט, אין שני מקרי קצה שמתרחשים עבור אותו גודל, כי לא קשה להראות שאין לאותו מספר טבעי שני ייצוגים שונים מהצורה {% equation %}\frac{k\left(3k-1\right)}{2}{% endequation %} כאשר {% equation %}k{% endequation %} שלם. זה יפה בפני עצמו, וזה עוד יותר יפה כשזוכרים שזה מה שמוביל בסופו של דבר לנוסחת הנסיגה המופלאה עבור פונקציית החלוקה שראינו בפוסט הקודם.
