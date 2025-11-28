---
title: "טורי טיילור - ההוכחות הפורמליות"
layout: post
categories:
  - אנליזה מתמטית
tags:
  - טורי טיילור
---

<a href="https://gadial.net/2024/05/03/taylor_series/">בפוסט הקודם</a> הצגתי טורי טיילור והראיתי שלל דוגמאות, תוך הבטחה שנראה את ההוכחות הפורמליות הנדרשות בהמשך. בואו נעשה את זה עכשיו. ראשית, אני אזכיר את ההגדרה: אם {% equation %}f{% endequation %} היא פונקציה שגזירה אינסוף פעמים בנקודה {% equation %}a{% endequation %}, אז <strong>טור הטיילור</strong> של {% equation %}f{% endequation %} סביב הנקודה {% equation %}a{% endequation %} הוא טור החזקות {% equation %}\sum_{n=0}^{\infty}\frac{f^{\left(n\right)}\left(a\right)}{n!}\left(z-a\right)^{n}{% endequation %}. כמה נקודות שצריך לשים לב אליהן בהגדרה הזו:

<ol> <li>משום מה אני משתמש ב-{% equation %}z{% endequation %} במקום ב-{% equation %}x{% endequation %} לציון המשתנה של הפונקציה. זה מכיוון שיותר מקובל להשתמש ב-{% equation %}z{% endequation %} לתיאור המשתנה של פונקציה <strong>מרוכבת</strong>, מה שמביא אותי לנקודה השניה:</li>


<li>לא אמרתי מה התחום והטווח של {% equation %}f{% endequation %}. זה כי אני בעצם רוצה לדבר בו זמנית על שני מקרים: המקרה של פונקציה {% equation %}f:D\to\mathbb{R}{% endequation %} כאשר {% equation %}D\subseteq\mathbb{R}{% endequation %} אבל גם המקרה של פונקציה {% equation %}f:D\to\mathbb{C}{% endequation %} כאשר {% equation %}D\subseteq\mathbb{C}{% endequation %} שהוא המקרה המעניין יותר עבורי כי אני רוצה להתקדם מפה לדיון על פונקציות מרוכבות, וטורי טיילור זו נקודת פתיחה חשובה של דיון כזה. אז אני מסמן את {% equation %}f{% endequation %} בתור {% equation %}f\left(z\right){% endequation %} אבל בפוסט הזה ההוכחות שלי עובדות גם ל-{% equation %}\mathbb{R}{% endequation %} וגם ל-{% equation %}\mathbb{C}{% endequation %} באותה מידה.</li>


<li>זה שהגדרתי טור חזקות לא אומר שהוא מתכנס ל-{% equation %}f{% endequation %} בכל נקודה שבה {% equation %}f{% endequation %} מוגדרת (כלומר, בכל {% equation %}z\in D{% endequation %}) או אפילו שהוא מתכנס בכלל ב-{% equation %}D{% endequation %}. המקום היחיד שעבורו זה מובטח הוא {% equation %}z=a{% endequation %}, כי כשמציבים אותו בטור כל האיברים מתאפסים למעט הראשון, שהוא על פי הגדרה {% equation %}f\left(a\right){% endequation %}. בפוסט הקודם ראינו דוגמא לפונקציה <strong>ממשית</strong> שגזירה אינסוף פעמים ב-0 אבל טור הטיילור שלה סביב 0 שונה ממנה בכל נקודה שונה מ-0: הפונקציה {% equation %}f\left(x\right)=\begin{cases} e^{-\frac{1}{x^{2}}} & x\ne0\\ 0 & x=0\end{cases}{% endequation %}


. בפוסט הזה ננסה להבין מתי כן מובטחת לנו התכנסות כזו. </li></ol>

השאלה הראשונה שאני שואל את עצמי היא - התחלנו מהדרישה ש-{% equation %}f{% endequation %} תהיה גזירה אינסוף פעמים. האם זה <strong>הכרחי</strong>, כדי ש-{% equation %}f{% endequation %} תיוצג על ידי טור חזקות? ובכן, אני יכול לקחת פונקציה מממשית כמו {% equation %}f\left(x\right)=\left|x\right|{% endequation %} שלא גזירה ב-{% equation %}x=0{% endequation %} ועדיין "לייצג" אותה עם טור החזקות {% equation %}\sum_{n=0}^{\infty}x^{n}{% endequation %} במובן זה שהיא תהיה שווה ל-{% equation %}f{% endequation %} ב-{% equation %}x=0{% endequation %} ושונה מ-{% equation %}f{% endequation %} בכל {% equation %}x{% endequation %} אחר. זו דוגמא לכמה מעצבנות וקטנוניות יכולות להיות דוגמאות נגדיות בחדו"א אם לא מנסים את הדרישה שלנו בזהירות. מה שלרוב גורם לעניינים להתנהג נחמד הוא לא לדרוש משהו <strong>נקודתי</strong> אלא משהו שיתקיים ב<strong>סביבה</strong> של נקודה, עבור כל האיברים שלה. כלומר, אנחנו מניחים שקיימת קבוצה פתוחה {% equation %}D{% endequation %} כך ש-{% equation %}f{% endequation %} מוגדרת על כל {% equation %}D{% endequation %} ושואלים את עצמנו מה אפשר לדעת על {% equation %}f{% endequation %} מכך ש-{% equation %}f{% endequation %} מיוצגת על ידי טור חזקות שמתכנס אליה <strong>לכל</strong> {% equation %}z\in D{% endequation %}.

מכיוון ש"קבוצה פתוחה" היא מושג קריטי, בפרט באנליזה מרוכבת, הנה תזכורת מה זה: זו פשוט קבוצה כך שכל נקודה בה היא נקודת פנים שלה, כש"נקודת פנים" פירושו שקיימת סביבה של הנקודה שמוכלת בקבוצה. פורמלית, {% equation %}D{% endequation %} פתוחה אם לכל {% equation %}a\in D{% endequation %} קיים {% equation %}\varepsilon>0{% endequation %} כך שאם {% equation %}\left|z-a\right|<\varepsilon{% endequation %} אז {% equation %}z\in D{% endequation %}. אפשר וכדאי לחשוב על קבוצות פתוחות בתור "תת-יקום זעיר" של {% equation %}\mathbb{R}{% endequation %} או {% equation %}\mathbb{C}{% endequation %}, שמתנהג מאוד דומה לקבוצות הללו - יש בו אינסוף איברים ואין בו נקודות קצה ברורות. זו אנלוגיה שעשוי להישבר לפעמים (מה אם יש לנו קבוצה פתוחה "עם חור" באמצע, כמו בייגלה? לא ניכנס לזה כרגע) אבל זו התחלה טובה. אני לפעמים משתמש במילה <strong>תחום</strong> (Domain) כדי לתאר קבוצה פתוחה - זה קצת מבלבל עם המושג של <strong>תחום ההגדרה</strong> של פונקציה, אבל יהיה טוב.

אם כן, נניח שיש לנו טור חזקות <strong>כלשהו</strong> {% equation %}\sum_{n=0}^{\infty}a_{n}\left(z-a\right)^{n}{% endequation %} עם רדיוס התכנסות {% equation %}R>0{% endequation %}. נסמן {% equation %}f\left(z\right)=\sum_{n=0}^{\infty}a_{n}\left(z-a\right)^{n}{% endequation %}. נתחיל עם הוכחה ש-{% equation %}f^{\prime}\left(z\right){% endequation %} קיימת. מה היינו <strong>מצפים</strong> שהנגזרת הזו תהיה? ובכן, הנה תזכורת כללית. גם עבור פונקציה ממשית וגם עבור פונקציה מרוכבת, הנגזרת של פונקציה {% equation %}g{% endequation %} כלשהי היא

{% equation %}\lim_{h\to0}\frac{g\left(z+h\right)-g\left(z\right)}{h}{% endequation %}

לא קשה להראות, בעזרת הבינום של ניוטון, שאם {% equation %}g\left(z\right)=z^{n}{% endequation %} אז {% equation %}g^{\prime}\left(z\right)=nz^{n-1}{% endequation %}, ולא קשה להראות שנגזרת היא לינארית, מה שאומר שעבור כל סכום <strong>סופי</strong> של איברים מהצורה {% equation %}a_{n}\left(z-a\right)^{n}{% endequation %}, אם נגזור את הסכום נקבל סכום של איברים מהצורה {% equation %}na_{n}\left(z-a\right)^{n-1}{% endequation %}. לכן האינטואיציה שלנו היא שאמור להתקיים

{% equation %}f^{\prime}\left(z\right)=\sum_{n=1}^{\infty}na_{n}\left(z-a\right)^{n-1}{% endequation %}

אבל בשלב הזה מדובר על אינטואיציה בלבד, כי הטענה על סכומים <strong>סופיים</strong> לא עובדת עבור סכומים <strong>אינסופיים</strong> תמיד; היא כן עובדת במקרה הזה, הפשוט יחסית, שבו הסכום האינסופי נותן לנו טור חזקות.

אם כן, בואו נסתכל על טור החזקות {% equation %}\sum_{n=1}^{\infty}na_{n}\left(z-a\right)^{n-1}{% endequation %}. אמרתי שלטור המקורי היה רדיוס התכנסות {% equation %}R{% endequation %}? קודם כל אני רוצה להוכיח שגם לטור הזה יש רדיוס התכנסות {% equation %}R{% endequation %}. כזכור מ<a href="https://gadial.net/2024/04/27/power_series/">הפוסט על טורי חזקות</a>, יש לנו למרבה השמחה נוסחה מדויקת לרדיוס ההתכנסות של כל טור חזקות:

{% equation %}\frac{1}{R}=\lim\sup\sqrt[n]{\left|a_{n}\right|}{% endequation %}

אז כל מה שאנחנו צריכים לעשות הוא להוכיח שעבור הטור החדש מתקיים גם כן

{% equation %}\lim\sup\sqrt[n-1]{\left|na_{n}\right|}=\frac{1}{R}{% endequation %}

(למי שה-{% equation %}n-1{% endequation %} בחזקה מציק לו, היה אפשר לעשות גם {% equation %}\sqrt[n]{\left(n+1\right)a_{n+1}}{% endequation %}, אבל זה יותר מסורבל).

את {% equation %}\lim\sup\sqrt[n-1]{\left|na_{n}\right|}{% endequation %} אפשר לחשב על ידי פירוק של הגבול העליון הזה למכפלה:

{% equation %}\lim\sup\sqrt[n-1]{\left|na_{n}\right|}=\lim\sup\left(\sqrt[n-1]{\left|n\right|}\right)\cdot\lim\sup\sqrt[n-1]{\left|a_{n}\right|}{% endequation %}

את המעבר הזה <strong>אי אפשר לבצע באופן כללי</strong> אבל אפשר לבצע כמעט באופן כללי: אם {% equation %}b_{n},c_{n}{% endequation %} הן שתי סדרות כלשהן של מספרים חיוביים וממשיים ואם {% equation %}b=\lim_{n\to\infty}b_{n},c=\lim\sup c_{n}{% endequation %} אז 

{% equation %}\lim\sup\left(b_{n}c_{n}\right)=bc{% endequation %}

שימו לב לחוסר הסימטריה: עבור {% equation %}b_{n}{% endequation %} אני דורש את הדרישה הקשוחה יותר {% equation %}b=\lim_{n\to\infty}b_{n}{% endequation %} (אם סדרה היא מתכנסת אז הגבול שלה הוא גם ה-{% equation %}\lim\sup{% endequation %} שלה), פשוט כי אם הייתי דורש רק {% equation %}b=\lim\sup b_{n}{% endequation %} המשפט לא היה נכון (תסתכלו על הסדרות {% equation %}2,\frac{1}{2},2,\frac{1}{2},\ldots{% endequation %} ו-{% equation %}\frac{1}{2},2,\frac{1}{2},2,\ldots{% endequation %}).

אני לא אוכיח כאן את טענת העזר הזו; היא מה שנקרא "תרגיל טוב" (כלומר, זה יהיה טכני מדי עבורי להתחיל להוכיח אותה באמצע משהו אחר). במקום זה בואו ונראה מה אני הולך להראות כדי שאוכל להשתמש בה:

<ul> <li>{% equation %}\lim\sup\left(\sqrt[n-1]{\left|n\right|}\right)=\lim_{n\to\infty}\left(\sqrt[n-1]{\left|n\right|}\right)=1{% endequation %}</li>


<li>{% equation %}\lim\sup\sqrt[n-1]{\left|a_{n}\right|}=\frac{1}{R}{% endequation %}</li>

</ul>

בשביל {% equation %}\lim_{n\to\infty}\left(\sqrt[n-1]{\left|n\right|}\right)=1{% endequation %}, בואו קודם כל נכתוב בצורה קצת יותר ברורה את הביטוי הזה: {% equation %}\lim_{n\to\infty}n^{\frac{1}{n-1}}{% endequation %}. טריק נפוץ כדי להתמודד עם ביטויים עם חזקה מעצבנת הוא לקחת לוגריתם של הביטוי, מה שמוריד את החזקה למטה: {% equation %}\ln n^{\frac{1}{n-1}}=\frac{\ln n}{n-1}{% endequation %}. עכשיו, אם נוכיח {% equation %}\lim_{n\to\infty}\ln n^{\frac{1}{n-1}}=0{% endequation %} ינבע מכך {% equation %}\lim_{n\to\infty}n^{\frac{1}{n-1}}=1{% endequation %} בזכות הרציפות של {% equation %}\ln{% endequation %} (הנה עוד תרגיל טוב). את {% equation %}\lim_{n\to\infty}\frac{\ln n}{n-1}=0{% endequation %} קל להוכיח אם מוכיחים את הטענה המקבילה לפונקציות, {% equation %}\lim_{x\to\infty}\frac{\ln x}{x-1}=0{% endequation %} (הנה עוד תרגיל טוב) על ידי שימוש בכלל לופיטל (אני מניח שאנחנו מכירים את כלל לופיטל), שנותן את הגבול {% equation %}\lim_{x\to\infty}\frac{1/x}{1}=0{% endequation %}. זה מסיים את הטענה הראשונה.

הטענה השניה, {% equation %}\lim\sup\sqrt[n-1]{\left|a_{n}\right|}=\frac{1}{R}{% endequation %}, נראית קלה באופן מתעתע: הרי מה ההבדל הגדול כל כך בין {% equation %}\sqrt[n-1]{\left|a_{n}\right|}{% endequation %} ובין {% equation %}\sqrt[n]{\left|a_{n}\right|}{% endequation %} כשמשאיפים את {% equation %}n{% endequation %} לאינסוף? אבל כמובן, יכול להיות הבדל כזה, הכל תלוי באיך {% equation %}a_{n}{% endequation %} מתנהגת. הנקודה שבה הדמיון בין שני הביטויים כן עוזר לנו היא בכך שאפשר לחשוב גם על {% equation %}\lim\sup\sqrt[n-1]{\left|a_{n}\right|}{% endequation %} בתור משהו שנותן רדיוס התכנסות של טור חזקות: הטור {% equation %}\sum_{n=0}^{\infty}a_{n+1}z^{n}{% endequation %}. 

הטור {% equation %}\sum_{n=0}^{\infty}a_{n+1}z^{n}{% endequation %} דומה מאוד לטור {% equation %}\sum_{n=0}^{\infty}a_{n}z^{n}{% endequation %} המקורי; אפשר לקבל אותו מהטור המקורי על ידי פירוק שלו לאיבר הראשון וכל היתר, והוצאת {% equation %}z{% endequation %} החוצה (אם יצא לכן להתעסק עם פונקציות יוצרות, הטריקים הללו עשויים להיות מוכרים):

{% equation %}\sum_{n=0}^{\infty}a_{n}z^{n}=a_{0}+\sum_{n=1}^{\infty}a_{n}z^{n}=a_{0}+z\sum_{n=1}^{\infty}a_{n}z^{n-1}=a_{0}+z\sum_{n=0}^{\infty}a_{n+1}z^{n}{% endequation %}

עבור {% equation %}z{% endequation %} קבוע, ההתכנסות של {% equation %}a_{0}+z\sum_{n=0}^{\infty}a_{n+1}z^{n}{% endequation %} לא מושפעת מה-{% equation %}a_{0}{% endequation %} בחוץ או מה-{% equation %}z{% endequation %} שבו הכל מוכפל, ולכן אם {% equation %}\sum_{n=0}^{\infty}a_{n+1}z^{n}{% endequation %} מתכנס נובע מכך שגם {% equation %}\sum_{n=0}^{\infty}a_{n}z^{n}{% endequation %} מתכנס. בדומה, אם {% equation %}\sum_{n=0}^{\infty}a_{n}z^{n}{% endequation %} מתכנס נובע מכך ש-{% equation %}\sum_{n=0}^{\infty}a_{n+1}z^{n}=\frac{\sum_{n=0}^{\infty}a_{n}z^{n}-a_{0}}{z}{% endequation %} מתכנס (אם {% equation %}z=0{% endequation %} הוא בוודאי מתכנס גם בלי לחלק שום דבר ב-{% equation %}z{% endequation %}), לכן רדיוסי ההתכנסות של הטורים הללו זהים, מה שמשלים את ההוכחה.

בואו ניזכר מה היה היעד שלנו. הגדרנו {% equation %}f\left(z\right)=\sum_{n=0}^{\infty}a_{n}\left(z-a\right)^{n}{% endequation %} ורצינו להראות ש-{% equation %}f^{\prime}\left(z\right)=\sum_{n=1}^{\infty}na_{n}\left(z-a\right)^{n-1}{% endequation %}. עוד לא הראינו את זה; הראינו רק שהטור {% equation %}\sum_{n=1}^{\infty}na_{n}\left(z-a\right)^{n-1}{% endequation %} הוא בעל רדיוס ההתכנסות {% equation %}R{% endequation %} של הטור המקורי, ולכן הוא מגדיר פונקציה על אותו תחום כמו זה של {% equation %}f{% endequation %}. אבל עדיין צריך להראות שהוא שווה אל {% equation %}f^{\prime}\left(z\right){% endequation %}. עכשיו, איך מגדירים את {% equation %}f^{\prime}\left(z\right){% endequation %}? ההגדרה עבור פונקציות מרוכבות זהה להגדרה עבור פונקציות ממשיות:

{% equation %}f^{\prime}\left(z\right)=\lim_{w\to z}\frac{f\left(w\right)-f\left(z\right)}{w-z}{% endequation %}

רק שכאן {% equation %}w{% endequation %} הוא מספר מרוכב כלשהו והשאיפה {% equation %}w\to z{% endequation %} היא שאיפה במובן של מספרים מרוכבים, כלומר ש-{% equation %}\left|w-z\right|{% endequation %} שואף לאפס עבור פונקציית הערך המוחלט של מספרים מרוכבים. מי שזוכרים חדו"א של מספרים ממשיים אולי מכירים את הגדרת הנגזרת עם {% equation %}\lim_{h\to0}\frac{f\left(x+h\right)-f\left(x\right)}{h}{% endequation %}; זה אותו רעיון, פשוט {% equation %}w=x+h{% endequation %} ולכן אם {% equation %}h\to0{% endequation %} אז {% equation %}w\to x{% endequation %}.

כרגיל, יהיה נוח להניח בלי הגבלת הכלליות שהטורים שלנו מוגדרים סביב 0 - זו אותה הוכחה עבור כשהם מוגדרים סביב {% equation %}a{% endequation %} כלשהו, פשוט עם סימונים יותר מסורבלים.

אוקיי, אז הנה הסימונים והמטרות שלנו:

{% equation %}f\left(z\right)=\sum_{n=0}^{\infty}a_{n}z^{n}{% endequation %}

{% equation %}g\left(z\right)=\sum_{n=1}^{\infty}na_{n}z^{n-1}{% endequation %} 

רדיוס ההתכנסות של שני הטורים הללו הוא {% equation %}R{% endequation %}. ניקח {% equation %}z{% endequation %} כך ש-{% equation %}\left|z\right|<R{% endequation %} ונרצה להראות ש-{% equation %}f^{\prime}\left(z\right)=g\left(z\right){% endequation %}. כלומר, אני ארצה להראות שהביטוי {% equation %}\frac{f\left(w\right)-f\left(z\right)}{w-z}{% endequation %} הולך ומתקרב אל {% equation %}g\left(z\right){% endequation %} כאשר {% equation %}w{% endequation %} מתקרב אל {% equation %}z{% endequation %}. זו הוכחת אפסילון-דלתא רגילה: אני לוקח {% equation %}\varepsilon>0{% endequation %} שרירותי כלשהו וצריך למצוא ערך טוב של {% equation %}\delta>0{% endequation %} כך שאם {% equation %}0<\left|w-z\right|<\delta{% endequation %} אז {% equation %}\left|\frac{f\left(w\right)-f\left(z\right)}{w-z}-g\left(z\right)\right|<\varepsilon{% endequation %}.

הביטוי {% equation %}f\left(w\right)-f\left(z\right){% endequation %} שבמונה הוא הפרש בין שני טורים אינסופיים וקצת קשה לעבוד עם זה, אז מה שנרצה לעשות הוא לפרק את הטור האינסופי{% equation %}f\left(z\right)=\sum_{n=0}^{\infty}a_{n}z^{n}{% endequation %} לשני טורים - "ראש" סופי ו"זנב" אינסופי. הנקודה שבה הפיצול הזה יתבצע תהיה {% equation %}n{% endequation %}, כש-{% equation %}n{% endequation %} הוא כרגע שרירותי ובהמשך נבחר אותו להיות מה שמתאים לנו. אני אכתוב

{% equation %}f\left(z\right)=\sum_{k=0}^{\infty}a_{k}z^{k}=\sum_{k=0}^{n}a_{k}z^{k}+\sum_{k=n+1}^{\infty}a_{k}z^{k}=S_{n}\left(z\right)+R_{n}\left(z\right){% endequation %}

כש-{% equation %}S_{n}\left(z\right){% endequation %} היא הפונקציה שמתאימה לסכום החלקי עד {% equation %}n{% endequation %} ו-{% equation %}R_{n}\left(z\right){% endequation %} היא הפונקציה שמתארת את השארית (אלו סימונים סטנדרטיים אז תסלחו לי על השימוש ב-{% equation %}R{% endequation %} גם לרדיוס ההתכנסות וגם לפונקציית השארית).

עכשיו בואו נעבור לחלק הכיפי ביותר בחדו"א - האלגברה:

{% equation %}\frac{f\left(w\right)-f\left(z\right)}{w-z}-g\left(z\right)=\left[\frac{S_{n}\left(w\right)-S_{n}\left(z\right)}{w-z}-S_{n}^{\prime}\left(z\right)\right]+\left[S_{n}^{\prime}\left(z\right)-g\left(z\right)\right]+\left[\frac{R_{n}\left(w\right)-R_{n}\left(z\right)}{w-z}\right]{% endequation %}

פיצלתי כאן את הביטוי המקורי לסכום של שלושה ביטויים, תוך שאני גם מחבר ומחסר {% equation %}S_{n}^{\prime}\left(z\right){% endequation %}, מתוך ראייה קדימה שאני אוכל לחסום את הגודל של כל אחד מהביטויים הללו על ידי בחירה נכונה של {% equation %}n,\delta{% endequation %}. אני אמצא ערכים מתאימים כדי שכל אחד מהם בערכו המוחלט יהיה קטן מ-{% equation %}\frac{\varepsilon}{3}{% endequation %}, כך שהסכום של שלושתם לא יעלה על {% equation %}\varepsilon{% endequation %}.

שימו לב שאין בעיה להשתמש ב-{% equation %}S_{n}^{\prime}\left(z\right){% endequation %} כאן: מכיוון ש-{% equation %}S_{n}\left(z\right)=\sum_{k=0}^{n}a_{k}z^{k}{% endequation %} היא פונקציה שמוגדרת על ידי סכום <strong>סופי</strong> הנגזרת שלה קיימת ופשוטה מאוד לחישוב על ידי גזירה "איבר-איבר" של אברי הטור. מה שאנחנו בעצם עושים בהוכחה הזו הוא לקחת את הפשטות הסופית הזו ולגרור אותה מעלה, אל המקרה האינסופי. שימו לב עד כמה הגרירה הזו קשה! המתח הזה שבין "סופי-קל, אינסופי-קשה" חוזר על עצמו בכל מקום במתמטיקה.

את שניים מהביטויים קל לחסום. ראשית, {% equation %}\frac{S_{n}\left(w\right)-S_{n}\left(z\right)}{w-z}-S_{n}^{\prime}\left(z\right){% endequation %} הוא פשוט כי צד שמאל של החיסור הוא בדיוק מה שמופיע בהגדרת הנגזרת של צד ימין: {% equation %}S_{n}^{\prime}\left(z\right)=\lim_{w\to z}\frac{S_{n}\left(w\right)-S_{n}\left(z\right)}{w-z}{% endequation %}. זה אומר שאפשר למצוא {% equation %}\delta>0{% endequation %} כך שלכל {% equation %}0<\left|w-z\right|<\delta{% endequation %} מתקיים {% equation %}\left|\frac{S_{n}\left(w\right)-S_{n}\left(z\right)}{w-z}-S_{n}^{\prime}\left(z\right)\right|<\frac{\varepsilon}{3}{% endequation %}.

שנית, {% equation %}S_{n}^{\prime}\left(z\right)-g\left(z\right){% endequation %} הוא פשוט למדי כי {% equation %}S_{n}^{\prime}\left(z\right){% endequation %} הוא בסך הכל הרישא של הטור {% equation %}g\left(z\right)=\sum_{n=1}^{\infty}na_{n}z^{n-1}{% endequation %}, ולכן {% equation %}\lim_{n\to\infty}S_{n}^{\prime}\left(z\right)=g\left(z\right){% endequation %}, כך שעל פי הגדרת הגבול - קיים {% equation %}N_{1}{% endequation %} כך שלכל {% equation %}n>N_{1}{% endequation %} מתקיים {% equation %}\left|S_{n}^{\prime}\left(z\right)-g\left(z\right)\right|<\frac{\varepsilon}{3}{% endequation %}.

לבסוף, הביטוי שיהיה לי הכי קשה לטפל בו הוא השארית, {% equation %}\frac{R_{n}\left(w\right)-R_{n}\left(z\right)}{w-z}{% endequation %}. אני צריך למצוא עבורה {% equation %}N_{2}{% endequation %} כך שאם {% equation %}n>N_{2}{% endequation %} אז {% equation %}\left|\frac{R_{n}\left(w\right)-R_{n}\left(z\right)}{w-z}\right|<\frac{\varepsilon}{3}{% endequation %}. הבעיה עם השארית הזו היא שיש לנו פה טור אינסופי, אבל די בקלות נוכל לבצע רדוקציה שלו אל הטור {% equation %}g\left(z\right){% endequation %} שכבר טיפלנו בו קודם.

ראשית, על פי ההגדרה של {% equation %}R_{n}{% endequation %}, נקבל{% equation %}\frac{R_{n}\left(w\right)-R_{n}\left(z\right)}{w-z}=\sum_{k=n+1}^{\infty}a_{k}\frac{w^{k}-z^{k}}{w-z}{% endequation %} לכן אם ניקח להכל ערך מוחלט, נקבל

{% equation %}\left|\frac{R_{n}\left(w\right)-R_{n}\left(z\right)}{w-z}\right|\le\sum_{k=n+1}^{\infty}\left|a_{k}\right|\left|\frac{w^{k}-z^{k}}{w-z}\right|{% endequation %}

ביטוי כמו {% equation %}\frac{w^{k}-z^{k}}{w-z}{% endequation %} אפשר לפשט אלגברית:

{% equation %}\frac{w^{k}-z^{k}}{w-z}=w^{k-1}+w^{k-2}z+\ldots+wz^{k-2}+z^{k-1}{% endequation %}

כדי לראות שזה עובד, פשוט כופלים את שני האגפים ב-{% equation %}w-z{% endequation %} ורואים איך באגף ימין כל איבר מתקבל פעמיים עם סימנים שונים, חוץ מ-{% equation %}w^{k}{% endequation %} ו-{% equation %}z^{k}{% endequation %}. עכשיו, בואו ניזכר בכך ש-{% equation %}z{% endequation %} נבחר מלכתחילה כך ש-{% equation %}\left|z\right|<R{% endequation %} ועל {% equation %}w{% endequation %} יש לנו אילוץ ש-{% equation %}\left|z-w\right|<\delta{% endequation %}. אז אפשר למצוא {% equation %}r<R{% endequation %} כך ש-{% equation %}\left|z\right|<r{% endequation %} ולבחור את {% equation %}\delta{% endequation %} כך ש-{% equation %}\left|z-w\right|{% endequation %} קטן מהמרחק מ-{% equation %}z{% endequation %} אל {% equation %}r{% endequation %} כך ש-{% equation %}\left|w\right|<r{% endequation %} גם כן, ואז אפשר למצוא חסם בערך מוחלט על הביטוי שמצאנו קודם:

{% equation %}\left|\frac{w^{k}-z^{k}}{w-z}\right|\le\left|w^{k-1}\right|+\ldots+\left|z^{k-1}\right|\le kr^{k-1}{% endequation %}

כי בסכום הזה יש {% equation %}k{% endequation %} איברים שכל אחד מהם הוא מכפלה של שני מונומים ({% equation %}w{% endequation %} ו-{% equation %}z{% endequation %}) שסכום המעריכים שלהם הוא {% equation %}k-1{% endequation %}.

קיבלנו:

{% equation %}\left|\frac{R_{n}\left(w\right)-R_{n}\left(z\right)}{w-z}\right|\le\sum_{k=n+1}^{\infty}\left|a_{k}\right|kr^{k-1}{% endequation %}

מה שיש באגף ימין דומה מאוד לטור של {% equation %}g\left(z\right){% endequation %}:

{% equation %}g\left(z\right)=\sum_{n=1}^{\infty}na_{n}z^{n-1}{% endequation %}

כבר הוכחנו ש-{% equation %}g\left(z\right){% endequation %} מתכנס לכל {% equation %}\left|z\right|<R{% endequation %}, ולכן הוא בפרט יתכנס עבור {% equation %}z=r{% endequation %} (כי {% equation %}r<R{% endequation %}) ולכן הוא גם יתכנס בערך מוחלט, מה שאומר שזנב הטור יתכנס לאפס. כלומר אפשר למצוא {% equation %}N_{2}{% endequation %} כך שאם {% equation %}n>N_{2}{% endequation %} אז {% equation %}\sum_{k=n+1}^{\infty}\left|a_{k}\right|kr^{k-1}<\frac{\varepsilon}{3}{% endequation %}.

זה בעצם מסיים את ההוכחה! ניקח {% equation %}n=\max\left\{ N_{1},N_{2}\right\} +1{% endequation %} ואת ה-{% equation %}\delta{% endequation %} שבחרנו קודם על בסיס שני האילוצים שצצו לנו בהוכחה, ונקבל {% equation %}\left|\frac{f\left(w\right)-f\left(z\right)}{w-z}-g\left(z\right)\right|<\frac{\varepsilon}{3}+\frac{\varepsilon}{3}+\frac{\varepsilon}{3}=\varepsilon{% endequation %}.

מה יצא לנו מכל זה? ובכן, הוכחה פורמלית למה שנראה על פניו די מובן מאליו: שאם {% equation %}f\left(z\right)=\sum_{n=0}^{\infty}a_{n}\left(z-a\right)^{n}{% endequation %} עם רדיוס התכנסות {% equation %}R{% endequation %} סביב {% equation %}a{% endequation %}, אז {% equation %}f{% endequation %} גזירה בכל התחום הזה (הכדור הפתוח ברדיוס {% equation %}R{% endequation %} סביב {% equation %}a{% endequation %}) והנגזרת שלה היא {% equation %}f^{\prime}\left(z\right)=\sum_{n=1}^{\infty}na_{n}\left(z-a\right)^{n-1}{% endequation %} והיא בעלת אותו רדיוס התכנסות. ואם אפשר לעשות את זה פעם אחת, אפשר לעשות את זה שוב, ולקבל שגם הנגזרת גזירה שוב, והנגזרת שלה היא בעלת אותו רדיוס התכנסות, וכן הלאה עד אינסוף.

זו תוצאה די חזקה, אז בואו נגיד אותה שוב. אני אומר שפונקציה {% equation %}f{% endequation %} היא <strong>אנליטית</strong> בתחום {% equation %}D{% endequation %} אם לכל {% equation %}a\in D{% endequation %}, קיים ל-{% equation %}f{% endequation %} ייצוג באמצעות טור חזקות סביב {% equation %}a{% endequation %} עם רדיוס התכנסות גדול מ-0. צריך את התנאי הזה של "גדול מ-0" כי אנחנו כבר יודעים שאם מרשים רדיוס התכנסות 0, אז כל טור חזקות שהאיבר החופשי שלו הוא {% equation %}f\left(a\right){% endequation %} יעבוד.

מה שהוכחנו כרגע הוא שאם {% equation %}f{% endequation %} היא אנליטית, אז היא גזירה <strong>אינסוף פעמים</strong> בכל נקודה של {% equation %}D{% endequation %}. זו תוצאה חזקה מאוד, אבל בתורת הפונקציות המרוכבות היא מתגלה כחזקה עוד יותר בזכות העובדה שאם פונקציה {% equation %}f{% endequation %} גזירה בכל נקודה של הקבוצה הפתוחה {% equation %}D{% endequation %}, אז היא אנליטית ב-{% equation %}D{% endequation %}. כלומר, כשאנחנו עוסקים בפונקציות מרוכבות, להיות גזיר פעם אחת גורר את להיות גזיר <strong>אינסוף פעמים</strong>, כל עוד הגזירות היא לא "נקודתית" אלא בתחום שלם {% equation %}D{% endequation %}. אין שום מקבילה לתוצאה הזו בתורת הפונקציות הממשיות, וזו בעצם נקודת התחלה לא רעה כדי לראות כמה קסמים מתרחשים באנליזה מרוכבת.

עכשיו בואו נראה עוד משהו. נניח של-{% equation %}f{% endequation %} יש ייצוג בתור {% equation %}f\left(z\right)=\sum_{n=0}^{\infty}a_{n}\left(z-a\right)^{n}{% endequation %} כשלטור יש רדיוס התכנסות גדול מאפס. נציב {% equation %}z=a{% endequation %} ונקבל

{% equation %}f\left(a\right)=a_{0}{% endequation %}

כי שאר האיברים התאפסו. עכשיו נגזור ונקבל

{% equation %}f^{\prime}\left(z\right)=\sum_{n=1}^{\infty}na_{n}\left(z-a\right)^{n-1}{% endequation %}

ולכן אם נציב {% equation %}z=a{% endequation %} נקבל

{% equation %}f^{\prime}\left(a\right)=1\cdot a_{1}{% endequation %}

ואם נגזור שוב, נקבל

{% equation %}f^{\prime\prime}\left(z\right)=\sum_{n=2}^{\infty}n\left(n-1\right)a_{n}\left(z-a\right)^{n-2}{% endequation %}

ולכן

{% equation %}f^{\prime\prime}\left(a\right)=1\cdot2\cdot a_{2}{% endequation %}

ובאופן כללי:

{% equation %}f^{\left(k\right)}\left(a\right)=1\cdot2\cdots k\cdot a_{k}{% endequation %}

או במילים אחרות:

{% equation %}a_{k}=\frac{f^{\left(k\right)}\left(a\right)}{k!}{% endequation %}

וזה נותן לנו את כל אינסוף המקדמים של טור החזקות - מה שמראה שטור החזקות הזה <strong>שווה</strong> למה שקראתי לו טור הטיילור של {% equation %}f{% endequation %}:

{% equation %}f\left(z\right)=\sum_{n=0}^{\infty}\frac{f^{\left(n\right)}\left(a\right)}{n!}\left(z-a\right)^{n}{% endequation %}

עשינו את אותו החשבון גם בפוסט הקודם, אבל עכשיו יש לנו <strong>הצדקה</strong> לעשות אותו. עכשיו גם יש לנו תשובה לשאלה מתחילת הפוסט: התחלנו מהדרישה ש-{% equation %}f{% endequation %} תהיה גזירה אינסוף פעמים. האם זה <strong>הכרחי</strong>, כדי ש-{% equation %}f{% endequation %} תיוצג על ידי טור חזקות? כפי שראינו, התשובה היא <strong>כן</strong>: אם {% equation %}f{% endequation %} מיוצגת על ידי טור חזקות (במובן לא טריוויאלי של טורים עם רדיוס התכנסות 0) אז היא אוטומטית גזירה אינסוף פעמים, ולכן זה אכן הכרחי. זמן טוב לעצור בו. 