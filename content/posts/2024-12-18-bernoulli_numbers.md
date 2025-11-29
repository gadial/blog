---
title: "מספרי ברנולי"
layout: post
categories:
  - תורת המספרים
  - קומבינטוריקה
tags:
  - מספרי ברנולי
  - סכומי חזקות
  - פונקציות יוצרות אקספוננציאליות
---


<h2>בואו נסכום סכומים</h2>

אחד מהדברים הבאמת נחמדים שלמדתי במתמטיקה בתיכון היה הנוסחה לסכום של סדרה חשבונית, שבמקרה הפשוט ביותר שלה הוא הסכום הבא:

{% equation %}1+2+3+\ldots+n=\frac{n\left(n+1\right)}{2}{% endequation %}

סביב הסכום הזה יש את הצ'יזבט האהוב על המתמטיקאי קרל פרידריך גאוס, שלכאורה גילה אותו בתור ילד קטן שהמורה בבית הספר נתן לו וליתר התלמידים לסכום את המספרים מ-1 עד 100 כדי להעסיק אותם בזמן שהוא נח. גאוס הילד היה נאמן לסלוגן על כך שמתמטיקאים הם עצלנים: במקום לחבר את הכל במפורש, הוא שם לב לכך ש-1 ועוד 100 שווה 101, וגם 2 ועוד 99 שווה 101 וכן הלאה, כך שיש לו 50 זוגות מספרים שהסכום של כולם הוא 101 ורק צריך לחשב את הכפל הקל 50 כפול 101 ואת זה אפילו אני יודע לעשות בראש ולקבל 5050. הנוסחה שכתבתי למעלה היא אותו דבר: יש לנו {% equation %}\frac{n}{2}{% endequation %} זוגות שהסכום של כולם הוא {% equation %}n+1{% endequation %}, אז אנחנו פשוט כופלים (אם {% equation %}n{% endequation %} אי זוגי יש איבר בודד באמצע שאי אפשר למצוא לו בן זוג, אבל הנוסחה עדיין עובדת כי היא סופרת אותו בתור "חצי זוג" - נסו בעצמכם לבדוק על מספרים קטנים!)

מה שלא שמעתי עליו בבית הספר, וקצת חבל, הוא שיש לנו נוסחה דומה גם עבור הסכום של <strong>הריבועים</strong> של הטבעיים:

{% equation %}1^{2}+2^{2}+3^{2}+4^{2}+\ldots+n^{2}=\frac{n\left(n+1\right)\left(2n+1\right)}{6}{% endequation %}

הנוסחה הזו פחות פשוטה מהקודמת, אבל היא עדיין די פשוטה ומערבת רק מכפלה של שלושה מספרים. זה מעלה את השאלה אם גם כשאני מחבר חזקות גבוהות יותר של הטבעיים, אני עדיין אקבל נוסחה פשוטה יחסית. מה למשל קורה עם {% equation %}1^{3}+2^{3}+3^{3}+\ldots{% endequation %}? התשובה היא שאכן, יש נוסחה פשוטה יחסית למקרה הזה ובעצם לכל מקרה של {% equation %}1^{m}+2^{m}+3^{m}+\ldots+n^{m}{% endequation %}, אם כי "פשוטה" זה כמובן עניין יחסי כי ככל ש-{% equation %}m{% endequation %} גדול יותר הנוסחה תהיה מסובכת יותר. אבל מה שאפשר לומר שהופך את העניין לפשוט הוא שני דברים:

<ul> <li>הנוסחה היא תמיד <strong>פולינום</strong> ממעלה {% equation %}m+1{% endequation %}.</li>


<li>אפשר לכתוב את הנוסחה באופן כללי, לכל {% equation %}m{% endequation %} שהוא, בעזרת משהו שנקרא <strong>מספרי ברנולי.</strong></li>

</ul>

קודם כל - מה זה "פולינום"? יהיה קל להסביר את זה אם ניקח את הנוסחה {% equation %}\frac{n\left(n+1\right)}{2}{% endequation %} ונפתח את הסוגריים. נקבל, על פי כללי החשבון הרגילים, {% equation %}\frac{1}{2}n^{2}+\frac{1}{2}n{% endequation %}. באופן דומה אם נפתח את {% equation %}\frac{n\left(n+1\right)\left(2n+1\right)}{6}{% endequation %} נקבל {% equation %}\frac{1}{3}n^{3}+\frac{1}{2}n^{2}+\frac{1}{6}n{% endequation %}. ביטוי כזה נקרא <strong>פולינום</strong>: זה ביטוי שכולל <strong>משתנה</strong>, במקרה שלנו {% equation %}n{% endequation %}, שהרעיון בו הוא שהוא לא מייצג מספר קונקרטי (אבל אפשר <strong>להציב</strong> בו מספרים קונקרטיים ולראות מה קורה) ואנחנו מסתכלים גם על חזקות שלו, כמו למשל {% equation %}n^{2}{% endequation %} או {% equation %}n^{3}{% endequation %}, ועל מכפלות של כל אלו במספרים, ועל סכומים של כל זה. בביטוי כמו {% equation %}\frac{1}{3}n^{3}+\frac{1}{2}n^{2}+\frac{1}{6}n{% endequation %} אני אומר שה-{% equation %}\frac{1}{3}{% endequation %} שבו מוכפל {% equation %}n^{3}{% endequation %} הוא <strong>המקדם</strong> של {% equation %}n^{3}{% endequation %} (ולכן {% equation %}\frac{1}{6}{% endequation %} הוא המקדם של {% equation %}n{% endequation %} וכדומה). באופן כללי יכול להופיע בפולינום גם מספר שלא מוכפל ב-{% equation %}n{% endequation %} ואז הוא נקרא <strong>המקדם החופשי</strong> אבל אפשר לחשוב עליו כאילו הוא מוכפל ב-{% equation %}n^{0}{% endequation %} (<a href="https://gadial.net/2018/01/01/zero_power_equals_one/">הנה פוסט</a> על למה דברים בחזקת 0 נחשבים 1) אם כי בהקשר שלנו מקדם חופשי כזה פשוט לא הולך להופיע. בנוסף, <strong>המעלה</strong> של פולינום היא החזקה הגבוהה ביותר שמופיעה בו, כלומר לדוגמא, המעלה של {% equation %}\frac{1}{3}n^{3}+\frac{1}{2}n^{2}+\frac{1}{6}n{% endequation %} היא 3.

פולינומים הם באמת ובתמים פונקציות פשוטות מאוד. אם מציבים ערך בפולינום, החישוב רק דורש לחשב חזקות של הערך, לכפול אותן במקדמים, ולחבר. אם אני מצליח לתרגם את החיבור של המספרים {% equation %}1^{10}+2^{10}+3^{10}+\ldots+1000^{10}{% endequation %} לחישוב של הצבה של 1000 בפולינום ממעלה 11, המרתי את הבעיה של חישוב 1000 חזקות עשיריות של מספרים וחיבור של כולן, לבעיה של חישוב 11 חזקות שונות של אותו מספר (וכשהמספר הזה הוא 1,000 זה לא בדיוק החלק הקשה פה) ואז כפל של 11 החזקות הללו במקדמים וחיבור שלהן - משמעותית פחות עבודה. זה הוביל את יעקב ברנולי, שגילה את הנוסחה הכללית (ולא אכנס כאן לדיון ההיסטורי של מי בדיוק גילה מה ובאיזה נוסח למרות שיש דיון כזה) לכתוב בהתלהבות ביומן שלו שבעזרת הנוסחה לקחה לו פחות מרבע שעה כדי לחשב את סכום החזקות העשיריות של המספרים עד 1000 ולקבל שיצא {% equation %}91,409,924,241,424,243,424,241,924,242,500{% endequation %}. גם ברנולי היה נאמן לסלוגן "מתמטיקאים הם עצלנים", בדרך המאוד מוזרה שבה העצלנות הזו מתבטאת בפועל. 

בהמשך אני אראה איך מגיעים לנוסחה ומוכיחים אותה, אבל מכיוון שזה ידרוש מתמטיקה טיפה לא טריוויאלית בואו נתחיל קודם מתיאור של הנוסחה עצמה. בשביל לתאר אותה צריך להגדיר את מספרי ברנולי, ובשבילם צריך קצת קונבנציות מתמטיות.

ראשית, יש את הסימון המוסכם לסכימה. למשל, במקום לכתוב {% equation %}1^{m}+2^{m}+3^{m}+\ldots+n^{m}{% endequation %} אני כותב {% equation %}\sum_{k=1}^{n}k^{m}{% endequation %}. כאן הסימן {% equation %}\Sigma{% endequation %} אומר שיש לי תיאור של סכום, ה-{% equation %}k^{m}{% endequation %} שליד ה-{% equation %}\Sigma{% endequation %} הוא "האיבר הכללי" של הסכום - כלומר, הצורה שיש לכל איבר בסכום. ה-{% equation %}k=1{% endequation %} למטה גם אומר שמשתנה הסכימה הוא {% equation %}k{% endequation %}, מה שאומר שבביטוי {% equation %}k^{m}{% endequation %} אני מציב ערכים ב-{% equation %}k{% endequation %} אבל משאיר את {% equation %}m{% endequation %} כמות שהוא, וגם שהערך של {% equation %}k{% endequation %} הזה מתחיל מ-1. ה-{% equation %}n{% endequation %} למעלה אומר שהערך הגדול ביותר ש-{% equation %}k{% endequation %} מגיע אליו הוא {% equation %}n{% endequation %}, והקונבנציה הלא כתובה היא שמגדילים בכל פעם את הערך של {% equation %}k{% endequation %} ב-1. לכן {% equation %}\sum_{k=1}^{n}k^{m}=1^{m}+2^{m}+3^{m}+\ldots+n^{m}{% endequation %}. למרות שסימון הסכימה הזה נראה קצת מרתיע בהתחלה הוא הרבה יותר קומפקטי וברור אחרי שמתרגלים אליו.

שנית, אנחנו הולכים לראות מספרים מהצורה {% equation %}{a \choose b}{% endequation %}. הסימון הזה, שנקרא <strong>מקדם הבינום</strong> (אסביר בהמשך למה) מוגדר באופן הבא. ראשית, מגדירים <strong>עצרת</strong> של מספר טבעי, שמסומנת בתור המספר עם סימן קריאה אחריו: {% equation %}a!=1\cdot2\cdot3\cdots a{% endequation %}, כלומר מכפלת כל המספרים הטבעיים מ-1 עד {% equation %}a{% endequation %} (למשל {% equation %}4!=1\cdot2\cdot3\cdot4=24{% endequation %}) ובנוסף ההגדרה המפורשת {% equation %}0!=1{% endequation %}. שנית, {% equation %}{a \choose b}=\frac{a!}{b!\left(a-b!\right)}{% endequation %} והביטוי הזה מוגדר כאשר {% equation %}0\le b\le a{% endequation %}. יש הגיון מאחורי הביטוי הזה, לא סתם החלטנו להמציא אותו: {% equation %}{a \choose b}{% endequation %} סופר את מספר הדרכים שבהן אפשר לבחור {% equation %}b{% endequation %} איברים מתוך {% equation %}a{% endequation %} איברים, במקרה שבו אין חשיבות לסדר שבו הבחירה הזו מתבצעת. (אני מתאר את זה <a href="https://gadial.net/2010/06/20/combinatorics_intro/">כאן</a>).

לבסוף, בנוסחה שאני הולך להציג יופיעו <strong>מספרי ברנולי</strong> שמסומנים ב-{% equation %}B_{0},B_{1},B_{2},\ldots{% endequation %} והם יהיו המושג המרכזי בפוסט.

אני אגלה כבר עכשיו שמספרי ברנולי הראשונים הם {% equation %}B_{0}=1,B_{1}=-\frac{1}{2},B_{2}=\frac{1}{6},B_{3}=0{% endequation %} ואת ההגדרה הכללית שלהם אביא עוד מעט, אבל קודם אני רוצה להראות איך הם נותנים לנו את הנוסחה לסכום החזקות. אלא שכאן יש סיבוך קטן. אמרתי ש-{% equation %}B_{1}=-\frac{1}{2}{% endequation %}, אבל יש גם כאלו שמעדיפים להגדיר {% equation %}B_{1}=\frac{1}{2}{% endequation %}. שתי הקונבנציות סבירות, אבל אני בפוסט הזה הולך להשתמש בקונבנציה ש-{% equation %}B_{1}=-\frac{1}{2}{% endequation %} וזה טיפה משפיע על הנוסחה: במקום להסתכל על {% equation %}\sum_{k=1}^{n}k^{m}{% endequation %} אני מסתכל על {% equation %}\sum_{k=1}^{n-1}k^{m}{% endequation %}, כלומר על הסכום {% equation %}1^{m}+2^{m}+\ldots+\left(n-1\right)^{m}{% endequation %}. את הסכום הזה אני אסמן ב-{% equation %}S_{m}\left(n\right){% endequation %}. כמובן שזה לא שינוי גדול במיוחד; אם ניקח את הנוסחה {% equation %}\frac{n\left(n+1\right)}{2}{% endequation %} שראינו קודם ונחליף את {% equation %}n{% endequation %} ב-{% equation %}n-1{% endequation %} נקבל {% equation %}S_{1}\left(n\right)=\frac{n\left(n-1\right)}{2}=\frac{1}{2}n^{2}-\frac{1}{2}n{% endequation %}. באופן דומה אם ניקח את {% equation %}\frac{n\left(n+1\right)\left(2n+1\right)}{6}{% endequation %} ונחליף את {% equation %}n{% endequation %} ב-{% equation %}n-1{% endequation %} נקבל {% equation %}S_{2}\left(n\right)=\frac{n\left(n-1\right)\left(2n-1\right)}{6}=\frac{1}{3}n^{3}-\frac{1}{2}n^{2}+\frac{1}{6}n{% endequation %}.

עכשיו אפשר להציג את הנוסחה הכללית

<ul> <li>{% equation %}S_{m}\left(n\right)=\frac{1}{m+1}\sum_{k=0}^{m}{m+1 \choose k}B_{k}n^{m+1-k}{% endequation %}</li>

</ul>

בואו נראה איך היא נותנת את הסכומים שכבר ראינו. ראשית, עבור {% equation %}1+2+3+\ldots+n-1{% endequation %}, זה הסכום {% equation %}\sum_{k=1}^{n-1}k^{1}{% endequation %}, כלומר {% equation %}m=1{% endequation %}. לכן כשמשתמשים בנוסחה הכללית שראינו, מקבלים

{% equation %}S_{1}\left(n\right)=\frac{1}{2}\left[{2 \choose 0}B_{0}n^{2}+{2 \choose 1}B_{1}n^{1}\right]=\frac{1}{2}\left[n^{2}+2\cdot\left(-\frac{1}{2}\right)n\right]=\frac{1}{2}n^{2}-\frac{1}{2}n{% endequation %}

ובאופן דומה:

{% equation %}S_{2}\left(n\right)=\frac{1}{3}\left[{3 \choose 0}B_{0}n^{3}+{3 \choose 1}B_{1}n^{2}+{3 \choose 2}B_{2}n\right]=\frac{1}{3}\left[n^{3}-\frac{3}{2}n^{2}+\frac{3}{6}n\right]=\frac{1}{3}n^{3}-\frac{1}{2}n^{2}+\frac{1}{6}n{% endequation %}

לי הנוסחה הכללית נראית טיפה מפחידה, אבל כשאני מקליד את המקרים המפורשים החוקיות "מרגישה" לי הרבה יותר פשוטה - בעצם אין בנוסחאות הללו כמעט שום דבר מסובך, חוץ ממספרי ברנולי עצמם - הם ה"לב" של הסיבוך כאן. אז איך מגדירים אותם? ולמה זה עובד? אני פשוט אציג את ההגדרה כאן, ובהמשך נגיע אל ההוכחה שגם תסביר לנו מאיפה ההגדרה בעצם צצה.

ההגדרה היא <strong>רקורסיבית</strong>: אני מניח שכבר הגדרתי את כל המספרים {% equation %}B_{0},B_{1},B_{2},\ldots,B_{k-1}{% endequation %} ומגדיר באמצעותם את {% equation %}B_{k}{% endequation %}, בצורה הבאה:

{% equation %}B_{k}=-\frac{1}{k+1}\sum_{i=0}^{k-1}{k+1 \choose i}B_{i}{% endequation %}

עם מקרה הבסיס {% equation %}B_{0}=1{% endequation %}. גם פה, הרבה יותר קל "להרגיש" את ההגדרה כשכותבים כמה מקרים ידנית:

{% equation %}B_{1}=-\frac{1}{2}{2 \choose 0}B_{0}=-\frac{1}{2}{% endequation %}

{% equation %}B_{2}=-\frac{1}{3}\left[{3 \choose 0}B_{0}+{3 \choose 1}B_{1}\right]=-\frac{1}{3}\left[1-\frac{3}{2}\right]=-\frac{1}{3}\left(-\frac{1}{2}\right)=\frac{1}{6}{% endequation %}

ואם ממשיכים בחישובים, מקבלים את הסדרה הבאה:

{% equation %}1,-\frac{1}{2},\frac{1}{6},0,-\frac{1}{30},0,\frac{1}{42},0,-\frac{1}{30},0,\frac{5}{66},0,-\frac{691}{2730},\ldots{% endequation %}

בדרך כלל ה-{% equation %}-\frac{691}{2730}{% endequation %} הוא זה שבו מרימים ידיים בייאוש ושואלים "אתם צוחקים עלינו?!". עד לשם, אפשר לראות ניצוצות של חוקיות סבירה - כל המספרים במקומות האי זוגיים למעט {% equation %}B_{1}{% endequation %} הם 0; המספרים האחרים מחליפים סימן בין מינוס לפלוס; במכנה מופיעים מספרים סבירים יחסית כולל 42 יקיר המין האנושי; אבל אז מגיע {% equation %}-\frac{691}{2730}{% endequation %} שכולל מונה ומכנה שאין לאף אחד שמץ של מושג מה הם רוצים מחיינו, והורס כל תקווה לאיזו נוסחה פשוטה יחסית, יותר מנוסחת הנסיגה שיש לנו (יש גם נוסחאות סגורות שכוללות סכימה ואני לא חושב שאפשר לומר שהן פשוטות יותר).

אוקיי, אז זה מה שעושים עם זה, בואו נוכיח שזה עובד.

<h2>בואו נביים בינומים</h2>

לפני שאני מגיע להוכחה האמיתית, שמשתמשת בכלי אלגנטי ויפה אבל לא טריוויאלי להבנה, הנה גישה קצת יותר בסיסית לנושא שכל אחד יכול להבין. בינתיים אני לא אנסה להוכיח את הנוסחה שראינו למעלה אלא משהו צנוע יותר - להוכיח ש-{% equation %}S_{m}\left(n\right){% endequation %} הוא פולינום ממעלה {% equation %}m+1{% endequation %} ולהראות איך למצוא אותו. בשביל זה אני קודם כל הולך להשתמש במשהו שנקרא <strong>הבינום של ניוטון</strong> (יש לי עליו <a href="https://gadial.net/2010/06/22/newton_binom/">פוסט</a>) שאומר באופן כללי:

{% equation %}\left(a+b\right)^{n}=\sum_{i=0}^{n}{n \choose i}a^{i}b^{n-i}{% endequation %}

אם במקום {% equation %}b{% endequation %} יש לי 1 זה נהיה משמעותית פשוט יותר:

{% equation %}\left(a+1\right)^{n}=\sum_{i=0}^{n}{n \choose i}a^{i}=1+{n \choose 1}a+{n \choose 2}a^{2}+\ldots+{n \choose n-1}a^{n-1}+a^{n}{% endequation %}

עכשיו נשתמש בזה עבור {% equation %}a=k{% endequation %} ו-{% equation %}n=m+1{% endequation %} ונקבל את הדבר הבא:

{% equation %}\left(k+1\right)^{m+1}-k^{m+1}=1+{m+1 \choose 1}k+{m+1 \choose 2}k^{2}+\ldots+{m+1 \choose m}k^{m}{% endequation %}

מה שנחמד בביטוי {% equation %}\left(k+1\right)^{m+1}-k^{m+1}{% endequation %} הוא שהוא יוצר לנו <strong>טור טלסקופי</strong>, כלומר טור שבו כל האיברים מבטלים זה את זה חוץ מהראשון והאחרון. כדי לראות את זה, בואו נחבר את כל הביטויים הללו עבור {% equation %}k=0,1,2,\ldots,n-1{% endequation %}:

{% equation %}\left[n^{m+1}-\left(n-1\right)^{m+1}\right]+\left[\left(n-1\right)^{m+1}-\left(n-2\right)^{m+1}\right]+\ldots+\left[2^{m+1}-1^{m+1}\right]+\left[1^{m+1}-0^{m+1}\right]=n^{m+1}{% endequation %}

אז אם אנחנו מחברים את אגף <strong>שמאל</strong> של הביטוי

{% equation %}\left(k+1\right)^{m+1}-k^{m+1}=1+{m+1 \choose 1}k+{m+1 \choose 2}k^{2}+\ldots+{m+1 \choose m}k^{m}{% endequation %}

לכל {% equation %}k=0,1,2,\ldots,n-1{% endequation %} אנחנו מקבלים {% equation %}n^{m+1}{% endequation %}. מה קורה כשאנחנו מחברים את אגף <strong>ימין</strong>? אפשר להסתכל על כל מחובר לבד. המחובר {% equation %}1{% endequation %} יחובר לעצמו {% equation %}n{% endequation %} פעמים ויהפוך ל-{% equation %}n{% endequation %}; המחובר {% equation %}{m+1 \choose 1}k{% endequation %} הופך לטור {% equation %}{m+1 \choose 1}\left(1+2+\ldots+n-1\right)={m+1 \choose 1}S_{1}\left(n\right){% endequation %}. המחובר {% equation %}{m+1 \choose 2}k^{2}{% endequation %} הופך לטור {% equation %}{m+1 \choose 2}S_{2}\left(n\right){% endequation %} וכן הלאה. אז אנחנו מקבלים:

{% equation %}n^{m+1}=n+{m+1 \choose 1}S_{1}\left(n\right)+{m+1 \choose 2}S_{2}\left(n\right)+\ldots+{m+1 \choose m}S_{m}\left(n\right){% endequation %}

וזו נוסחה די מרהיבה כי היא מקשרת את כל הנוסחאות לסכומים עד לחזקה ה-{% equation %}m{% endequation %}-ית. אפשר לבודד את {% equation %}S_{m}\left(n\right){% endequation %} ולקבל

{% equation %}S_{m}\left(n\right)=\frac{1}{m+1}\left[n^{m+1}-{m+1 \choose m-1}S_{m-1}\left(n\right)-\ldots-{m+1 \choose 1}S_{1}\left(n\right)-n\right]{% endequation %}

אם אנחנו כבר יודעים, אינדוקטיבית, שכל {% equation %}S_{k}\left(n\right){% endequation %} כזה הוא ממעלה לכל היותר {% equation %}k+1{% endequation %} המסקנה היא שהביטוי באגף ימין הוא פולינום ממעלה {% equation %}m+1{% endequation %} (בגלל ה-{% equation %}n^{m+1}{% endequation %} שמופיע שם והעובדה שכל ה-{% equation %}S_{k}\left(n\right){% endequation %}-ים הם ממעלה קטנה יותר). הנוסחה הזו גם פותחת פתח לבניה רקורסיבית של ה-{% equation %}B_{m}{% endequation %}-ים ויש ספרים שנוקטים בגישה הזו (למשל Concrete Mathematics של קנות' ושות') אבל זה טכני לא כיף. אני רוצה טכני כיף.

<h2>בואו טכני כיף</h2>

הכלי הטכני שאני משתמש בו נקרא <strong>פונקציות יוצרות</strong>. הרעיון בפונקציות יוצרות הוא זה: אם יש לנו סדרה, אפשר "לשתול" את האיברים שלה בתור מקדמים של טור חזקות, ואז לבצע מניפולציות על הפונקציה שטור החזקות הזה מתאר והמניפולציות הללו יתורגמו למניפולציות בסדרות ש"שתלנו".

זה לא נושא קל לעיכול (<a href="https://gadial.net/2011/08/07/generating_functions_hardcore_1/">יש לי פוסט</a> עליו) אבל חלק מהקושי בו, לטעמי, הוא שקשה להבין אותו בלי לראות דוגמאות קונקרטיות לשימושים שלו - וכאלו שבאמת מפשטים דברים. עכשיו יש לנו הזדמנות לראות דבר כזה.

הנה מבוא קצרצר לפונקציות יוצרות: בהינתן סדרת מספרים {% equation %}a_{0},a_{1},a_{2},\ldots{% endequation %} <strong>הפונקציה היוצרת</strong> שלה היא הטור {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %}. צריך להבהיר כבר עכשיו נקודה קריטית - הטור הזה הוא <strong>אובייקט פורמלי</strong>, כמו פולינום. הוא לא פונקציה. לא מציבים ב-{% equation %}x{% endequation %} ערכים (<strong>אפשר</strong> להציב ב-{% equation %}x{% endequation %} ערכים כחלק מניתוח מתקדם יותר של מה שהפונקציה היוצרת מייצגת, אבל לא <strong>חייבים</strong> לעשות את זה). המשמעות של זה היא שאפשר לכתוב משהו כמו {% equation %}1+x+x^{2}+\ldots=\frac{1}{1-x}{% endequation %} וזה יהיה שוויון תקין, שלא תלוי בסייגים כמו לומר ש-{% equation %}\left|x\right|<1{% endequation %} או משהו.

איך זה עובד? האובייקט הבסיסי הוא כאמור הטור עצמו. על האובייקט הזה מגדירים פעולות חיבור וכפל שהופכות אותו לחוג:

<ul> <li>{% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}+\sum_{n=0}^{\infty}b_{n}x^{n}=\sum_{n=0}^{\infty}c_{n}x^{n}{% endequation %} עם {% equation %}c_{n}=a_{n}+b_{n}{% endequation %}</li>


<li>{% equation %}\left(\sum_{n=0}^{\infty}a_{n}x^{n}\right)\left(\sum_{n=0}^{\infty}b_{n}x^{n}\right)=\sum_{n=0}^{\infty}c_{n}x^{n}{% endequation %} עם {% equation %}c_{n}=\sum_{k=0}^{n}a_{n-k}b_{k}{% endequation %}</li>

</ul>

הדוגמא הקלאסית לכפל היא {% equation %}\left(1+x+x^{2}+\ldots\right)\left(1-x\right)=1{% endequation %} (נסו לבצע את החישוב בעצמכם!) שהיא זו שמצדיקה את הכתיב {% equation %}1+x+x^{2}+\ldots=\left(1-x\right)^{-1}{% endequation %} או, בכתיב הנפוץ יותר, {% equation %}1+x+x^{2}+\ldots=\frac{1}{1-x}{% endequation %}. אני בכוונה לא נכנס יותר מדי לפרטים כי כאמור, יש לי פוסט על זה.

דבר אחד שאין בפוסט וכן נשתמש בו כאן הוא <strong>פונקציות יוצרות אקספוננציאליות</strong>. הפונקציה היוצרת האקספוננציאלית של {% equation %}\left\{ a_{n}\right\} _{n=0}^{\infty}{% endequation %} היא {% equation %}\sum_{n=0}^{\infty}a_{n}\frac{x^{n}}{n!}{% endequation %}. זה עדיין ביטוי פורמלי וההגדרות למעלה עדיין תקפות לגביו, אבל בואו נראה מה קורה לפעולות החיבור והכפל. עבור חיבור עדיין נקבל {% equation %}\sum_{n=0}^{\infty}a_{n}\frac{x^{n}}{n!}+\sum_{n=0}^{\infty}b_{n}\frac{x^{n}}{n!}=\sum_{n=0}^{\infty}c_{n}\frac{x^{n}}{n!}{% endequation %} עם {% equation %}c_{n}=a_{n}+b_{n}{% endequation %}, כלומר פעולת החיבור של פונקציות יוצרות של שתי סדרות מניבה את הפונקציה היוצרת של סדרת הסכומים. כפל, לעומת זאת, הוא קצת יותר טריקי.

מה שאנחנו רוצים לעשות הוא, בהינתן הסדרות {% equation %}a_{n},b_{n}{% endequation %}, להבין מה הסדרה {% equation %}c_{n}{% endequation %} שעבורה תתקיים המשוואה

{% equation %}\left(\sum_{n=0}^{\infty}a_{n}\frac{x^{n}}{n!}\right)\left(\sum_{n=0}^{\infty}b_{n}\frac{x^{n}}{n!}\right)=\sum_{n=0}^{\infty}c_{n}\frac{x^{n}}{n!}{% endequation %}

כדי להבין למה זה טריקי, בואו נראה מה קורה עבור {% equation %}x^{2}{% endequation %}: אנחנו רוצים שהמכפלה תיתן את המקדם {% equation %}\frac{c_{2}}{2!}{% endequation %}. עכשיו, אם מסתכלים על {% equation %}\left(a_{0}+a_{1}x+\frac{a_{2}}{2!}x^{2}\right)\left(b_{0}+b_{1}x+\frac{b_{2}}{2!}x^{2}\right){% endequation %} ופותחים סוגריים ומקבצים לפי החזקה של {% equation %}x{% endequation %}, מקבלים

{% equation %}\left(\frac{a_{2}}{2}b_{0}+a_{1}b_{1}+a_{0}\frac{b_{2}}{2}\right)x^{2}{% endequation %}

אנחנו רוצים להוציא החוצה את ה-{% equation %}\frac{1}{2!}{% endequation %} ולכן נקבל

{% equation %}\left(a_{2}b_{0}+2a_{1}b_{1}+a_{0}b_{2}\right)\frac{x^{2}}{2!}{% endequation %}

מה קורה באופן כללי? המקדם של {% equation %}x^{n}{% endequation %} יהיה {% equation %}\sum_{k=0}^{n}\frac{a_{k}}{k!}\frac{b_{n-k}}{\left(n-k\right)!}{% endequation %}. עכשיו, זכרו את הבינום של ניוטון: {% equation %}{n \choose k}=\frac{n!}{k!\left(n-k\right)!}{% endequation %}. לכן, אם נכפול ונחלק את הסכום ב-{% equation %}n!{% endequation %}, נקבל

{% equation %}\sum_{k=0}^{n}\frac{a_{k}}{k!}\frac{b_{n-k}}{\left(n-k\right)!}=\frac{1}{n!}\sum_{k=0}^{n}{n \choose k}a_{k}b_{n-k}{% endequation %}

כלומר, את נוסחת הכפל צריך לתקן באופן הבא:

<ul> <li>{% equation %}\left(\sum_{n=0}^{\infty}a_{n}\frac{x^{n}}{n!}\right)\left(\sum_{n=0}^{\infty}b_{n}\frac{x^{n}}{n!}\right)=\sum_{n=0}^{\infty}c_{n}\frac{x^{n}}{n!}{% endequation %} עם {% equation %}c_{n}=\sum_{k=0}^{n}{n \choose k}a_{n-k}b_{k}{% endequation %}</li>

</ul>

עכשיו אפשר לדבר על הפונקציה היוצרת האקספוננציאלית הבסיסית שלנו: זו שמתאימה לסדרה {% equation %}a_{n}=1{% endequation %}, כלומר לטור {% equation %}\sum_{n=0}^{\infty}\frac{x^{n}}{n!}{% endequation %}. את הפונקציה הזו אני אסמן בסימון המקוצר המסתורי {% equation %}e^{x}{% endequation %}. כמובן, ייתכן שחלקכם מכירים את הסימון הזה והוא לא נראה להם מסתורי, אבל זה <strong>מסוכן מאוד</strong> לחשוב ככה כי למשל אם אני אכתוב עכשיו {% equation %}e^{2x}{% endequation %} אתם תגידו "כמובן, זה הטור {% equation %}\sum_{n=0}^{\infty}2^{n}\frac{x^{n}}{n!}{% endequation %}" וזה יהיה נכון בכל מה שנוגע לפונקציה שנקראת "אקספוננט" שאנחנו פוגשים בחדו"א, אבל כאן אנחנו בעולם קצת שונה, של טורי חזקות פורמליים, והביטוי {% equation %}e^{2x}{% endequation %} הוא פשוט <strong>לא מוגדר</strong>. מה שמתבקש הוא להגדיר אותו בתור {% equation %}e^{x}\cdot e^{x}{% endequation %}, כי כפל כן הגדרנו, אבל צריך לוודא שזה עובד.

מכיוון ש-{% equation %}e^{x}{% endequation %} התאים לסדרה {% equation %}a_{n}=1{% endequation %}, אז {% equation %}e^{x}\cdot e^{x}{% endequation %} מתאים לסדרה {% equation %}c_{n}=\sum_{k=0}^{n}{n \choose k}{% endequation %}. למרבה השמחה, אנחנו יודעים ש-{% equation %}\sum_{k=0}^{n}{n \choose k}=2^{n}{% endequation %} (הוכחה קומבינטורית: {% equation %}{n \choose k}{% endequation %} הוא מספר הדרכים לבחור {% equation %}k{% endequation %} איברים מתוך {% equation %}n{% endequation %}, ואילו {% equation %}2^{n}{% endequation %} הוא מספר הדרכים לבחור תת-קבוצה כלשהי מתוך {% equation %}n{% endequation %}) ולכן באמת מקבלים ש-{% equation %}e^{x}\cdot e^{x}{% endequation %} מיוצג על ידי הטור {% equation %}\sum_{n=0}^{\infty}2^{n}\frac{x^{n}}{n!}{% endequation %} מה ש"מצדיק" את הסימון {% equation %}e^{2x}=e^{x}\cdot e^{x}{% endequation %}. בגישה קצת פחות פורמלית הייתי אומר "מכיוון ש-{% equation %}e^{x}{% endequation %} שלי הוגדרה עם אותו טור כמו אקספוננט אז כל תוצאה שיש לנו על אקספוננט עובדת כאן עם הבונוס שלא צריך להתחשב בשיקולי התכנסות" אבל אני לא אעשה את זה.

עכשיו, אם יש לנו את {% equation %}e^{2x}{% endequation %}, מה עם {% equation %}e^{kx}{% endequation %} עבור {% equation %}k{% endequation %} טבעי כללי? ההגדרה המתבקשת היא {% equation %}e^{kx}=\sum_{n=0}^{\infty}k^{n}\frac{x^{n}}{n!}{% endequation %}. הייתי רוצה להראות שזו באמת החזקה ה-{% equation %}k{% endequation %}-ית של {% equation %}e^{x}{% endequation %}, ואת זה אני יכול להוכיח באינדוקציה. נניח שבאמת מתקיים {% equation %}e^{kx}=\sum_{n=0}^{\infty}k^{n}\frac{x^{n}}{n!}{% endequation %} ונוכיח ש-{% equation %}e^{x}\cdot e^{kx}=\sum_{n=0}^{\infty}\left(k+1\right)^{n}\frac{x^{n}}{n!}{% endequation %}.

לצורך ההוכחה שוב נתבסס על הגדרת הכפל עבור האיבר הכללי - הפעם הוא יוצא {% equation %}c_{n}=\sum_{i=0}^{n}{n \choose i}k^{i}{% endequation %}. על {% equation %}{n \choose i}k^{i}{% endequation %} אפשר לחשוב קומבינטורית בתור בחירה של {% equation %}i{% endequation %} מתוך {% equation %}n{% endequation %} איברים, ואז צביעה של כל איבר בצבע מתוך קבוצה בת {% equation %}k{% endequation %} צבעים, כך שאפשר לבחור את אותו צבע יותר מפעם אחת. עכשיו, אם אני סופר את מספר הדרכים לבחור <strong>תת-קבוצה</strong> של {% equation %}n{% endequation %} האיברים ולצבוע את אבריה ב-{% equation %}k{% endequation %} צבעים, אפשר להתחכם טיפה - ל-{% equation %}k{% endequation %} הצבעים נוסיף "צבע שקוף", ואז פשוט נצבע את כל {% equation %}n{% endequation %} האיברים ב-{% equation %}k+1{% endequation %} הצבעים, ומי שצבוע בצבע שקוף ייחשב כאילו לא לקחנו אותו לתת הקבוצה. כך קיבלנו שמספר הדרכים הכולל הוא {% equation %}\left(k+1\right)^{n}{% endequation %}, כלומר {% equation %}c_{n}=\left(k+1\right)^{n}{% endequation %}, כמו שרצינו להראות.

למה אני בכלל טורח כל כך להתעסק בחזקות של {% equation %}e^{x}{% endequation %}? מן הסתם אני חותר למשהו. בואו נחזור אל המטרה שלנו - אנחנו רוצים למצוא נוסחה עבור {% equation %}S_{m}\left(n\right){% endequation %}, לכל {% equation %}m{% endequation %}. קודם ראינו שאולי קשה להבין את {% equation %}S_{m}\left(n\right){% endequation %} עבור {% equation %}m{% endequation %} <strong>בודד</strong> אבל אם מסתכלים על ה-{% equation %}S_{m}{% endequation %}-ים הללו <strong>כמכלול</strong>, כולם ביחד, יש ביניהם קשרים. פונקציות יוצרות הן בדיוק דרך לנצל את הקשרים הללו, אז די מתבקש לקחת את {% equation %}S_{m}{% endequation %} ולשתול אותם בתוך פונקציה יוצרת. עכשיו, בפונקציה יוצרת מה ששותלים הוא <strong>סדרות מספרים</strong>, אבל {% equation %}S_{m}{% endequation %} היא לא סדרה של מספרים, היא סדרה של פונקציות - אז נבחר {% equation %}n{% endequation %} קונקרטי, נקבל עבורו סדרה קונקרטית של מספרים, {% equation %}\left\{ S_{m}\left(n\right)\right\} _{m=0}^{\infty}{% endequation %}. נשתול אותה בתוך פונקציה יוצרת אקספוננציאלית ונראה מה נקבל:

{% equation %}\sum_{m=0}^{\infty}S_{m}\left(n\right)\frac{x^{m}}{m!}=\sum_{m=0}^{\infty}\left(\sum_{k=0}^{n-1}k^{m}\right)\frac{x^{m}}{m!}{% endequation %}

עכשיו שימו לב מה קורה כאן: יש לנו פונקציה יוצרת אקספוננציאלית שהאיבר הכללי שלה הוא <strong>סכום סופי</strong> של איברים. זה מתאים לסיטואציה {% equation %}c_{n}=a_{n}+b_{n}{% endequation %} שראינו קודם, רק לא עם שני איברים אלא עם {% equation %}n{% endequation %} איברים, אבל באינדוקציה אפשר להראות שכל איבר כללי שהוא סכום של מספר סופי כלשהו של איברים מתפרק לסכום של פונקציות יוצרות, ולכן נקבל

{% equation %}\sum_{m=0}^{\infty}S_{m}\left(n\right)\frac{x^{m}}{m!}=\sum_{m=0}^{\infty}\left(\sum_{k=0}^{n-1}k^{m}\right)\frac{x^{m}}{m!}=\sum_{k=0}^{n-1}\left[\sum_{m=0}^{\infty}k^{m}\frac{x^{m}}{m!}\right]{% endequation %}

הפלא ופלא, כל הפונקציות היוצרות שבסכום מתאימות בדיוק לחזקות של {% equation %}e{% endequation %} שראינו קודם, אז קיבלנו את התוצאה

{% equation %}\sum_{m=0}^{\infty}S_{m}\left(n\right)\frac{x^{m}}{m!}=e^{0x}+e^{x}+e^{2x}+e^{3x}+\ldots+e^{\left(n-1\right)x}{% endequation %}

עכשיו אפשר סוף סוף לראות את הכוח של פונקציות יוצרות: את הביטוי {% equation %}e^{0x}+e^{x}+e^{2x}+e^{3x}+\ldots+e^{\left(n-1\right)x}{% endequation %} אפשר לראות בתור <strong>טור הנדסי</strong>. כזכור, אם יש לנו טור הנדסי {% equation %}1+q+q^{2}+q^{3}+\ldots+q^{n-1}{% endequation %} אנחנו יודעים לחשב את הסכום שלו על ידי הטריק הבא: נכפול ונחלק ב-{% equation %}\left(q-1\right){% endequation %} ואז נקבל במונה טור טלסקופי שכל מה שיישאר ממנו הוא {% equation %}q^{n}-1{% endequation %}, בזמן שבמכנה יהיה לנו {% equation %}q-1{% endequation %}, כלומר קיבלנו {% equation %}1+q+q^{2}+q^{3}+\ldots+q^{n-1}=\frac{q^{n}-1}{q-1}{% endequation %}. אם נציב {% equation %}q=e^{x}{% endequation %}, זה נותן לנו את הביטוי {% equation %}\frac{e^{nx}-1}{e^{x}-1}{% endequation %} (חדי העין ישימו לב שטיפה רימיתי פה - אני אחזור לזה בהמשך).

עכשיו, בואו נכפול ונחלק את הביטוי הזה ב-{% equation %}x{% endequation %} ונקבל {% equation %}\frac{e^{nx}-1}{e^{x}-1}=\frac{e^{nx}-1}{x}\frac{x}{e^{x}-1}{% endequation %}. אני עוד מעט אקדיש חלק שלם כדי להסביר למה {% equation %}\frac{x}{e^{x}-1}=\sum_{k=0}^{\infty}B_{k}\frac{x^{k}}{k!}{% endequation %}, כלומר {% equation %}\frac{x}{e^{x}-1}{% endequation %} הוא הפונקציה היוצרת האקספוננציאלית של מספרי ברנולי. לגבי {% equation %}\frac{e^{nx}-1}{x}{% endequation %}, קל יותר לטפל בו: {% equation %}e^{nx}=1+nx+\frac{n^{2}x^{2}}{2}+\ldots{% endequation %} ולכן {% equation %}\frac{e^{nx}-1}{x}=n+\frac{n^{2}x}{2}+\ldots=\sum_{k=0}^{\infty}\frac{n^{k+1}}{k+1}\cdot\frac{x^{k}}{k!}{% endequation %}

נסכם לרגע בזהירות את מה שראינו:

{% equation %}\sum_{m=0}^{\infty}S_{m}\left(n\right)\frac{x^{m}}{m!}=\left(\sum_{k=0}^{\infty}\frac{n^{k+1}}{k+1}\frac{x^{k}}{k!}\right)\left(\sum_{k=0}^{\infty}B_{k}\frac{x^{k}}{k!}\right){% endequation %}

כלומר, כשעוברים מרמת הפונקציות היוצרות האקספוננציאליות לרמת האיבר הבודד, וזוכרים איך כפל של פונקציות יוצרות אקספוננציאליות עובד כשעוברים לרמת האיבר הבודד, מקבלים:

{% equation %}S_{m}\left(n\right)=\sum_{k=0}^{m}{m \choose k}B_{k}\frac{n^{\left(m-k\right)+1}}{\left(m-k\right)+1}{% endequation %}

את הגורם שבפנים אפשר לפשט עם עוד תעלול אלגברי/קומבינטורי קטן:

{% equation %}{m \choose k}\frac{1}{m-k+1}=\frac{m!}{k!\left(m-k\right)!}\cdot\frac{1}{m-k+1}=\frac{m!}{k!\left(m-k+1\right)!}=\frac{1}{m+1}\frac{\left(m+1\right)!}{k!\left(m-k+1\right)!}=\frac{1}{m+1}{m+1 \choose k}{% endequation %}

וקיבלנו את הנוסחה שמציגים בכל מקום:

{% equation %}S_{m}\left(n\right)=\frac{1}{m+1}\sum_{k=0}^{m}{m+1 \choose k}n^{m+1-k}B_{k}{% endequation %}

וזה היה... ממש טכני? ובכן, כן ולא. אני יודע שזה די מרתיע אבל בסופו של דבר כשמבינים את הרעיון של פונקציות יוצרות כל מה שעשינו פה הוא מאוד סטנדרטי. זה לא אומר שהיה כיף גדול לעשות את זה, אבל בהתחשב בתוצאה הדי כללית שמקבלים פה זה ממש נחמד - בפרט שזו תוצאה שמטפלת בכל אינסוף ה-{% equation %}S_{m}\left(n\right){% endequation %}-ים בו זמנית.

אבל עדיין לא סיימתי כי נשאר לי להסביר מאיפה מספרי ברנולי הגיעו.

<h2>בואו למסע אל מקורות הברנולי</h2>

אני טענתי, ללא הוכחה, ש-{% equation %}\frac{x}{e^{x}-1}=\sum_{k=0}^{\infty}B_{k}\frac{x^{k}}{k!}{% endequation %}. כלומר אני <strong>מגדיר</strong> את מספרי ברנולי בתור הסדרה ש-{% equation %}\frac{x}{e^{x}-1}{% endequation %} היא הפונקציה היוצרת האקספוננציאלית שלה. יש כאן שתי שאלות

<ul> <li>למה אני יודע בכלל ש-{% equation %}\frac{x}{e^{x}-1}{% endequation %} ניתן לתיאור על ידי טור חזקות כזה?</li>


<li>איך אני יודע שאלו מספרי ברנולי? כלומר, איך אני מראה שמתקיימת הנוסחה הרקורסיבית {% equation %}B_{n}=-\frac{1}{n+1}\sum_{k=0}^{n-1}{n+1 \choose k}B_{k}{% endequation %} שהצגתי קודם?</li>

</ul>

נתחיל מהשאלה הראשונה, למה {% equation %}\frac{x}{e^{x}-1}{% endequation %} ניתן לתיאור על ידי טור חזקות פורמלי. אם לא היינו עובדים במסגרת פורמלית אלא בחדו"א, הסיפור היה הולך ככה: היינו שמים לב שכשמציבים {% equation %}x=0{% endequation %} אז {% equation %}e^{x}=1{% endequation %} ולכן {% equation %}e^{x}-1=0{% endequation %} ולכן המכנה של {% equation %}\frac{x}{e^{x}-1}{% endequation %} יכול להתאפס ומדובר בקטסטרופה. אבל מצד שני, גם <strong>המונה</strong> מתאפס כש-{% equation %}x=0{% endequation %} ולכן אפשר להשתמש בלהטוט החדו"אי שנקרא כלל לופיטל ולקבל {% equation %}\lim_{x\to0}\frac{x}{e^{x}-1}=\lim_{x\to0}\frac{1}{e^{x}}=1{% endequation %}. כלומר, אפשר "לתקן" את הפונקציה {% equation %}\frac{x}{e^{x}-1}{% endequation %} כך שב-{% equation %}x=0{% endequation %} היא תוגדר להיות 1 ולקבל פונקציה נחמדה שאפשר לפתח לטור והכל טוב ויפה.

אני לא הולך לעשות את זה כאן. כאמור, אני דוגל בגישה הפורמלית. בגישה הזו כל מה שיש בעולם הוא טורי חזקות פורמליים ולכן הביטוי {% equation %}\frac{x}{e^{x}-1}{% endequation %} הוא בסך הכל <strong>סימון מקוצר</strong> לטור חזקות פורמלי כלשהו. איזה? על פניו, הטור {% equation %}x\left(e^{x}-1\right)^{-1}{% endequation %} כאשר {% equation %}\left(e^{x}-1\right)^{-1}{% endequation %} הוא טור החזקות ההופכי של {% equation %}e^{x}-1{% endequation %}, דהיינו הטור שכשכופלים אותו ב-{% equation %}e^{x}-1{% endequation %} מקבלים {% equation %}1{% endequation %}. אבל, לצערנו, <strong>אין טור חזקות כזה</strong>. בשביל שטור חזקות יהיה "הפיך" במובן שציינתי, המקדם החופשי שלו צריך להיות הפיך - ובמקרה שלנו, המקדם החופשי של {% equation %}e^{x}-1{% endequation %} הוא 0 שאינו הפיך.

אבל לא הכל אבוד, אני לא באמת צריך הופכיים פה. מה שאני רוצה להגיד בביטוי {% equation %}\frac{x}{e^{x}-1}=f\left(x\right){% endequation %} הוא שמתקיים השוויון {% equation %}x=f\left(x\right)\left(e^{x}-1\right){% endequation %}. אז אני אבדוק אם אני מסוגל <strong>להגדיר</strong> את {% equation %}f\left(x\right){% endequation %} כדי שהשוויון הזה יתקיים; אם אני מסוגל, אז אפשר יהיה להשתמש בסימון המקוצר {% equation %}\frac{x}{e^{x}-1}{% endequation %} כמו קודם.

בואו נתחיל מלכתוב את {% equation %}f\left(x\right){% endequation %} בתור טור חזקות אקספוננציאלי כללי: {% equation %}f\left(x\right)=\sum_{k=0}^{\infty}b_{k}\frac{x^{k}}{k!}{% endequation %}. כרגע אני <strong>לא יודע</strong> שה-{% equation %}b_{k}{% endequation %}-ים הללו הם מספרי ברנולי, או אפילו שאני יכול לבחור להם ערכים בצורה כזו שתצדיק את השוויון {% equation %}\frac{x}{e^{x}-1}=f\left(x\right){% endequation %}, אבל אני כן יכול לקחת טור חזקות אקספוננציאלי כללי כלשהו, לתת למקדמים שלו את הסימון {% equation %}b_{k}{% endequation %}, לכפול אותו ב-{% equation %}e^{x}-1{% endequation %} ולראות מה קורה. נוסחת הכפל הרגילה של טורי חזקות אקספוננציאליים תקפה גם כאן:

{% equation %}c_{n}=\sum_{k=0}^{n}{n \choose k}a_{n-k}b_{k}{% endequation %}

אצלנו {% equation %}a_{0}=0{% endequation %} ואילו {% equation %}a_{k}=1{% endequation %} לכל {% equation %}k>0{% endequation %} (כי החסרת 1 מ-{% equation %}e^{x}{% endequation %} הורידה 1 מהאיבר במקום 0; אם למשל היינו רוצים להוריד 3 מהאיבר במקום 2 היינו צריכים לחסר {% equation %}3x^{2}{% endequation %}). בנוסחה {% equation %}c_{n}=\sum_{k=0}^{n}{n \choose k}a_{n-k}b_{k}{% endequation %} אני מקבל את {% equation %}a_{0}{% endequation %} כאשר {% equation %}k=n{% endequation %} ולכן המקרה הזה אף פעם לא יופיע, ואני מקבל:

{% equation %}c_{n}=\sum_{k=0}^{n-1}{n \choose k}b_{k}{% endequation %}

כלומר, עבור {% equation %}c_{0}{% endequation %} אני מקבל סכום "ריק" ולכן {% equation %}c_{0}=0{% endequation %} תמיד, אין לי שליטה על זה (זו בדיוק הסיבה שבגללה {% equation %}e^{x}-1{% endequation %} לא הפיך). זו לא באמת בעיה, כי אנחנו רוצים לקבל את התוצאה {% equation %}x{% endequation %}, כלומר התוצאה שמתאימה למקרה שבו {% equation %}c_{1}=1{% endequation %} ואילו {% equation %}c_{n}=0{% endequation %} לכל {% equation %}n\ne1{% endequation %}. אז מה באמת קורה עבור {% equation %}c_{1}{% endequation %}?

{% equation %}c_{1}={1 \choose 0}b_{0}=b_{0}{% endequation %}

זה מאלץ אותנו להגדיר {% equation %}b_{0}=1{% endequation %}, אבל יופי - אם אנחנו מגדירים את {% equation %}b_{0}=1{% endequation %} אנחנו באמת מקבלים את הערך המבוקש של {% equation %}c_{1}{% endequation %}. מה עם היתר?

עבור {% equation %}c_{2}{% endequation %} צריך להתקיים {% equation %}c_{2}=0{% endequation %}, ואנחנו יודעים ש-

{% equation %}c_{2}={2 \choose 0}b_{0}+{2 \choose 1}b_{1}{% endequation %}

כלומר:

{% equation %}0=b_{0}+2b_{1}{% endequation %}

כלומר:

{% equation %}b_{1}=-\frac{1}{2}b_{0}=-\frac{1}{2}{% endequation %}

בינתיים זה מתקדם כמו שרצינו! באמת הגדרנו ש-{% equation %}b_{1}=-\frac{1}{2}{% endequation %} בהגדרה שלנו למספרי ברנולי! אז יופי, בואו נעבור למקרה הכללי. נניח שכבר הגדרנו את {% equation %}b_{0},b_{1},\ldots,b_{n-1}{% endequation %} בצורה כזו שבה כל המקדמים עד {% equation %}c_{n}{% endequation %} קיבלו את הערך הנכון, ונטפל ב-{% equation %}c_{n+1}=0{% endequation %}. על פי נוסחת המכפלה, אנחנו יודעים ש-

{% equation %}c_{n+1}=\sum_{k=0}^{n}{n+1 \choose k}b_{k}{% endequation %}

נציב {% equation %}c_{n+1}=0{% endequation %} וכמו כן נפריד את {% equation %}b_{n}{% endequation %} מכל היתר:

{% equation %}0={n+1 \choose n}b_{n}+\sum_{k=0}^{n-1}{n+1 \choose k}b_{k}{% endequation %}

עכשיו, {% equation %}{n+1 \choose n}=n+1{% endequation %} ולכן אחרי העברת אגפים וחלוקה:

{% equation %}b_{n}=-\frac{1}{n+1}\sum_{k=0}^{n-1}{n+1 \choose k}b_{k}{% endequation %}

וזו בדיוק, אבל בדיוק, הנוסחה עבור מספרי ברנולי:

{% equation %}B_{n}=-\frac{1}{n+1}\sum_{k=0}^{n-1}{n+1 \choose k}B_{k}{% endequation %}

מה שמשיג את שתי המטרות שלנו: הראנו שבאמת קיימת פונקציה {% equation %}f\left(x\right){% endequation %} כך ש-{% equation %}f\left(x\right)\left(e^{x}-1\right)=x{% endequation %} למרות ש-{% equation %}e^{x}-1{% endequation %} לא הפיכה, והראינו שהמקדמים של הפונקציה היוצרת האקספוננציאלית שלה הם מספרי ברנולי {% equation %}B_{k}{% endequation %}, ולכן אפשר לכתוב

{% equation %}\frac{x}{e^{x}-1}=\sum_{k=0}^{\infty}B_{k}\frac{x^{k}}{k!}{% endequation %}

כפי שרצינו.

האם סיימנו? כמעט. אני עדיין רוצה להסביר את הפורמליות שמאחורי יתר נפנופי הידיים שביצעתי. בואו ניזכר מה בדיוק קרה שם:

<ul> <li>הגעתי איכשהו אל הפונקציה היוצרת {% equation %}e^{0x}+\ldots+e^{\left(n-1\right)x}{% endequation %}</li>


<li>טענתי ש-{% equation %}e^{0x}+\ldots+e^{\left(n-1\right)x}=\frac{e^{nx}-1}{e^{x}-1}{% endequation %}</li>


<li>טענתי ש-{% equation %}\frac{e^{nx}-1}{e^{x}-1}=\frac{e^{nx}-1}{x}\frac{x}{e^{x}-1}{% endequation %}</li>

</ul>

אלו טענות "מפוקפקות" כי הן מחלקות בדברים שאין להם הופכי (גם {% equation %}e^{x}-1{% endequation %} וגם {% equation %}x{% endequation %}). אז בואו ננסח אותן מחדש בצורה פורמלית יותר אם כי אינטואיטיבית פחות.

כבר ראיתי שיש פונקציה {% equation %}f\left(x\right)=\frac{x}{e^{x}-1}{% endequation %}, כלומר פורמלית זה טור חזקות שמקיים {% equation %}\left(e^{x}-1\right)f\left(x\right)=x{% endequation %}.

בנוסף, ראיתי שיש {% equation %}g\left(x\right)=\frac{e^{nx}-1}{x}{% endequation %}, כלומר פורמלית זה טור חזקות שמקיים {% equation %}xg\left(x\right)=e^{nx}-1{% endequation %}.

בנוסף, במקום להשתמש בנוסחת הטור ההנדסי אפשר לתאר את הסיטואציה בעזרת כפל בלבד, כלומר להישאר ברמת הטור הטלסקופי: {% equation %}\left(e^{x}-1\right)\left(e^{0x}+\ldots+e^{\left(n-1\right)x}\right)=e^{nx}-1{% endequation %}.

עכשיו אני יכול לעשות שרשרת של הצבות:

{% equation %}\left(e^{x}-1\right)\left(e^{0x}+\ldots+e^{\left(n-1\right)x}\right)=e^{nx}-1=xg\left(x\right)=\left(e^{x}-1\right)f\left(x\right)g\left(x\right){% endequation %}

וכאן מגיע להטוט אחד אחרון: באופן כללי, בכל חוג שהוא <strong>תחום שלמות</strong> (כלומר, אין בו מחלקי אפס - איברים שונים מאפס שכשכופלים אותם מקבלים אפס) אפשר תמיד <strong>לצמצם</strong>: אם יש לי {% equation %}ab=ac{% endequation %} עבור {% equation %}a\ne0{% endequation %} אז נובע מכך {% equation %}b=c{% endequation %} אפילו אם {% equation %}a{% endequation %} לא הפיך, פשוט כי אני מסתכל על {% equation %}a\left(b-c\right)=0{% endequation %} ובגלל שאני בתחום שלמות ו-{% equation %}a\ne0{% endequation %} אז {% equation %}b-c=0{% endequation %} כלומר {% equation %}b=c{% endequation %}. זה בדיוק מה שאני אשתמש בו למעלה כדי להיפטר מה-{% equation %}e^{x}-1{% endequation %} המשותף, ולקבל את השוויון הפורמלי לחלוטין:

{% equation %}e^{0x}+\ldots+e^{\left(n-1\right)x}=f\left(x\right)g\left(x\right){% endequation %}

מה שמסיים את ההוכחה.

הסיפור של מספרי ברנולי לא נגמר כאן - יש עוד כל מני דברים מעניינים להראות עליהם, אבל עם סיום התוצאה הבסיסית הזו הגענו אל נקודה טובה לעצור בה לבינתיים. 
