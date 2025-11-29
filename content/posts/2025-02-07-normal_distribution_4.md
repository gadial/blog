---
title: "מה הקטע עם התפלגות נורמלית? (חלק ד' ואחרון: משפט הגבול המרכזי)"
layout: post
categories:
  - הסתברות
tags:
  - התפלגות נורמלית
image: "/assets/img/2025/histogram_10.png"
description: "איך בערך מוכיחים את משפט הגבול המרכזי ולמה הוא נראה כמו שהוא נראה"

---


<h2>אז מה משפט הגבול המרכזי אומר?</h2>

סדרת הפוסטים הזו מנסה להבין למה התפלגות נורמלית נראית כמו שהיא נראית. מן הסתם השאלה הראשונה שצריך לענות עליה בשביל זה היא "מה זו בכלל התפלגות נורמלית?" ולזה יש שתי תשובות: אחת יבשה, של לתת את ההגדרה הפורמלית, וזה מה שעשינו בפוסטים הקודמים; והשניה, המהותית יותר, היא להסביר למה בכלל מתעניינים בהתפלגות הזו - והתשובה היא <strong>משפט הגבול המרכזי</strong>. תיארתי אותו בנפנופי ידיים קודם, אז עכשיו הגיע הזמן לתת את הניסוח הפורמלי.

משפט הגבול המרכזי מסתכל על סדרה אינסופית {% equation %}X_{1},X_{2},X_{3},\ldots{% endequation %} של משתנים מקריים שהם בלתי תלויים ובעלי אותה התפלגות (בדומה לתנאים של <strong>חוק המספרים הגדולים</strong> שהזכרתי בפוסט הקודם). אנחנו מסמנים ב-{% equation %}\mu{% endequation %} את התוחלת וב-{% equation %}\sigma^{2}{% endequation %} את השונות שלהם (בפרט, אנחנו מניחים שהמספרים הללו מוגדרים, סופיים וש-{% equation %}\sigma\ne0{% endequation %}). עכשיו, לכל {% equation %}n{% endequation %} אנחנו מגדירים משתנה מקרי {% equation %}Z_{n}{% endequation %} שהוא בערך הסכום של ה-{% equation %}X_{i}{% endequation %}-ים עד האיבר ה-{% equation %}n{% endequation %}-י, אבל עם שקלול נוסף שאמור לנרמל את הסכום:

{% equation %}Z_{n}=\frac{X_{1}+\ldots+X_{n}-n\mu}{\sigma\sqrt{n}}{% endequation %}

אז הסדרה {% equation %}Z_{n}{% endequation %} שואפת להתפלגות הנורמלית {% equation %}N\left(0,1\right){% endequation %} כאשר {% equation %}n{% endequation %} שואף לאינסוף. פורמלית, לכל {% equation %}-\infty<a<\infty{% endequation %}:

{% equation %}\lim_{n\to\infty}P\left(Z_{n}\le a\right)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{a}e^{-x^{2}/2}dx{% endequation %}

זה הניסוח הפורמלי, אבל הוא די שונה ממה שהצגתי עד כה בפוסטים שלי. מה שאני תמיד אמרתי הוא "בואו ניקח משתנה מקרי {% equation %}X{% endequation %} כלשהו. עכשיו בואו נחזור על ההגרלה שלו המון פעמים ונחבר את התוצאות" - כלומר, הסתכלתי על הסכום {% equation %}X_{1}+\ldots+X_{n}{% endequation %}. מכאן אמרתי "היי תראו עכשיו אם מציירים היסטוגרמה של הסכום אז פתאום יש עקומה של התפלגות נורמלית שמתארת אותה די במדויק". כדי לקבל את העקומה, חישבתי את {% equation %}\text{E}\left[X\right]=\mu{% endequation %} ואת {% equation %}\text{Var}\left(X\right)=\sigma^{2}{% endequation %} ואז בניתי את העקומה {% equation %}N\left(n\mu,\sqrt{n}\sigma\right){% endequation %}. בואו נראה שזה באמת אמור לעבוד, על פי משפט הגבול המרכזי.

ראשית, תזכורת: טענתי בפוסט הקודם שאם {% equation %}N\left(\mu,\sigma\right){% endequation %} היא התפלגות נורמלית עם תוחלת {% equation %}\mu{% endequation %} וסטיית תקן {% equation %}\sigma{% endequation %} אז {% equation %}N\left(0,1\right)=\frac{N\left(\mu,\sigma\right)-\mu}{\sigma}{% endequation %}, או בניסוח אחר - {% equation %}N\left(\mu,\sigma\right)=\sigma N\left(0,1\right)+\mu{% endequation %}.

עכשיו, אם אני אסמן {% equation %}Y_{n}=X_{1}+\ldots+X_{n}{% endequation %} אז משפט הגבול המרכזי אומר ש-{% equation %}N\left(0,1\right){% endequation %} היא קירוב טוב של {% equation %}Z_{n}=\frac{Y_{n}-n\mu}{\sigma\sqrt{n}}{% endequation %}. השוויון הזה מלמד אותי ש-{% equation %}Y_{n}=\sigma\sqrt{n}Z_{n}+n\mu{% endequation %}, כך שאני מצפה שקירוב טוב אל {% equation %}Y_{n}{% endequation %} (שהוא המשתנה המקרי שהופיע בהיסטוגרמות שלי) יהיה {% equation %}\sigma\sqrt{n}N\left(0,1\right)+n\mu=N\left(n\mu,\sigma\sqrt{n}\right){% endequation %}, וזו העקומה שציירתי בפועל. זה מסביר מאיפה האיורים שלי הגיעו אבל עדיין לא ברור למה משפט הגבול המרכזי נראה כמו שהוא נראה; לי למשל מפריע שהחלוקה היא ב-{% equation %}\sqrt{n}{% endequation %} ולא ב-{% equation %}n{% endequation %} כמו שעושים בחוק המספרים הגדולים. בהוכחה של משפט הגבול המרכזי אנחנו נראה למה הדברים הללו הם כמות שהם.

<h2>פונקציות יוצרות מומנטים</h2>

הכלי הטכני המרכזי שבו משתמשים בהוכחה הוא מושג שטרם הזכרתי בסדרת הפוסטים הזו: <strong>פונקציה יוצרת מומנטים</strong>. מה זה מומנטים כן הזכרתי, בחטף: עבור משתנה מקרי {% equation %}X{% endequation %}, <strong>המומנטים</strong> שלו הם הערכים המספריים {% equation %}\text{E}\left[X^{n}\right]{% endequation %} עבור {% equation %}n=1,2,\ldots{% endequation %}. עבור {% equation %}n=1{% endequation %} המומנט הוא פשוט התוחלת, וראינו שעבור {% equation %}n=2{% endequation %} המומנט הוא פשוט השונות ועוד התוחלת בריבוע (כי {% equation %}\text{Var}\left(X\right)=\text{E}\left[X^{2}\right]-\text{E}\left[X\right]^{2}{% endequation %}), אבל לא דיברתי על המומנטים עבור חזקות גבוהות יותר. הרעיון הוא שסדרת המומנטים של משתנה מקרי היא כמו ה-DNA שלו: מכילה כמות גדולה כל כך של מידע עליו שאפשר להסיק ממנה דברים מאוד לא טריוויאליים, גם אם היא לבדה לא כל הסיפור.

עוד מושג מאוד מועיל במתמטיקה, <a href="https://gadial.net/2011/08/07/generating_functions_hardcore_1/">שכבר הזכרתי</a> בבלוג כמה פעמים, הוא <strong>פונקציה יוצרת</strong>. הרעיון בפונקציה יוצרת הוא זה: אם יש לנו סדרה מעניינת של מספרים, {% equation %}a_{0},a_{1},a_{2},\ldots{% endequation %}, אחד מהקסמים שאנחנו יכולים לעשות הוא "לשתול" את המספרים הללו בתור מקדמים של טור חזקות, {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} ואז פתאום אנחנו מסוגלים לעשות עם הטור הזה מניפולציות מעניינות שמתורגמות לפעולות לא טריוויאליות על כל סדרת המספרים בבת אחת. זה כלי חזק ומרהיב.

על הרעיון הבסיסי הזה יש כמה וריאציות מועילות, ואחת מהן היא מה שנקרא <strong>הפונקציה היוצרת האקספוננציאלית</strong> של סדרת המספרים. כאן הרעיון הוא לשתול את המספרים בתוך הטור {% equation %}\sum_{n=0}^{\infty}a_{n}\frac{x^{n}}{n!}{% endequation %} שמזכיר קצת את הטור של פונקציית האקספוננט (עבור הסדרה {% equation %}a_{n}=1{% endequation %} מקבלים בדיוק את הטור של {% equation %}e^{x}{% endequation %}). איכשהו יצא לגמרי במקרה שדיברתי על הפונקציה הזו <a href="https://gadial.net/2024/12/18/bernoulli_numbers/">באחד מהפוסטים האחרונים</a> בבלוג; זה לא יצא ככה בכוונה, פשוט היא כל כך מועילה שהיא מתעקשת לצוץ בשני הקשרים שונים כמעט בו זמנית (אחרי שמעולם לא כתבתי עליה קודם בבלוג לדעתי אבל נעזוב את זה).

מה שנקרא בתורת ההסתברות <strong>פונקציה יוצרת מומנטים</strong> הוא בדיוק זה - הפונקציה היוצרת האקספוננציאלית של סדרת המומנטים, אם כי נוח להגדיר אותה בצורה קצת שונה. ראשית, אני אשתמש במשתנה {% equation %}t{% endequation %} כדי לא לבלבל עם המשתנה המקרי {% equation %}X{% endequation %} שהוא מרכז הדיון שלנו. עכשיו, עם משתנה מקרי אפשר כזכור להשתגע בשלל צורות, כי בסופו של דבר מדובר במשהו שמחזיר מספרים ממשיים אז אפשר לעשות איתו דברים שאנחנו עושים עם מספרים ממשיים - למשל להסתכל על {% equation %}e^{X}{% endequation %}, שזה פשוט משתנה מקרי שאומר "תגריל תוצאה כלשהי, תבדוק מה הערך ש-{% equation %}X{% endequation %} נותן על התוצאה הזו, תעלה את {% equation %}e{% endequation %} בחזקת הערך הזה". כדי לעשות את זה מעניין אני יכול גם לדחוף פנימה ערך מספרי {% equation %}t{% endequation %} כלשהו שאני מתייחס אליו כפרמטר ומכפיל אותו ב-{% equation %}X{% endequation %}, כלומר אני מסתכל על המשתנה המקרי {% equation %}e^{tX}{% endequation %}. אם זה משתנה מקרי, אפשר לחשב את התוחלת שלו, והיא תהיה תלויה בפרמטר {% equation %}t{% endequation %}, כלומר קיבלנו <strong>פונקציה</strong>

{% equation %}M\left(t\right)=\text{E}\left[e^{tX}\right]{% endequation %}

זו הפונקציה יוצרת המומנטים, ואנחנו ליטרלי יכולים להשתמש בה כדי <strong>ליצור</strong> את המומנטים על ידי "חילוץ" המקדמים מתוך הטור של {% equation %}e^{tX}{% endequation %} על ידי גזירה, כמו שקורה בחדו"א עם מה שנקרא <strong>טור טיילור</strong>. הנה איך שזה עובד:

{% equation %}M^{\prime}\left(t\right)=\left(\text{E}\left[e^{tX}\right]\right)^{\prime}=\text{E}\left[\left(e^{tX}\right)^{\prime}\right]=\text{E}\left[Xe^{tX}\right]{% endequation %}

אוקיי, קצת מיהרתי פה. אני מבצע <strong>החלפה</strong> בין אופרטור התוחלת ואופרטור הגזירה במעבר האמצעי - למה זה מעבר לגיטימי? אם פותחים את ההגדרה של התוחלת במקרה הסופי מקבלים

{% equation %}\text{E}\left[e^{tX}\right]=\sum_{i=1}^{k}P\left(X=a_{i}\right)e^{ta_{i}}{% endequation %}

ואפשר להשתמש בכך שנגזרת היא לינארית, כלומר {% equation %}\left(f+g\right)^{\prime}=f^{\prime}+g^{\prime}{% endequation %}, מה שניתן להכללה באינדוקציה לכל סכום סופי, ולכן 

{% equation %}\left[\sum_{i=1}^{k}P\left(X=a_{i}\right)e^{ta_{i}}\right]^{\prime}=\sum_{i=1}^{k}P\left(X=a_{i}\right)\left(e^{ta_{i}}\right)^{\prime}=\sum_{i=1}^{k}P\left(X=a_{i}\right)a_{i}e^{ta_{i}}{% endequation %}

וקיבלנו בדיוק את הביטוי של {% equation %}\text{E}\left[Xe^{tX}\right]{% endequation %}.

העניין הוא שמה שעובד עבור סכום <strong>סופי</strong> לא בהכרח עובד במקרה של סכום אינסופי, או במקרה הרציף שבו התוחלת היא אינטגרל. כלומר, את הקסם הזה אי אפשר לעשות <strong>לכל</strong> משתנה מקרי אלא רק לכאלו שהם "נחמדים מספיק", אבל בואו לא ניכנס לתנאים המדויקים הפעם. במקום זה, בואו נראה איך אפשר להשתמש בזה: אם {% equation %}M^{\prime}\left(t\right)=\text{E}\left[Xe^{tX}\right]{% endequation %} אז {% equation %}M^{\prime}\left(0\right)=\text{E}\left[X\right]{% endequation %} וקיבלנו את המומנט הראשון.

עכשיו, אפשר להמשיך לגזור את {% equation %}Xe^{tX}{% endequation %}. מכיוון שהנגזרת היא על פי {% equation %}t{% endequation %}, ה-{% equation %}X{% endequation %} שבו מוכפל {% equation %}e^{tX}{% endequation %} הוא בסך הכל קבוע, ולכן מקבלים

{% equation %}M^{\prime\prime}\left(t\right)=\text{E}\left[X^{2}e^{tX}\right]{% endequation %}

כלומר

{% equation %}M^{\prime\prime}\left(0\right)=\text{E}\left[X^{2}\right]{% endequation %}

ובאופן כללי נקבל {% equation %}M^{\left(i\right)}=\text{E}\left[X^{i}\right]{% endequation %}. זה בדיוק מה שקורה גם כשגוזרים את הטור {% equation %}\sum_{n=0}^{\infty}a_{n}\frac{x^{n}}{n!}{% endequation %} בדיוק {% equation %}i{% endequation %} פעמים ומציבים {% equation %}x=0{% endequation %}; מקבלים את {% equation %}a_{i}{% endequation %}.

איך כל זה מתקשר למשפט הגבול המרכזי? עם הטענה הבאה: אם יש לנו סדרה {% equation %}Z_{1},Z_{2},\ldots{% endequation %} של משתנים מקריים עם פונקציות צפיפות {% equation %}F_{Z_{n}}{% endequation %} ופונקציות יוצרות הסתברות {% equation %}M_{Z_{n}}{% endequation %}, ואם {% equation %}Z{% endequation %} הוא משתנה מקרי עם פונקציית צפיפות {% equation %}F_{Z}{% endequation %} ופונקציה יוצרת הסתברות {% equation %}M_{Z}{% endequation %}, אז אם מתקיים {% equation %}\lim_{n\to\infty}M_{Z_{n}}\left(t\right)=M_{Z}\left(t\right){% endequation %} עבור כל {% equation %}t{% endequation %}, אז {% equation %}F_{Z_{n}}\left(t\right)\to F_{Z}\left(t\right){% endequation %} עבור כל {% equation %}t{% endequation %} שעבורו {% equation %}F_{Z}\left(t\right){% endequation %} רציפה. במילים אחרות - מספיק לנו להראות שאיפה של סדרת הפונקציות יוצרות המומנטים כדי להראות שאיפה של פונקציות הצפיפות, שהן לכאורה האובייקט המורכב יותר.

הטענה הזו היא טענה <strong>כבדה</strong>. כדי להוכיח אותה אני אצטרך כנראה פוסט שלם (או אפילו יותר) ולהיכנס למתמטיקה טכנית יותר מאשר אני רוצה כרגע. המטרה שלי בפוסטים הללו היא לראות איך זה שהתפלגות נורמלית היא מה שהיא גורר את משפט הגבול המרכזי; אז בואו נראה איך טענת העזר הזו מוכיחה לנו את משפט הגבול המרכזי.

<h2>הוכחת משפט הגבול המרכזי</h2>

בואו נזכיר שוב מה אנחנו רוצים להוכיח. אנחנו לוקחים סדרה {% equation %}X_{1},X_{2},\ldots{% endequation %} של משתנים מקריים בלתי תלויים שמתפלגים באותו אופן, עם תוחלת {% equation %}\mu{% endequation %} וסטיית תקן {% equation %}\sigma{% endequation %}, מגדירים

{% equation %}Z_{n}=\frac{X_{1}+\ldots+X_{n}-n\mu}{\sigma\sqrt{n}}{% endequation %}

ומקבלים שהסדרה {% equation %}Z_{n}{% endequation %} שואפת להתפלגות הנורמלית {% equation %}N\left(0,1\right){% endequation %} כאשר {% equation %}n{% endequation %} שואף לאינסוף. מה שנוכיח הוא את המשפט למקרה שבו {% equation %}\mu=0,\sigma=1{% endequation %}, כי אפשר לבצע רדוקציה מהמקרה הכללי למקרה הזה: אם נגדיר {% equation %}Y_{i}=\frac{X_{i}-\mu}{\sigma}{% endequation %} אז נקבל שהתוחלת של {% equation %}Y_{i}{% endequation %} היא 0 וסטיית התקן היא 1, ולכן {% equation %}\frac{Y_{i}+\ldots+Y_{n}}{\sqrt{n}}{% endequation %} שואפת אל {% equation %}N\left(0,1\right){% endequation %}. עכשיו נציב את {% equation %}Y_{i}=\frac{X_{i}-\mu}{\sigma}{% endequation %} בביטוי {% equation %}\frac{Y_{i}+\ldots+Y_{n}}{\sqrt{n}}{% endequation %} ששואף ל-{% equation %}N\left(0,1\right){% endequation %} ונקבל את הביטוי {% equation %}\frac{X_{1}+\ldots+X_{n}-n\mu}{\sigma\sqrt{n}}{% endequation %} שגם שואף ל-{% equation %}N\left(0,1\right){% endequation %} כי זה אותו ביטוי.

אם כן, מעתה והלאה נניח {% equation %}\mu=0{% endequation %} ו-{% equation %}\sigma=1{% endequation %} ולכן {% equation %}Z_{n}=\frac{X_{1}+\ldots+X_{n}}{\sqrt{n}}=\frac{X_{1}}{\sqrt{n}}+\ldots+\frac{X_{n}}{\sqrt{n}}{% endequation %}. המטרה שלי היא למצוא את {% equation %}M_{Z_{n}}\left(t\right){% endequation %} - הפונקציה יוצרת המומנטים של {% equation %}Z_{n}{% endequation %}, ולראות לאן היא שואפת (כשאני אראה לאן היא שואפת זה מה ש<strong>יכתיב</strong> לי את האופן שבו התפלגות נורמלית אמורה להיראות). מכיוון שהצגתי את {% equation %}Z_{n}{% endequation %} בתור סכום סופי, בואו קודם נראה איך הפונקציה יוצרת המומנטים של כל איבר בסכום נראית. 

ראשית, עבור {% equation %}X_{i}{% endequation %}, הפונקציה יוצרת המומנטים שלו היא {% equation %}M\left(t\right)=\text{E}\left[e^{tX_{i}}\right]{% endequation %}. שנית, עבור האיבר המנורמל {% equation %}\frac{X_{i}}{\sqrt{n}}{% endequation %} הפונקציה יוצרת המומנטים היא {% equation %}\text{E}\left[e^{t\frac{X_{i}}{\sqrt{n}}}\right]=\text{E}\left[e^{\frac{t}{\sqrt{n}}X_{i}}\right]=M\left(\frac{t}{\sqrt{n}}\right){% endequation %}. ולכן עכשיו נקבל

{% equation %}M_{Z_{n}}\left(t\right)=\text{E}\left[e^{tZ_{n}}\right]=\text{E}\left[e^{t\sum_{i=1}^{n}\frac{X_{i}}{\sqrt{n}}}\right]=\text{E}\left[\prod_{i=1}^{n}e^{t\frac{X_{i}}{\sqrt{n}}}\right]{% endequation %}

כי זה הקסם של אקספוננט - סכום במעריך הופך למכפלת אקספוננטים (על פי כללי החזקות: {% equation %}e^{a+b}=e^{a}\cdot e^{b}{% endequation %}).

עכשיו, זה <strong>בהחלט לא נכון</strong> באופן כללי שתוחלת של מכפלה היא מכפלת התוחלות, כלומר {% equation %}\text{E}\left[XY\right]\ne\text{E}\left[X\right]\text{E}\left[Y\right]{% endequation %} באופן כללי, וזה די ברור - אם זה היה נכון, היינו מקבלים ש-{% equation %}\text{E}\left[X^{2}\right]=\text{E}\left[X\right]^{2}{% endequation %} וכל מושג סטיית התקן היה נעלם. אבל השוויון {% equation %}\text{E}\left[XY\right]=\text{E}\left[X\right]\text{E}\left[Y\right]{% endequation %} דווקא <strong>כן נכון</strong> אם {% equation %}X,Y{% endequation %} הם משתנים מקריים בלתי תלויים, וזה בדיוק מה שאני מניח כאן - שכל אברי הסדרה {% equation %}X_{1},X_{2},\ldots,X_{n}{% endequation %} הם בלתי תלויים, ולכן גם המשתנים {% equation %}e^{t\frac{X_{i}}{\sqrt{n}}}{% endequation %} שנבנים מתוכם. כך שאני מקבל:

{% equation %}\text{E}\left[\prod_{i=1}^{n}e^{t\frac{X_{i}}{\sqrt{n}}}\right]=\prod_{i=1}^{n}\text{E}\left[e^{t\frac{X_{i}}{\sqrt{n}}}\right]=\prod_{i=1}^{n}M\left(\frac{t}{\sqrt{n}}\right)=\left[M\left(\frac{t}{\sqrt{n}}\right)\right]^{n}{% endequation %}

אז מה שאנחנו רוצים להבין הוא את הגבול {% equation %}\lim_{n\to\infty}\left[M\left(\frac{t}{\sqrt{n}}\right)\right]^{n}{% endequation %}. זה בעצם המקום הראשון שבו קופץ לעיניים למה "צריך" ש-{% equation %}e{% endequation %} יופיע בהתפלגות נורמלית. כזכור, אחת מהדרכים השקולות לתאר את {% equation %}e^{x}{% endequation %} היא באמצעות גבול: {% equation %}e^{x}=\lim_{n\to\infty}\left(1+\frac{x}{n}\right)^{n}{% endequation %}, אז העובדה שיש לנו בביטוי {% equation %}\lim_{n\to\infty}\left[M\left(\frac{t}{\sqrt{n}}\right)\right]^{n}{% endequation %} גבול שתלוי ב-{% equation %}n{% endequation %}, חזקה שהיא {% equation %}n{% endequation %} ואיבר פנימי שהוא {% equation %}\frac{t}{\sqrt{n}}{% endequation %} זה... מעורר חשד. 

עכשיו, איך מטפלים בביטוי {% equation %}\left[M\left(\frac{t}{\sqrt{n}}\right)\right]^{n}{% endequation %}? ה-{% equation %}n{% endequation %} במעריך הוא מעצבן, והדרך הסטנדרטית להיפטר ממנו היא לקחת לוגריתם להכל, כי {% equation %}\left(a^{n}\right)=n\log a{% endequation %}{% equation %}\log{% endequation %}. אז בואו נשאל את עצמנו מהו הגבול

{% equation %}\lim_{n\to\infty}n\log M\left(\frac{t}{\sqrt{n}}\right){% endequation %}

אם הגבול הזה יהיה {% equation %}A{% endequation %} והלוגריתם שלי הוא על בסיס {% equation %}a{% endequation %}, אז הגבול של {% equation %}\lim_{n\to\infty}\left[M\left(\frac{t}{\sqrt{n}}\right)\right]^{n}{% endequation %} יהיה {% equation %}a^{A}{% endequation %}. איזה בסיס של לוגריתם <strong>כדאי לי</strong> לבחור? אני לא רוצה שיהיו לי החלטות שרירותיות, אז בואו נתקדם עם ההוכחה ונראה איזה בסיס יצוץ מאליו (ספוילר: {% equation %}e{% endequation %}. זה תמיד {% equation %}e{% endequation %}).

אם כן, הביטוי שאנחנו צריכים להבין עכשיו הוא הפונקציה {% equation %}\log M\left(\frac{t}{\sqrt{n}}\right){% endequation %}. הכל נהיה פשוט יותר אחרי שיש לנו סימונים, אז נסמן: {% equation %}L\left(t\right)=\log M\left(t\right){% endequation %}, ועכשיו אנחנו רוצים להבין את הגבול {% equation %}\lim_{n\to\infty}nL\left(\frac{t}{\sqrt{n}}\right){% endequation %}. איך עושים את זה? אין לי מושג, אבל לגשש בצורה עיוורת אפשר, ואחד מהכלים המועילים שיש לנו בחישוב גבולות הוא <strong>כלל לופיטל</strong>. הרעיון בו פשוט: אם {% equation %}f\left(x\right),g\left(x\right){% endequation %} הן שתי פונקציות כך ש-{% equation %}\lim_{x\to\infty}f\left(x\right)=\lim_{x\to\infty}g\left(x\right)=0{% endequation %} אז {% equation %}\lim_{x\to\infty}\frac{f\left(x\right)}{g\left(x\right)}=\lim_{x\to\infty}\frac{f^{\prime}\left(x\right)}{g^{\prime}\left(x\right)}{% endequation %}. כלומר, בדומה לאינטגרציה בחלקים שבה השתמשתי בפוסט הקודם, גם כאן אפשר לחשב דברים על ידי גזירה של הפונקציות הרלוונטיות עד שיהיו פשוטות מספיק.

אצלנו הגבול הוא לא של פונקציות אלא של סדרה, אבל כל עוד הפונקציות המעורבות הן רציפות מקבלים אותו דבר. אבל בשביל להשתמש בלופיטל אנחנו צריכים <strong>מנה </strong>של שתי פונקציות ששואפות לאפס: אצלנו יש <strong>מכפלה</strong> של שתי פונקציות, {% equation %}nL\left(\frac{t}{\sqrt{n}}\right){% endequation %}, שאחת מהן ({% equation %}n{% endequation %}) בכלל שואפת לאינסוף... אה, הטריק פה הוא פשוט מאוד: {% equation %}nL\left(\frac{t}{\sqrt{n}}\right)=\frac{L\left(\frac{t}{\sqrt{n}}\right)}{n^{-1}}{% endequation %}, ועכשיו הפונקציה במכנה היא {% equation %}\frac{1}{n}{% endequation %} ששואפת לאפס כש-{% equation %}n\to\infty{% endequation %}. ומה קורה במונה? הרציפות של {% equation %}L{% endequation %} אומרת ש-{% equation %}L\left(\frac{t}{\sqrt{n}}\right)\to L\left(0\right){% endequation %}, אבל מהו {% equation %}L\left(0\right){% endequation %}? ומה נקבל אחרי שנגזור?

ובכן, כזכור {% equation %}L\left(t\right)=\log M\left(t\right){% endequation %}. מכיוון ש-{% equation %}M\left(t\right)=\text{E}\left[e^{tX_{i}}\right]{% endequation %} הרי ש-{% equation %}M\left(0\right)=\text{E}\left[e^{0\cdot X_{i}}\right]=\text{E}\left[1\right]=1{% endequation %} כך ש-{% equation %}L\left(0\right)=\log1=0{% endequation %}. זה טוב, זה בדיוק מה שאנחנו רוצים. עכשיו, מה עם הנגזרת? יש לנו כאן עסק עם הרכבה של פונקציות: {% equation %}\log{% endequation %} שמורכבת על {% equation %}M{% endequation %}. זה מצריך מאיתנו שני דברים: את הכלל של נגזרת של לוגריתם, ואת כלל השרשרת. והכלל לנגזרת של לוגריתם הוא

{% equation %}\left(\log_{a}t\right)^{\prime}=\frac{1}{t\ln a}{% endequation %}, כאשר {% equation %}\ln{% endequation %} הוא לוגריתם על בסיס {% equation %}e{% endequation %}. הביטוי הזה הופך לפשוט יותר אם מלכתחילה הלוגריתם שלנו הוא על בסיס {% equation %}e{% endequation %}; אז מקבלים {% equation %}\left(\log t\right)^{\prime}=\frac{1}{t}{% endequation %}. אז יש לנו סיבה טובה לבחור שהלוגריתם שלנו יהיה על בסיס {% equation %}e{% endequation %}, מה שאומר שאחרי שנצליח לחשב את {% equation %}\lim_{n\to\infty}n\log M\left(\frac{t}{\sqrt{n}}\right)=A{% endequation %}, נקבל ש-{% equation %}\lim_{n\to\infty}\left[M\left(\frac{t}{\sqrt{n}}\right)\right]^{n}=e^{A}{% endequation %}.

עכשיו, על פי כלל השרשרת {% equation %}\left[f\left(g\left(x\right)\right)\right]^{\prime}=f^{\prime}\left(g\left(x\right)\right)g^{\prime}\left(x\right){% endequation %} אנחנו מקבלים

{% equation %}L^{\prime}=\left(\log M\right)^{\prime}=\frac{M^{\prime}}{M}{% endequation %} (יש לדבר כזה שם - "הנגזרת הלוגריתמית" של {% equation %}M{% endequation %})

ראינו כבר ש-{% equation %}M\left(0\right)=1{% endequation %}. כמו כן, {% equation %}M^{\prime}\left(0\right)=\text{E}\left[X\right]=\mu=0{% endequation %} (זוכרים? ראינו שככה פונקציה יוצרת מומנטים עובדת). אז קיבלנו ש-{% equation %}L^{\prime}\left(0\right)=0{% endequation %}, מה שאומר שכלל לופיטל צפוי להיתקל בקשיים כי גם אחרי הגזירה המונה ישאף ל-0. אבל אפשר לגזור שוב! הפעם נשתמש בכלל לגזירה של מנה, {% equation %}\left(\frac{f}{g}\right)^{\prime}=\frac{f^{\prime}g-fg^{\prime}}{g^{2}}{% endequation %} ונקבל

{% equation %}L^{\prime\prime}=\left(\frac{M^{\prime}}{M}\right)^{\prime}=\frac{M^{\prime\prime}M-\left(M^{\prime}\right)^{2}}{M^{2}}{% endequation %}

ולכן כשנציב {% equation %}0{% endequation %} ונשתמש בכך ש-{% equation %}M\left(0\right)=1,M^{\prime}\left(0\right)=0,M^{\prime\prime}\left(0\right)=\text{E}\left[X^{2}\right]=\sigma^{2}+\mu^{2}=1{% endequation %}, נקבל

{% equation %}L^{\prime\prime}\left(0\right)=\frac{1-0^{2}}{1}=1{% endequation %}

וזה כבר משהו לעבוד איתו! כל מה שנשאר לנו הוא לקחת את הביטוי {% equation %}\frac{L\left(\frac{t}{\sqrt{n}}\right)}{n^{-1}}{% endequation %} ולגזור בו (בנפרד!) את המונה והמכנה פעמיים. זה לא יהיה כזה נורא, נכון? נקודה אחת שצריך לשים לב אליה היא שהגזירה שלנו היא ביחס למשתנה {% equation %}n{% endequation %}, ואילו דווקא אל {% equation %}t{% endequation %} אנחנו מתייחסים בתור קבוע, כי הגבול שלנו הוא כש-{% equation %}n{% endequation %} רץ לאינסוף. זה הופך את הכל לטיפה יותר מסובך.

כלל הגזירה הבסיסי ביותר הוא {% equation %}\left(x^{a}\right)^{\prime}=ax^{a-1}{% endequation %}. מכאן נקבל ש-{% equation %}\left(n^{-1}\right)^{\prime}=-n^{-2}{% endequation %} וש-{% equation %}\left(\frac{1}{\sqrt{n}}\right)^{\prime}=\left(n^{-\frac{1}{2}}\right)^{\prime}=-\frac{1}{2}n^{-\frac{3}{2}}{% endequation %}.

הנגזרת של {% equation %}L\left(\frac{t}{\sqrt{n}}\right){% endequation %} על פי כלל השרשרת היא {% equation %}\left(\frac{t}{\sqrt{n}}\right)^{\prime}L^{\prime}\left(\frac{t}{\sqrt{n}}\right)=-\frac{t}{2}n^{-\frac{3}{2}}L^{\prime}\left(\frac{t}{\sqrt{n}}\right){% endequation %} , ולכן מכלל לופיטל אנחנו מקבלים

{% equation %}\lim_{n\to\infty}\frac{L\left(\frac{t}{\sqrt{n}}\right)}{n^{-1}}=\lim_{n\to\infty}\frac{-\frac{t}{2}n^{-\frac{3}{2}}L^{\prime}\left(\frac{t}{\sqrt{n}}\right)}{-n^{-2}}=\lim_{n\to\infty}\frac{tL^{\prime}\left(\frac{t}{\sqrt{n}}\right)}{2n^{-1/2}}{% endequation %}

המונה עדיין שואף לאפס כש-{% equation %}n\to\infty{% endequation %} (כי ראינו {% equation %}L^{\prime}\left(0\right)=0{% endequation %}) והמכנה, שהוא עכשיו {% equation %}-\frac{2}{\sqrt{n}}{% endequation %}, גם כן שואף לאפס, אז אפשר להשתמש שוב בכלל לופיטל. הנגזרת של המכנה תהיה {% equation %}\left(2n^{-\frac{1}{2}}\right)^{\prime}=-n^{-\frac{3}{2}}{% endequation %}. המונה יהיה כמו קודם (אל ה-{% equation %}t{% endequation %} שמופיע שם אנחנו כאמור מתייחסים בתור קבוע והוא לא משפיע על הגזירה). לכן נקבל מכלל לופיטל

{% equation %}\lim_{n\to\infty}\frac{tL^{\prime}\left(\frac{t}{\sqrt{n}}\right)}{2n^{-1/2}}=\lim_{n\to\infty}\frac{-\frac{t^{2}}{2}n^{-\frac{3}{2}}L^{\prime\prime}\left(\frac{t}{\sqrt{n}}\right)}{-n^{-3/2}}=\lim_{n\to\infty}\frac{t^{2}}{2}L^{\prime\prime}\left(\frac{t}{\sqrt{n}}\right){% endequation %}

הופה! העלמנו לגמרי את מה שהופיע במכנה! ועכשיו, בגלל ש-{% equation %}L^{\prime\prime}\left(0\right)=1{% endequation %}, אנחנו מקבלים גבול פשוט במיוחד: {% equation %}\lim_{n\to\infty}\frac{t^{2}}{2}L^{\prime\prime}\left(\frac{t}{\sqrt{n}}\right)=\frac{t^{2}}{2}{% endequation %}. זה אומר שמצאנו את מה שהפונקציה יוצרת המומנטים של {% equation %}Z_{n}{% endequation %} שואפת אליו: {% equation %}\lim_{n\to\infty}M_{Z_{n}}\left(t\right)=e^{\frac{t^{2}}{2}}{% endequation %}. זה, סוף כל סוף, מסביר מאיפה מגיע {% equation %}e^{\frac{t^{2}}{2}}{% endequation %} להתפלגות הנורמלית - לפחות מבחינה טכנית - אם כי יש עוד שלב לא טריוויאלי אחד שצריך להתגבר עליו.

<h2>הפונקציה יוצרת המומנטים של התפלגות נורמלית</h2>

ההוכחה עדיין לא בדיוק הסתיימה. מה שהראיתי הוא שאם {% equation %}Z{% endequation %} הוא משתנה מקרי עם פונקציה יוצרת מומנטים {% equation %}M_{Z}\left(t\right)=e^{\frac{t^{2}}{2}}{% endequation %} אז הפונקציה יוצרת המומנטים של אברי הסדרה {% equation %}Z_{n}{% endequation %} תתכנס לפונקציה יוצרת המומנטים של {% equation %}Z{% endequation %}. המסקנה, מטענת העזר שציטטתי בלי הוכחה, היא ש-{% equation %}F_{Z_{n}}\left(t\right){% endequation %} מתכנסת אל {% equation %}F_{Z}\left(t\right){% endequation %}. אבל מהי פונקציית הצפיפות {% equation %}F_{Z}\left(t\right){% endequation %}? זה השלב שבו צריך לקחת את ההתפלגות הנורמלית, לחשב את הפונקציה יוצרת המומנטים שלה ולקבל {% equation %}e^{\frac{t^{2}}{2}}{% endequation %}. זה חישוב די פשוט בהינתן כל החישובים שכבר עברנו, אבל יש כאן גם שאלה מעניינת - האם אפשר ללכת "בכיוון השני"? להתחיל מהשוויון שצריך להתקיים ולהסיק איך ההתפלגות הנורמלית אמורה להיראות?

באופן כללי אני יכול לסמן {% equation %}F_{Z}\left(z\right)=f\left(z\right){% endequation %} ואז להשתמש בשוויון {% equation %}e^{t^{2}/2}=\text{E}\left[e^{tZ}\right]{% endequation %} כש-{% equation %}\text{E}\left[e^{tZ}\right]{% endequation %} הוא מה ש<strong>מגדיר</strong> את הפונקציה יוצרת המומנטים, ולקבל שאני צריך שיתקיים השוויון 

{% equation %}e^{t^{2}/2}=\int_{-\infty}^{\infty}e^{tz}f\left(z\right)dz{% endequation %}

הדבר הזה נקרא <strong>משוואה אינטגרלית</strong>: בדומה למשוואה דיפרנציאלית, זו משוואה שבה הנעלם הוא לא סתם ערך מספרי אלא <strong>פונקציה</strong>, והמידע שיש לנו על הפונקציה הזו מערב אינטגרל שלה. כמו עם משוואות דיפרנציאליות, פתרון משוואות אינטגרליות זה עניין מסובך והרבה פעמים לומר "אוקיי, בואו ננחש שהפתרון הוא מהצורה כך וכך..." הוא לגיטימי, אבל עבור המשוואה שלעיל דווקא יש שיטת פתרון כללית, פחות או יותר, בעזרת מה שנקרא <strong>התמרת לפלס</strong>. להיכנס לזה לוקח אותי רחוק מדי ממה שאפשר לדבר עליו במרוכז כאן, אז בואו ננקוט בגישה השניה: נתחיל עם ההגדרה הידועה של {% equation %}f\left(z\right){% endequation %} עבור התפלגות נורמלית ונראה שאנחנו מקבלים את השוויון למעלה. החישובים הספציפיים שנצטרך לבצע הם דומים למדי לחישובים שצריך לעשות אם פותרים את המשוואה האינטגרלית.

אם כן, {% equation %}f\left(z\right)=\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}{% endequation %}, ולכן אנחנו מחשבים את האינטגרל

{% equation %}\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{tz}e^{-z^{2}/2}dz{% endequation %}

לב העניין הוא מה שהולך בחזקה של {% equation %}e{% endequation %}. בהתחלה כתוב שם

{% equation %}tz-\frac{z^{2}}{2}{% endequation %}

לב הרעיון הטכני (גם פה וגם בגישת המשוואה האינטגרלית) הוא <strong>להשלים לריבוע</strong> את הביטוי הזה; להכניס את ה-{% equation %}z{% endequation %}-ים בצורה יפה לסוגריים שאותם מעלים בריבוע, ואולי להוציא החוצה איזה קבוע שקשור ל-{% equation %}t{% endequation %}. זו בדיוק אותה השלמה לריבוע שאיתה גם פותרים משוואה ריבועית, <a href="https://gadial.net/2023/12/16/quadratic_equations/">כמו שהראיתי</a> פעם בבלוג.

אז ראשית, בואו נעשה חישובון:

{% equation %}tz-\frac{z^{2}}{2}=-\frac{1}{2}\left(z^{2}-2tz\right){% endequation %}

מה שבתוך הסוגריים כבר די קרוב למשהו ריבועי! רק צריך להוסיף ולחסר {% equation %}t^{2}{% endequation %}:

{% equation %}-\frac{1}{2}\left(z^{2}-2tz\right)=-\frac{1}{2}\left(z^{2}-2tz+t^{2}-t^{2}\right)=\frac{t^{2}}{2}-\frac{1}{2}\left(z-t\right)^{2}{% endequation %}

בום! ה-{% equation %}\frac{t^{2}}{2}{% endequation %} שקיבלנו יהיה בדיוק אותו {% equation %}\frac{t^{2}}{2}{% endequation %} ב-{% equation %}e^{t^{2}/2}{% endequation %} שאנחנו מצפים לקבל בסוף הדרך. בואו נחזור אל האינטגרל:

{% equation %}\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{tz}e^{-z^{2}/2}dz=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{t^{2}/2-\left(z-t\right)^{2}/2}dz{% endequation %}

עכשיו אפשר להוציא את הקבוע החוצה, תוך שימוש בכך ש-{% equation %}e^{a-b}=e^{a}e^{-b}{% endequation %}:

{% equation %}\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{t^{2}/2-\left(z-t\right)^{2}/2}dz=e^{t^{2}/2}\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-\left(z-t\right)^{2}/2}dz{% endequation %}

את האינטגרל {% equation %}\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-\left(z-t\right)^{2}/2}dz{% endequation %} אנחנו כבר יודעים לחשב; שברנו עליו את הראש כשרצינו להוכיח שפונקציית הצפיפות של ההתפלגות הנורמלית מסתכמת ל-1. העובדה שאנחנו צריכים לעבור דרכו היא "חוק שימור הקושי" - גם אם הייתי מנסה ללכת דרך משוואות אינטגרליות הייתי צריך לצלול בים טכני של טענות כלליות על הלהטוטים שאנחנו יכולים לעשות במסגרת חדו"א; למזלי בגישה הנוכחית אני יכול פשוט לומר שכבר עשינו את זה. מה שראינו היה {% equation %}\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-\frac{x^{2}}{2}}dx=1{% endequation %}, וזה בדיוק אותו הדבר כמו אצלנו עד כדי החלפת המשתנה {% equation %}x=z-t{% endequation %} שלא משפיעה על האינטגרל כי גבולות האינטגרציה הם ממילא מ-{% equation %}-\infty{% endequation %} עד {% equation %}\infty{% endequation %} והיעקוביאן של ההחלפה (שהוא במקרה הזה פשוט נגזרת) יוצא 1.

<h2>ולסיום - אז למה הדברים הם כמו שהם?</h2>

לסיום סדרת הפוסטים הזו, בואו נחזור אל הפונקציה שאותה רצינו להבין: {% equation %}f\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\left(x-\mu\right)^{2}/2\sigma^{2}}{% endequation %}, פונקציית הצפיפות של התפלגות נורמלית. בשלב הזה אנחנו כבר יודעים ש-{% equation %}\pi{% endequation %} כאן כדי להבטיח שהכל יסתכם ל-1, שה-{% equation %}\mu{% endequation %} וה-{% equation %}\sigma{% endequation %} מייצגים את התוחלת וסטיית התקן ואפשר לנרמל אותם החוצה ושהאקספוננט מגיע, בגדול, מזה שהפונקציה שמתארת התנהלות של סכום משתנים מקריים בלתי תלויים ומפולגים אחיד נראית כמו{% equation %}\lim_{n\to\infty}\left[M\left(\frac{t}{\sqrt{n}}\right)\right]^{n}{% endequation %}. וזה בעצם מגיע אל מה שהטריד <strong>אותי</strong> עם משפט הגבול המרכזי: מה זה ה-{% equation %}\frac{1}{\sqrt{n}}{% endequation %} הזה? למה כדי לנרמל מחלקים דווקא בו? מה קרה ל-{% equation %}\frac{1}{n}{% endequation %} הישן והטוב? ולמה לחלק בכלל? בתחילת הפוסט הזכרתי את השימוש שעשיתי במשפט הגבול המרכזי - פשוט חיברתי את ה-{% equation %}X_{i}{% endequation %}-ים שלי וקירבתי את התוצאה הזו עם עקומה נורמלית; בשביל לעשות את זה לא הספיק לדעת רק את {% equation %}\mu,\sigma{% endequation %} אלא הייתי צריך להכניס גם את {% equation %}n{% endequation %} למשוואה: כפלתי ב-{% equation %}n{% endequation %} גם את {% equation %}\mu{% endequation %} וגם את {% equation %}\sigma^{2}{% endequation %} (כלומר, בפועל כפלתי את {% equation %}\sigma{% endequation %} ב-{% equation %}\sqrt{n}{% endequation %} והנה השורש צץ שוב).

אבל מה היה קורה אם מלכתחילה הייתי מנרמל על ידי חלוקה ב-{% equation %}n{% endequation %} ולכן מגיע אל חישוב של {% equation %}\lim_{n\to\infty}\left[M\left(\frac{t}{n}\right)\right]^{n}{% endequation %}? התשובה, כמובן, היא ששום דבר לא היה עובד. כזכור, כדי להתמודד עם הגבול הזה הגדרתי {% equation %}L\left(t\right)=\log M\left(t\right){% endequation %} ואז חישבתי את הגבול {% equation %}\lim_{n\to\infty}nL\left(\frac{t}{\sqrt{n}}\right){% endequation %} באמצעות כלל לופיטל. עוד לפני שאומרים לופיטל, כבר ברור שהגבול {% equation %}\lim_{n\to\infty}nL\left(\frac{t}{\sqrt{n}}\right){% endequation %} קיים בכלל רק בזכות זה שיש פה שני כוחות שונים וסותרים שמאזנים אחד את השני. ה-{% equation %}n{% endequation %} שבו כופלים שואף לאינסוף, בעוד שה-{% equation %}L\left(\frac{t}{\sqrt{n}}\right){% endequation %} שואף לאפס. בגבולות מהצורה "משהו ששואף לאינסוף כפול משהו ששואף לאפס" פחות או יותר הכל יכול לקרות, והסיכוי שנקבל תוצאה סופית תלוי ביחסים העדינים בין שתי הפונקציות שאותם כופלים. כלל לופיטל הוא בדיוק דרך "לקלף" מעל שתי הפונקציות המעורבות שכבה אחר שכבה של סיבוכיות עד שמגיעים אל הגרעין העדין שלהן שאנחנו יודעים להשוות. ועכשיו חדל פילוסופיה ובואו נדבר תכל'ס. מה היה קורה אם היינו מחלקים ב-{% equation %}n{% endequation %} ולא ב-{% equation %}\sqrt{n}{% endequation %}? (אם לא היינו מחלקים <strong>בכלל</strong> ב-{% equation %}n{% endequation %} אז היינו מקבלים {% equation %}\lim_{n\to\infty}L\left(t\right)=L\left(t\right){% endequation %} וקבוע כפול אינסוף הוא אינסוף).

בואו נעשה קופי-פייסט מההוכחה שכתבתי קודם ונחליף כל מופע של -{% equation %}\sqrt{n}{% endequation %} ב-{% equation %}n{% endequation %}, עם ההשלכות המתאימות:

הנגזרת של {% equation %}L\left(\frac{t}{n}\right){% endequation %} על פי כלל השרשרת היא {% equation %}\left(\frac{t}{n}\right)^{\prime}L^{\prime}\left(\frac{t}{n}\right)=-tn^{-2}L^{\prime}\left(\frac{t}{n}\right){% endequation %} , ולכן מכלל לופיטל אנחנו מקבלים

{% equation %}\lim_{n\to\infty}\frac{L\left(\frac{t}{n}\right)}{n^{-1}}=\lim_{n\to\infty}\frac{-tn^{-2}L^{\prime}\left(\frac{t}{n}\right)}{-n^{-2}}=\lim_{n\to\infty}tL^{\prime}\left(\frac{t}{n}\right){% endequation %}

וזה... טוב? נפטרנו לגמרי מהגורם שבמכנה! אבל ראינו קודם ש-{% equation %}L^{\prime}\left(0\right)=0{% endequation %}, כלומר {% equation %}\lim_{n\to\infty}tL^{\prime}\left(\frac{t}{n}\right)=0{% endequation %}, וזה ממש לא טוב לנו. זה אומר שעבור המשתנה המקרי {% equation %}Z_{n}=\frac{X_{1}+\ldots+X_{n}}{n}{% endequation %} מתקיים {% equation %}M_{Z}=e^{0}=1{% endequation %}, ובמילים אחרות - קיבלנו משתנה מקרי שכל המומנטים שלו הם 0. או, בניסוח שקצת יותר קל להבין - קיבלנו אפס. וזה לא אמור להיות מפתיע שקיבלנו אפס כי זה בדיוק מה שאומר <strong>אי-שוויון צ'בישב</strong> עבור התפלגויות שסטיית התקן שלהן היא אפס. כזכור, הוא אומר באופן כללי ש-

{% equation %}P\left(\left|X-\mu\right|\ge k\right)\le\frac{\sigma^{2}}{k^{2}}{% endequation %}

ואם סטיית התקן {% equation %}\sigma=0{% endequation %} זה אומר שלכל {% equation %}k>0{% endequation %}, ההסתברות ש-{% equation %}X{% endequation %} יקבל ערך שסוטה מהתוחלת ולו ב-{% equation %}k{% endequation %} היא פשוט 0. עגול. לא קירוב ולא כלום. עכשיו שוב, צריך להזכיר שזה <strong>לא</strong> אומר שהמשתנה המקרי הוא זהותית אפס; כשאנחנו עוסקים במשתנים מקריים רציפים כל מה שזה יכול לומר הוא שמידת ההסתברות של קבוצת כל התוצאות ששונות מ-{% equation %}\mu{% endequation %} היא אפס.

את מה שראינו עכשיו אפשר לקחת טיפה יותר רחוק. בפוסט הקודם הגדרתי {% equation %}\overline{X}_{n}=\frac{X_{1}+X_{2}\ldots+X_{n}}{n}{% endequation %} (שזה בדיוק מה שקראתי לו כאן {% equation %}Z_{n}{% endequation %}) ואז הוכחתי שבהסתברות 1 מתקיים {% equation %}\overline{X}_{n}\to\mu{% endequation %}. התוצאה הזו, שנקראה <strong>החוק החזק של המספרים הגדולים</strong>, דיברה על ההתנהגות של כל הסדרה {% equation %}\overline{X}_{n}{% endequation %} "בבת אחת". אפשר לדבר על זה גם מזווית טיפה שונה. הרי אנחנו יודעים ש-{% equation %}\overline{X}_{n}{% endequation %} לא בהכרח יהיה <strong>שווה</strong> לתוחלת - אנחנו צריכים לקחת עוד ועוד איברים ולהגדיל את {% equation %}n{% endequation %} כדי שהממוצע יתקרב לתוחלת וגם אז הסיכוי שהוא יהיה שווה לה הוא לא בהכרח גדול. אבל אפשר להעריך בצורה גסה מה יהיה גודל הטעות, בעזרת צ'בישב. 

אז נניח שיש לי משתנה {% equation %}X{% endequation %} כך ש-{% equation %}\text{E}\left[X\right]=\mu{% endequation %} ו-{% equation %}\text{Var}\left(X\right)=\sigma^{2}{% endequation %}. עכשיו בניתי משתנה חדש, {% equation %}\overline{X}_{n}=\frac{X_{1}+\ldots+X_{n}}{n}{% endequation %}. מה התוחלת שלו? לינאריות התוחלת נותנת לנו

{% equation %}\text{E}\left[\overline{X}_{n}\right]=\text{E}\left[\frac{X_{1}+\ldots+X_{n}}{n}\right]=\frac{\text{E}\left[X_{1}\right]+\ldots+\text{E}\left[X_{n}\right]}{n}=\frac{\mu+\ldots+\mu}{n}=\mu{% endequation %}

עכשיו, שונות של משתנים מקריים לא מקיימת לינאריות באופן כללי, אבל היא <strong>כן</strong> משמרת חיבור של משתנים מקריים <strong>בלתי תלויים</strong> (די בדומה לאיך שתוחלת של מכפלה של משתנים בלתי תלויים מתפרקת למכפלת תוחלות). בפוסט הקודם גם הזכרתי ש-{% equation %}\text{Var}\left(\alpha X\right)=\alpha^{2}X{% endequation %}. לכן אפשר לחשב:

{% equation %}\text{Var}\left(\overline{X}_{n}\right)=\text{Var}\left(\frac{X_{1}+\ldots+X_{n}}{n}\right)=\frac{\text{Var}\left(X_{1}\right)+\ldots+\text{Var}\left(X_{n}\right)}{n^{2}}=\frac{\sigma^{2}+\ldots\sigma^{2}}{n^{2}}=\frac{\sigma^{2}}{n}{% endequation %}

ולכן מאי-שוויון צ'בישב:

{% equation %}P\left(\left|\overline{X}_{n}-\mu\right|\ge\varepsilon\right)\le\frac{\sigma^{2}}{n\varepsilon^{2}}{% endequation %}

המספר המעניין פה הוא ה-{% equation %}n{% endequation %} שנשאר במכנה. בזכותו, אם משאיפים את {% equation %}n{% endequation %} לאינסוף, מקבלים

{% equation %}\lim_{n\to\infty}P\left(\left|\overline{X}_{n}-\mu\right|\ge\varepsilon\right)=0{% endequation %}

זה מה שנקרא <strong>החוק החלש של המספרים הגדולים</strong> (כי החוק החזק של המספרים הגדולים גורר אותו - ה"התכנסות" שלו היא חזקה יותר מההתכנסות שיש בחוק החלש) וזו דרך קצת יותר פשוטה לראות את "חוסר הטעם" שבהסתכלות על הממוצעים {% equation %}\overline{X}_{n}{% endequation %} אם אנחנו רוצים לקבל משתנה מקרי שמדמה את ההתפלגות של {% equation %}X_{1}+\ldots+X_{n}{% endequation %} כש-{% equation %}n{% endequation %} גדול. המיצוע שאנחנו עושים הוא "טוב מדי" - הוא משמר את המידע על ההתפלגות שבא לידי ביטוי בתוחלת {% equation %}\mu{% endequation %} אבל מוחק את המידע על ההתפלגות שבא לידי ביטוי בסטיית התקן {% equation %}\sigma{% endequation %}. המיצוע שבו מחלקים ב-{% equation %}\sqrt{n}{% endequation %} הוא "עדין" יותר ומשמר גם את המידע הזה, והוכחת החוק החלש של המספרים הגדולים נותנת עוד דרך לראות את זה - אם היינו מחלקים ב-{% equation %}\sqrt{n}{% endequation %} ומנסים להשתמש בצ'בישב, היינו מקבלים רק {% equation %}P\left(\left|\frac{X_{1}+\ldots+X_{n}}{\sqrt{n}}-\mu\right|\ge\varepsilon\right)\le\frac{\sigma^{2}}{\varepsilon^{2}}{% endequation %} שזו תוצאה מעניינת טיפה בפני עצמה אבל אין בה שאיפה לאפס של ההסתברות אלא רק חסם אחיד לכל הממוצעים, לא משנה כמה רחוק ניקח אותם.

הקסם הגדול של משפט הגבול המרכזי בעיני, כמו שאמרתי כבר לפני כמה פוסטים, הוא שלא משנה כמה המשתנה {% equation %}X{% endequation %} שאנחנו מתחילים איתו הוא מורכב ומתוסבך - ההתנהגות של {% equation %}X_{1}+\ldots+X_{n}{% endequation %} תהיה ניתנת לקירוב מצוין רק עם שני הפרמטרים המספריים {% equation %}\mu,\sigma{% endequation %}. ראינו את זה בתוך ההוכחה של משפט הגבול המרכזי עצמו (היינו צריכים רק לדעת את {% equation %}L^{\prime}\left(0\right){% endequation %} ואת {% equation %}L^{\prime\prime}\left(0\right){% endequation %} כדי לקבל אותו ולא משהו שתלוי במומנטים מתקדמים יותר) וראינו את זה גם עם החוק החלש של המספרים הגדולים עכשיו (אם המומנט השני הוא אפס גורלה של ההתפלגות נחרץ להיות קבועה בהסתברות 1), אבל למרות שראינו את זה אני עדיין מתקשה להאמין לזה. אולי כי זו לא סתם תוצאה מספרית - זה משהו שבאמת בא לידי ביטוי אמפירית, במציאות, בעולם שלנו, ומשפיע עלינו בשלל דרכים שונות. גם זה אחד מהקסמים של המתמטיקה. 
