---
id: 3589
title: "חוגי פולינומים"
date: 2018-03-29 10:21:36
layout: post
categories: 
  - אלגברה מופשטת
tags: 
  - חוג פולינומים
  - פולינומים
  - קריטריון אייזנשטיין
---
סדרת הפוסטים שלי על אלגברה מופשטת מתקרבת לסיום החלק שעסק במבוא לחוגים ומתקרבת אל החלק שעוסק בשדות, והחוט המקשר המרכזי בין שני אלו הם <strong>חוגי פולינומים</strong> שעליהם ארצה לדבר עכשיו. פולינומים הם מאותם יצורים שצצים במתמטיקה בשלל מקומות, וגולשים גם למתמטיקה התיכונית, ואנחנו לכאורה מכירים די טוב - אבל זה לא אומר שאין הרבה מה לומר עליהם. את חלק מהדברים שאגיד עכשיו אמרתי ממש לא מזמן, אבל בכל זאת אגיד שוב, כדי לקבל פוסט שעומד בפני עצמו ככל שניתן.
<h2>מה זה בכלל פולינומים?</h2>
השאלה "מה זה בכלל פולינום" היא קצת יותר טריקית משנדמה במבט ראשון. הנה הגדרה מהשרוול: פולינום הוא <strong>ביטוי</strong> מהצורה {% equation %}a_{n}x^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}{% endequation %} כאשר {% equation %}x{% endequation %} מכונה <strong>משתנה</strong> ואילו {% equation %}a_{0},a_{1},\dots,a_{n}{% endequation %} נקראים <strong>מקדמים</strong> של הפולינום. האינטואיציה היא שפולינום מתאר איזה "תרגיל חשבון פוטנציאלי": אנחנו יכולים <strong>להציב</strong> איזה שהוא ערך במקום {% equation %}x{% endequation %}, ואז לחשב את החזקות של הערך הזה, לכפול אותן במקדמים, לסכום את הכל ולקבל תוצאה. בראיה האינטואיטיבית הזו הפולינום הוא בסך הכל דרך לכתוב חישוב כלשהו - לתאר <strong>פונקציה</strong> כלשהי. אבל באלגברה מודרנית זה כלל לא המצב; פולינום הוא יצור עם זכות קיום בפני עצמו, אפילו אם בכלל לא מציבים בו ערכים. ואני רוצה לתת דוגמא שתבהיר מייד את הסיטואציה.

בואו נסתכל על החוג {% equation %}\mathbb{Z}_{3}=\left\{ 0,1,2\right\} {% endequation %} שבו פעולות החיבור והכפל הן מודולו 3, ונתבונן על הפולינום הבא: {% equation %}p\left(x\right)=x^{3}-x{% endequation %}. בדיקה ישירה תראה לנו שאם אנחנו מציבים בו איבר <strong>כלשהו</strong> של {% equation %}\mathbb{Z}_{3}{% endequation %} אז אנחנו מקבלים 0. כלומר, אם מסתכלים על {% equation %}p\left(x\right)=x^{3}-x{% endequation %} בתור "דרך לתאר פונקציה ותו לא" אז זו פונקציית האפס בדיוק כמו הפולינום {% equation %}q\left(x\right)=0{% endequation %}. אבל שני הפולינומים הללו הם יצורים שונים - באחד מופיעים {% equation %}x{% endequation %} ו-{% equation %}x^{3}{% endequation %} ובשני לא, למשל. אם כן, גם אם פולינומים שונים מגדירים את אותה הפונקציה, אנחנו עדיין רוצים לחשוב עליהם בתור יצורים שונים.

אם אני רוצה לדבר עליהם בתור יצורים עם קיום עצמאי, עדיף לתת הגדרה קצת יותר ברורה מ"אה... זה ביטוי...". ראשית, בואו ניקח חוג {% equation %}R{% endequation %} כלשהו שממנו יילקחו המקדמים של הפולינומים שמעניינים אותנו. עכשיו בואו "נרחיב" את החוג {% equation %}R{% endequation %} על ידי כך שנוסיף אליו אובייקט חדש שאני מסמן ב-{% equation %}x{% endequation %} ומגדיר על ה-{% equation %}x{% endequation %} הזה כללי חשבון: אם {% equation %}a\in R{% endequation %} אז {% equation %}ax=xa{% endequation %}, וכמו כן חישובים שמערבים את {% equation %}x{% endequation %} מקיימים דיסטריביוטיביות. במקום לכתוב {% equation %}x\cdot x\cdots x{% endequation %} כאשר כופלים את {% equation %}x{% endequation %} בעצמו {% equation %}n{% endequation %} פעמים אני אכתוב {% equation %}x^{n}{% endequation %} ונוסיף את המוסכמה ש-{% equation %}x^{0}=1{% endequation %} (כאשר {% equation %}1{% endequation %} הוא איבר היחידה של {% equation %}R{% endequation %}). עם כל אלו, אפשר לשאול את עצמנו איך נראה איבר כללי של החוג {% equation %}R\left[x\right]{% endequation %} שמתקבל מ-{% equation %}R{% endequation %} על ידי הוספת {% equation %}x{% endequation %} פנימה ולקיחת החוג הקטן בותר שמכיל את {% equation %}R{% endequation %} ואת {% equation %}x{% endequation %} (כלומר, סגור לחיבור ולכפל). התשובה היא ש-{% equation %}R\left[x\right]{% endequation %} יהיה בדיוק אוסף האיברים מהצורה {% equation %}a_{n}x^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}{% endequation %}, כפי שראינו קודם.

קרוב לודאי שגם זה לא מספיק לחלקכם - אתם אולי זועמים "מי {% equation %}x{% endequation %}? מה {% equation %}x{% endequation %}? מאיפה הוא הגיע? איך בונים אותו? מה הולך כאן?". ובכן, למרות שזה לגמרי לגיטימי לייצר איברים חדשים יש מאין בצורה הזו (מה שחשוב הוא להגדיר את ההתנהגות שלהם ביחס לפעולות החשבון של {% equation %}R{% endequation %} ולווודא ששום דבר בהגדרות של חוג לא נשבר כשמוסיפים אותם), אם ממש מתעקשים אפשר גם להגדיר פורמלית את הפולינום {% equation %}a_{n}x^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}{% endequation %} בתור הסדרה {% equation %}\left(a_{0},a_{1},\dots,a_{n}\right){% endequation %}; בצורה הזו, ה-{% equation %}x{% endequation %} הוא אכן רק סימון, אבל כזה שעוזר לנו להבין איך ייראה כפל של פולינומים.

יש נקודה עדינה אחת בהגדרה הזו שחשוב להתייחס אליה: אם אני כותב יצור כמו {% equation %}p\left(x\right)=0\cdot x^{2}+x+1{% endequation %} אני לא רוצה לחשוב עליו בתור אובייקט שונה מאשר {% equation %}x+1{% endequation %}. לכן, למרות שלפעמים משתלם לי מאוד לכתוב פולינום שהחזקות הגבוהות שלו מוכפלות ב-0 (עוד רגע נראה דוגמא לכך, בהגדרת חיבור וכפל פולינומים) אני רוצה לומר שזה עדיין אותו פולינום כמו זה שיתקבל על ידי כך שפשוט לא נכתוב את החזקות הגבוהות הללו. לכן לכל פולינום אנחנו בוחרים ייצוג <strong>קנוני</strong> {% equation %}a_{n}x^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}{% endequation %} שבו {% equation %}a_{n}\ne0{% endequation %}, למעט במקרה שבו הפולינום הוא פולינום האפס {% equation %}p\left(x\right)=0{% endequation %}. אם אתם רוצים פורמליזם, אז אני מגדיר פולינום בתור סדרה <strong>אינסופית</strong> {% equation %}\left(a_{0},a_{1},\dots\right){% endequation %} עם הדרישה הנוספת ש<strong>החל ממקום מסויים</strong> כל אברי הסדרה שווים 0.

ל-{% equation %}a_{n}{% endequation %} בייצוג הקנוני של הפולינום קוראים <strong>המקדם המוביל</strong> של הפולינום, ואם {% equation %}a_{n}=1{% endequation %} אומרים שהפולינום <strong>מתוקן</strong>. על הדרך אעיר ש-{% equation %}a_{0}{% endequation %} נקרא <strong>המקדם החופשי</strong> של הפולינום. <strong>המעלה</strong> (או כמו שאני לפעמים כותב בלי לשים לב, <strong>הדרגה</strong>) של הפולינום {% equation %}a_{n}x^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}{% endequation %}, כאשר {% equation %}a_{n}\ne0{% endequation %}, היא {% equation %}n{% endequation %}; מסמנים זאת {% equation %}\deg\left(p\right)=n{% endequation %}. עבור פולינום האפס בדרך כלל לא מגדירים בכלל את המעלה.

חיבור וכפל של פולינומים מתבצעים בצורה שמשמרת את חוקי החשבון הרגילים של {% equation %}R{% endequation %}, אבל בואו נכתוב את זה באופן כללי:
<ul>
 	<li>חיבור: {% equation %}\sum_{i=0}^{n}a_{i}x^{i}+\sum_{i=0}^{n}b_{i}x^{i}=\sum_{i=0}^{n}\left(a_{i}+b_{i}\right)x^{i}{% endequation %}</li>
 	<li>כפל: {% equation %}\left(\sum_{i=0}^{n}a_{i}x^{i}\right)\cdot\left(\sum_{i=0}^{m}b_{i}x^{i}\right)=\sum_{k=0}^{n+m}\left(\sum_{i=0}^{k}a_{i}b_{k-i}\right)x^{k}{% endequation %}</li>
</ul>
שימו לב שבחיבור השתמשתי ב-{% equation %}n{% endequation %} כדי לסמן את המקדם הגדול ביותר שאני כותב בכל אחד מהפולינומים; זה לא מגביל את הכלליות של ההגדרה כי בהינתן שני פולינומים ממעלה שונה, אני יכול לכתוב איברים נוספים עם מקדם 0 (למשל, במקום לכתוב {% equation %}\left(x^{2}+3\right)+\left(2x\right){% endequation %} אפשר לכתוב {% equation %}\left(x^{2}+0\cdot x+3\right)+\left(0\cdot x^{2}+2x+0\right){% endequation %}).

פעולת החיבור היא קצת "משעממת"; אם היינו מתארים פולינומים בתור סדרות אז חיבור היה בסך הכל ביצוע חיבור "איבר-איבר" בשתי הסדרות, כלומר

{% equation %}\left(a_{1},\dots,a_{n}\right)+\left(b_{1},\dots,b_{n}\right)=\left(a_{1}+b_{1},\dots,a_{n}+b_{n}\right){% endequation %}

אבל הכפל הוא כבר סיפור שונה לגמרי. הכפל מתאים לפעולה המתמטית שנקראת <strong>קונבולוציה</strong>, וזו פעולה מעניינת ושימושית מאוד. קונבולוציה של שתי סדרות מתבצעת כך: ראשית הופכים את הסדר של אחת מהסדרות, ואז כותבים את הסדרה האחת מעל השניה, כופלים את האיברים שנמצאים האחד מעל השני, ומחברים את כל המכפלות שמתקבלות בצורה הזו. <a href="http://gadial.net/2014/05/21/discrete_fourier_transform_intro/">תיארתי את זה בעבר בבלוג</a>, והנה זה שוב. ראשית נכתוב את הסדרות כך:

{% equation %}\begin{array}{ccccccc} \cdots & b_{2} & b_{1} & b_{0}\\ & & & a_{0} & a_{1} & a_{2} & \cdots \end{array}{% endequation %}

חשבו על מקומות ריקים בתור 0, ולכן איברים שמתחת או מעל להם יש מקום ריק לא יתרמו לסכום; הסכום שנקבל למעלה הוא פשוט {% equation %}a_{0}b_{0}{% endequation %}, וזה גם המקדם של {% equation %}x^{0}{% endequation %} במכפלה של שני הפולינומים.

כעת נזיז את הסדרה העליונה מקום אחד ימינה ונקבל

{% equation %}\begin{array}{ccccccc} \cdots & b_{3} & b_{2} & b_{1} & b_{0}\\ & & & a_{0} & a_{1} & a_{2} & \cdots \end{array}{% endequation %}

זה נותן לנו את הסכום {% equation %}a_{0}b_{1}+a_{1}b_{0}{% endequation %} שמתאים למקדם של {% equation %}x^{1}{% endequation %}, וכן הלאה. בסופו של דבר, מכיוון ששתי הסדרות סופיות, השלב האחרון יהיה

{% equation %}\begin{array}{ccccccc} & & & b_{m} & b_{m-1} & \cdots\\ & \cdots & a_{n-1} & a_{n} \end{array}{% endequation %}

שייתן לנו את המקדם {% equation %}a_{n}b_{m}{% endequation %} של {% equation %}x^{n+m}{% endequation %}. במילים אחרות, מכפלת שני הפולינומים {% equation %}\sum_{i=0}^{n}a_{i}x^{i}{% endequation %} ו-{% equation %}\sum_{i=0}^{m}b_{i}x^{i}{% endequation %} מייצרת לנו פולינום חדש, שמקדמיו הם כל הקונבולוציות האפשריות של הסדרות {% equation %}\left(a_{0},\dots,a_{n}\right){% endequation %} ו-{% equation %}\left(b_{0},\dots,b_{m}\right){% endequation %}.

הכפל המעניין הזה מזכיר קצת את מה שקורה עם מטריצות; גם מטריצות נראות במבט ראשון כמו דרך לא כל כך מעניינת לתאר סדרות (במקרה הזה, סדרות דו-ממדיות) והחיבור שלהן הוא איבר-איבר, אבל <a href="http://gadial.net/2011/10/06/matrix_product/">הכפל שלהן</a> הוא מאוד מוזר ממבט ראשון, ומאוד מעניין ממבט שני בגלל היכולת שלו לתאר דברים שונים ומשונים.
<h2>תכונות בסיסיות של חוגי פולינומים</h2>
אפשר לבדוק ולראות במפורש שההגדרות של חיבור וכפל פולינומים הופכות את {% equation %}R\left[x\right]{% endequation %} לחוג, לכל {% equation %}R{% endequation %}. איך החוג הזה יתנהג בדיוק, זה כבר תלוי בשאלה מהו {% equation %}R{% endequation %}. כש-{% equation %}R{% endequation %} הוא חוג כללי קשה להגיד יותר מדי דברים ברורים על מה יקרה לפולינומים מעליו. למשל, תכונה שאנחנו מכירים מהיומיום של פולינומים היא ש-{% equation %}\deg\left(pq\right)=\deg\left(p\right)+\deg\left(q\right){% endequation %} - כשכופלים פולינומים מקבלים פולינום מדרגה שהיא סכום הדרגות שלהם. זה לא עובד לחוג פולינומים מעל {% equation %}R{% endequation %} כללי; למשל, ניקח {% equation %}R=\mathbb{Z}_{4}{% endequation %}, אז {% equation %}\left(2x+1\right)\cdot\left(2x+1\right)=4x^{2}+4x+1=1{% endequation %}, כשהשוויון הוא בחוג {% equation %}\mathbb{Z}_{4}{% endequation %}. קיבלנו אם כן פולינום ממעלה 0 על ידי כפל שני פולינומים ממעלה 1. ה"בעיה" הייתה שהמקדמים המובילים של הפולינומים שכפלנו היו <strong>מחלקי אפס</strong>; אם הם לא כאלו, או ש-{% equation %}R{% endequation %} הוא תחום שלמות, אז {% equation %}\deg\left(pq\right)=\deg\left(p\right)+\deg\left(q\right){% endequation %} אכן מתקיים. עד שלומדים על חוגים ושדות ההקשר שבו רואים פולינומים הוא בדרך כלל כזה שבו {% equation %}R{% endequation %} הוא <strong>שדה</strong>, למשל המספרים הממשיים, ולכן התכונה הזו נראית לנו (אולי) מובנת מאליה.

שימו לב למשהו נוסף שראינו בדוגמא שלי: {% equation %}2x+1{% endequation %} היה ההופכי של עצמו. אם {% equation %}R{% endequation %} הוא תחום שלמות זה לא יכול לקרות: התכונה על סכום המעלות מבטיחה שההפיכים היחידים ב-{% equation %}R\left[x\right]{% endequation %} יהיו "פולינומים" ממעלה 0, ופולינומים כאלו הם פשוט איברים של {% equation %}R{% endequation %}, כך שההפיכים ב-{% equation %}R\left[x\right]{% endequation %} הם בדיוק ההפיכים של {% equation %}R{% endequation %}. במילים אחרות, אפשר לשכוח מכך ש-{% equation %}R\left[x\right]{% endequation %} יהיה שדה; אבל אם {% equation %}R{% endequation %} הוא תחום שלמות אז {% equation %}R\left[x\right]{% endequation %} הוא תחום שלמות ואז אפשר לדבר על <a href="http://gadial.net/2018/01/30/rings_of_fractions/">שדה השברים</a> של {% equation %}R\left[x\right]{% endequation %}. השדה הזה, שהאיברים שלו הם כל היצורים מהצורה {% equation %}\frac{p\left(x\right)}{q\left(x\right)}{% endequation %} כאשר {% equation %}q\left(x\right){% endequation %} איננו פולינום האפס, נקרא <strong>שדה הפונקציות הרציונליות</strong> מעל {% equation %}R{% endequation %}. לא נדבר עליו יותר כאן, אבל כדאי לדעת שדבר כזה קיים.

הסיטואציה המעניינת ביותר מבחינתנו היא זו שבה החוג שמעליו אנחנו עובדים הוא שדה; בדרך כלל מסמנים אותו ב-{% equation %}F{% endequation %} במקרה הזה ולא ב-{% equation %}R{% endequation %} כדי שיהיה ברור שאנחנו בסיטואציה הזו. החשיבות של המקרה הזה היא בכך שבו אפשר להגדיר <strong>חלוקה עם שארית</strong> על הפולינומים. כלומר, אם {% equation %}a\left(x\right),b\left(x\right)\in F\left[x\right]{% endequation %} הם פולינומים כך ש-{% equation %}b\left(x\right)\ne0{% endequation %} אז קיימים {% equation %}q\left(x\right),r\left(x\right)\in F\left[x\right]{% endequation %} כך ש-

{% equation %}a\left(x\right)=b\left(x\right)q\left(x\right)+r\left(x\right){% endequation %}

עם התכונה הנוספת לפיה {% equation %}\deg\left(r\right)&lt;\deg b{% endequation %} או ש-{% equation %}r=0{% endequation %}. שימו לב שזה חייב להיות מעל שדה: למשל, ב-{% equation %}\mathbb{Z}\left[x\right]{% endequation %} הפולינום {% equation %}x{% endequation %} פשוט לא מתחלק עם שארית על ידי {% equation %}2{% endequation %}. זה טיפה שובר אינטואיציה כי הרי אנחנו רגילים לחשוב על "חלוקה עם שארית" בדיוק בהקשר של {% equation %}\mathbb{Z}{% endequation %}.

בואו נוכיח את הטענה על החלוקה עם שארית פורמלית, באינדוקציה על המעלה של {% equation %}a\left(x\right){% endequation %}. אם לחדד - אנחנו קובעים מראש פולינום {% equation %}b\left(x\right){% endequation %} כלשהו ומוכיחים שלכל {% equation %}a\left(x\right){% endequation %} ניתן לחלק עם שארית את {% equation %}a\left(x\right){% endequation %} ב-{% equation %}b\left(x\right){% endequation %}.

בסיס האינדוקציה הוא כל המקרים שבהם {% equation %}\deg\left(a\right)&lt;\deg\left(b\right){% endequation %}. במקרים הללו אפשר פשוט "לרמות" ולהגדיר {% equation %}q\left(x\right)=0{% endequation %} ו-{% equation %}r\left(x\right)=a\left(x\right){% endequation %} ומקבלים {% equation %}a\left(x\right)=b\left(x\right)q\left(x\right)+r\left(x\right){% endequation %} תוך עמידה בקריטריון {% equation %}\deg\left(r\right)&lt;\deg\left(b\right){% endequation %} (זה כמו האופן שבו מחלקים את 6 ב-17 עם שארית - המנה היא 0 והשארית היא 6).

כעת נעבור לצעד האינדוקציה: נניח ש-{% equation %}\deg\left(a\right)=n\ge\deg\left(b\right){% endequation %} ושהוכחנו כבר את הטענה לכל מעלה קטנה מ-{% equation %}n{% endequation %}. הרעיון הוא להעלים את המקדם המוביל של {% equation %}a\left(x\right){% endequation %} כדי לקבל פולינום ממעלה נמוכה יותר שאנחנו כבר יודעים איך לחלק - זה למעשה גם הרעיון מאחורי השיטות הפרקטיות שבהן אנחנו מבצעים חילוק ארוך (של שלמים/פולינומים) ביד.

אם כן, נסמן {% equation %}a\left(x\right)=a_{n}x^{n}+\dots+a_{1}x+a_{0}{% endequation %}, כאשר {% equation %}a_{n}\ne0{% endequation %}. באופן דומה נסמן {% equation %}b\left(x\right)=b_{m}x^{m}+\dots+b_{1}x+b_{0}{% endequation %} עם {% equation %}b_{m}\ne0{% endequation %}. ההנחה שלנו היא ש-{% equation %}n\ge m{% endequation %} אחרת היינו מטפלים במקרה הזה כחלק מהבסיס. נגדיר כעת פולינום חדש באופן הבא:

{% equation %}a^{\prime}\left(x\right)=a\left(x\right)-\frac{a_{n}}{b_{m}}x^{n-m}b\left(x\right){% endequation %}

הפולינום הזה יהיה לכל היותר ממעלה {% equation %}n-1{% endequation %} ולכן אפשר להשתמש עליו בהנחת האינדוקציה ולקבל:

{% equation %}a^{\prime}\left(x\right)=q^{\prime}\left(x\right)b\left(x\right)+r\left(x\right){% endequation %} כך ש-{% equation %}\deg\left(r^{\prime}\right)&lt;\deg\left(b\right){% endequation %} או {% equation %}r=0{% endequation %} (שימו לב - לא שמתי תג על {% equation %}b{% endequation %} מכיוון שאנחנו מוכיחים את המשפט עבור כל ה-{% equation %}a\left(x\right){% endequation %}-ים האפשריים ועם {% equation %}b\left(x\right){% endequation %} <strong>קבוע</strong> עבור כולם; ועל {% equation %}r{% endequation %} לא שמתי תג כי הוא יהיה גם השארית הסופית שארצה לקבל).

יש לנו עכשיו שתי משוואות שמערבות את {% equation %}a^{\prime}\left(x\right){% endequation %}. נשווה את שתיהן ונקבל:

{% equation %}a\left(x\right)=\frac{a_{n}}{b_{m}}x^{n-m}b\left(x\right)+q^{\prime}\left(x\right)b\left(x\right)+r\left(x\right)=\left(\frac{a_{n}}{b_{m}}x^{n-m}+q^{\prime}\left(x\right)\right)+r\left(x\right){% endequation %}

כלומר, קיבלנו את המבוקש, עם {% equation %}q\left(x\right)=\frac{a_{n}}{b_{m}}x^{n-m}+q^{\prime}\left(x\right){% endequation %}.

החילוק-עם-שארית הזה הוא עסק רציני מאוד - זה הופך את {% equation %}F\left[x\right]{% endequation %} ל<a href="https://gadial.net/2018/03/01/euclidean_domains_and_pids/">תחום אוקלידי</a> לכל שדה {% equation %}F{% endequation %} אפשרי. בפרט זה אומר ש-{% equation %}F\left[x\right]{% endequation %} הוא תחום פריקות יחידה (כלומר, כל פולינום מתפרק באופן יחיד לגורמים אי-פריקים) ותחום ראשי (כלומר, כל אידאל נוצר בידי פולינום יחיד). שני אלו יהיו מאוד חשובים בהמשך, כשנדבר על תורת השדות.
<h2>שורשים של פולינומים</h2>
קודם עשיתי מהומה גדולה סביב זה שפולינום הוא יותר מאשר סתם פונקציה ושאפשר להתעסק עם פולינומים גם בלי להציב בהם דברים בכלל, אבל זה לא אומר שזה לא מעניין להציב בהם דברים. אחד מהדברים החשובים ביותר שאפשר לעשות עם פולינום הוא להציב בו דברים, כמו שאחד מהדברים החשובים ביותר שאפשר לעשות עם מטריצה הוא לכפול אותה בוקטורים.

אם {% equation %}p\left(x\right)\in R\left[x\right]{% endequation %} כך ש-{% equation %}p\left(x\right)=a_{n}x^{n}+\dots+a_{1}x+a_{0}{% endequation %} ו-{% equation %}r\in R{% endequation %} אז <strong>הצבה</strong> של {% equation %}r{% endequation %} ב-{% equation %}p\left(x\right){% endequation %} מניבה לנו איבר ב-{% equation %}R{% endequation %} שמחושב באופן הבא:

{% equation %}p\left(r\right)=a_{n}r^{n}+\dots+a_{1}r+a_{0}{% endequation %}

אין כאן שום דבר מפתיע או חדש, כמובן. יש רק נקודה קטנה שאני רוצה להתייחס אליה במפורש: אפשר להציב בפולינום גם ערכים שנלקחים מתוך קבוצה שלא בהכרח שווה לחוג {% equation %}R{% endequation %} שממנו נלקחו מקדמי הפולינום; כל מה שנדרש הוא שהמקדמים ידעו "לשחק יפה" עם {% equation %}r{% endequation %}, כלומר שתהיה משמעות לכפל שלהם. זו הסיבה שבגללה אפשר להציב, למשל, <strong>מטריצות</strong> בתוך פולינומים; יש לנו מושג של כפל מטריצה בסקלר שהוא האופן שבו המטריצה משחקת יפה עם המקדמים של הפולינום. עם זאת, ההקשר שמעניין אותי בתורת השדות הוא כמעט תמיד זה שבו מציבים בתוך פולינום מ-{% equation %}R\left[x\right]{% endequation %} ערך מחוג ש<strong>מרחיב</strong> את {% equation %}R{% endequation %} - כלומר, כולל את {% equation %}R{% endequation %} בתור תת-חוג. במקרה הזה, ה"משחק יפה" הוא פשוט פעולת הכפל הרגילה בחוג ההרחבה הזה. למשל, בפולינום {% equation %}p\left(x\right)=3x^{2}+1\in\mathbb{Q}\left[x\right]{% endequation %} אין שום בעיה להציב את {% equation %}\pi{% endequation %} ולקבל {% equation %}p\left(\pi\right)=3\pi^{2}+1{% endequation %} וזאת למרות ש-{% equation %}\pi\notin\mathbb{Q}{% endequation %}.

בואו נדבר עכשיו על המקרה שבו {% equation %}F{% endequation %} שדה, {% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} ו-{% equation %}a\in F{% endequation %}. אנחנו אומרים ש-{% equation %}a{% endequation %} הוא <strong>שורש</strong> של {% equation %}p\left(x\right){% endequation %} אם {% equation %}p\left(a\right)=0{% endequation %}. שורשים של פולינומים מעניינים אותנו במיוחד כי הם במובן מסויים אבני הבניין של הפולינום: אם {% equation %}p\left(a\right)=0{% endequation %} ואנחנו מעל שדה, אז אני טוען שהפולינום {% equation %}\left(x-a\right){% endequation %} מחלק את {% equation %}p\left(x\right){% endequation %}. ההוכחה פשוטה: אנחנו מעל שדה אז אפשר לחלק עם שארית ולקבל

{% equation %}p\left(x\right)=q\left(x\right)\left(x-a\right)+r\left(x\right){% endequation %}

עכשיו, {% equation %}\deg\left(r\right)&lt;\deg\left(x-a\right)=1{% endequation %} ולכן בהכרח {% equation %}\deg\left(r\right)=0{% endequation %} כך ש-{% equation %}r{% endequation %} הוא קבוע. אם נציב {% equation %}a{% endequation %} בשני אגפי המשוואה, נקבל

{% equation %}p\left(a\right)=0=q\left(a\right)\cdot0+r=r{% endequation %}

כלומר, נקבל שהשארית היא בהכרח 0, ומכאן ש-{% equation %}x-a{% endequation %} מחלק את {% equation %}p\left(x\right){% endequation %} בלי שארית.

עכשיו, שימו לב מה קרה כאן. ראינו ש-{% equation %}p\left(x\right)=q\left(x\right)\left(x-a\right){% endequation %}, אז {% equation %}\deg\left(p\right)=\deg\left(q\right)+1{% endequation %}, כלומר הצגנו את {% equation %}p\left(x\right){% endequation %} בתור מכפלה של שני פולינומים ממעלה נמוכה יותר. נניח שגם ל-{% equation %}q\left(x\right){% endequation %} יש שורש, אז גם אותו אפשר לפרק ככה, ואם לכל הפולינומים שנגיע אליהם בצורה הזו יש שורש, בסוף נקבל את השוויון

{% equation %}p\left(x\right)=a\left(x-a_{1}\right)\left(x-a_{2}\right)\dots\left(x-a_{n}\right){% endequation %}

כאשר {% equation %}a_{1},\dots,a_{n}{% endequation %} הם השורשים (לאו דווקא שונים זה מזה) של {% equation %}p\left(x\right){% endequation %} ו-{% equation %}a\in F{% endequation %} הוא המקדם המוביל של {% equation %}p\left(x\right){% endequation %}. במילים אחרות - אם כל השורשים של {% equation %}p\left(x\right){% endequation %} שייכים לשדה {% equation %}F{% endequation %}, אז הפירוק לגורמים אי פריקים של {% equation %}p\left(x\right){% endequation %} הוא בדיוק המכפלה הנ"ל. למשל, הפולינום {% equation %}x^{2}-1{% endequation %} מתפרק מעל {% equation %}\mathbb{R}{% endequation %} ל-{% equation %}\left(x-1\right)\left(x+1\right){% endequation %} והשורשים שלו הם 1 ו-{% equation %}-1{% endequation %}; הפולינום {% equation %}x^{2}+x-6{% endequation %} מתפרק ל-{% equation %}\left(x-2\right)\left(x+3\right){% endequation %} והשורשים שלו הם 2 ו-{% equation %}-3{% endequation %}; ואילו {% equation %}x^{2}+1{% endequation %} לא מתפרק כלל מעל {% equation %}\mathbb{R}{% endequation %} אבל מעל {% equation %}\mathbb{C}{% endequation %} הוא יתפרק ל-{% equation %}\left(x+i\right)\left(x-i\right){% endequation %}.

הפירוק הזה גם מלמד אותנו בדיוק איך בנויים המקדמים של {% equation %}p\left(x\right){% endequation %}; הם כולם מורכבים מסכומים של מכפלות של שורשים של {% equation %}p\left(x\right){% endequation %}. בואו נראה דוגמא עבור פולינום ממעלה שלישית עם שורשים {% equation %}a,b,c{% endequation %}: הפירוק שלו הוא {% equation %}\left(x-a\right)\left(x-b\right)\left(x-c\right){% endequation %}. לפתוח את הסוגריים באופן מפורש זו עבודה טכנית, אבל היא תשתלם לנו, כי אחרי שנעשה אותה נראה (ונרגיש) שהפולינום הוא מהצורה

{% equation %}x^{3}-\left(a+b+c\right)x^{2}+\left(ab+ac+bc\right)x-abc{% endequation %}

שימו לב ל<strong>סימטריה</strong> שיש בכל המקדמים - במקדם של {% equation %}x^{2}{% endequation %} משתתפים כל הסכומים האפשריים של מכפלה של שורש בודד; במקדם של {% equation %}x{% endequation %} כל הסכומים של מכפלה של שני שורשים, ובמקדם של {% equation %}x^{0}{% endequation %} כל הסכומים של מכפלה של שלושה. על כך אומרים לפעמים שהמקדמים של הפולינום הם <strong>פונקציות סימטריות</strong> בשורשים שלו. העובדה שהפולינום נבנה כולו מתוך השורשים (עד כדי כפל של כל הפולינום באיבר כלשהו של {% equation %}F{% endequation %}) מצביעה יפה על החשיבות הרבה שלהם.

אבל מה קורה אם אותו שורש מופיע יותר מפעם אחת? נסתכל למשל על {% equation %}x^{3}-9x+27x-27{% endequation %}. קל לראות שהפירוק של הפולינום הזה לגורמים הוא {% equation %}\left(x-3\right)\left(x-3\right)\left(x-3\right){% endequation %}, כלומר יש לו שורש בודד שהוא 3 שמופיע שלוש פעמים. אין עם זה בעיה; הנוסחה מלמעלה עובדת גם כאשר {% equation %}a=b=c=3{% endequation %} (בדקו!). במקרה הזה אומרים על 3 שהוא שורש <strong>מריבוי</strong> שלוש, ובאופן כללי מספר הפעמים ששורש כלשהו מופיע בפירוק הוא ה<strong>ריבוי</strong> שלו. הנה דרך אחרת להגדיר ריבוי של שורש: {% equation %}a{% endequation %} הוא שורש מריבוי {% equation %}k{% endequation %} של {% equation %}p\left(x\right){% endequation %} אם {% equation %}p\left(x\right)=\left(x-a\right)^{k}q\left(x\right){% endequation %} כך ש-{% equation %}a{% endequation %} אינו שורש של {% equation %}q\left(x\right){% endequation %}.

עכשיו אפשר לדבר על קשר ברור שיש בין המעלה של פולינום ובין מספר השורשים שלו - מספר השורשים לא יכול להיות גדול מהמעלה שלו, פשוט כי ראינו שלכל שורש {% equation %}a{% endequation %} אפשר להקטין את המעלה של הפולינום ב-1 על ידי חלוקה ב-{% equation %}x-a{% endequation %}. זה נכון רק מעל שדה; למשל, מעל החוג {% equation %}\mathbb{Z}_{8}{% endequation %} שאיננו שדה, קל לראות של-{% equation %}x^{2}-1{% endequation %} יש ארבעה שורשים: {% equation %}1,3,5,7{% endequation %}. זהירות לא לבלבל את התוצאה הזו, שלפולינום ממעלה {% equation %}n{% endequation %} מעל שדה יש לכל היותר {% equation %}n{% endequation %} שורשים, עם מה שנקרא <strong>המשפט היסודי של האלגברה</strong> שאומר משהו שונה לגמרי; הוא אומר שאם {% equation %}p\left(x\right)\in\mathbb{C}\left[x\right]{% endequation %} ו-{% equation %}p\left(x\right){% endequation %} הוא ממעלה {% equation %}n{% endequation %}, אז ל-{% equation %}p\left(x\right){% endequation %} יש <strong>בדיוק</strong> {% equation %}n{% endequation %} שורשים ב-{% equation %}\mathbb{C}{% endequation %} (כולל ריבוי, כלומר שורש יכול להיספר יותר מפעם אחת, על פי מספר הפעמים שהוא מופיע בפירוק). בניסוח שקול: לכל פולינום ממעלה לפחות 1 מעל המרוכבים יש שורש מרוכב (ואז אפשר לחלק ב-{% equation %}x-a{% endequation %} ולהמשיך באינדוקציה). המשפט הזה מדבר ספציפית על {% equation %}\mathbb{C}{% endequation %}, וכשנדבר על תורת השדות נראה שיש שם כללי יותר לתופעה שהוא מתאר: הוא בעצם אומר "שדה המרוכבים <strong>סגור אלגברית</strong>" אבל על זה נדבר בהמשך.
<h2>פולינומים פריקים ואי פריקים</h2>
מה שראינו קודם הוא שאם לפולינום ממעלה לפחות 2 {% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} יש שורש {% equation %}a\in F{% endequation %}, אז הוא פריק מעל {% equation %}F{% endequation %}: ניתן לכתוב אותו בתור {% equation %}p\left(x\right)=\left(x-a\right)q\left(x\right){% endequation %} כאשר אף אחד משני המוכפלים אינו הפיך (כלומר, אינו פולינום ממעלה 0). זה קריטריון <strong>מספיק</strong> לכך שפולינום יהיה פריק, אבל הוא לא <strong>הכרחי</strong>: מעל {% equation %}\mathbb{R}{% endequation %} אין לפולינום {% equation %}x^{4}+2x^{2}+1{% endequation %} שורשים, אבל הוא מתפרק ל-{% equation %}\left(x^{2}+1\right)\left(x^{2}+1\right){% endequation %}. מכיוון שבהמשך הפריקות/אי הפריקות של פולינומים תשחק תפקיד חשוב, מעניין לדעת מה השיטות הבסיסיות שאיתן בודקים דברים כאלו. יש כמה כללי אצבע סטנדרטיים שאתאר את כולם פה, אבל הם בוודאי לא מהווים תיאור ממצה של כל מה שאפשר לעשות.

ראשית, שימו לב שהדוגמא שלי לפולינום פריק שאין לו שורש הייתה ממעלה 4. זה לא מקרי; פולינום ממעלה 2 או 3 הוא פריק אם ורק אם יש לו שורש, פשוט כי אחד מהגורמים בפירוק חייב להיות מדרגה 1 (כלומר, להיות מהצורה {% equation %}ax+b=a\left(x-\left(-\frac{b}{a}\right)\right){% endequation %} שמתאימה לשורש {% equation %}-\frac{b}{a}{% endequation %}).

שנית, הנה תעלול נחמד, שנוגע ברעיון עמוק יותר שבא לידי ביטוי בחלק של תורת השדות שנקרא <strong>תורת גלואה</strong>: אם {% equation %}p\left(x\right)\in\mathbb{R}\left[x\right]{% endequation %} הוא פולינום עם מקדמים ממשיים ו-{% equation %}z=a+bi{% endequation %} הוא שורש <strong>מרוכב</strong> של הפולינום, אז גם הצמוד שלו {% equation %}\overline{z}=a-bi{% endequation %} הוא שורש של הפולינום. כדי לראות את זה, בואו נכתוב לרגע את הפולינום במפורש: {% equation %}p\left(x\right)=a_{n}x^{n}+\dots+a_{1}x+a_{0}{% endequation %}. אם נציב את {% equation %}z{% endequation %} נקבל

{% equation %}p\left(z\right)=a_{n}z^{n}+\dots+a_{1}z+a_{0}=0{% endequation %}

עכשיו אפשר לקחת את הצמוד של שני האגפים, ולהשתמש בתכונות הסטנדרטיות של הצמוד שהן {% equation %}\overline{z_{1}+z_{2}}=\overline{z_{1}}+\overline{z_{2}}{% endequation %} ו-{% equation %}\overline{z_{1}\cdot z_{2}}=\overline{z_{1}}\cdot\overline{z_{2}}{% endequation %}. נקבל:

{% equation %}\overline{p\left(z\right)}=\overline{a_{n}z^{n}+\dots+a_{1}z+a_{0}}=\overline{a_{n}}\cdot\overline{z}^{n}+\dots+\overline{a_{1}}\cdot\overline{z}+\overline{a_{0}}{% endequation %}

אבל המקדמים של הפולינום הם ממשיים, כלומר שווים לצמוד של עצמם, כך שנקבל

{% equation %}\overline{a_{n}}\cdot\overline{z}^{n}+\dots+\overline{a_{1}}\cdot\overline{z}+\overline{a_{0}}=a_{n}\cdot\overline{z}^{n}+\dots+a_{1}\cdot\overline{z}+a_{0}=p\left(\overline{z}\right){% endequation %}

קיבלנו ש-{% equation %}p\left(\overline{z}\right)=\overline{p\left(z\right)}=\overline{0}=0{% endequation %}. התעלול הזה, כאמור, ניתן להכללה מרחיקת לכת, אבל בינתיים נבין איך הוא עוזר לנו פה.

ראשית, אם {% equation %}z{% endequation %} הוא מספר מרוכב כלשהו, אז {% equation %}z\cdot\overline{z}{% endequation %} ו-{% equation %}z+\overline{z}{% endequation %} הם ממשיים (פשוט בדקו זאת!). לכן, אם {% equation %}z{% endequation %} הוא שורש של {% equation %}p\left(x\right){% endequation %} והוא שונה מהצמוד שלו (כלומר, אינו ממשי) אז גם {% equation %}\left(x-z\right){% endequation %} וגם {% equation %}\left(x-\overline{z}\right){% endequation %} הם גורמים של {% equation %}p\left(x\right){% endequation %} כשמפרקים אותו לגורמים מעל {% equation %}\mathbb{C}{% endequation %}; ומכפלת שני הגורמים הללו היא {% equation %}x^{2}-\left(z+\overline{z}\right)x+z\cdot\overline{z}{% endequation %}, שהוא פולינום <strong>עם מקדמים ממשיים</strong>. קיבלנו שיש ל-{% equation %}p\left(x\right){% endequation %} גורם ממעלה 2 על כל שורש מרוכב שאינו ממשי של {% equation %}p\left(x\right){% endequation %}; ובנוסף לכך על כל שורש ממשי של {% equation %}p\left(x\right){% endequation %} נקבל גורם ממעלה 1. המסקנה היא שכל פולינום מעל {% equation %}\mathbb{R}{% endequation %} מתפרק למכפלה של גורמים שהם לכל היותר ממעלה 2. שימו לב שהשתמשנו כאן כמעט במובלע במשפט היסודי של האלגברה, כשהנחנו שכל השורשים של {% equation %}p\left(x\right){% endequation %} הם או ממשיים או מרוכבים שאינם ממשיים.

והנה תעלול למציאת שורשים שעובד רק ברציונליים ואוהבים לקרוא לו "משפט הניחוש האינטליגנטי" כי הוא נותן לנו רשימה בתקווה מצומצמת של מועמדים להיות השורשים <strong>הרציונליים</strong> של פולינום שהמקדמים שלו הם <strong>שלמים</strong>: נניח ש-{% equation %}p\left(x\right)=a_{n}x^{n}+\dots+a_{1}x+a_{0}{% endequation %} הוא פולינום שכל מקדמיו ב-{% equation %}\mathbb{Z}{% endequation %}; אז אם {% equation %}\frac{r}{s}{% endequation %} הוא שורש שלו שמוצג בצורה מצומצמת, כלומר ל-{% equation %}r,s{% endequation %} אין גורם משותף, אז בהכרח {% equation %}r|a_{0}{% endequation %} ו-{% equation %}s|a_{n}{% endequation %} ({% equation %}r{% endequation %} מחלק את המקדם החופשי ו-{% equation %}s{% endequation %} מחלק את המקדם המוביל). כמקרה פרטי מקבלים שאם {% equation %}p\left(x\right){% endequation %} הוא פולינום מתוקן, אז השורשים הרציונליים שלו הם בהכרח שלמים ומחלקים את המקדם החופשי.

אין בהוכחה משהו מתוחכם. פשוט מציבים {% equation %}x=\frac{r}{s}{% endequation %}, מכפילים ב-{% equation %}s^{n}{% endequation %} כדי לנטרל את השבר, ומקבלים את התוצאה

{% equation %}a_{n}r^{n}+a_{n-1}r^{n-1}s+\dots+a_{1}rs^{n-1}+a_{0}s^{n}=0{% endequation %}

עכשיו, אפשר להעביר את הגורם הראשון אגף ומקבלים

{% equation %}-a_{n}r^{n}=s\left(a_{n-1}r^{n-1}+\dots+a_{0}s^{n-1}\right){% endequation %}

כלומר, {% equation %}s{% endequation %} מחלק את אגף ימין, ולכן את אגף שמאל, אבל באגף שמאל הוא לא מחלק את {% equation %}r^{n}{% endequation %} (אחרת {% equation %}\frac{r}{s}{% endequation %} לא היה שבר מצומצם) ולכן הוא בהכרח מחלק את {% equation %}a_{n}{% endequation %}; באופן דומה, אפשר להעביר את הגורם האחרון אגף, לקבל {% equation %}-a_{0}s^{n}=r\left(a_{n}r^{n-1}+\dots+a_{1}s^{n-1}\right){% endequation %} ומכך ינבע ש-{% equation %}r{% endequation %} מחלק את {% equation %}a_{0}{% endequation %}. זו הוכחה טכנית אבל אני אוהב אותה כי כשזוכרים את הרעיון שלה קל להיזכר במשפט מהראש - למה מחלקים דווקא את המקדם המוביל והמקדם החופשי ולמה המכנה מחלק את המקדם המוביל והמונה את החופשי.

כלל האצבע האחרון שאני רוצה להראות הוא טכניקה שמאפשרת להוכיח שפולינום הוא אי-פריק (משהו שעד עכשיו לא הראיתי). היא לא יעילה תמיד, אבל כשהיא כן היא מאוד פשוטה לבדיקה - ועוד יתרון הוא שקל יחסית <strong>לבנות</strong> פולינום אי פריק על סמך מה שהיא מציעה. השיטה הזו נקראת <strong>קריטריון אייזנשטיין</strong>. נתחיל מלהציג מקרה פרטי שלה: ניקח פולינום <strong>מתוקן</strong> עם מקדמים שלמים {% equation %}a\left(x\right)=x^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}{% endequation %}. כעת, נניח ש-{% equation %}p{% endequation %} הוא מספר <strong>ראשוני </strong>שמחלק את כל המקדמים של הפולינום למעט את זה של {% equation %}x^{n}{% endequation %}, ובנוסף לכך ש-{% equation %}p^{2}{% endequation %} <strong>אינו</strong> מחלק את {% equation %}a_{0}{% endequation %} - אז הפולינום אי פריק מעל {% equation %}\mathbb{Q}{% endequation %}. למשל, {% equation %}x^{3}+2x+6{% endequation %} הוא אי פריק בגלל {% equation %}p=2{% endequation %} (הייתם יכולים לראות זאת גם בעזרת הטכניקות הקודמות; השורשים האפשריים היחידים של הפולינום הזה מעל הרציונליים הם 1,2,3,6 והשלילות שלהם, ובדיקה ישירה מראה שאף אחד מהם אינו שורש, ואם פולינום ממעלה שלישית הוא פריק בהכרח יש לו שורש).

איך מוכיחים את הקריטריון? אין סיבה לא להוכיח אותו בצורה כללית יותר, עבור תחום שלמות כלשהו. יהא {% equation %}R{% endequation %} תחום שלמות ו-{% equation %}a\left(x\right)=x^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}{% endequation %} פולינום מתוקן ב-{% equation %}R\left[x\right]{% endequation %}. אם קיים <strong>אידאל ראשוני</strong> {% equation %}P{% endequation %} כך ש-{% equation %}a_{0},a_{1},\dots,a_{n-1}\in P{% endequation %} אבל {% equation %}a_{0}\notin P^{2}{% endequation %} אז {% equation %}p\left(x\right){% endequation %} אי-פריק מעל {% equation %}R{% endequation %}.

אולי כדאי להזכיר מהו {% equation %}P^{2}{% endequation %}. מכפלה של אידאלים באופן כללי היא אוסף הסכומים הסופיים של מכפלות של אברי האידאלים. כלומר, במקרה שלנו {% equation %}P^{2}=\left\{ \sum ab\ |\ a\in P,b\in P\right\} {% endequation %}.

בואו נראה כעת איך מוכיחים את הקריטריון. נניח בשלילה ש-{% equation %}a\left(x\right)=b\left(x\right)c\left(x\right){% endequation %} עבור פולינומים ממעלה לפחות 1 {% equation %}b\left(x\right),c\left(x\right){% endequation %} מעל {% equation %}R{% endequation %}. עכשיו בואו נעבור לדבר על החוג {% equation %}R/P{% endequation %}. החוג הזה הוא תחום שלמות כי {% equation %}P{% endequation %} הוא אידאל ראשוני, ואפשר לדבר על פולינומים מעל החוג הזה. בפרט, אפשר לדבר על {% equation %}a\left(x\right),b\left(x\right),c\left(x\right){% endequation %} מעליו; אנחנו פשוט מחליפים כל מקדם של הפולינומים הללו בתמונה שלו בחוג המנה {% equation %}R/P{% endequation %}. למשל, אני מסמן

{% equation %}\overline{a\left(x\right)}=x^{n}+\left(a_{n-1}+P\right)x^{n-1}+\dots+\left(a_{1}+P\right)x+\left(a_{0}+P\right){% endequation %}

עכשיו, אם {% equation %}a_{i}\in P{% endequation %} אז {% equation %}a_{i}+P=P{% endequation %}; אתם צריכים לחשוב על {% equation %}P{% endequation %} בתור "סקלר האפס" בחוג המנה {% equation %}R/P{% endequation %}, כך ש-{% equation %}\overline{a\left(x\right)}{% endequation %} הוא בעצם פולינום פשוט במיוחד: {% equation %}\overline{a\left(x\right)}=x^{n}+P{% endequation %}. כדי לפשט לי את הסימונים אני אפסיק לכתוב {% equation %}+P{% endequation %} ולשים גג מעל פולינומים; פשוט נבין שפעולות החשבון שאנחנו מבצעים הן מעכשיו בחוג {% equation %}R/P{% endequation %}.

אם כן, בחוג {% equation %}R/P{% endequation %} יש לנו את הסיטואציה הבאה: שני פולינומים ממעלה 1 לפחות {% equation %}b\left(x\right),c\left(x\right){% endequation %} כך ש-{% equation %}b\left(x\right)c\left(x\right)=x^{n}{% endequation %}. אכתוב אותם במפורש:

{% equation %}b\left(x\right)=b_{m}x^{m}+\dots+b_{1}x+b_{0}{% endequation %}

{% equation %}c\left(x\right)=c_{k}x^{k}+\dots+c_{1}x+c_{0}{% endequation %}

כאשר {% equation %}m,k&lt;n{% endequation %} ו-{% equation %}m+k=n{% endequation %}. מכך ש-{% equation %}b\left(x\right)c\left(x\right)=x^{n}{% endequation %} אני מקבל {% equation %}n+1{% endequation %} משוואות שמתארות את הקונבולוציה של המקדמים של {% equation %}b\left(x\right),c\left(x\right){% endequation %}:

{% equation %}b_{0}c_{0}=0{% endequation %}

{% equation %}b_{0}c_{1}+b_{1}c_{0}=0{% endequation %}

{% equation %}\vdots{% endequation %}

{% equation %}b_{m-1}c_{k}+b_{m}c_{k-1}=0{% endequation %}

{% equation %}b_{m}c_{k}=1{% endequation %}

בואו נתחיל מהמשוואה הראשונה, {% equation %}b_{0}c_{0}=0{% endequation %}. אנחנו בתחום שלמות {% equation %}R/P{% endequation %} ולכן או {% equation %}b_{0}{% endequation %} או {% equation %}c_{0}{% endequation %} הם 0; נניח בלי הגבלת הכלליות ש-{% equation %}b_{0}=0{% endequation %}. עכשיו נכנס לפעולה הנתון לפיו {% equation %}a_{0}\notin P^{2}{% endequation %}; אם ב-{% equation %}R/P{% endequation %} היה מתקיים ש-{% equation %}b_{0}=c_{0}=0{% endequation %} זה היה אומר שבחוג {% equation %}R{% endequation %} מתקיים {% equation %}b_{0}\in P{% endequation %} <strong>וגם</strong> {% equation %}c_{0}\in P{% endequation %} ולכן {% equation %}a_{0}=b_{0}c_{0}\in P^{2}{% endequation %}. זה בלתי אפשרי, ולכן בחוג {% equation %}R/P{% endequation %} מתקיים {% equation %}c_{0}\ne0{% endequation %}. אני טוען שאי השוויון הקטן הזה יגרום לתגובת שרשרת בקרב כל משוואות הקונבולוציה שלעיל שתכריח את כל המקדמים של {% equation %}b\left(x\right){% endequation %} להיות אפס, עד אשר נקבל סתירה במשוואה האחרונה, {% equation %}b_{m}c_{k}=1{% endequation %}.

ראינו כבר ש-{% equation %}b_{0}=0{% endequation %}. זה הופך את המשוואה השניה ל-{% equation %}b_{1}c_{0}=0{% endequation %}, ומכיוון ש-{% equation %}c_{0}\ne0{% endequation %} אז {% equation %}b_{1}=0{% endequation %}. עכשיו המשוואה השלישית, שלא כתבתי, תהפוך ל-{% equation %}b_{2}c_{0}=0{% endequation %}, וכן הלאה וכן הלאה. מתישהו נגיע אל {% equation %}b_{m}c_{0}=0{% endequation %} (במשוואה של המקדם {% equation %}x^{m}{% endequation %}, שהוא {% equation %}\sum_{i=0}^{m}b_{i}c_{m-i}=0{% endequation %} כי {% equation %}m&lt;n{% endequation %}) ונסיק ש-{% equation %}b_{m}=0{% endequation %}; אבל עכשיו המשוואה {% equation %}b_{m}c_{k}=1{% endequation %} לא יכולה להתקיים, והגענו לסתירה עם ההנחה ש-{% equation %}a\left(x\right){% endequation %} היה פריק.

זה מסיים את ההוכחה של קריטריון אייזנשטיין וגם את הפוסט; כמובן שזה לא סוף הסיפור של הפולינומים אלא בקושי ההתחלה.

