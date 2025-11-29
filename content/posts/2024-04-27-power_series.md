---
title: "טורי חזקות ורדיוס התכנסות"
layout: post
categories:
  - אנליזה מתמטית
tags:
  - טורי חזקות
---


<h2>מבוא</h2>

<a href="https://gadial.net/2024/02/24/sequences_and_series_of_functions/">בפוסט הקודם</a> דיברתי על סדרות וטורים כלליים של פונקציות, והפעם אני רוצה לדבר על סוג ספציפי של טורי פונקציות, שהוא נחמד/שימושי/ברור מספיק כדי לתת לו שם משל עצמו ולעסוק בנפרד בתכונות שלו - <strong>טור חזקות</strong>.

מה זה טור חזקות? בהגדרה הפשוטה שלו, זה טור פונקציות מהצורה {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} כאשר ה-{% equation %}a_{n}{% endequation %}-ים הם מספרים ("המקדמים"). כלומר, זה טור שמתקבל מסדרה שהאיבר הכללי שלה הוא {% equation %}a_{n}x^{n}{% endequation %} - פונקציה שהיא <strong>חזקה</strong> של {% equation %}x{% endequation %}, ומכאן שמו. בואו נראה כמה דוגמאות. 

ראשית, הטור הפשוט שבו {% equation %}a_{n}=1{% endequation %} לכל {% equation %}n{% endequation %}: {% equation %}\sum_{n=0}^{\infty}x^{n}{% endequation %}. אם אני אציב ערך קונקרטי ב-{% equation %}x{% endequation %}, למשל {% equation %}2{% endequation %}, אני אקבל את מה שנקרא <strong>טור הנדסי</strong>: {% equation %}1+2+4+8+16+\ldots{% endequation %}. היופי בטורים הנדסיים הוא שיש לנו נוסחה לסכום של מספר סופי של איברים בטור כזה, ואני אף פעם לא אשתעמם מלהראות איך מוצאים את הנוסחה הזו. בואו נסתכל על הטור {% equation %}1+q+q^{2}+\ldots+q^{n}{% endequation %}. אם {% equation %}q=1{% endequation %} אנחנו יודעים מה הסכום שלו - {% equation %}n{% endequation %} (כי יש {% equation %}n{% endequation %} איברים, כל אחד מהצורה {% equation %}1^{k}=1{% endequation %}). אם {% equation %}q\ne1{% endequation %} בואו נעשה תעלול: ניקח את הסכום {% equation %}q^{n}+q^{n-1}+\ldots+q+1{% endequation %} (שימו לב, הפכתי את הסדרה וכתבתי אותה מהגדול לקטן) ונכפול אותו ב-{% equation %}\left(q-1\right){% endequation %}, מה שגורם כמעט לכל האיברים להצטמצם, כי כשאני כופל את הטור ב-{% equation %}q{% endequation %} אני מקבל

{% equation %}q^{n+1}+q^{n}+\ldots+q^{2}+q{% endequation %}

וכשאני כופל ב-{% equation %}-1{% endequation %} אני מקבל

{% equation %}-q^{n}-q^{n-1}-\ldots-q-1{% endequation %}

וכשמחברים את שניהם כל החזקות של {% equation %}q{% endequation %} נעלמות מלבד הגדולה ביותר והקטנה ביותר, כלומר אני מקבל {% equation %}\left(1+q+q^{2}+\ldots+q^{n}\right)\left(q-1\right)=q^{n+1}-1{% endequation %}. עכשיו נחלק את שני האגפים ב-{% equation %}q-1{% endequation %} (הנחתי ש-{% equation %}q\ne1{% endequation %} אז מותר לי, אין פה חלוקה באפס) ונקבל

{% equation %}1+q+q^{2}+\ldots+q^{n}=\frac{q^{n+1}-1}{q-1}{% endequation %}

עכשיו, אם {% equation %}\left|q\right|<1{% endequation %} אז {% equation %}\lim_{n\to\infty}q^{n+1}=0{% endequation %} ולכן נקבל

{% equation %}\lim_{n\to\infty}\frac{q^{n+1}-1}{q-1}=\frac{-1}{q-1}=\frac{1}{1-q}{% endequation %}

כלומר, קיבלנו {% equation %}\sum_{n=0}^{\infty}q^{n}=\frac{1}{1-q}{% endequation %}. זו הנוסחה <strong>לסכום טור הנדסי אינסופי מתכנס</strong>. אם לעומת זאת {% equation %}\left|q\right|=1{% endequation %} אפשר להראות שהטור תמיד מתבדר. לכן, אם אני חוזר לטור החזקות {% equation %}\sum_{n=0}^{\infty}x^{n}{% endequation %}, למדתי עליו משהו: למדתי שאם {% equation %}\left|x\right|<1{% endequation %} אז הטור מתכנס ואילו עבור {% equation %}\left|x\right|\ge1{% endequation %} הטור מתבדר. זה מקרה פרטי של תכונה כללית חזקה מאוד עבור טורי חזקות: אם קיים ערך שונה מאפס שעבורו הטור מתכנס, וקיים ערך שעבורו הטור מתבדר, אז קיים מספר ממשי {% equation %}R>0{% endequation %} שנקרא <strong>רדיוס ההתכנסות</strong> של הטור, כך שאם {% equation %}\left|x\right|<R{% endequation %} אז {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתכנס ואילו אם {% equation %}\left|x\right|>R{% endequation %} הוא מתבדר (אם {% equation %}\left|x\right|=R{% endequation %} הטור יכול או להתבדר או להתכנס; לא מובטח לנו משהו בודאות). סדרת המקדמים {% equation %}a_{n}{% endequation %} היא שקובעת מה בדיוק יהיה ה-{% equation %}R{% endequation %} הזה ועוד מעט נראה גם דרכים להעריך אותו.

בואו נחזור לרגע אל הטור {% equation %}\sum_{n=0}^{\infty}2^{n}=1+2+4+8+16+\ldots{% endequation %}. אמרנו שהטור הזה לא מתכנס, כי הוא מתאים למקרה {% equation %}\left|q\right|=2>1{% endequation %}. מה אם בכל זאת ננסה להציב את הטור הזה בנוסחה? נקבל {% equation %}\sum_{n=0}^{\infty}2^{n}=\frac{1}{1-2}=-1{% endequation %}, מה שנראה הזוי לחלוטין - איך אפשר לחבר איברים חיוביים ולקבל סכום שלילי? אז זהו, שאפשר. כל מה שאני מדבר עליו בפוסט הזה מתרחש מעל המספרים הממשיים, {% equation %}\mathbb{R}{% endequation %}, ועוד מעט אדבר גם על המרוכבים, {% equation %}\mathbb{C}{% endequation %}; אבל יש עוד יקומים מתמטיים מעניינים שאפשר לעשות בהם חדו"א, ואחד מהם (<a href="https://gadial.net/2010/01/12/padic_numbers_analytic_constructions/">שעליו אני מדבר למשל פה</a>) הוא מה שנקרא "מספרים {% equation %}p{% endequation %}-אדיים" - זה לא יקום מתמטי אחד אלא אוסף שלם של יקומים, ובאחד מהם הטור {% equation %}\sum_{n=0}^{\infty}2^{n}{% endequation %} בהחלט מתכנס (על פי אותה הגדרת התכנסות כמו בחדו"א) והשוויון {% equation %}\sum_{n=0}^{\infty}2^{n}=-1{% endequation %} הוא נכון לגמרי ונובע מאותן טכניקות שראינו פה. אז לא לפסול שום דבר על הסף! לזכור שמה שאנחנו רואים פה הוא רק קצה מעניין אחד של קרחון מעניין ממש.

כשאנחנו עובדים מעל הממשיים, קל לראות ש-{% equation %}\sum_{n=0}^{\infty}2^{n}{% endequation %} לא יכול להתכנס כי האיבר הכללי של הטור הזה, {% equation %}2^{n}{% endequation %}, לא שואף לאפס - ומעל הממשיים תנאי הכרחי לכך שהטור {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} יתכנס הוא ש-{% equation %}\lim_{n\to\infty}a_{n}=0{% endequation %}. אני אזכיר איך מוכיחים את התכונה הזו: נסמן {% equation %}S_{n}=\sum_{k=0}^{n}a_{k}{% endequation %} ונניח שהטור מתכנס, כלומר שיש {% equation %}L{% endequation %} כך ש-{% equation %}\lim_{n\to\infty}S_{n}=L{% endequation %}. נגדיר גם סדרה אחרת, {% equation %}T_{n}=\sum_{k=0}^{n-1}a_{k}{% endequation %} (כאן {% equation %}T_{0}=0{% endequation %}, {% equation %}T_{1}=a_{0}{% endequation %}, {% equation %}T_{2}=a_{0}+a_{1}{% endequation %} וכן הלאה). כלומר, לכל {% equation %}n>0{% endequation %} מתקיים {% equation %}T_{n}=S_{n-1}{% endequation %} ולכן ברור שגם {% equation %}\lim_{n\to\infty}T_{n}=L{% endequation %} (זה תרגיל ממש פשוט להוכיח את זה, תנסו). כמו כן {% equation %}S_{n}-T_{n}=a_{n}{% endequation %} ממש על פי ההגדרה, ולכן נקבל

{% equation %}\lim_{n\to\infty}a_{n}=0=\lim_{n\to\infty}\left(S_{n}-T_{n}\right)=\lim_{n\to\infty}S_{n}-\lim_{n\to\infty}T_{n}=L-L=0{% endequation %}

(את הפיצול הזה של גבול של הפרש סדרות להפרש של גבולות הסדרות אפשר לעשות כששתי הסדרות מתכנסות)

שימו לב שהקריטריון הזה שהאיבר הכללי שואף לאפס הוא <strong>הכרחי</strong> אבל לא <strong>מספיק</strong> - למשל הטור ההרמוני {% equation %}\sum_{n=0}^{\infty}\frac{1}{n}{% endequation %} לא מתכנס (<a href="https://gadial.net/2010/07/25/harmonic_series_converges_to_137/">הנה הוכחה</a>) למרות שהאיבר הכללי שלו כן שואף לאפס. כשאנחנו במספרים ה-{% equation %}p{% endequation %}-אדיים, אגב, זה דווקא <strong>כן</strong> תנאי מספיק להתכנסות (וביקום הספציפי שבו {% equation %}\sum_{n=0}^{\infty}2^{n}{% endequation %} מתכנס, המספרים ה-2-אדיים, באמת {% equation %}2^{n}{% endequation %} שואף לאפס).

עכשיו, בואו נחזור לטורי חזקות כלליים. אם אני מציב ב-{% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} את הערך 2 ומקבל את הטור {% equation %}\sum_{n=0}^{\infty}a_{n}2^{n}{% endequation %} בהחלט עדיין יש לי תקווה שהטור יתכנס - זה תלוי במקדמים של טור החזקות, ה-{% equation %}a_{n}{% endequation %}-ים. מה שברור הוא שאני רוצה שהם לא סתם ישאפו לאפס, אלא ישאפו לאפס חזק מספיק כדי לנצח את {% equation %}2^{n}{% endequation %}. האם יש דרך לדעת כמה חזק זה צריך להיות? ובכן, לפעמים כן. לצורך כך אפשר לגייס לשירותינו שני מבחנים שקושי גילה עבור התכנסות של טורים רגילים: <strong>מבחן השורש</strong> ו<strong>מבחן המנה</strong>. הרעיון בשני המבחנים הללו הוא זה - בהינתן טור המספרים <strong>החיוביים </strong>{% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} אפשר לנסות לחשב את הגבול של הסדרה {% equation %}R=\lim_{n\to\infty}\sqrt[n]{a_{n}}{% endequation %} או את הגבול של הסדרה {% equation %}R=\lim_{n\to\infty}\frac{a_{n+1}}{a_{n}}{% endequation %}. אם חישבנו את אחד מהגבולות הללו, אז

<ul> <li>אם {% equation %}R<1{% endequation %} הטור מתכנס.</li>


<li>אם {% equation %}R>1{% endequation %} הטור מתבדר.</li>


<li>אם {% equation %}R=1{% endequation %} אז המבחן לא סיפק לנו מידע נוסף.</li>

</ul>

אני לא אוכיח כאן שהמבחנים עובדים; אין מנוס מלשבת ולכתוב גם פוסטים על טורי מספרים "רגילים". אבל הם בהחלט יוכלו לסייע לנו כאן. למשל, עבור {% equation %}\sum_{n=0}^{\infty}a_{n}2^{n}{% endequation %} אם אני אשתמש במבחן השורש אני צריך שיתקיים {% equation %}\lim_{n\to\infty}\sqrt[n]{a_{n}2^{n}}=\lim_{n\to\infty}2\sqrt[n]{a_{n}}<1{% endequation %} כדי שהטור יתכנס, כלומר אני רוצה {% equation %}\lim_{n\to\infty}\sqrt[n]{a_{n}}<\frac{1}{2}{% endequation %} אז אני יכול לבחור {% equation %}a_{n}=\left(\frac{1}{3}\right)^{n}{% endequation %}, למשל, וזה יעבוד לי (כמובן, אפשר לומר לא הייתי צריך את מבחן השורש, אם אני סתם מציב {% equation %}a_{n}=\left(\frac{1}{3}\right)^{n}{% endequation %} אני מקבל את הטור ההנדסי המתכנס {% equation %}\sum_{n=0}^{\infty}\left(\frac{2}{3}\right)^{n}{% endequation %}; ובכן, זה קצת רומז על האופן שבו מוכיחים את מבחן השורש). עכשיו, {% equation %}\left(\frac{1}{3}\right)^{n}{% endequation %} זו דרך אחרת לכתוב {% equation %}\frac{1}{3\cdot3\cdot3\cdots3}{% endequation %} כשיש {% equation %}n{% endequation %} מוכפלים במכנה; אני יכול להחליף את זה ב-{% equation %}\frac{1}{1\cdot2\cdot3\cdots n}=\frac{1}{n!}{% endequation %} ואז יילך לי אפילו טוב יותר, כפי שמבחן המנה מראה:

{% equation %}\lim_{n\to\infty}\frac{2^{n+1}/\left(n+1\right)!}{2^{n}/n!}=\lim_{n\to\infty}2\frac{n!}{\left(n+1\right)!}=\lim_{n\to\infty}\frac{2}{n+1}=0{% endequation %}

וכאן אפשר לראות שגם אם נחליף את ה-{% equation %}2{% endequation %} בכל מספר אחר, עדיין נקבל גבול שהוא 0, ולכן הטור {% equation %}\sum_{n=0}^{\infty}\frac{x^{n}}{n!}{% endequation %} מתכנס לכל {% equation %}x{% endequation %} (על מקרה כזה אומרים שרדיוס ההתכנסות של הטור הוא {% equation %}R=\infty{% endequation %}); אנחנו בהחלט הולכים לפגוש את הטור הזה עוד מעט שוב.

בואו ננסה עכשיו לטפל בשאלת ההתכנסות באופן כללי יותר: ניקח את הטור הכללי {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} וננסה להשתמש עליו במבחן המנה, כלומר נסתכל על

{% equation %}\lim_{n\to\infty}\frac{a_{n+1}x^{n+1}}{a_{n}x^{n}}=\lim_{n\to\infty}\frac{a_{n+1}}{a_{n}}x=x\cdot\lim_{n\to\infty}\frac{a_{n+1}}{a_{n}}{% endequation %}

בינתיים זה נראה פשוט! ה-{% equation %}x{% endequation %} יצא החוצה ואנחנו נשארים עם המנה {% equation %}\frac{a_{n+1}}{a_{n}}{% endequation %} ואם היא קיימת, אז... אז בעצם אי אפשר לומר שום דבר כי מבחן המנה מניח שהטור שלנו <strong>חיובי</strong> אבל בשום מקום לא אמרתי שה-{% equation %}a_{n}{% endequation %}-ים או ה-{% equation %}x{% endequation %} חיוביים. האופן שבו מתגברים על הבעיה הזו היא להשתמש בערך מוחלט על אברי הטור, ולעבור לנתח טור אחר, את הטור {% equation %}\sum_{n=0}^{\infty}\left|a_{n}x^{n}\right|{% endequation %} שהוא באמת טור חיובי. באופן כללי, לשים ערך מוחלט על אברי טור יכול להיות "בעייתי" במובן זה שהטור המקורי מתכנס אבל אחרי ששמים עליו ערכים מוחלטים הוא מתבדר - הדוגמא הקלאסית היא הטור {% equation %}\sum_{n=0}^{\infty}\frac{\left(-1\right)^{n+1}}{n}{% endequation %} שמתכנס אל {% equation %}\ln2{% endequation %} אבל הרי {% equation %}\sum_{n=0}^{\infty}\left|\frac{\left(-1\right)^{n+1}}{n}\right|=\sum_{n=0}^{\infty}\frac{1}{n}{% endequation %} לא מתכנס. אנחנו נראה שבטורי חזקות הבעיה הזו לא תהיה קיימת.

בואו נתחיל להיכנס יותר במסודר לתיאוריה שנצטרך כדי לנסח את הטענות המלאות על רדיוסי התכנסות.

<h2>תזכורת זריזה מחדו"א בסיסי</h2>

בואו שוב נשכח לרגע מטורי חזקות ונחזור לחומר בסיסי של טורי מספרים. מכיוון שהעניין העיקרי שלי בטורי חזקות בהמשך יהיה בהקשר של מספרים מרוכבים, בואו נניח מעכשיו שכל המספרים שאני מדבר עליהם הם מספרים מרוכבים כלליים ולא רק מספרים ממשיים. אני צריך לציין את ההנחה הזו במפורש כי כמעט לא נשים לב לזה; רק צריך לזכור שעבור מספרים מרוכבים קיימת פונקציית ערך מוחלט שמרחיבה את הפונקציה הזו שמוגדרת על הממשיים, והיא מקיימת את אותן תכונות כמו אי שוויון המשולש.

אנחנו אומרים שהטור {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} <strong>מתכנס בהחלט</strong> אם הטור {% equation %}\sum_{n=0}^{\infty}\left|a_{n}\right|{% endequation %} מתכנס. כפי שכבר ראינו עם הדוגמא של הטור ההרמוני, התכנסות של טור לא גוררת התכנסות בהחלט שלו, אבל ההפך <strong>כן</strong> נכון וזו אחת מהסיבות למה התכנסות בהחלט היא מושג מועיל. בואו נוכיח שאם {% equation %}\sum_{n=0}^{\infty}\left|a_{n}\right|{% endequation %} מתכנס אז גם {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} מתכנס.

אנחנו רוצים להראות ש-{% equation %}S_{n}=\sum_{k=0}^{n}a_{k}{% endequation %} היא סדרה מתכנסת. לצורך כך מספיק להראות שהיא <strong>סדרת קושי</strong>, כלומר שלכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שאם {% equation %}n\ge m>N{% endequation %} אז {% equation %}\left|S_{n}-S_{m}\right|<\varepsilon{% endequation %}. אז בואו נחשב חסם על ההפרש הזה, תוך שאנחנו משתמשים באי שוויון המשולש:

{% equation %}\left|S_{n}-S_{m}\right|=\left|\sum_{k=m+1}^{n}a_{k}\right|\le\sum_{k=m+1}^{n}\left|a_{k}\right|\le\sum_{k=0}^{n}\left|a_{k}\right|{% endequation %}

עכשיו, מה זה {% equation %}\sum_{k=0}^{n}\left|a_{k}\right|{% endequation %}? זה בדיוק סכום חלקי של הטור <strong>שמתכנס בהחלט</strong>. כלומר, עבור ה-{% equation %}\varepsilon{% endequation %} הקונקרטי שלנו קיים {% equation %}N{% endequation %} כך שלכל {% equation %}n>N{% endequation %} מתקיים {% equation %}\sum_{k=0}^{n}\left|a_{k}\right|<\varepsilon{% endequation %}. זה בדיוק ה-{% equation %}N{% endequation %} שאנחנו רוצים, מה שמסיים את ההוכחה. פשוט מאוד!

דבר שני שצריך לזכור נקרא <strong>מבחן ההשוואה</strong> לטורים חיוביים. הרעיון פשוט: אם לכל {% equation %}n{% endequation %} מתקיים {% equation %}0\le a_{n}\le b_{n}{% endequation %} והטור {% equation %}\sum_{n=0}^{\infty}b_{n}{% endequation %} מתכנס, כך גם {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %}. הרעיון פה הוא לסמן את סדרות הסכומים החלקיים המתאימות לטורים הללו ב-{% equation %}T_{n}{% endequation %} ו-{% equation %}S_{n}{% endequation %} ואז מ-{% equation %}a_{n}\le b_{n}{% endequation %} מקבלים ש-{% equation %}S_{n}\le T_{n}{% endequation %}, ומכך ש-{% equation %}0\le a_{n}{% endequation %} מקבלים ששתי הסדרות הללו הן <strong>מונוטוניות עולות</strong>. מכיוון ש-{% equation %}T_{n}\to L{% endequation %} והיא סדרה מונוטונית עולה, אז {% equation %}S_{n}\le T_{n}\le L{% endequation %}, ועכשיו משתמשים במשפט מחדו"א בסיסי לפיו סדרה מונוטונית עולה וחסומה היא מתכנסת (ההוכחה של זה נובעת ישירות מהתכונות הבסיסיות של המספרים הממשיים, שמהן נובע החדו"א).

משני אלו נובעת מסקנה פשוטה: אם יש לנו טור {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} שהאיברים שלו יכולים להיות מספרים מרוכבים כלליים, ומתקיים שהחל ממקום מסוים {% equation %}N{% endequation %}, לכל {% equation %}n\ge N{% endequation %} מתקיים {% equation %}\left|a_{n}\right|<b_{n}{% endequation %} כאשר {% equation %}\sum_{n=N}^{\infty}b_{n}{% endequation %} טור מתכנס, אז גם {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} מתכנס. כדי לראות את זה, ראשית נפצל את {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} לשני טורים: {% equation %}\sum_{n=0}^{\infty}a_{n}=\sum_{k=0}^{N-1}a_{k}+\sum_{n=N}^{\infty}a_{n}{% endequation %}. הטור שהוא המחובר השמאלי הוא סופי, ולכן בוודאי מתכנס; נשארה רק שאלת ההתכנסות של הטור הימני. כפי שכבר ראינו, מספיק שהטור יתכנס בהחלט, כלומר מספיק להראות ש-{% equation %}\sum_{n=N}^{\infty}\left|a_{n}\right|{% endequation %} מתכנס, וזה נובע מייד ממשפט ההשוואה עם {% equation %}\sum_{n=N}^{\infty}b_{n}{% endequation %}.

<h2>המשפט המרכזי שלנו: על קיום רדיוס ההתכנסות ואיך לחשב אותו</h2>

עכשיו בואו נחזיר לתמונה את רדיוס ההתכנסות. ניקח טור חזקות כללי {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} (כאן ה-{% equation %}a_{n}{% endequation %}-ים יכולים להיות מרוכבים כללים וגם ב-{% equation %}x{% endequation %} אפשר להציב מרוכבים כלשהם; לרוב יותר מקובל להשתמש ב-{% equation %}z{% endequation %} כדי לתאר משתנה כזה אבל נוותר על זה הפעם). הנה טיפה אינטואיציה: אם קיים הגבול {% equation %}\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=L{% endequation %} אז אפשר להשתמש בשילוב של הדברים שראינו כדי להשתכנע ש-{% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתכנס: מספיק לראות ש-{% equation %}\sum_{n=0}^{\infty}\left|a_{n}x^{n}\right|{% endequation %} מתכנס, ובשביל זה אפשר לנסות את מבחן המנה, כלומר לבדוק את גבול הסדרה

{% equation %}\frac{\left|a_{n+1}x^{n+1}\right|}{\left|a_{n}x^{n}\right|}=\left|x\right|\frac{\left|a_{n+1}\right|}{\left|a_{n}\right|}=\left|x\right|\left|\frac{a_{n+1}}{a_{n}}\right|\to\left|x\right|L{% endequation %}

כדי להבטיח התכנסות צריך שיתקיים {% equation %}\left|x\right|L<1{% endequation %}, כלומר {% equation %}\left|x\right|<\frac{1}{L}{% endequation %}. לכן {% equation %}R=\frac{1}{L}{% endequation %} הוא <strong>מועמד טוב</strong> להיות רדיוס ההתכנסות שלנו.

הבעיה בגישה הזו היא שאני נזקק להנחה שהגבול {% equation %}\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|{% endequation %} קיים. הוא לא תמיד קיים. זה נכון שאם הוא קיים הוא באמת יהיה שווה לרדיוס ההתכנסות וזו דרך טובה <strong>לחשב</strong> אותו, וגם נוכיח שזה עובד בהמשך - אבל אנחנו רוצים הגדרה לרדיוס ההתכנסות שתעבוד <strong>תמיד</strong>. לצורך כך נכניס לתמונה שני דברים: את מבחן השורש, ואת מושג ה-{% equation %}\lim\sup{% endequation %} של סדרות, שהוא דרך לעשות הגיון בשגעון של סדרות שלאו דווקא מתכנסות.

מה זה {% equation %}\lim\sup{% endequation %}? קודם כל בואו ניזכר מה זה {% equation %}\text{sup}{% endequation %}, סופרמום: סופרמום של קבוצת מספרים הוא המספר <strong>הקטן ביותר</strong> שגדול או שווה לכל אברי הקבוצה; קצת כמו המקסימום שלה, אבל עובד גם לקבוצות אינסופיות שאינן להן מקסימום. למשל הסופרמום של {% equation %}\left\{ 0,\frac{1}{2},\frac{2}{3},\frac{3}{4},\ldots\right\} {% endequation %} יהיה 1. אם קבוצה של מספרים ממשיים היא חסומה, אז הסופרמום שלה תמיד קיים; זו אחת מהתכונות הבסיסיות של המספרים הממשיים. אם לעומת זאת הקבוצה לא חסומה אומרים שהסופרמום שלה הוא {% equation %}\infty{% endequation %}, כך שאפשר להניח שהסופרמום במובן המוכלל הזה תמיד קיים לכל קבוצה של ממשיים. ה"תמיד קיים" הזה הוא מה שנותן ל-{% equation %}\lim\sup{% endequation %} יתרון על גבול "רגיל" ומבטיח שהוא יהיה קיים תמיד. ההגדרה הפורמלית היא:

{% equation %}\lim\sup\left\{ a_{0},a_{1},a_{2},\ldots\right\} =\lim_{n\to\infty}\sup\left\{ a_{n},a_{n+1},a_{n+2},\ldots\right\} {% endequation %}

כלומר - אנחנו לוקחים את הסדרה שלנו, מורידים ממנה את ה"זנב" ומסתכלים מה קורה ממקום {% equation %}n{% endequation %} והלאה. יש לנו קבוצה של איברים, אז יש לה סופרמום, ולכן לכל {% equation %}n{% endequation %} אנחנו מקבלים מספר, ואז אפשר לשאול לאן סדרת המספרים הזו מתכנסת. והנה הקאץ': זו סדרה <strong>יורדת</strong> של מספרים. כי ככל ש-{% equation %}n{% endequation %} גדול יותר, כך יש בקבוצה {% equation %}\left\{ a_{n},a_{n+1},a_{n+2},\ldots\right\} {% endequation %} פחות איברים ולכן הסופרמום שלה לא יכול להפוך פתאום לגדול יותר; ובמספרים הממשיים, כל סדרה יורדת של מספרים מתכנסת (אולי ל-{% equation %}-\infty{% endequation %}).

הנה דוגמא פשוטה לאופן שבו זה עובד: אם ניקח את הסדרה {% equation %}0,1,0,1,0,1,\ldots{% endequation %} לא יהיה לסדרה הזו גבול כי היא "מזפזפת" בין איברים שונים, אבל ה-{% equation %}\lim\sup{% endequation %} שלה יהיה פשוט 1 (והמושג המקביל, {% equation %}\lim\inf{% endequation %}, יהיה 0). עכשיו בואו נשתמש בזה עם המשפט המרכזי והמפוצץ שלנו:

בהינתן טור חזקות כלשהו {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %}, נגדיר את המספר {% equation %}R{% endequation %} על ידי

{% equation %}\frac{1}{R}=\lim\sup\sqrt[n]{\left|a_{n}\right|}{% endequation %}

אז {% equation %}R{% endequation %} הוא רדיוס ההתכנסות של {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %}, כלומר

<ul> <li>אם {% equation %}\left|x\right|<R{% endequation %} אז הטור {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתכנס, ואפילו מתכנס בהחלט.</li>


<li>אם {% equation %}\left|x\right|>R{% endequation %} אז הטור {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתבדר.</li>


<li>{% equation %}R{% endequation %} הוא המספר היחיד שמקיים את שתי התכונות הללו יחד.</li>


<li>בונוס: לכל {% equation %}0<r<R{% endequation %}, הטור {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתכנס <strong>במידה שווה</strong> בקבוצה {% equation %}\left\{ x\ |\ \left|x\right|<r\right\} {% endequation %}</li>

</ul>

ההתכנסות במידה שווה הזו היא תכונה משמחת במיוחד, כי כזכור - אנחנו צריכים אותה בשביל דברים כמו שימור של רציפות ושל אינטגרלים. אבל באופן כללי המשפט הזה די משמח בגלל המבנה המאוד מסודר שהוא נותן לנו לטורי חזקות. בואו נוכיח אותו.

ראשית, בואו נוודא ש-{% equation %}R{% endequation %} באמת קיים: {% equation %}\left|a_{n}\right|{% endequation %} הוא מספר אי שלילי, לכן {% equation %}\sqrt[n]{\left|a_{n}\right|}{% endequation %} תמיד קיים, לכן {% equation %}\lim\sup\sqrt[n]{\left|a_{n}\right|}{% endequation %} תמיד קיים. מכיוון שזו סדרה של מספרים אי שליליים, ה-{% equation %}\lim\sup{% endequation %} גם גדול או שווה לאפס, ובפרט הוא לא {% equation %}-\infty{% endequation %}. אבל הוא יכול לקבל שני ערכים "בעייתיים": או 0 או {% equation %}\infty{% endequation %}. הרי אין פתרון למשוואה {% equation %}\frac{1}{R}=0{% endequation %} או {% equation %}\frac{1}{R}=\infty{% endequation %} בחשבון רגיל; אבל זו אחת מהסיטואציות שבהן משתלם להגדיר {% equation %}\frac{1}{\infty}=0{% endequation %} ו-{% equation %}\frac{1}{0}=\infty{% endequation %}, במובן המאוד צר לפיו אם {% equation %}\lim\sup\sqrt[n]{\left|a_{n}\right|}=0{% endequation %} אז אומרים ש-{% equation %}R=\infty{% endequation %} ואם {% equation %}\lim\sup\sqrt[n]{\left|a_{n}\right|}=\infty{% endequation %} אז אומרים ש-{% equation %}R=0{% endequation %}. המשמעות של {% equation %}R=\infty{% endequation %} היא שהטור מתכנס <strong>תמיד</strong> ואילו המשמעות של {% equation %}R=0{% endequation %} היא שהטור מתבדר <strong>תמיד</strong>.

בואו ניקח עכשיו {% equation %}x{% endequation %} כך ש-{% equation %}\left|x\right|<R{% endequation %} ונוכיח ש-{% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתכנס בהחלט, כלומר ש-{% equation %}\sum_{n=0}^{\infty}\left|a_{n}x^{n}\right|{% endequation %} מתכנס. כדי לעשות את זה נשתמש במבחן השוואה: נראה שקיים מספר {% equation %}0<\beta<1{% endequation %} כך ש-{% equation %}\left|a_{n}x^{n}\right|<\beta^{n}{% endequation %} החל ממקום מסוים. בגלל ש-{% equation %}0<\beta<1{% endequation %} אז הטור {% equation %}\sum_{n=0}^{\infty}\beta^{n}{% endequation %} הוא <strong>טור הנדסי מתכנס</strong> ואפשר להשתמש עליו במבחן ההשוואה. רק נשאר למצוא את ה-{% equation %}\beta{% endequation %} הזה.

אם כן, מכיוון ש-{% equation %}\left|x\right|<R{% endequation %} נובע שקיים {% equation %}r{% endequation %} כך ש-{% equation %}\left|x\right|<r<R{% endequation %} (התכונה הזו נקראת <strong>הצפיפות</strong> של הממשיים). זה אומר ש-{% equation %}\frac{1}{R}<\frac{1}{r}{% endequation %} (זה נכון גם במקרה של {% equation %}R=\infty{% endequation %}) ומכיוון ש-{% equation %}\lim\sup\sqrt[n]{\left|a_{n}\right|}=\frac{1}{R}<\frac{1}{r}{% endequation %} זה אומר שקיים {% equation %}N{% endequation %} שהחל ממנו, לכל {% equation %}n>N{% endequation %} מתקיים {% equation %}\sqrt[n]{\left|a_{n}\right|}<\frac{1}{r}{% endequation %}. זה לא טיעון פשוט כמו שהוא אולי נראה במבט ראשון אז בואו נדבר עליו.

ראשית, הנה טענה כללית על סדרות: אם {% equation %}\lim_{n\to\infty}c_{n}=A{% endequation %} וגם {% equation %}A<B{% endequation %} אז החל ממקום מסויים, {% equation %}c_{n}<B{% endequation %}. ההוכחה של זה היא טכניקה סטנדרטית בעבודה עם סדרות: קחו {% equation %}\varepsilon=\frac{B-A}{2}{% endequation %}, ואז החל ממקום מסוים {% equation %}\left|c_{n}-A\right|<\varepsilon{% endequation %} ומכאן נובע {% equation %}c_{n}<A+\varepsilon=\frac{B+A}{2}<\frac{2B}{2}=B{% endequation %}. אינטואיטיבית, מרגע ש-{% equation %}c_{n}{% endequation %} קרובה ממש ל-{% equation %}A{% endequation %} היא כבר לא יכולה להיות קרובה ממש גם ל-{% equation %}B{% endequation %} ובטח שלא לעבור אותו.

אבל מי היא {% equation %}c_{n}{% endequation %} במקרה שלנו? כזכור, {% equation %}c_{n}=\sup\left\{ \sqrt[k]{\left|a_{k}\right|}\right\} _{k>n}{% endequation %}. זה אומר שה-{% equation %}c_{n}{% endequation %}-ים הם לא האיברים שמעניינים אותו בפני עצמם, אבל למרבה השמחה, הם <strong>חסם</strong> שלהם: אם {% equation %}c_{n}<\frac{1}{r}{% endequation %} אז בוודאי ש-{% equation %}\sqrt[n]{\left|a_{n}\right|}\le c_{n}<\frac{1}{r}{% endequation %} וזה מה שרצינו לקבל. עכשיו נעלה את שני האגפים בחזקת {% equation %}n{% endequation %} ונקבל {% equation %}\left|a_{n}\right|<\frac{1}{r^{n}}{% endequation %}, ולכן נקבל

{% equation %}\left|a_{n}x^{n}\right|=\left|a_{n}\right|\left|x\right|^{n}<\left(\frac{\left|x\right|}{r}\right)^{n}{% endequation %}

כלומר, נבחר {% equation %}\beta=\frac{\left|x\right|}{r}{% endequation %} וזה המספר שחיפשנו. מכיוון ש-{% equation %}\left|x\right|<r{% endequation %} נקבל שאכן {% equation %}\beta<1{% endequation %}, כמבוקש.

זה החלק של ההתכנסות, אבל מה עם הבונוס של ההתכנסות במ"ש? בשביל זה נשתמש במבחן ה-M של ויירשטראס. כזכור, הרעיון בו הוא לחסום את טור הפונקציות שרוצים להוכיח שמתכנס במ"ש על ידי טור מתכנס של מספרים חיוביים. אני אעשה את זה באופן די דומה למה שעשיתי לפני רגע: הפעם אנחנו מתחילים עם {% equation %}0<r<R{% endequation %} ספציפי וצריכים לחסום את כל ה-{% equation %}\left|a_{n}x^{n}\right|{% endequation %}-ים עבור {% equation %}\left|x\right|<r{% endequation %}. אז מה שנעשה הוא לקחת {% equation %}s{% endequation %} כך ש-{% equation %}r<s<R{% endequation %} ולנקוט באותה טכניקה של קודם כדי לחסום את {% equation %}\left|a_{n}x^{n}\right|{% endequation %} על ידי {% equation %}\left(\frac{\left|x\right|}{s}\right)^{n}{% endequation %}. מכיוון ש-{% equation %}\left|x\right|<r<s{% endequation %} שוב קיבלנו ש-{% equation %}\sum\left(\frac{\left|x\right|}{s}\right)^{n}{% endequation %} הוא טור הנדסי מתכנס, וסיימנו.

מה עם התבדרות? ובכן, על פניו ברור מה צריך לעשות - נחסום את הטור <strong>מלמטה</strong> על ידי טור הנדסי מתבדר, ולכן נקבל שהטור עצמו מתבדר. עם זאת, תהיה פה נקודה עדינה שצריך להיזהר לא לפספס ותאלץ אותנו להשתמש בטיעון קצת שונה. הנה מה שקורה אם אני מנסה ללכת עם מה שנראה מתבקש: אם {% equation %}\left|x\right|>R{% endequation %} אז ניקח {% equation %}\left|x\right|>r>R{% endequation %} ועכשיו {% equation %}\frac{1}{r}<\frac{1}{R}{% endequation %}. עכשיו אני רוצה להגיע למצב שבו אני אומר "אוקיי, {% equation %}\left|a_{n}x^{n}\right|>\left(\frac{\left|x\right|}{r}\right)^{n}>1{% endequation %} ולכן אפשר לבצע השוואה עם הטור המתבדר {% equation %}\sum\left(\frac{\left|x\right|}{r}\right)^{n}{% endequation %} שמתבדר כי {% equation %}\left|x\right|>r{% endequation %} ולכן {% equation %}\frac{\left|x\right|}{r}>1{% endequation %}". אבל כדי להגיע אליו אני צריך שיתקיים {% equation %}\left|a_{n}\right|>\frac{1}{r^{n}}{% endequation %} וזה... לא מובן מאליו.

בואו נחזור רגע אחורה. כשהתקיים {% equation %}\frac{1}{R}<\frac{1}{r}{% endequation %} זה היה קל - הסתכלנו על סדרת ה-{% equation %}c_{n}=\sup\left\{ \sqrt[k]{\left|a_{k}\right|}\right\} _{k>n}{% endequation %} ואמרנו שהחל ממקום מסויים היא קרובה מספיק ל-{% equation %}\frac{1}{R}{% endequation %} כך שמובטח לנו {% equation %}c_{n}<\frac{1}{r}{% endequation %}, ואז השתמשנו בכך ש-{% equation %}\sqrt[n]{\left|a_{n}\right|}\le c_{n}{% endequation %}. עכשיו אנחנו רוצים לעשות משהו שהוא סוג של ההפך: אפשר למצוא מקום {% equation %}N{% endequation %} שהחל ממנו, לכל {% equation %}n>N{% endequation %} מתקיים {% equation %}c_{n}>\frac{1}{r}{% endequation %} - שוב, פשוט בגלל קרבה מספיק גדולה אל {% equation %}\frac{1}{R}{% endequation %}. אלא שעכשיו <strong>אי אפשר</strong> להסיק מזה {% equation %}\sqrt[n]{\left|a_{n}\right|}>\frac{1}{r}{% endequation %} כי <strong>לא נכון</strong> ש-{% equation %}\sqrt[n]{\left|a_{n}\right|}\ge c_{n}{% endequation %}. אז מה כן נכון?

שימו לב שקודם כל מה שהשתמנו בו היה {% equation %}\sqrt[n]{\left|a_{n}\right|}\le c_{n}{% endequation %}, כלומר ש-{% equation %}c_{n}{% endequation %} הוא <strong>חסם מלמעלה</strong> של הסדרה. לא השתמשנו בכך שהוא סופרמום - שהוא החסם מלמעלה <strong>הקטן ביותר</strong>. באופן כללי, אם {% equation %}A=\sup X{% endequation %} זה אומר שלכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}x\in X{% endequation %} כך ש-{% equation %}x{% endequation %} קרוב אל {% equation %}A{% endequation %} עד כדי {% equation %}\varepsilon{% endequation %}. אז מה שאני <strong>יכול</strong> לעשות, אם מובטח לי {% equation %}c_{n}>\frac{1}{r}{% endequation %}, הוא להגיד שיש איבר {% equation %}\sqrt[k]{\left|a_{k}\right|}{% endequation %} כלשהו עם {% equation %}k\ge n{% endequation %} שקרוב מספיק אל {% equation %}c_{n}{% endequation %} ולכן מקיים {% equation %}\frac{1}{r}<\sqrt[k]{\left|a_{k}\right|}{% endequation %}. מכיוון שאני יכול לעשות את זה <strong>לכל</strong> {% equation %}n>N{% endequation %}, אני מקבל שיש אינסוף איברים {% equation %}\sqrt[k]{\left|a_{k}\right|}{% endequation %} כאלו (זה לא יכול להיות כל פעם אותו איבר לכל ערך של {% equation %}n{% endequation %} כי מתישהו נקבל {% equation %}n>k{% endequation %} ואז האיבר שיתאים לו יהיה חדש).

אז אם לסכם, הצלחתי להראות שמתקיים {% equation %}\left|a_{n}\right|>\frac{1}{r^{n}}{% endequation %} עבור אינסוף ערכים שונים של {% equation %}n{% endequation %}, אבל לא "לכל {% equation %}n>N{% endequation %} עבור {% equation %}N{% endequation %} מסוים". זה לא מאפשר לי להשתמש במבחן השוואה, אבל כאן אני לא צריך את זה כי הטור {% equation %}\sum\left(\frac{\left|x\right|}{r}\right)^{n}{% endequation %} לא סתם מתבדר - האיבר הכללי שלו שואף לאינסוף ובפרט לא מתכנס לאפס (להבדיל מהטור {% equation %}\sum\frac{1}{n}{% endequation %} שמתבדר למרות שהאיבר הכללי שלו שואף לאפס).

כזכור, התחלנו עם {% equation %}x{% endequation %} שמקיים {% equation %}\left|x\right|>r{% endequation %}, כלומר {% equation %}\frac{\left|x\right|}{r}>1{% endequation %}, ולכן {% equation %}\left(\frac{\left|x\right|}{r}\right)^{n}>1{% endequation %}, ולכן עבור אינסוף ערכים של {% equation %}n{% endequation %}

{% equation %}\left|a_{n}x^{n}\right|=\left|a_{n}\right|\left|x\right|^{n}>\frac{\left|x\right|^{n}}{r^{n}}=\left(\frac{\left|x\right|}{r}\right)^{n}>1{% endequation %}

וזה מספיק טוב, כי זה מראה שהאיבר הכללי של הטור {% equation %}\sum a_{n}x^{n}{% endequation %} לא שואף לאפס, מה שמסיים את ההוכחה שהטור מתבדר.

מה לגבי היחידות של {% equation %}R{% endequation %}? ובכן, ראינו שמתקיים

<ul> <li>אם {% equation %}\left|x\right|<R{% endequation %} אז הטור {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתכנס.</li>


<li>אם {% equation %}\left|x\right|>R{% endequation %} אז הטור {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתבדר.</li>

</ul>

בואו נניח שזה קורה עבור שני ערכים {% equation %}R_{1},R_{2}{% endequation %} ונראה מה אפשר לומר עליהם. במקרה הזה שימו לב ששניהם חייבים להיות <strong>ממשיים</strong> (או {% equation %}\infty{% endequation %}) אחרת אין משמעות להשוואה כמו {% equation %}\left|x\right|<R{% endequation %} (אין יחס סדר טבעי על המספרים המרוכבים כי כל יחס סדר שננסה להגדיר "לא ישחק יפה" עם פעולות החשבון). אם אפשר להשוות אותם בפרט אפשר להשוות אותם זה לזה. נניח ש-{% equation %}R_{1}<R_{2}{% endequation %} וניקח {% equation %}x{% endequation %} כך ש-{% equation %}R_{1}<\left|x\right|<R_{2}{% endequation %}. אז מכיוון ש-{% equation %}\left|x\right|<R_{2}{% endequation %} הטור {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתכנס, אבל בגלל ש-{% equation %}R_{1}<\left|x\right|{% endequation %} אז אותו טור מתבדר - מן הסתם זה לא יכול לקרות, ולכן {% equation %}R_{1}=R_{2}{% endequation %}. זה מסיים את המשפט הזה: הראינו שלטור חזקות יש רדיוס התכנסות, וגם מצאנו סוג של דרך לחשב אותו.

<h2>מה קורה עם מבחן המנה?</h2>

לפני ההוכחה הארוכה הזו, הצעתי את האפשרות הזו: להסתכל על הגבול {% equation %}\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=L{% endequation %} אם הוא קיים, ולהגדיר {% equation %}R=\frac{1}{L}{% endequation %}. אפשר גם לעשות את זה פשוט יותר: להגדיר {% equation %}R=\lim_{n\to\infty}\left|\frac{a_{n}}{a_{n+1}}\right|{% endequation %} <strong>אם</strong> הגבול הזה קיים. אני טוען ש<strong>אם</strong> הגבול קיים, אז הוא באמת שווה לרדיוס ההתכנסות. בואו נוכיח את זה.

בזכות טענת היחידות שראינו קודם, מה שאנחנו צריכים להוכיח הוא את שני הדברים הבאים:

<ul> <li>אם {% equation %}\left|x\right|<R{% endequation %} אז הטור {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתכנס.</li>


<li>אם {% equation %}\left|x\right|>R{% endequation %} אז הטור {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתבדר.</li>

</ul>

נתחיל מהמקרה {% equation %}\left|x\right|<R{% endequation %}. כרגיל, נתחיל בלקחת {% equation %}r{% endequation %} כך ש-{% equation %}\left|x\right|<r<R{% endequation %}. עכשיו, כדי להוכיח ש-{% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מתכנס, אני אמצא קבוע {% equation %}B{% endequation %} כך שמתקיים

{% equation %}\sum_{n=N}^{\infty}\left|a_{n}x^{n}\right|\le\sum_{n=N}^{\infty}B\left(\frac{\left|x\right|}{r}\right)^{n}{% endequation %} 

החל ממקום מסוים {% equation %}N{% endequation %}, וזה יסיים את ההוכחה כי הטור הימני הוא טור הנדסי מתכנס (הוא מתכנס כי {% equation %}\left|x\right|<r{% endequation %}) ולכן אפשר להשתמש במבחן ההשוואה. 

כדי למצוא את {% equation %}B{% endequation %} אני אשתמש בכך ש-{% equation %}\lim_{n\to\infty}\left|\frac{a_{n}}{a_{n+1}}\right|=R{% endequation %} ולכן אפשר לקחת {% equation %}N{% endequation %} גדול דיו כך ש-{% equation %}\left|\frac{a_{n}}{a_{n+1}}\right|>r{% endequation %} לכל {% equation %}n\ge N{% endequation %}. עכשיו אני אגדיר {% equation %}B=\left|a_{N}\right|r^{N}{% endequation %}, ועכשיו בואו נראה שלכל {% equation %}n\ge N{% endequation %} מתקיים {% equation %}\left|a_{n}\right|r^{n}\le B{% endequation %}. 

ראשית, מכיוון ש-{% equation %}\left|\frac{a_{n}}{a_{n+1}}\right|>r{% endequation %} לכל {% equation %}n\ge N{% endequation %} אז בפרט {% equation %}r\cdot\left|a_{n+1}\right|<\left|a_{n}\right|{% endequation %} לכל {% equation %}n\ge N{% endequation %}, וזה טוב לי כי זה מאפשר לי לעשות טיעון אינדוקטיבי. ראשית:

{% equation %}\left|a_{N+1}\right|r^{N+1}=r\left|a_{N+1}\right|r^{N}<\left|a_{N}\right|r^{N}=B{% endequation %}

שנית:

{% equation %}\left|a_{N+2}\right|r^{N+2}=r\left|a_{N+2}\right|r^{N+1}<\left|a_{N+1}\right|r^{N+1}<B{% endequation %}

וכן הלאה; אני מקבל ש-{% equation %}\left|a_{n}\right|r^{n}\le B{% endequation %} לכל {% equation %}n\ge N{% endequation %}, כלומר {% equation %}\left|a_{n}\right|\le B\cdot\frac{1}{r^{n}}{% endequation %} ולכן {% equation %}\left|a_{n}x^{n}\right|\le B\left(\frac{\left|x\right|}{r}\right)^{n}{% endequation %} והשגנו את מה שרצינו.

עכשיו נניח ש-{% equation %}\left|x\right|>R{% endequation %} ונוכיח שהטור מתבדר עם טיעון מאוד דומה, אפילו נשתמש באותו {% equation %}B{% endequation %}. מי שיהיה שונה הפעם הוא {% equation %}r{% endequation %}, מה שסוג של יהפוך את הטיעון שהשתמשנו בו קודם. אנחנו בוחרים {% equation %}r{% endequation %} כך ש-{% equation %}R<r<\left|x\right|{% endequation %} ולוקחים {% equation %}N{% endequation %} גדול דיו כך ש-{% equation %}\left|\frac{a_{n}}{a_{n+1}}\right|<r{% endequation %} לכל {% equation %}b\ge N{% endequation %}. ההיפוך של אי השוויון הפעם משמעותו ש-{% equation %}\left|a_{n}\right|<r\cdot\left|a_{n+1}\right|{% endequation %} ולכן הטיעון האינדוקטיבי של קודם מוכיח הפעם ש-{% equation %}\left|a_{n}\right|r^{n}\ge B=\left|a_{N}\right|r^{N}{% endequation %} ולכן נקבל את החסם

{% equation %}\left|a_{n}x^{n}\right|\ge B\left(\frac{\left|x\right|}{r}\right)^{n}{% endequation %}

מה שחוסם את {% equation %}\sum_{n=N}^{\infty}\left|a_{n}x^{n}\right|{% endequation %} מלמטה על ידי טור הנדסי מתבדר, ומסיים את ההוכחה גם במקרה הזה.

<h2>שתי הערות מרוכבות לסיום</h2>

לפני שאני מסיים את הפוסט הזה, הנה שתי נקודות על מה בעצם ההיקף של מה שעשינו פה.

ראשית, כמו שאמרתי קודם, כל מה שהולך בפוסט הזה תקף לא רק במספרים ממשיים אלא גם במספרים מרוכבים - למעשה, במספרים מרוכבים העיסוק בטורי חזקות הרבה יותר דומיננטי (ואני מקווה להראות את זה בפוסטים הבאים). שווה להסתכל על ההוכחות שראינו ולבדוק האם משהו "נשבר" בגלל השימוש במרוכבים. מה שאפשר לשים לב אליו הוא שרוב הזמן אנחנו מפעילים את הערך המוחלט על האיברים שלנו (מתעסקים ב-{% equation %}\left|x\right|{% endequation %} וב-{% equation %}\left|a_{n}\right|{% endequation %}), מה שמעביר אותנו לטיעונים שעוסקים במספרים חיוביים, שהתורה של טורים עבורם היא פשוטה למדי. מה שאני רוצה לנסות לשכנע אתכם עכשיו הוא שהמרוכבים הם לא סתם טרמפיסטים שמצטרפים לתורה היפה של טורי חזקות במספרים ממשיים, אלא ממש ההקשר ה"נכון" שבו צריך לראות אותם. ובשביל זה יש לי דוגמא שאני מאוד אוהב לשלוף - הטור {% equation %}1-x^{2}+x^{4}-x^{6}+\ldots{% endequation %}.

ראשית, תזכורת קלה: ראינו שעבור הטור ההנדסי {% equation %}\sum_{n=0}^{\infty}t^{n}{% endequation %}, כאשר {% equation %}\left|t\right|<1{% endequation %} מתקיים {% equation %}\sum_{n=0}^{\infty}t^{n}=\frac{1}{1-t}{% endequation %}. עברתי להשתמש באות {% equation %}t{% endequation %} כי עכשיו אני הולך להציב בה דברים: אני אציב {% equation %}t=-x^{2}{% endequation %}, ואקבל את השוויון

{% equation %}\sum_{n=0}^{\infty}\left(-x^{2}\right)^{n}=\sum_{n=0}^{\infty}\left(-1\right)^{n}x^{2n}=\frac{1}{1+x^{2}}{% endequation %}

השוויון הזה נכון כאשר {% equation %}\left|t\right|<1{% endequation %}, כלומר כאשר {% equation %}\left|-x^{2}\right|<1{% endequation %}, כלומר כאשר {% equation %}\left|x\right|<1{% endequation %} - בדיוק כמו קודם. אפשר לחשב במפורש את רדיוס ההתכנסות של הטור: סדרת המקדמים שלו היא {% equation %}1,0,-1,0,1,0,-1,0,\ldots{% endequation %} ולכן {% equation %}\lim\sup\sqrt[n]{\left|a_{n}\right|}=1{% endequation %} ורדיוס ההתכנסות הוא אכן 1 והכל טוב ויפה. אבל <strong>למה, בעצם</strong>?

כי בואו נסתכל רגע על הפונקציה {% equation %}\frac{1}{1+x^{2}}{% endequation %}, שאמרנו שהטור שווה לה בתחומי רדיוס ההתכנסות. אם אנחנו עובדים במספרים ממשיים, אז {% equation %}x{% endequation %} יכול להתקרב אל רדיוס ההתכנסות בשתי דרכים: או להתקרב ל-{% equation %}1{% endequation %}, או להתקרב אל {% equation %}-1{% endequation %}. בשני המקרים הללו, {% equation %}x^{2}{% endequation %} יתקרב אל {% equation %}1{% endequation %} ולכן הערך של הפונקציה יתקרב ל-{% equation %}\frac{1}{2}{% endequation %} בצורה רציפה, והכל נראה בסדר גמור בלי שום בעיה. אז למה הטיעון הזה מפסיק לעבוד ב-{% equation %}\left|x\right|=1{% endequation %}?

כשאנחנו מסתכלים על פונקציה כמו {% equation %}\frac{1}{1-x}{% endequation %} שהגיעה מהטור ההנדסי המקורי, הבעיה ברורה לגמרי - כש-{% equation %}x{% endequation %} ישאף ל-1, הפונקציה "תתפוצץ". אבל ב-{% equation %}\frac{1}{1+x^{2}}{% endequation %} אין שום פיצוץ דומה. עבור מי שמכיר רק מספרים ממשיים, זו אנומליה. זה לא "פרדוקס" או "סתירה במתמטיקה" כי ראינו את כל ההוכחות והן עובדות טוב - אבל יש פה תחושה שחסר משהו. פיצוץ. איפה הפיצוץ?

התשובה, כמובן, היא שהפיצוץ מגיע <strong>במספרים מרוכבים</strong>. אם אני מציב {% equation %}x=i{% endequation %}, אז {% equation %}\frac{1}{1+x^{2}}{% endequation %} יתפוצץ. מכיוון ש-{% equation %}\left|x\right|=\left|i\right|=1{% endequation %} במקרה הזה, הפיצוץ <strong>באמת</strong> מתרחש ברדיוס ההתכנסות; פשוט אין לי שום דרך לראות אותו אם אני מגביל את העולם שלי למספרים ממשיים. זו המחשה שאני מאוד אוהב לכך שהמספרים המרוכבים "נמצאים שם" בין אם נאמין בהם ובין אם לא, והשאלה היא רק אם נצמצם את המתמטיקה שלנו בצורה מלאכותית כדי שתתעלם מקיומם, או לא (אני לא מכיר אף אחד שבאמת מתעלם מקיום מרוכבים כיום).

הנקודה השניה, ההגדרה של טור חזקות שהשתמשתי בה היא קצת מוגבלת. בואו נסתכל על הטור {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %}. אם אני מציב {% equation %}x=0{% endequation %}, הטור הזה <strong>תמיד מתכנס</strong>, פשוט כי הערך היחיד שלו שאולי שונה מאפס הוא {% equation %}a_{0}{% endequation %}. כלומר 0 היא נקודה "מיוחדת". כשאנחנו מדברים על רדיוס התכנסות, אנחנו מדברים על מספר {% equation %}R{% endequation %} כך שהטור מתכנס בכך הנקודות {% equation %}\left|x\right|<R{% endequation %}, כלומר, אם אני אקח את העצה שנתתי קודם ואסתכל על המספרים המרוכבים {% equation %}\mathbb{C}{% endequation %}, על כל הנקודות <strong>בעיגול </strong>הפתוח ברדיוס {% equation %}R{% endequation %} סביב {% equation %}0{% endequation %} (עיגול <strong>פתוח</strong> פירושו שלא לוקחים את השפה שלו אלא רק את מה ש"בפנים"). מכאן השם "רדיוס התכנסות" מגיע, כמובן. אבל למה הכל חייב להיות סביב 0? אי אפשר להסתכל על טורים שמתכנסים בעיגול סביב נקודה אחרת? ובכן, אפשר.

ההגדרה הכללית יותר של טור חזקות שנהוג להשתמש בה היא טור מהצורה {% equation %}\sum_{n=0}^{\infty}a_{n}\left(x-a\right)^{n}{% endequation %} כאשר על הנקודה {% equation %}a{% endequation %} אומרים שפיתחנו את הטור <strong>סביבה</strong>. כמו במקרה הקודם של {% equation %}a=0{% endequation %}, כך כאן - הטור תמיד יתכנס כאשר {% equation %}x=a{% endequation %}, וקיים רדיוס התכנסות {% equation %}R{% endequation %} כך שהטור מתכנס בכל הנקודות בעיגול הפתוח {% equation %}\left|x-a\right|<R{% endequation %}. כל ההוכחות שראינו קודם מספיקות כדי להוכיח את זה, כי בהינתן הטור {% equation %}\sum_{n=0}^{\infty}a_{n}\left(x-a\right)^{n}{% endequation %} תמיד ניתן לבצע את החלפת המשתנים {% equation %}y=x-a{% endequation %}, להוכיח הכל על הטור {% equation %}\sum_{n=0}^{\infty}a_{n}y^{n}{% endequation %}, ואז לחזור אל {% equation %}x{% endequation %}. רדיוס ההתכנסות עצמו הוא תכונה של סדרת המקדמים {% equation %}a_{n}{% endequation %}, לא של הנקודה שסביבה הטור מפותח.

כאן מסתיים הפוסט הזה, אבל אפשר בצדק לתהות למה להשקיע כל כך הרבה בטורי חזקות - האם הם באמת שימושיים? ובכן, אני מקווה לתת לזה תשובה חלקית בפוסט הבא. 
