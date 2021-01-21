---
id: 3104
title: "התמרת פורייה הבדידה - מה זה בכלל?"
date: 2014-05-21 22:40:48
layout: post
categories: 
  - אנליזה מתמטית
tags: 
  - התמרת פורייה
  - התמרת פורייה הבדידה
---
עד עכשיו ראינו שני סוגים של התמרות פורייה: אחת עבור פונקציות <strong>מחזוריות</strong> מעל הממשיים, כלומר פונקציות שמוגדרות מעל הקטע {% equation %}\left[-\pi,\pi\right]{% endequation %} ואנחנו יכולים "להרחיב" אותן לכל {% equation %}\mathbb{R}{% endequation %} באופן מחזורי; ופונקציות שהוגדרו מראש על כל {% equation %}\mathbb{R}{% endequation %}. להתמרה במקרה הראשון קראנו "טורי פורייה" כי התוצאה המתקבלת היא פירוק של הפונקציה לסכום - טור - של פונקציות בסיס. במקרה השני קיבלנו התמרה שהיא בעצמה פונקציה ממשית. ההבדל בין המקרה הראשון והשני הוא שבמקרה הראשון ההתמרה יוצאת לנו פונקציה<strong> </strong>שמוגדרת על מרחב <strong>בדיד </strong>בזמן שבמקרה השני יוצאת לנו פונקציה על מרחב <strong>רציף</strong>.

מה זה בדיוק מרחב רציף ומה זה בדיוק מרחב בדיד קשה לומר בלי הגדרות נוספות וזה לא קריטי לנו כרגע, אבל אינטואיציה לא רעה לעומק ההבדל היא שמרחב בדיד הוא בן מניה - יש לו מספר "קטן יחסית" של איברים, בזמן ש-{% equation %}\mathbb{R}{% endequation %} היא קבוצה לא בת מניה - יש בה "המון" איברים. ההבדל הזה גורם להבדלים טכניים ברורים - מעל מרחב בדיד יש משמעות לדיבור על טורים, מעל מרחב רציף התורה של טורים כבר לא עובדת וצריך לדבר על אינטגרלים במקום זה. גם בהסתברות יש לנו את התופעה הזו ואפשר לראות הבדל מובהק בין הסתברות על מרחב בדיד - שהיא פשוטה ונחמדה ואינטואיטיבית יחסית - ובין הסתברות על מרחב רציף שהיא מהומה שלמה. וכמובן, ייצוגים של פונקציות במחשב הם לרוב ייצוגים בדידים. אמנם, אפשר לאכסן במחשב במדויק פונקציה כמו {% equation %}f\left(x\right)=x^{2}{% endequation %} גם אם היא מוגדרת מעל הממשיים, אבל עבור פונקציות כלליות, שנתונות לנו בעיקר בתור אוסף זוגות קלט-פלט, זה כבר לא אפשרי.

כל המבוא הזה בא לומר שהצעד המתבקש הבא אחרי מה שכבר ראינו הוא לדבר על התמרת פורייה עבור פונקציות שמוגדרות לא מעל {% equation %}\mathbb{R}{% endequation %} אלא מעל {% equation %}\mathbb{Z}{% endequation %}. כמקודם, אני רוצה לדבר על שני מקרים שונים - זה של פונקציות מחזוריות וזה של פונקציות לא מחזוריות. הראשונות יהיו מעניינות במיוחד כי הן ניתנות לתיאור על ידי סדרה <strong>סופית</strong> של מספרים - כלומר, כולן ניתנות לייצוג מדויק לחלוטין במחשב. לשתי ההתמרות הללו אקרא "התמרת פורייה הבדידה", למרות שלרוב מי שמשתמש בביטוי הזה מתכוון רק למקרה של פונקציות מחזוריות, והמקרה השני מכונה לעתים "התמרת פורייה בזמן בדיד" כדי להבדיל ביניהם.

נתחיל, כרגיל, מהתיאוריה הבסיסית; אבל אחר כך אעבור סוף סוף להמחשה של שימוש בסיסי כלשהו לכל העסק הזה, על ידי הכנסת מושג מורכב יותר שנקרא <strong>קונבולוציה</strong>. הייתי יכול להראות קונבולוציות כבר קודם, אבל אני חושב שההקשר שבו הכי קל לעכל אותם הוא ההקשר הבדיד ולכן התאפקתי עד כה.

בשלב הזה אנחנו כבר למודי קרבות עם התמרות פורייה ויודעים מה מצפה לנו - מה שקראתי לו משוואות סינתזה ואנליזה. משוואת אנליזה לוקחת פונקציה ו"מפרקת" אותה לרכיבים - כלומר, נותנת לנו את ההתמרה של הפונקציה. משוואת סינתזה לוקחת את הרכיבים ו"בונה מחדש" את הפונקציה - כלומר, נותנת לנו את ההתמרה ההפוכה של הפונקציה. ה"רכיבים" שלנו בהקשר של פורייה הן פונקציות טריגונומטריות - בפוסט הקודם עברתי להשתמש באקספוננט מרוכב במקום לכתוב במפורש סינוסים וקוסינוסים.

לצורך תזכורת, הנה משוואות האנליזה והסינתזה של פונקציות {% equation %}f:\mathbb{R}\to\mathbb{C}{% endequation %} ו-{% equation %}g:\left[-\pi,\pi\right]\to\mathbb{C}{% endequation %}:

<strong>אנליזה</strong>:

{% equation %}\hat{f}\left(\omega\right)=\int_{-\infty}^{\infty}f\left(t\right)e^{-2\pi i\omega t}dt{% endequation %}

{% equation %}\hat{g}\left(n\right)=\frac{1}{2\pi}\int_{-\pi}^{\pi}g\left(x\right)e^{-inx}dx{% endequation %}

<strong>סינתזה:</strong>

{% equation %}f\left(t\right)=\int_{-\infty}^{\infty}\hat{f}\left(\omega\right)e^{2\pi i\omega t}d\omega{% endequation %}

{% equation %}g\left(x\right)=\sum_{n=-\infty}^{\infty}\hat{g}\left(n\right)e^{inx}{% endequation %}

עכשיו בואו נעבור לדבר על פונקציות בדידות. ניקח פונקציה {% equation %}f:\mathbb{Z}\to\mathbb{C}{% endequation %} ופונקציה {% equation %}g:\mathbb{Z}_{N}\to\mathbb{C}{% endequation %} כאשר {% equation %}N{% endequation %} הוא מספר טבעי חיובי כלשהו. {% equation %}\mathbb{Z}_{N}=\left\{ 0,1,2,\dots,N-1\right\} {% endequation %} למי שתוהה מה פשר הסימון הזה ולא מכיר אותו.

בואו נתחיל מ-{% equation %}f{% endequation %}. איך משוואת האנליזה שלה תיראה? האם הגיוני לכתוב {% equation %}\hat{f}\left(\omega\right)=\int_{-\infty}^{\infty}f\left(t\right)e^{-2\pi i\omega t}dt{% endequation %} גם במקרה הזה? התשובה היא כמובן "לא", כי {% equation %}f\left(t\right){% endequation %} לא מוגדרת כמעט עבור אף ערך של {% equation %}t{% endequation %}. אנחנו הולכים להצטמצם רק לערכים שבהם {% equation %}f{% endequation %} מוגדרת, ולכן נעבור מאינטגרל לסכום:

{% equation %}\hat{f}\left(\omega\right)=\sum_{n=-\infty}^{\infty}f\left(n\right)e^{-2\pi i\omega n}{% endequation %}

{% equation %}\hat{f}{% endequation %} היא פונקציה ממשית - לכל מספר ממשי שנציב בה, יש הגיון מאחורי הערך שנקבל. אבל די קל לראות שזו תהיה פונקציה <strong>מחזורית</strong>: באופן כללי, {% equation %}e^{2\pi ik}=1{% endequation %} לכל {% equation %}k{% endequation %} שלם (זה מייצג {% equation %}k{% endequation %} סיבובים נגד כיוון השעון על מעגל ברדיוס 1 כשנקודת ההתחלה שלנו היא הנקודה {% equation %}\left(1,0\right){% endequation %}), ולכן {% equation %}e^{-2\pi i\left(\omega+k\right)n}=e^{-2\pi i\omega n}\cdot e^{-2\pi ikn}=e^{-2\pi i\omega n}\cdot\left(e^{2\pi ik}\right)^{-n}=e^{-2\pi i\omega n}{% endequation %}. זה כמובן לא מפתיע בכלל - ראינו שפונקציה מחזורית על {% equation %}\mathbb{R}{% endequation %} עוברת לפונקציה על {% equation %}\mathbb{Z}{% endequation %} על ידי התמרת פורייה, ושיש התמרה בכיוון ההפוך שמחזירה את הפונקציה על {% equation %}\mathbb{Z}{% endequation %} להיות פונקציה מחזורית על {% equation %}\mathbb{R}{% endequation %}; מה שאנחנו עושים כרגע הוא פשוט להתחיל מהפונקציה על {% equation %}\mathbb{Z}{% endequation %}, אבל מה ההבדל?

התשובה היא שאין ממש הבדל - משוואות האנליזה והסינתזה יכולות להילקח מהמשוואות המתאימות עבור טורי פורייה, עם היפוך סימנים ותו לא:

<strong>אנליזה</strong>:

{% equation %}\hat{f}\left(x\right)=\sum_{n=-\infty}^{\infty}f\left(n\right)e^{-inx}{% endequation %}

<strong>סינתזה:</strong>

{% equation %}f\left(n\right)=\frac{1}{2\pi}\int_{-\pi}^{\pi}\hat{f}\left(x\right)e^{inx}dx{% endequation %}

בשל כך, אני רוצה לקפוץ אל החלק היותר מעניין של הפוסט - המקרה שבו יש לנו פונקציה מחזורית על הטבעיים, {% equation %}g:\mathbb{Z}_{N}\to\mathbb{C}{% endequation %}. במקרה הזה, אפשר לזהות את הפונקציה עם סדרת הערכים שהיא מחזירה - סדרה שאסמן {% equation %}a_{0},a_{1},a_{2},\dots,a_{N-1}{% endequation %} (כלומר - {% equation %}a_{k}=g\left(k\right){% endequation %}). התמרת פורייה לוקחת את סדרת הערכים הזו ומחזירה, כרגיל, את המקדמים בפירוק שלה לרכיבים. וממי יורכבו הרכיבים הללו? הבה וניזכר מה קרה בטורי פורייה המקוריים - התחלנו מפונקציה מחזורית, ומצאנו פונקציות מחזוריות "קנוניות" שבעזרתן נבנה אותה. גם כאן אנו מתחילים מפונקציה {% equation %}N{% endequation %}-מחזורית, ולכן רוצים פונקציות אקספוננט שהן {% equation %}N{% endequation %}-מחזוריות (על קלטים שהם מספרים שלמים). לא קשה במיוחד לראות שאלו חייבות להיות פונקציות מהצורה {% equation %}t\left(n\right)=e^{\frac{2\pi ik}{N}n}{% endequation %} כאשר {% equation %}0\le k&lt;N{% endequation %}. למה? כי בואו נניח ש-{% equation %}t\left(n\right)=e^{isn}{% endequation %} היא פונקצית אקספוננט {% equation %}N{% endequation %}-מחזורית, כלומר {% equation %}e^{isn}=e^{is\left(n+N\right)}{% endequation %}, אז נקבל {% equation %}e^{isN}=1{% endequation %}. עכשיו, למשוואה הזו יש פתרון רק אם {% equation %}2\pi|sN{% endequation %}, כלומר רק אם קיים {% equation %}k{% endequation %} כך ש-{% equation %}2\pi k=sN{% endequation %}, כלומר {% equation %}s=\frac{2\pi k}{N}{% endequation %}, כנדרש.

עכשיו, התרגלנו לחשוב על האקספוננטים שלנו בתור סינוסים וקוסינוסים, אבל בהקשר הנוכחי שלנו יש לפונקציות {% equation %}t\left(n\right)=e^{\frac{2\pi ik}{N}n}{% endequation %} משמעות נוספת - אלו הם <strong>שורשי היחידה</strong> מסדר {% equation %}N{% endequation %}. תזכורת: מספר מרוכב {% equation %}x{% endequation %} הוא שורש יחידה מסדר {% equation %}N{% endequation %} אם {% equation %}x^{N}=1{% endequation %} (במספרים הממשיים יש רק שני מספרים שחזקה שלהם יכולה לתת 1 - רק 1 עצמו ומינוס 1, ולכן זה מעניין רק בהקשר של מספרים מרוכבים). שורשי היחידה מסדר {% equation %}N{% endequation %} הם <strong>חבורה כפלית</strong> - אם כופלים שניים מהם מקבלים שוב פעם שורש יחידה מסדר {% equation %}N{% endequation %}. כמו כן, אם נסמן {% equation %}\omega=e^{\frac{2\pi i}{N}}{% endequation %} (אין קשר בין הסימן {% equation %}\omega{% endequation %} כאן לסימן שהשתמשנו בו קודם בשביל לתאר את המשתנה של "מרחב התדר" - זה פשוט אותו סימן שמשמש בהקשרים שונים) נקבל שורש יחידה מסדר {% equation %}N{% endequation %} שחזקות שלו נותנות את כל יתר שורשי היחידה - כל שורשי היחידה מסדר {% equation %}N{% endequation %} הם {% equation %}\omega^{0},\omega^{1},\omega^{2},\omega^{3},\dots\omega^{N-1}{% endequation %}. לצורך פשטות נהוג לסמן {% equation %}\omega_{k}=\omega^{k}{% endequation %} (למה? כי לעתים קרובות מעלים בחזקה כלשהי את ה-{% equation %}\omega_{k}{% endequation %} ולא רוצים שהחזקה ה-{% equation %}k{% endequation %}-ית "תתנגש" עם החזקה הנוספת).

אז אם לסכם - נתונה לנו סדרת מספרים מרוכבים {% equation %}a_{0},a_{1},\dots,a_{N-1}{% endequation %}. אני רוצה לייצג אותה איכשהו בתור צירוף לינארי של הפונקציות {% equation %}t_{k}\left(n\right)=\omega_{k}^{n}{% endequation %}. כלומר, אני רוצה למצוא מקדמים מרוכבים {% equation %}b_{0},b_{1},\dots,b_{N-1}{% endequation %} כך שמתקיים:

{% equation %}a_{n}=\sum_{k=0}^{N-1}b_{k}\omega_{k}^{n}{% endequation %}

זו משוואת הסינתזה שלנו - אחר כך אכתוב אותה בצורה הסטנדרטית של פונקציות, אבל לעת עתה בואו ננסה להבין מה משוואת האנליזה תהיה - כלומר, איך מוצאים את ה-{% equation %}b{% endequation %}-ים. יש כמה דרכים לעשות זאת, כמובן, והחביבה עלי הולכת ישירות דרך אלגברה לינארית - אחרי ככלות הכל, מה שיש לנו פה הוא את המרחב הוקטור {% equation %}\mathbb{C}^{N}{% endequation %} שהוא סוף-ממדי ולכן האלגברה הלינארית שלנו תהיה נחמדה וקלה. יחסית.

אם אסמן ב-{% equation %}\overline{a}{% endequation %} את הוקטור {% equation %}\overline{a}=\left(a_{0},a_{1},\dots,a_{N-1}\right){% endequation %} ובדומה אסמן גם את הוקטור {% equation %}\overline{b}{% endequation %}, אז נשים לב שמשוואות הסינתזה הן דרך לכתוב {% equation %}\overline{a}=W\cdot\overline{b}{% endequation %} כאשר {% equation %}W{% endequation %} היא מטריצה שמקודדת בתוכה את כל חזקות שורשי היחידה מסדר {% equation %}N{% endequation %}, בצורה הבאה: {% equation %}W_{nk}=\omega_{k}^{n}{% endequation %}. קונקרטית, הנה איך שהיא נראית:

{% equation %}W=\left[\begin{array}{ccccc}1 & 1 & 1 & \cdots & 1\\1 & \omega & \omega_{2} & \cdots & \omega_{N-1}\\1 & \omega^{2} & \omega_{2}^{2} & \dots & \omega_{N-1}^{2}\\\vdots & \vdots & \vdots & & \vdots\\1 & \omega^{N-1} & \omega_{2}^{N-1} & \cdots & \omega_{N-1}^{N-1}\end{array}\right]{% endequation %}

מה קורה כאן? כל עמודה מכילה את כל החזקות של אחד משורשי היחידה מסדר {% equation %}N{% endequation %}, החל מ-1 הטריוויאלי, עבור ב-{% equation %}\omega{% endequation %} וכלה בכל החזקות של {% equation %}\omega{% endequation %} עד {% equation %}\omega_{N-1}{% endequation %}. מטריצות כאלו הן מספיק מעניינות כדי לזכות לשם מיוחד משל עצמן - <strong>מטריצות ונדרמונדה</strong>, אם כי לרוב השם הזה מיועד למטריצות שבהן החזקות של האיברים הם <strong>בשורות</strong> ולא בעמודות. המבנה הכללי של מטריצת ונדרמונדה מסדר {% equation %}N\times N{% endequation %} על האיברים {% equation %}\alpha_{1},\dots,\alpha_{N}{% endequation %} הוא זה:

{% equation %}V\left(\alpha_{1},\dots,\alpha_{N}\right)=\left[\begin{array}{cccc}\alpha_{1}^{0} & \alpha_{1}^{1} & \cdots & \alpha_{1}^{N-1}\\\alpha_{2}^{0} & \alpha_{2}^{1} & \dots & \alpha_{2}^{N-1}\\\vdots & \vdots & & \vdots\\\alpha_{N-1}^{0} & \alpha_{N-1}^{1} & \cdots & \alpha_{N-1}^{N-1}\end{array}\right]{% endequation %}

אם נחשוב על זה לרגע נשים לב לכך ש-{% equation %}W{% endequation %} היא סימטרית, ולכן היא גם מטריצת ונדרמונדה במובן הרגיל של ההגדרה, אבל זה לא יהיה חשוב לנו כל כך כרגע.

מה שאנחנו רוצים לעשות הוא למצוא את ההופכית של {% equation %}W{% endequation %}, כדי לפתור את המשוואה {% equation %}\overline{a}=W\cdot\overline{b}{% endequation %} - נוכל להסיק ש-{% equation %}\overline{b}=W^{-1}\cdot\overline{a}{% endequation %}, והנה קיבלנו דרך מעשית לחשב את התמרת פורייה הבדידה. להפוך את {% equation %}W{% endequation %} זה סיפור מעניין - אמנם, יש נוסחה כללית להופכית של מטריצת ונדרמונדה אבל היא לא טריוויאלית, וכך גם להשתמש בשיטות הסטנדרטיות למציאת הופכית של מטריצה. הכי טוב אם פשוט אצליח לנחש את ההגדרה של {% equation %}W^{-1}{% endequation %} מהשמיים ואוכיח שהיא עובדת. מה הניחוש הכי טוב שלנו? ובכן, אנחנו מחפשים מטריצה שמקודדת משוואת אנליזה - משוואה שנותנת את {% equation %}b_{n}{% endequation %} בתור סכום כלשהו של {% equation %}a_{n}{% endequation %}. אפשר להתפלל שהמשוואה הזו תהיה דומה באופיה למשוואות של המקרה הרציף, לנסות, ולראות מה קורה.

אם משוואת הסינתזה של התמרת פורייה הבדידה היא זו:

{% equation %}g\left(n\right)=\sum_{k=0}^{N-1}\hat{g}\left(k\right)e^{\frac{2\pi ikn}{N}}{% endequation %}

אז אפשר לנחש שמשוואת האנליזה תהיה זו:

{% equation %}\hat{g}\left(n\right)=\sum_{k=0}^{N-1}g\left(k\right)e^{-\frac{2\pi ikn}{N}}{% endequation %}

זה רק ניחוש, ותכף נראה שהוא לא מדויק (צריך גם לכפול בקבוע כלשהו, כמו ה-{% equation %}\frac{1}{2\pi}{% endequation %} של המשוואה עבור טורי פורייה) אבל הוא למעשה לא רע בכלל. כדי לפשט עניינים נחזור לסמן {% equation %}\omega_{k}^{n}=e^{\frac{i\pi kn}{N}}{% endequation %}, והמינוס הזה מטופל על ידי מעבר לצמוד המרוכב: {% equation %}e^{-\frac{i\pi kn}{N}}=\overline{\omega_{k}^{n}}{% endequation %}. אם כן, המועמד שלנו להיות ההופכי של {% equation %}W{% endequation %} היא המטריצה {% equation %}W^{*}{% endequation %} - המטריצה הצמודה של {% equation %}W{% endequation %}, שמתקבלת על ידי שחלוף (שלא משנה כלום) והצמדה. עכשיו, כדי לפשט נוסחאות עם הצמוד, בואו נחשוב שניה על דרך יותר פשוטה לסמן אותו: {% equation %}\omega\cdot\overline{\omega}=\left|\omega\right|^{2}=1{% endequation %} ולכן {% equation %}\overline{\omega}=\omega^{-1}{% endequation %} (למעשה, אפשר לראות את זה מיידית מההגדרה). לכן באופן כללי {% equation %}\overline{\omega_{k}^{n}}=\omega_{k}^{-n}{% endequation %}.

כעת, הבה ונתבונן ב-{% equation %}\left(WW^{*}\right)_{nk}{% endequation %}:

{% equation %}\left(WW^{*}\right)_{nk}=\sum_{i=0}^{N-1}W_{ni}W_{ik}^{*}=\sum_{i=0}^{N-1}\omega_{i}^{n}\overline{\omega_{i}^{k}}=\sum_{i=0}^{N-1}\omega_{i}^{n-k}{% endequation %}

כאשר {% equation %}n=k{% endequation %} נקבל {% equation %}\omega_{i}^{n-k}=1{% endequation %} ולכן {% equation %}\sum_{i=0}^{N-1}\omega_{i}^{n-k}=N{% endequation %}. לעומת זאת, המקרה שבו {% equation %}n\ne k{% endequation %} מעניין יותר. אם לשאוב אינטואיציה ממה שקרה בטורי פורייה, אנחנו מצפים שהסכום יצא 0 במקרה הזה - אבל למה? ובכן, שימו לב לכך ש-{% equation %}\sum_{i=0}^{N-1}\omega_{i}^{n-k}=\sum_{i=0}^{N-1}\omega_{n-k}^{i}{% endequation %}, כלומר אפשר לחשוב על הסכום הזה בתור <strong>טור גאומטרי</strong> - סכום חזקות של שורש יחידה כלשהו מסדר {% equation %}N{% endequation %}. לטור גאומטרי יש באופן כללי נוסחה פשוטה: {% equation %}\sum_{i=0}^{t}a^{i}=\frac{a^{t+1}-1}{a-1}{% endequation %}, ולכן במקרה שלנו נקבל {% equation %}\sum_{i=0}^{N-1}\omega_{n-k}^{i}=\frac{\omega_{n-k}^{N}-1}{\omega_{n-k}-1}=0{% endequation %} - האיבר במונה מתאפס כי {% equation %}\omega_{n-k}^{N}=1{% endequation %} (זו המשמעות של להיות שורש יחידה מסדר {% equation %}N{% endequation %}).

לסיכום, {% equation %}WW^{*}=NI{% endequation %}, כלומר זו מטריצה סקלרית שיש בה {% equation %}N{% endequation %} באלכסון הראשי ו-0 בכל מקום אחר. זה אומר שאפשר להפוך את {% equation %}W{% endequation %} למטריצה אוניטרית על ידי נרמול - חלוקה ב-{% equation %}\sqrt{N}{% endequation %} - אבל לא נזדקק לזה. די לנו במסקנה: {% equation %}W^{-1}=\frac{1}{N}W^{*}{% endequation %}. זה נותן לנו את משוואת האנלזיה שחיפשנו:

{% equation %}b_{n}=\frac{1}{N}\sum_{k=0}^{N-1}a_{k}\omega_{k}^{-n}{% endequation %}

המשוואות הללו נותנות לנו אלגוריתם פרקטי לגמרי לחישוב התמרת פורייה הבדידה, גם במחשב, אבל זה לא סוף הסיפור. אם רוצים להשתמש בהתמרה בשביל דברים כמו זה שאראה עוד מעט, רצוי שתהיה דרך מהירה <strong>עוד יותר</strong> לחשב אותה - ומה שיפה הוא שדרך כזו קיימת, פחות או יותר עוד מזמנו של גאוס, לפני פורייה בכלל. שיטות חישוב מהירות של התמרת פורייה הבדידה נקראות, באופן הולם למדי, "התמרת פורייה מהירה" (Fast Fourier Transform, או FFT בקיצור) ואני אראה את השיטה הידועה ביותר בפוסט נפרד.

בפוסט הקודם הראיתי שיש קשר בין התמרת פורייה של פונקציות ממשיות כלליות ובין התמרת פורייה של פונקציות ממשיות מחזוריות ("טורי פורייה"), שבא לידי ביטוי ב<strong>דיאגרמה קומוטטיבית</strong>:

{% equation %}\begin{array}{ccc}f & \leftrightarrow & \hat{f}\\\downarrow & & \downarrow\\g & \leftrightarrow & \hat{g}\end{array}{% endequation %}

כאשר המעבר מ-{% equation %}f{% endequation %} אל {% equation %}g{% endequation %} התבצע על ידי פעולה של <strong>סכימה</strong> (שלקחה פונקציה כללית והפכה אותה למחזורית) והמעבר מ-{% equation %}\hat{f}{% endequation %} אל {% equation %}\hat{g}{% endequation %} התבצע על ידי <strong>דגימה</strong> (שלקחה פונקציה על מרחב רציף והפכה אותה לפונקציה על מרחב בדיד). בצורה לא מפתיעה במיוחד, אותה דיאגרמה (עם אותן פעולות, עד כדי הפרמטרים שלהן שעשויים להיות שונים) מתאימה גם להתמרות שראינו הפעם - התמרה של פונקציה "כללית" על {% equation %}\mathbb{Z}{% endequation %} והתמרה של פונקציה מחזורית על {% equation %}\mathbb{Z}{% endequation %}. אז יש לנו עוד עותק של הדיאגרמה

{% equation %}\begin{array}{ccc}u & \leftrightarrow & \hat{u}\\\downarrow & & \downarrow\\v & \leftrightarrow & \hat{v}\end{array}{% endequation %}

עכשיו, די בבירור יש לנו מעברים מהפונקציות {% equation %}f{% endequation %} אל {% equation %}u{% endequation %} ומ-{% equation %}g{% endequation %} אל {% equation %}v{% endequation %} על ידי דגימה (הסבירו לעצמכם למה!) ומ-{% equation %}\hat{f}{% endequation %} אל {% equation %}\hat{u}{% endequation %} ומ-{% equation %}\hat{g}{% endequation %} אל {% equation %}\hat{v}{% endequation %} על ידי סכימה (עם פרמטרים ספציפיים שונים לכל סכימה). אז אנחנו מקבלים דיאגרמה קומוטטיבית דמויית קוביה, שהדיאגרמה הראשונה שהראיתי היא הפאה העליונה שלה, והדיאגרמה השניה היא הפאה התחתונה שלה. נסו לצייר אותן!

כעת, בואו נעבור להדגמה הפשוטה ביותר שאני יכול לחשוב עליה על שימוש יעיל להתמרת פורייה הבדידה (ולהתמרות פורייה באופן כללי). בשביל זה אני צריך את מושג ה<strong>קונבולוציה</strong> שלדעתי הכי קל להסביר דרך המושג של כפל פולינומים.

בואו נסתכל לרגע על המכפלה הבאה של שני פולינומים ממעלה שנייה: {% equation %}\left(a_{2}x^{2}+a_{1}x+a_{0}\right)\left(b_{2}x^{2}+b_{1}x+b_{0}\right){% endequation %}. אני הולך לפתוח את המכפלה ולכתוב את כל האיברים לא כי בא לי לעשות חשבון אלא כי זה יהיה סופר-חשוב להמשך לראות מה קורה כאן. תנסו לעקוב אחרי מה שעשיתי ולבצע את החישוב בראש בעצמכם (הכי טוב אם תעשו את זה על נייר - אבל נו טוב, אני לא מצפה שמישהו יתחיל לכתוב באמצע קריאת פוסט). מה שאני מקבל הוא זה:

{% equation %}a_{2}b_{2}x^{4}+\left(a_{1}b_{2}+a_{2}b_{1}\right)x^{3}+\left(a_{0}b_{2}+a_{1}b_{1}+a_{2}b_{0}\right)x^{2}+\left(a_{0}b_{1}+a_{1}b_{0}\right)x+a_{0}b_{0}{% endequation %}

לפתוח את הכל ידנית זה סיפור לא כיפי, ולכן מה שעושה המתמטיקאי אחרי שהוא מקבל את הנוסחה הזו הוא להביט בה ולנסות להבין מה התבנית שיש כאן - מה ההגיון הכללי מאחורי הנוסחה. אני מקבל סכום של חזקות של {% equation %}x{% endequation %} עם מקדמים שנבנים איכשהו מהמקדמים של הפולינומים שהכפלתי, אבל על פי איזו חוקיות? בואו נסתכל לרגע על המקדם הכי מסובך, זה של {% equation %}x^{2}{% endequation %}. כשאנחנו כופלים את הביטוי {% equation %}\left(a_{2}x^{2}+a_{1}x+a_{0}\right)\left(b_{2}x^{2}+b_{1}x+b_{0}\right){% endequation %} אנחנו בעצם בוחרים איבר מהסוגריים השמאליים ואיבר מהסוגריים הימניים, כופלים אותם, וסוכמים את כל המכפלות שמתקבלות כך. כל מכפלה כזו ש-{% equation %}x^{2}{% endequation %} מופיע בה עם מקדם קבוע כלשהו תתרום את המקדם הזה למקדם של {% equation %}x^{2}{% endequation %} בתוצאה הסופית. כך שנשאלת השאלה - באילו דרכים אפשר לבחור איבר מהסוגריים השמאליים ואיבר מהסוגריים הימניים ולכפול אותם כדי לקבל משהו קבוע כפול {% equation %}x^{2}{% endequation %}?

ובכן, זה פשוט מאוד: צריך לבחור מהסוגריים איברים שסכום חזקות ה-{% equation %}x{% endequation %} שלהם שווה ל-2. כלומר, {% equation %}a_{2}x^{2}\cdot b_{0}x^{0}{% endequation %} (כי {% equation %}2+0=2{% endequation %}) ו-{% equation %}a_{1}x^{1}\cdot b_{1}x^{1}{% endequation %} ו-{% equation %}a_{0}x^{0}\cdot b_{2}x^{2}{% endequation %}. זה נותן לנו בדיוק את המקדם של {% equation %}x^{2}{% endequation %} שראינו כאן.

ומה קורה באופן הכי כללי שרק אפשר? בואו ניקח שני פולינומים {% equation %}\sum_{k=0}^{t}a_{k}x^{k}{% endequation %} ו-{% equation %}\sum_{k=0}^{t}b_{k}x^{k}{% endequation %} (חלק מהמקדמים עלולים להיות 0 ואין עם זה בעיה) ונכפול אותם: נקבל פולינום {% equation %}\sum_{k=0}^{r}c_{k}x^{k}{% endequation %} שמקיים באופן כללי:

{% equation %}c_{n}=\sum_{k=0}^{n}a_{k}b_{n-k}{% endequation %}

כלומר - {% equation %}c_{n}{% endequation %} הוא סכום שבו מכפילים את כל ה-{% equation %}a_{k}{% endequation %}-ים עד {% equation %}a_{n}{% endequation %} ב-{% equation %}b{% endequation %}-ים, אבל ב-{% equation %}b{% endequation %}-ים שבאים בסדר <strong>הפוך - </strong>מתחילים ב-{% equation %}b_{n}{% endequation %} ומגיעים עד ל-{% equation %}b_{0}{% endequation %}. שימו לב שהמשכי שתי הסדרות (האיברים שאחרי האיברים במקום ה-{% equation %}n{% endequation %}) בכלל לא רלוונטיים.

סדרת ה-{% equation %}c_{n}{% endequation %}-ים הזו היא בדיוק מה שנקרא <strong>קונבולוציה</strong> של הסדרות {% equation %}a_{n},b_{n}{% endequation %}. בואו נגדיר את זה פורמלית: אם {% equation %}a_{0},a_{1},a_{2},\dots{% endequation %} ו-{% equation %}b_{0},b_{1},b_{2},\dots{% endequation %} הן סדרות (שיכולות להיות אינסופיות, אין עם זה בעיה) אז הקונבולוציה שלהן היא סדרה {% equation %}c_{0},c_{1},c_{2},\dots{% endequation %} שמוגדרת על ידי הנוסחה שכבר נתתי: {% equation %}c_{n}=\sum_{k=0}^{n}a_{k}b_{n-k}{% endequation %}.

אני מאוד אוהב להציג את העניין הזה בצורה ציורית. בואו נכתוב את אברי הסדרה {% equation %}a_{n}{% endequation %}, ומעליהם נכתוב את אברי הסדרה {% equation %}b_{n}{% endequation %} אבל בסדר הפוך, כך שנקודת ה"חיבור" היחידה שלהם היא באיברים עם אינדקס 0:

{% equation %}\begin{array}{ccccccc}\cdots & b_{2} & b_{1} & b_{0}\\ & & & a_{0} & a_{1} & a_{2} & \cdots\end{array}{% endequation %}

חשבו על המקומות שנותרו ריקים בתור 0-ים.

עכשיו נכפול כל איבר בשורה העליונה באיבר שבדיוק מתחתיו בשורה התחתונה, ונסכום הכל. די ברור שכל הכפולות פרט למספר סופי יהיו 0 כך שהסכום הוא בעצם סופי, ולכן מוגדר היטב, וגם קל לראות שהוא פשוט יהיה {% equation %}a_{0}b_{0}{% endequation %}. עד כאן, כתיבה מסובכת לדבר פשוט, אבל הנה האופן שבו אני מקבל את האיבר הבא בסכום: אקח את סדרת ה-{% equation %}b{% endequation %}-ים שבשורה העליונה ואזיז אותה צעד אחד ימינה:

{% equation %}\begin{array}{ccccccc}\cdots & b_{3} & b_{2} & b_{1} & b_{0}\\ & & & a_{0} & a_{1} & a_{2} & \cdots\end{array}{% endequation %}

כעת הכפלה של כל זוג איברים וסכום של כולם תניב לי את {% equation %}a_{0}b_{1}+a_{1}b_{0}{% endequation %}, וכן הלאה וכן הלאה. {% equation %}c_{n}{% endequation %} יתקבל אחרי שאזיז את ה-{% equation %}b{% endequation %}-ים למעלה {% equation %}n{% endequation %} צעדים ימינה, אכפול ואסכום. התיאור הציורי הזה נותן לי אישית אינטואיציה טובה לגבי "מה הולך כאן בכלל".

כמובן שההגדרה של קונבולוציה היא יותר כללית מאשר "רק" עבור סדרות. הנה הגדרה דומה עבור פונקציות {% equation %}f:\mathbb{R}\to\mathbb{C}{% endequation %}, כאשר אני משתמש בסימן {% equation %}*{% endequation %} כדי לסמן קונבולוציה: {% equation %}\left(f*g\right)\left(t\right)=\int_{-\infty}^{\infty}f\left(x\right)g\left(t-x\right)dx{% endequation %}. אפשר גם לתת הגדרה כללית יותר שמתאימה לכל הקשר שבו אפשר לדבר על התמרת פורייה, אבל לא אכנס לכך כרגע.

כפי שכבר הבנו מהמקרה של פולינומים, קונבולוציה היא לא פעולה טריוויאלית לחישוב. מצד שני, כפי שכבר הבנו מהמקרה של פולינומים, קונבולוציה היא משהו שצץ באופן טבעי במתמטיקה, בין אם אנחנו מדברים על התמרת פורייה ובין אם לאו. ולכן הקשר של התמרת פורייה לקונבולוציות הוא לא טריוויאלי ומעניין. ומה הקשר הזה? פשוט מאוד: ההתמרה של קונבולוציה היא מכפלת ההתמרות. בנוסחה, אם {% equation %}f,g{% endequation %} הן פונקציות ואם אני מסמן ב-{% equation %}\mathcal{F}\left[f\right],\mathcal{F}\left[g\right]{% endequation %} את התמרות הפורייה שלהן (וזו יכולה להיות כל אחת משלושת סוגי ההתמרות שכבר ראינו, וזה עובד גם להתמרות פורייה בהקשרים אחרים שלא ראינו), אז {% equation %}\mathcal{F}\left[f*g\right]=\mathcal{F}\left[f\right]\cdot\mathcal{F}\left[g\right]{% endequation %}.

בפרט, אם אנחנו יודעים גם לחשב את ההתמרה ההפוכה, {% equation %}\mathcal{F}^{-1}{% endequation %}, זה נותן לנו שיטה פשוטה לחשב קונבולוציות: {% equation %}f*g=\mathcal{F}^{-1}\left[\mathcal{F}\left[f\right]\cdot\mathcal{F}\left[g\right]\right]{% endequation %}. עוברים ל"מישור התדר", מבצעים את הכפל שם, ואז חוזרים למשתנה המקורי. נראה מוכר? באלגברה לינארית עושים את זה כל הזמן - אם יש לנו פעולה מסובכת בבסיס הנוכחי שלנו (למשל, העלאה בחזקה גבוהה של איזה אופרטור) אז עוברים לבסיס אחר, נוח יותר, מבצעים את החישוב שם, ואז חוזרים לבסיס המקורי. במובן מסויים זו בדיוק המהות של התמרות פורייה - מעבר לבסיס נוח יותר לצרכים מסויימים.

לא סתם התחלתי מדוגמת הפולינומים. התעלול הזה של ההתמרות נותן לנו אלגוריתם יעיל לכפל פולינומים - יותר יעיל מאשר פשוט לבצע חישוב. זה לא קריטי לפולינומים קטנים, אבל תחשבו על פולינומים עם אלפי מקדמים (או יותר!). כמובן, זה דורש שההתמרות יתבצעו בעזרת FFT, כך שהאלגוריתם שמבצע את הכפל המהיר הזה הוא לא טריוויאלי - אבל <strong>עושים את זה בפועל כי זה עובד טוב</strong> (למעשה, משתמשים בהתמרת פורייה מהירה גם כדי לחשב כפל של מספרים רגילים עם כמות גדולה של ספרות - עשרות אלפים).

היישום הזה של התמרות פורייה הוא חימום. הוא רק קצה הקרחון. הסיבה העיקרית שאני כותב את הפוסטים הללו היא כדי שאוכל בעתיד להציג שימושים בלי לדאוג לכך שלא הצגתי את הרקע. אבל מה כדאי להראות? שאלה מצויינת, ואתם מוזמנים להשאיר הצעות בתגובות.
