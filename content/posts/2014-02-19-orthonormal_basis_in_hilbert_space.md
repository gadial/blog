---
id: 3057
title: "בסיסים אורתונורמליים במרחבי הילברט"
date: 2014-02-19 17:28:45
layout: post
categories: 
  - אלגברה לינארית
  - אנליזה מתמטית
tags: 
  - בסיס אורתונורמלי
  - מרחב הילברט
---
<a href="http://www.gadial.net/2014/02/09/hilbert_spaces/">בפוסט הקודם</a> כתבתי עוד ועוד מילים במקום להגיד "מרחב הילברט הוא מרחב מכפלה פנימית שלם ביחס למטריקה שמושרת מהמכפלה הפנימית שלו". בעיקר ניסיתי לדבר על ההבדל שבין מרחב סוף-ממדי למרחב אינסוף ממדי, שמתבטא בכך שבמרחב אינסוף-ממדי יותר יעיל לנו לפעמים לדבר על מושג של "בסיס" שלא זהה למושג הסטנדרטי. בפוסט הזה אני רוצה להרחיב על כך.

בואו נתחיל מהדוגמה שהיא האבטיפוס. הגדרתי את המרחב {% equation %}l^{2}{% endequation %} בתור מרחב וקטורי מעל {% equation %}\mathbb{C}{% endequation %} שכולל את כל הסדרות מהצורה {% equation %}a=a_{1},a_{2},a_{3},\dots{% endequation %} של מספרים מרוכבים, שמקיימות {% equation %}\sum_{n=1}^{\infty}\left|a_{n}\right|^{2}&lt;\infty{% endequation %}. על המרחב הזה הגדרתי את המכפלה הפנימית {% equation %}\left\langle a,b\right\rangle =\sum_{n=1}^{\infty}a_{n}\overline{b_{n}}{% endequation %}. כמובן, לא הוכחתי שכל ההגדרות הללו עובדות: למשל, שסכום של שתי סדרות עדיין מקיים את הדרישה על סכום הערכים המוחלטים. ההוכחות לא מסובכות אבל כן טכניות ולכן אני בורח מהן, לפחות לבינתיים.

אז בואו קבלו את קיומו של {% equation %}l^{2}{% endequation %} כנתון, ובוא נתבונן בוקטורים הבאים: {% equation %}e_{n}{% endequation %} יסמן את הוקטור שהוא סדרה שכולה 0-ים פרט למקום ה-{% equation %}n{% endequation %}-י, שהוא 1. בבירור {% equation %}e_{n}\in l^{2}{% endequation %} לכל {% equation %}n{% endequation %}, ומתקיים {% equation %}\left\langle e_{i},e_{j}\right\rangle =\delta_{ij}{% endequation %}, כלומר כל ה-{% equation %}e_{n}{% endequation %}-ים אורתוגונליים זה לזה, ו-{% equation %}\|e_{n}\|=1{% endequation %} לכל {% equation %}n{% endequation %}. זה מזכיר את מה שקראתי לו "בסיס אורתונורמלי" במרחבים סוף-ממדיים, אבל כמובן שזה לא בסיס במובן הרגיל של המילה, כי צירוף לינארי של מספר סופי של {% equation %}e_{n}{% endequation %}-ים שכאלו יניב וקטור שכל הכניסות שלו פרט למספר סופי הן 0, וב-{% equation %}l^{2}{% endequation %} יש וקטורים רבים שאינם כאלו. אבל מה כן נכון? שאם {% equation %}a{% endequation %} הוא וקטור כלשהו ב-{% equation %}l^{2}{% endequation %}, אז ניתן לכתוב:

{% equation %}a=\sum_{n=1}^{\infty}a_{n}e_{n}{% endequation %}

אבל צריך קצת להיזהר עם כתיבת שוויונות כאלו - באיזה מובן יש כאן שוויון? באיזה מובן יש משמעות לסכום האינסופי הזה? ובכן, בפוסט הקודם דיברתי על זה - השוויון הזה הוא דרך אחרת לומר ש-{% equation %}\lim_{n\to\infty}\|a-\sum_{k=1}^{n}a_{k}e_{k}\|=0{% endequation %}. עכשיו, שימו לב למקדמים של הצירוף הלינארי - ה-{% equation %}a_{k}{% endequation %}-ים. מאיפה ידעתי לכתוב אותם? ובכן, אם אתם זוכרים מה קרה במרחבים סוף-ממדיים, ראינו שם שאם יש לנו בסיס אורתונורמלי כלשהו {% equation %}e_{1},\dots,e_{n}{% endequation %} ויש לנו וקטור {% equation %}a{% endequation %} במרחב, אז {% equation %}a=\sum_{k=1}^{n}\left\langle a,e_{k}\right\rangle e_{k}{% endequation %}. כלומר, המקדמים של {% equation %}a{% endequation %} בצירוף הלינארי של הבסיס האורתונורמלי הם בדיוק המכפלה הפנימית של {% equation %}a{% endequation %} באיברים של אותו בסיס. במקרה הספציפי של {% equation %}l^{2}{% endequation %}, הבסיס {% equation %}e_{n}{% endequation %} שהצגתי והוקטור {% equation %}a=\left(a_{1},a_{2},a_{3},\dots\right){% endequation %}, קל לראות שעל פי הגדרה {% equation %}\left\langle a,e_{n}\right\rangle =a_{n}{% endequation %}.

כעת נשאלת השאלה - האם זה עובד באופן כללי? אם אנחנו לוקחים סדרה אינסופית כלשהי {% equation %}e_{1},e_{2},\dots{% endequation %} של וקטורים אורתונורמליים במרחב הילברט {% equation %}\mathcal{H}{% endequation %} כלשהו, ולוקחים {% equation %}a\in\mathcal{H}{% endequation %}, האם נקבל ש-{% equation %}a=\sum_{n=1}^{\infty}\left\langle a,e_{n}\right\rangle e_{n}{% endequation %}? ובכן, באסה, לא. חסר לנו עדיין משהו שיהפוך את הסדרה של הוקטורים האורתונורמליים ל"בסיס אינסופי". אבל לפני שנדבר עליו, בואו ננסה להעריך עד כמה השוויון {% equation %}a=\sum_{n=1}^{\infty}\left\langle a,e_{n}\right\rangle e_{n}{% endequation %} יכול להיכשל. לשם כך אני הולך להציג את מה שמכונים שוויון ואי-שוויון <strong>בסל</strong>: הם עוסקים בנסיון לקרב וקטור {% equation %}a{% endequation %} על ידי קבוצה <strong>סופית</strong> של וקטורים אורתונורמליים. נתחיל מהשוויון:

{% equation %}\|a-\sum_{k=1}^{n}\left\langle a,e_{k}\right\rangle e_{k}\|^{2}=\|a\|^{2}-\sum_{k=1}^{n}\left|\left\langle a,e_{k}\right\rangle \right|^{2}{% endequation %}

כדי להבין מה קורה פה, בואו ניזכר מה זה {% equation %}\sum_{k=1}^{n}\left\langle a,e_{k}\right\rangle e_{k}{% endequation %}: אנחנו לוקחים את המרחב שנפרש על ידי הוקטורים {% equation %}\left\{ e_{1},\dots,e_{n}\right\} {% endequation %} ומטילים את {% equation %}a{% endequation %} עליו. ההטלה הזו מיוצגת על ידי הסכום, ולכן {% equation %}a-\sum_{k=1}^{n}\left\langle a,e_{k}\right\rangle e_{k}{% endequation %} הוא הרכיב שנותר מ-{% equation %}a{% endequation %} אחרי שקיזזנו את מה שהוטל על המרחב שנפרש על ידי הוקטורים האורתונורמליים. שוויון בסל אומר מה הגודל של ה"מה שנשאר" הזה - הגודל בריבוע שווה לגודל של {% equation %}a{% endequation %} בריבוע, פחות סכום הריבועים של המקדמים של הרכיב המוטל של {% equation %}a{% endequation %}.

ההוכחה היא סטנדרטית למדי ומבוססת בעיקר על סדרה של שוויונות, אבל אני רוצה להראות אותה בכל זאת בגלל שטמונה בה תובנה נוספת על כך ש-{% equation %}\left\langle a,e_{k}\right\rangle {% endequation %} הם המקדמים ה"נכונים" לבחור בהם כשאנחנו רוצים לפרק את {% equation %}a{% endequation %} לגורמים.

אז מה שנעשה הוא זה: נסתכל על צירוף לינארי <strong>כלשהו</strong>, {% equation %}\sum_{k=1}^{n}\alpha_{k}e_{k}{% endequation %} וננסה לחשב ישירות מההגדרה את גודל הנורמה במקרה שלו:

{% equation %}\|a-\sum_{k=1}^{n}\alpha_{k}e_{k}\|^{2}=\left\langle a-\sum_{k=1}^{n}\alpha_{k}e_{k},a-\sum_{k=1}^{n}\alpha_{k}e_{k}\right\rangle {% endequation %}

{% equation %}=\left\langle a,a\right\rangle -\left\langle a,\sum_{k=1}^{n}\alpha_{k}e_{k}\right\rangle -\left\langle \sum_{k=1}^{n}\alpha_{k}e_{k},a\right\rangle +\left\langle \sum_{k=1}^{n}\alpha_{k}e_{k},\sum_{k=1}^{n}\alpha_{k}e_{k}\right\rangle {% endequation %}

{% equation %}=\|a\|^{2}-\left\langle a,\sum_{k=1}^{n}\alpha_{k}e_{k}\right\rangle -\left\langle \sum_{k=1}^{n}\alpha_{k}e_{k},a\right\rangle +\sum_{k=1}^{n}\alpha_{k}\overline{\alpha_{k}}{% endequation %}

המעבר האחרון חיסל את המכפלה הפנימית הימנית על ידי שימוש באורתונורמליות של {% equation %}\left\{ e_{1},\dots,e_{n}\right\} {% endequation %}. עכשיו נשתמש בלינאריות של מכפלה פנימית ונקבל:

{% equation %}=\|a\|^{2}-\sum_{k=1}^{n}\overline{\alpha_{k}}\left\langle a,e_{k}\right\rangle -\sum_{k=1}^{n}\alpha_{k}\overline{\left\langle a,e_{k}\right\rangle }+\sum_{k=1}^{n}\alpha_{k}\overline{\alpha_{k}}{% endequation %}

{% equation %}=\|a\|^{2}+\sum_{k=1}^{n}\left[-\overline{\alpha_{k}}\left\langle a,e_{k}\right\rangle -\alpha_{k}\overline{\left\langle a,e_{k}\right\rangle }+\alpha_{k}\overline{\alpha_{k}}\right]{% endequation %}

{% equation %}=\|a\|^{2}-\sum\left\langle a,e_{k}\right\rangle \overline{\left\langle a,e_{k}\right\rangle }+\sum\left[\left\langle a,e_{k}\right\rangle \overline{\left\langle a,e_{k}\right\rangle }-\overline{\alpha_{k}}\left\langle a,e_{k}\right\rangle -\alpha_{k}\overline{\left\langle a,e_{k}\right\rangle }+\alpha_{k}\overline{\alpha_{k}}\right]{% endequation %}

{% equation %}=\|a\|^{2}-\sum\left\langle a,e_{k}\right\rangle \overline{\left\langle a,e_{k}\right\rangle }+\sum\left[\left(\left\langle a,e_{k}\right\rangle -\alpha_{k}\right)\overline{\left(\left\langle a,e_{k}\right\rangle -\alpha_{k}\right)}\right]{% endequation %}

{% equation %}=\|a\|^{2}-\sum\left|\left\langle a,e_{k}\right\rangle \right|^{2}+\sum\left|\left\langle a,e_{k}\right\rangle -\alpha_{k}\right|^{2}{% endequation %}

בשביל מה זה היה טוב, תשאלו? ובכן, כעת בבירור הערך המינימלי של הביטוי הזה מתקבל כאשר {% equation %}\alpha_{k}=\left\langle a,e_{k}\right\rangle {% endequation %}, ובמקרה הזה נקבל את השוויון {% equation %}\|a-\sum_{k=1}^{n}\alpha_{k}e_{k}\|^{2}=\|a\|^{2}-\sum\left|\left\langle a,e_{k}\right\rangle \right|^{2}{% endequation %} שרצינו. כזכור, המקדמים {% equation %}\left\langle a,e_{k}\right\rangle {% endequation %} הללו נקראים <strong>מקדמי פורייה</strong> של {% equation %}a{% endequation %}, על פי הבסיס {% equation %}\left(e_{n}\right){% endequation %}.

כעת לאי השוויון, שהוא מפורסם יותר: מכיוון שבשוויון לעיל אגף שמאל תמיד חיובי, הרי ש-{% equation %}\|a\|^{2}-\sum\left|\left\langle a,e_{k}\right\rangle \right|^{2}\ge0{% endequation %}, ועל ידי העברת אגפים נקבל ש-{% equation %}\sum_{k=1}^{n}\left|\left\langle a,e_{k}\right\rangle \right|^{2}\le\|a\|^{2}{% endequation %}. אי השוויון הזה תקף לכל {% equation %}n{% endequation %}, ולכן נובעת ממנו המסקנה הבאה:

{% equation %}\sum_{k=1}^{\infty}\left|\left\langle a,e_{k}\right\rangle \right|^{2}\le\|a\|^{2}{% endequation %}

ההוכחה סטנדרטית: אם מניחים בשלילה שהשוויון אינו נכון, אז יהיה סכום חלקי כלשהו שבעצמו כבר עובר את {% equation %}\|a\|^{2}{% endequation %} וזו תהיה סתירה לנתון.

עכשיו, מכיוון שהטור חסום, האיבר הכללי שלו בהכרח שואף לאפס, כלומר {% equation %}\left\langle a,e_{n}\right\rangle \to0{% endequation %}, וזה נכון לכל {% equation %}a{% endequation %}. התכונה הזו, של "התכנסות בעזרת מכפלה פנימית", היא כל כך מעניינת שנותנים לה שם: <strong>התכנסות חלשה</strong>. פורמלית, אם יש לנו סדרה {% equation %}x_{1},x_{2},x_{3},\dots{% endequation %}, אז מסמנים {% equation %}x_{n}\overset{w}{\to x}{% endequation %} אם מתקיים ש-{% equation %}\left\langle x_{n}-x,a\right\rangle =0{% endequation %} לכל {% equation %}a{% endequation %} במרחב. במקרה שלנו קיבלנו ש-{% equation %}e_{n}\overset{w}{\to0}{% endequation %}.

השם "התכנסות חלשה" נובע מכך שהתכנסות "רגילה", כלומר {% equation %}\|x-x_{n}\|\to0{% endequation %}, גוררת את ההתכנסות החלשה: בואו נניח לרגע שמתקיים {% equation %}\lim_{n\to\infty}\|x_{n}-x\|=0{% endequation %}. אני רוצה להראות שזה גורר את הסוג השני של התכנסות, כלומר ש- {% equation %}\left\langle x_{n}-x,a\right\rangle \to0{% endequation %}. כדי להראות את זה, בואו נשתמש ב<strong>אי-שוויון קושי שוורץ</strong>: {% equation %}\left|\left\langle a,b\right\rangle \right|\le\|a\|\|b\|{% endequation %}. אי השוויון הזה עובד בכל מרחב מכפלה פנימית ואני מתחמק מלהוכיח אותו כרגע, אבל בואו נראה מה הוא נותן לנו כאן:

{% equation %}\left|\left\langle x_{n}-x,a\right\rangle \right|\le\|x_{n}-x\|\|a\|{% endequation %}

עכשיו, {% equation %}\|a\|{% endequation %} הוא קבוע, ואילו {% equation %}\|x_{n}-x\|\to0{% endequation %}, ולכן {% equation %}\left|\left\langle x_{n}-x,a\right\rangle \right|\to0{% endequation %}, כלומר {% equation %}\left\langle x_{n}-x,a\right\rangle \to0{% endequation %}, וזאת בלי קשר לשאלה מהו {% equation %}a{% endequation %}.

כדי לראות ששני סוגי ההתכנסויות אינם זהים, מספיק לשים לב לכך שעבור הסדרה האורתונורמלית שלנו, {% equation %}\|e_{n}\|=1{% endequation %} לכל {% equation %}n{% endequation %} ולכן {% equation %}\|e_{n}-0\|{% endequation %} בוודאי שאינו שואף ל-0. כלומר, ה-{% equation %}e_{n}{% endequation %}-ים מתכנסים חלש לאפס אך לא חזק.

עכשיו, אי השוויון {% equation %}\sum_{k=1}^{\infty}\left|\left\langle a,e_{k}\right\rangle \right|^{2}\le\|a\|^{2}{% endequation %} בעצם אומר לנו שטור מקדמי הפורייה של {% equation %}a{% endequation %} מתכנס תמיד. האם אפשר להסיק מכך שהטור {% equation %}\sum_{n=1}^{\infty}\left\langle a,e_{n}\right\rangle e_{n}{% endequation %} גם כן מתכנס תמיד? ובכן, אוף, לא. אבל מה שכן קל להראות, עם טכניקות דומות לאלו שהשתמשנו בהן עד כה, הוא שכאשר אנחנו במרחב הילברט, הטור אכן מתכנס תמיד. מה שעושים הוא להראות שבאופן כללי, {% equation %}\sum_{k=1}^{n}\alpha_{n}e_{n}{% endequation %} היא סדרת קושי, ולהשתמש בשלמות של המרחב כדי להסיק שהיא מתכנסת, וזאת כאשר המקדמים {% equation %}\alpha_{n}{% endequation %} מקיימים ש-{% equation %}\sum_{n=1}^{\infty}\left|\alpha_{n}\right|^{2}&lt;\infty{% endequation %}. כמו כן, לא קשה להראות שאם הטור מתכנס, אז שוויון פרסבל שהצגתי בפוסט הקודם (עבור סכום סופי של וקטורים אורתונורמליים) מתקיים גם כאן, כלומר {% equation %}\|\sum_{n=1}^{\infty}\alpha_{n}e_{n}\|^{2}=\sum_{n=1}^{\infty}\left|\alpha_{n}\right|^{2}{% endequation %}.

נפלא, אז האם במרחב הילברט מתקיים {% equation %}a=\sum_{n=1}^{\infty}\left\langle a,e_{n}\right\rangle e_{n}{% endequation %}? ובכן, לא, עדיין לא! הטור באגף ימין עשוי להתכנס, אבל לא מובטח שיתכנס אל {% equation %}a{% endequation %}!

בואו נראה דוגמה. נסתכל על המרחב {% equation %}\mathcal{H}=L^{2}\left(\left[-\pi,\pi\right]\right){% endequation %}, כלומר פונקציות {% equation %}f:\left[-\pi,\pi\right]\to\mathbb{C}{% endequation %} עם מכפלה פנימית שמוגדרת על ידי אינטגרל. נגדיר {% equation %}e_{n}=\frac{1}{\sqrt{\pi}}\sin nx{% endequation %}. כדי לראות שמדובר על סדרה של וקטורים אורתונורמליים נצטרך לעבוד טיפה. ראשית, המכפלה הפנימית של וקטור עם עצמו:

{% equation %}\left\langle e_{n},e_{n}\right\rangle =\frac{1}{\pi}\int_{-\pi}^{\pi}\sin^{2}nxdx=\frac{1}{\pi}\int_{-\pi}^{\pi}\frac{1-\cos2nx}{2}dx={% endequation %}

{% equation %}=\frac{1}{\pi}\left[\frac{x-\frac{1}{2n}\sin2nx}{2}\right]_{-\pi}^{\pi}=\frac{1}{\pi}\left(\frac{\pi+\pi}{2}\right)=1{% endequation %}

כאן השתמשנו בכך שסינוס של כפולה שלמה של {% equation %}\pi{% endequation %} הוא אפס. כמו כן, אם {% equation %}n\ne m{% endequation %} אז נקבל

{% equation %}\left\langle e_{n},e_{m}\right\rangle =\frac{1}{\pi}\int_{-\pi}^{\pi}\sin nx\sin mxdx=\frac{1}{\pi}\int_{-\pi}^{\pi}\frac{\cos\left(n-m\right)x-\cos\left(n+m\right)x}{2}dx=0{% endequation %}

כאן הרשיתי לעצמי לקפוץ ל-0 מהר, כי כבר ברור מה יקרה - שני הקוסינוסים יהפכו אחרי אינטגרציה לסינוסים וכשנציב בהם {% equation %}\pi{% endequation %} הם יתאפסו. הסיכוי היחיד של הביטוי להיות שונה מאפס הוא אכן כאשר {% equation %}n=m{% endequation %} ואז ה-{% equation %}\cos\left(n-m\right)x{% endequation %} הופך ל-1.

אז יש לנו וקטורים אורתונורמליים. עכשיו בואו ננסה לקחת את הוקטור {% equation %}a=\cos x{% endequation %} ולהציג אותו כסכום:

{% equation %}\sum_{n=1}^{\infty}\left\langle a,e_{n}\right\rangle e_{n}=\frac{\sin nx}{\sqrt{\pi}}\cdot\sum_{n=1}^{\infty}\frac{1}{\sqrt{\pi}}\int_{-\pi}^{\pi}\cos x\sin nxdx{% endequation %}

{% equation %}=\frac{\sin nx}{\sqrt{\pi}}\cdot\sum_{n=1}^{\infty}\frac{1}{\sqrt{\pi}}\int_{-\pi}^{\pi}\frac{\sin\left(n+1\right)x+\sin\left(n-1\right)x}{2}dx=0{% endequation %}

כאן אפס מגיע הרבה יותר בקלות - פשוט תוך הסתמכות על כך ש-{% equation %}\sin{% endequation %} היא פונקציה אי זוגית ({% equation %}f\left(-x\right)=-f\left(x\right){% endequation %}) ושאינטגרציה של פונקציות כאלו בתחום סימטרי סביב 0 נותנת 0 תמיד. אם כן, קיבלנו ש-{% equation %}\sum_{n=1}^{\infty}\left\langle \cos x,e_{n}\right\rangle e_{n}{% endequation %} שווה לאפס, במקום ל-{% equation %}\cos x{% endequation %}. הממממ. אז מה עוד חסר?

ראשית, בואו נגדיר את מה שאנחנו רוצים שיקרה: סדרה - של וקטורים אורתונורמליים {% equation %}e_{1},e_{2},e_{3},\dots{% endequation %} נקראת <strong>שלמה</strong> אם {% equation %}\sum_{n=1}^{\infty}\left\langle a,e_{n}\right\rangle e_{n}=a{% endequation %} לכל {% equation %}a{% endequation %} במרחב. בפרט נובע מכך שלכל וקטור במרחב יש דרך הצגה <strong>יחידה</strong> כסכום אינסופי של אברי הסדרה: כי נניח ש-{% equation %}\sum_{n=1}^{\infty}\alpha_{n}e_{n}=\sum_{n=1}^{\infty}\beta_{n}e_{n}{% endequation %}, אז נחסר את האגפים ונקבל {% equation %}0=\sum_{n=1}^{\infty}\left(\alpha_{n}-\beta_{n}\right)e_{n}{% endequation %} ומשוויון פרסבל נסיק ש-{% equation %}0=\sum_{n=1}^{\infty}\left|\alpha_{n}-\beta_{n}\right|^{2}{% endequation %}, מה שיכול לקרות רק אם {% equation %}\alpha_{n}=\beta_{n}{% endequation %} לכל {% equation %}n{% endequation %}. תכונת ה"קיום ויחידות" הזו מאוד דומה למה שקורה עם בסיס רגיל, רק ששם מדובר על צירוף לינארי סופי, לא אינסופי; עדיין, זה מספיק כדי שנשתמש שנקרא לסדרה אורתונורמלית שלמה "בסיס אורתונורמלי" (כשלכולם ברור מההקשר שזה לא בסיס של צירוף לינארי סופי).

טוב, ההגדרה של סדרה אורתונורמלית שלמה עדיין לא אומרת שיש לנו קריטריון קל לבדיקה שיכריע שסדרת וקטורים נתונה היא שלמה. בואו נחשוב לרגע - איך אפשר לזהות שקבוצה אורתונורמלית של וקטורים היא בסיס למרחב וקטורי ממימד סופי? ובכן, וקטורים אורתוגונליים הם בלתי תלויים לינארית, אז רק צריך להראות שזו קבוצה פורשת; אם היא לא פורשת, אז יש איזה שהוא וקטור שלא נפרש על ידי אברי הקבוצה, ולכן אפשר לפרק אותו לשני רכיבים - רכיב אחד של ההיטל שלו על אברי הקבוצה, ורכיב שני שאורתוגונלי לכל אברי הקבוצה. במילים אחרות, הקבוצה לא פורשת רק אם קיים וקטור שאורתוגונלי לכל אבריה אבל הוא איננו וקטור האפס.

ובכן, הקריטריון הזה עובד גם עבור סדרות אינסופיות. פורמלית, אם {% equation %}e_{1},e_{2},\dots{% endequation %} היא סדרה אורתונורמלית בעלת התכונה שאם {% equation %}\left\langle a,e_{n}\right\rangle =0{% endequation %} לכל {% equation %}e_{n}{% endequation %} בסדרה, אז בהכרח {% equation %}a=0{% endequation %} - אז במקרה כזה, {% equation %}e_{1},e_{2},\dots{% endequation %} היא סדרה אורתונורמלית שלמה. ברור, אגב, שזה חייב להתרחש אם הסדרה היא שלמה, כי אז לכל {% equation %}a{% endequation %} מתקיים {% equation %}a=\sum\left\langle a,e_{n}\right\rangle e_{n}{% endequation %} כך שאם כל המקדמים הם 0 נובע מכך שהסכום הוא 0. השאלה היא רק למה התכונה של המכפלה הפנימית הזו גוררת שהסדרה היא אכן שלמה.

אוקיי, אז בואו ניקח איזה {% equation %}a{% endequation %} ונגדיר {% equation %}b=\sum\left\langle a,e_{n}\right\rangle e_{n}{% endequation %}. כזכור, {% equation %}b{% endequation %} קיים, אבל אם הסדרה אינה שלמה קיימת הסכנה שהוא יהיה שונה מ-{% equation %}a{% endequation %}. אם נראה ש-{% equation %}a-b=0{% endequation %}, סיימנו; בגלל התכונה שלעיל, מספיק להראות ש-{% equation %}\left\langle a-b,e_{n}\right\rangle =0{% endequation %} לכל {% equation %}n{% endequation %}. בואו נפתח את החישוב של המכפלה הפנימית הזו:

{% equation %}\left\langle a-b,e_{n}\right\rangle =\left\langle a,e_{n}\right\rangle -\left\langle \sum\left\langle a,e_{k}\right\rangle e_{k},e_{n}\right\rangle =\left\langle a,e_{n}\right\rangle -\sum\left\langle a,e_{k}\right\rangle \delta_{nk}{% endequation %}

{% equation %}=\left\langle a,e_{n}\right\rangle -\left\langle a,e_{n}\right\rangle =0{% endequation %}

וזה מסיים את זה.

למעשה, אפשר לתת עוד קריטריון שקול לכך שסדרה אורתונורמלית היא שלמה - שוויון פרסבל. ניסחתי אותו כאן כבר בתור {% equation %}\|\sum_{n=1}^{\infty}\alpha_{n}e_{n}\|^{2}=\sum_{n=1}^{\infty}\left|\alpha_{n}\right|^{2}{% endequation %} - כלומר, בלי להתחייב על מהם המקדמים {% equation %}\alpha_{k}{% endequation %} - אבל אפשר עכשיו לנסח אותו שוב בצורה המוכרת יותר שלו, שתקפה רק עבור סדרה אורתונורמלית שלמה:

{% equation %}\|a\|^{2}=\sum_{n=1}^{\infty}\left|\left\langle a,e_{n}\right\rangle \right|^{2}{% endequation %}.

לא בכל מרחב הילברט יש סדרה אורתונורמלית שלמה; מרחבים שבהם יש כזו נקראים <strong>ספרביליים</strong>. עכשיו, בואו ניזכר לרגע במה שקרה באלגברה לינארית סוף-ממדית: ראינו שכל מרחב וקטורי ממימד {% equation %}n{% endequation %} איזומורפי ל-{% equation %}\mathbb{C}^{n}{% endequation %} - האיזומורפיזם כלל בחירת בסיס למרחב והתאמה לכל וקטור במרחב של וקטור הקואורדינטות שלו על פי הבסיס. בואו נראה עכשיו שאותה תוצאה עובדת גם עבור מרחבי הילברט ספרביליים (ובפרט עבור כל מרחבי המכפלה הפנימית ממימד סופי): נראה שכל מרחב כזה ממימד {% equation %}n{% endequation %} איזומורפי ל-{% equation %}\mathbb{C}^{n}{% endequation %} כמרחב מכפלה פנימית. ולמי יהיו איזומורפיים מרחבי הילברט הספרביליים האינסוף-ממדיים? נסו לנחש (זה לא קשה) בזמן שאני מגדיר פורמלית מה זה אומר איזומורפיזם כאן: אם {% equation %}U,V{% endequation %} הם שני מרחבי מכפלה פנימית מעל {% equation %}\mathbb{C}{% endequation %} (עזבו את {% equation %}\mathbb{R}{% endequation %}, אין לי כוח לנסח כל משפט פעמיים) אז פונקציה {% equation %}T:U\to V{% endequation %} היא איזומורפיזם שלהם אם היא לינארית ({% equation %}T\left(a+b\right)=T\left(a+b\right){% endequation %} ו-{% equation %}T\left(\lambda a\right)=\lambda T\left(a\right){% endequation %}), חד-חד-ערכית ועל, ומשמרת את המכפלה הפנימית, כלומר {% equation %}\left\langle T\left(a\right),T\left(b\right)\right\rangle =\left\langle a,b\right\rangle {% endequation %}.

אז בואו ניקח מרחב מכפלה פנימית ממימד {% equation %}n{% endequation %}. הוא סוף ממדי, ולכן יש לו בסיס רגיל. את הבסיס הרגיל אפשר לגרם-שמדט ולקבל בסיס אורתונורמלי {% equation %}\left\{ e_{1},\dots,e_{n}\right\} {% endequation %}. עכשיו נגדיר את {% equation %}T{% endequation %} באופן המתבקש, על ידי שליחת כל איבר לוקטור הקואורדינטות שלו, דהיינו {% equation %}T\left(a\right)=\left(\left\langle a,e_{1}\right\rangle ,\dots,\left\langle a,e_{n}\right\rangle \right){% endequation %}. הלינאריות של {% equation %}T{% endequation %} נובעת מייד מתכונות הלינאריות של מכפלה פנימית. כדי להראות ש-{% equation %}T{% endequation %} חח"ע ועל מספיק להראות שהגרעין שלה הוא 0, וזה נובע מכך שאם {% equation %}\left\langle a,e_{i}\right\rangle =0{% endequation %} לכל {% equation %}1\le i\le n{% endequation %} אז {% equation %}a=0{% endequation %} (פשוט בגלל ש-{% equation %}a=\sum_{i=1}^{n}\left\langle a,e_{i}\right\rangle e_{i}{% endequation %}). לבסוף, {% equation %}\left\langle a,b\right\rangle =\left\langle \sum\left\langle a,e_{i}\right\rangle e_{i},\sum\left\langle b,e_{j}\right\rangle e_{j}\right\rangle =\sum\left\langle a,e_{i}\right\rangle \overline{\left\langle b,e_{i}\right\rangle }{% endequation %} ו-

{% equation %}\left\langle T\left(a\right),T\left(b\right)\right\rangle =\left\langle \left(\left\langle a,e_{1}\right\rangle ,\dots,\left\langle a,e_{n}\right\rangle \right),\left(\left\langle b,e_{1}\right\rangle ,\dots,\left\langle b,e_{n}\right\rangle \right)\right\rangle =\sum\left\langle a,e_{i}\right\rangle \overline{\left\langle b,e_{i}\right\rangle }{% endequation %}

(תזכרו שבמקרה השני, המכפלה הפנימית היא הסטנדרטית על {% equation %}\mathbb{C}^{n}{% endequation %}).

ומה קורה במקרה שבו {% equation %}\mathcal{H}{% endequation %} לא סוף ממדי? עדיין מתבקש לשלוח איבר לוקטור הקואורדינטות שלו, כלומר לסדרה אינסופית של מספרים מרוכבים. זה מזכיר את {% equation %}l^{2}{% endequation %}, אבל כדי שההעתקה הזו באמת תהיה מ-{% equation %}\mathcal{H}{% endequation %} אל {% equation %}l^{2}{% endequation %}, צריך להתקיים שסדרת הקואורדינטות הזו תקיים את התנאי שמגדיר איברים של {% equation %}l^{2}{% endequation %}, שהוא כזכור שיתקיים {% equation %}\sum\left|a_{n}\right|^{2}&lt;\infty{% endequation %}. למרבה המזל, כבר ראינו את זה בפוסט: {% equation %}\sum_{k=1}^{\infty}\left|\left\langle a,e_{k}\right\rangle \right|^{2}\le\|a\|^{2}{% endequation %}, ולכן אם {% equation %}a\in\mathcal{H}{% endequation %} הוא איבר כלשהו, אז יש לנו חסם על {% equation %}\sum_{k=1}^{\infty}\left|\left\langle a,e_{k}\right\rangle \right|^{2}{% endequation %} - הנורמה של {% equation %}a{% endequation %}, שהיא תמיד סופית (כך היא מוגדרת). מכאן מקבלים ש-{% equation %}T\left(a\right)=\left(\left\langle a,e_{1}\right\rangle ,\left\langle a,e_{2}\right\rangle ,\dots\right){% endequation %} היא העתקה חוקית, וקל להראות שהיא לינארית ומשמרת נורמה כמו קודם. המסקנה היא שכל מרחב הילברט אינסוף ממדי ספרבילי הוא איזומורפי ל-{% equation %}l^{2}{% endequation %}, מה שהופך את {% equation %}l^{2}{% endequation %} ל"דוגמה קנונית למרחב הילברט".

עכשיו בואו נדבר על {% equation %}L^{2}{% endequation %}. ראינו כבר קבוצה שמנסה להיות סדרה אורתונורמלית שלמה ב-{% equation %}L^{2}\left(\left[-\pi,\pi\right]\right){% endequation %} ונכשלת בצורה מבישה. האם קיימת סדרה אורתונורמלית שלמה, כלומר האם המרחב הוא ספרבילי? התשובה חיובית, והסדרה האורתונורמלית שאני רוצה להראות היא חשובה ביותר: היא בעצם מהווה מקרה פרטי חשוב של מה שנקרא <strong>טורי פורייה</strong>.

קודם ניסינו את מזלנו עם סינוסים. זו הייתה בחירה טובה, כי קל להראות שהם אורתונורמליים; מה שהיה חסר לנו בשביל סדרה שלמה הוא גם קוסינוסים. אבל למעשה, אין צורך לדבר על סינוסים וקוסינוסים בנפרד אלו מאלו: אפשר לנצל את זה שהמרחב שלנו הוא מעל המרוכבים, {% equation %}\mathbb{C}{% endequation %}, ושבמרוכבים יש פונקציה שמאחדת גם את סינוס וגם את קוסינוס - האקספוננט המרוכב. גם למי שלא מכיר את זה, מספיק לראות את הנוסחה הבאה, "נוסחת אוילר": {% equation %}e^{i\theta}=\cos\theta+i\sin\theta{% endequation %}. הוכחה של נכונות הנוסחה היא עניין לפוסט באנליזה מרוכבת - בינתיים תאמינו לי שזה עובד.

אברי הסדרה שלנו יהיו האיברים הבאים: {% equation %}\varphi_{n}\left(x\right)=\frac{1}{\sqrt{2\pi}}e^{inx}{% endequation %} (אני משתמש ב-{% equation %}\varphi{% endequation %} כי {% equation %}e{% endequation %} תפוס על ידי הקבוע המתמטי), כאשר {% equation %}n{% endequation %} הוא מספר <strong>שלם</strong>, כלומר אנו מרשים גם מספרים שליליים. הסיבה להכפלה ב-{% equation %}\frac{1}{\sqrt{2\pi}}{% endequation %} היא כדי שנקבל שהנורמה של כל איבר היא 1 (תכף נעשה את החישוב) ואנחנו צריכים {% equation %}n{% endequation %}-ים שליליים אחרת הסדרה לא תהיה שלמה. כמובן, יש משהו קצת מוזר בכך שהסדרה שלנו אינסופית "לשני הכיוונים", אבל זו בסך הכל שיטת סימון קצת שונה שנועדה להקל עלינו; הייתי יכול באותה המידה להגדיר את הסדרה כך:

{% equation %}\varphi_{n}\left(x\right)=\begin{cases}\frac{1}{\sqrt{2\pi}}e^{ikx} & n=2k\\\frac{1}{\sqrt{2\pi}}e^{-ikx} & n=2k+1\end{cases}{% endequation %}

אבל זה יותר מסובך מבחינת הסימונים, ומתמטיקאים שונאים דברים כאלו, ואני מסכים איתם.

בואו נראה שמדובר על סדרה אורתונורמלית. ראשית, מכפלה של איבר בעצמו:

{% equation %}\left\langle \varphi_{n},\varphi_{n}\right\rangle =\int_{-\pi}^{\pi}\frac{1}{\sqrt{2\pi}}e^{inx}\cdot\frac{1}{\sqrt{2\pi}}e^{-inx}dx=\frac{1}{2\pi}\int_{-\pi}^{\pi}1dx=1{% endequation %}

כעת, מכפלה של שני איברים שונים:

{% equation %}\left\langle \varphi_{n},\varphi_{m}\right\rangle =\int_{-\pi}^{\pi}\frac{1}{\sqrt{2\pi}}e^{inx}\cdot\frac{1}{\sqrt{2\pi}}e^{-imx}dx=\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{i\left(n-m\right)x}dx{% endequation %}

{% equation %}=\frac{1}{2\pi}\left[\frac{1}{i\left(n-m\right)}e^{i\left(n-m\right)x}\right]_{-\pi}^{\pi}=\frac{e^{i\left(n-m\right)\pi}-e^{-i\left(n-m\right)\pi}}{2\pi\left(i\left(n-m\right)\right)}=0{% endequation %}

המעבר האחרון נובע מכך ש-{% equation %}e^{i\left(n-m\right)\pi}=\cos\left(\pi\left(n-m\right)\right){% endequation %} (מנוסחת אוילר) ו-{% equation %}e^{-i\left(n-m\right)\pi}=\cos\left(\pi\left(m-n\right)\right)=\cos\left(\pi\left(n-m\right)\right){% endequation %} (מכך שקוסינוס היא פונקציה זוגית - סימטרית ביחס לציר {% equation %}x=0{% endequation %}).

מה נשאר? להראות שזו סדרה אורתונורמלית שלמה. כלומר, אם להשתמש בטריק שראינו, להוכיח שאם {% equation %}\left\langle \varphi_{n},f\right\rangle =0{% endequation %} לכל {% equation %}n{% endequation %}, אז {% equation %}f=0{% endequation %}. אבל עם ההוכחה הזו נחכה קצת לפוסט ייעודי שידבר על טורי פורייה.

