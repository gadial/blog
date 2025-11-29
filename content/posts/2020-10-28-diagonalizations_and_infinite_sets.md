---
title: "תורת הקבוצות - לכסונים, או למה יש אינסוף אינסופים?"
layout: post
categories:
  - תורת הקבוצות
tags:
  - קבוצה סופית
  - קבוצה אינסופית
---


<h2>אז איך משווים קבוצות אינסופיות?</h2>

<a href="https://gadial.net/2020/10/09/what_are_infinite_sets/">בפוסט הקודם</a> בסדרת הפוסטים שלי על תורת הקבוצות הצגתי את הכלי הבסיסי שלנו להשוואת גדלים של קבוצות: אמרתי שאם קיימת פונקציה {% equation %}f:A\to B{% endequation %} שהיא חד-חד-ערכית ועל אז אנחנו אומרים ש-{% equation %}A,B{% endequation %} הן <strong>שוות עוצמה</strong> ומסמנים את זה ב-{% equation %}A\sim B{% endequation %} או ב-{% equation %}\left|A\right|=\left|B\right|{% endequation %}. הגדרתי "קבוצה סופית" בתור קבוצה שמקיימת {% equation %}A\sim n{% endequation %} עבור מספר טבעי {% equation %}n{% endequation %} כלשהו (זכרו: {% equation %}n{% endequation %}, פורמלית, הוא קבוצת הטבעיים הקטנים מ-{% equation %}n{% endequation %}) והגדרתי "קבוצה אינסופית" בתור קבוצה לא סופית. סיימנו בלראות שלכל קבוצה אינסופית {% equation %}A{% endequation %}, קיימת פונקציה {% equation %}f:\mathbb{N}\to A{% endequation %} שהיא חד-חד-ערכית אבל לא בהכרח על ואמרתי שאינטואיטיבית, זה אומר ש-{% equation %}A{% endequation %} גדולה לפחות כמו {% equation %}\mathbb{N}{% endequation %}. בואו נתחיל מלפרמל את האינטואיציה הזו.

כרגיל, שווה להתחיל מהמקרה הקונקרטי של קבוצות סופיות. אם {% equation %}A,B{% endequation %} סופיות ויש {% equation %}f:A\to B{% endequation %} שהיא חח"ע אבל <strong>לא על</strong> אז אפשר להוכיח ש-{% equation %}\left|A\right|<\left|B\right|{% endequation %}. עבור קבוצות אינסופיות זה פחות פשוט. למשל, הפונקציה {% equation %}f:\mathbb{N}^{+}\to\mathbb{N}{% endequation %} שמוגדרת בתור {% equation %}f\left(n\right)=n{% endequation %} היא חח"ע אבל <strong>לא על</strong> כי {% equation %}0{% endequation %} לא שייך ל-{% equation %}\mathbb{N}^{+}{% endequation %} אבל כן שייך ל-{% equation %}\mathbb{N}{% endequation %}. מצד שני, זה שהפונקציה הספציפית הזו היא לא על לא אומר שאי אפשר למצוא פונקציה <strong>אחרת</strong> שהיא כן: במקרה שלנו, {% equation %}g\left(n\right)=n-1{% endequation %} היא חח"ע ועל ולכן מוכיחה ש-{% equation %}\left|\mathbb{N}^{+}\right|=\left|\mathbb{N}\right|{% endequation %}. בקבוצות סופיות זה פשוט לא היה יכול לקרות, שיש לנו פונקציה חח"ע ולא על אבל אפשר למצוא אחת שהיא כן חח"ע ועל.

לכן אנחנו נוקטים בהגדרה הבאה: אם {% equation %}A,B{% endequation %} קבוצות כך ש-{% equation %}f:A\to B{% endequation %} היא פונקציה חח"ע (ולאו דווקא על; לא אוסרים עליה להיות על) אז מסמנים זאת {% equation %}\left|A\right|\le\left|B\right|{% endequation %}. שימוש בסימון כזה בחופשיות הוא מסוכן, כי האינטואיציה שלנו מאי-שוויונים "רגילים" היא שצריך להתקיים הדבר הבא: אם {% equation %}\left|A\right|\le\left|B\right|{% endequation %} וגם {% equation %}\left|B\right|\le\left|A\right|{% endequation %} אז צריך להתקיים {% equation %}\left|A\right|=\left|B\right|{% endequation %}. למרבה המזל, הטענה הזו <strong>נכונה</strong>: היא נקראת "משפט קנטור-שרדר-ברנשטיין". הנה עוד ניסוח שלה, קצת יותר מפורש:

משפט קנטור-שרדר-ברנשטיין: אם קיימת פונקציה {% equation %}f:A\to B{% endequation %} חח"ע ופונקציה {% equation %}g:B\to A{% endequation %} חח"ע אז קיימת פונקציה {% equation %}h:A\to B{% endequation %} חח"ע ועל.

אנחנו יכולים להוכיח את המשפט כאן, עם הידע שכבר יש לנו; הוא לא דורש משהו עמוק אלא בעיקר הגדרה מחוכמת למדי של {% equation %}h{% endequation %}. אני לא אעשה את זה כי כבר הוכחתי את המשפט <strong>פעמיים</strong> בבלוג, בצורה <a href="https://gadial.net/2012/01/21/cantor_schroeder-_bernstein_theorem/">יבשה יותר</a> ובצורה <a href="https://gadial.net/2016/11/30/csb_theorem_hilbert_hotel_style/">יבשה פחות</a>. אפשר לדלג על ההוכחה כרגע בכל מקרה - המשפט עצמו שימושי לנו אבל לא קריטי להבין כרגע למה הוא עובד.

עכשיו, משיש לנו מושג של "קטן-שווה" עבור קבוצות אינסופיות, זמן לשאול האם יש לנו גם מושג של "קטן ממש". כלומר, האם קיימות {% equation %}A,B{% endequation %} כך שיש פונקציה {% equation %}f:A\to B{% endequation %} שהיא חח"ע אבל לא על, ופשוט <strong>לא קיימת</strong> פונקציה חח"ע ועל מ-{% equation %}A{% endequation %} אל {% equation %}B{% endequation %}. כלומר, שמתקיים {% equation %}\left|A\right|\le\left|B\right|{% endequation %} אבל {% equation %}\left|A\right|\ne\left|B\right|{% endequation %}. דבר כזה יסומן בתור {% equation %}\left|A\right|<\left|B\right|{% endequation %}. כאן האינטואיציה הראשונית יכולה להיות שברור שזה קיים כי למשל {% equation %}\mathbb{N}^{+}{% endequation %} היא כמו {% equation %}\mathbb{N}{% endequation %} רק בלי המספר 0 ולכן {% equation %}\mathbb{N}^{+}{% endequation %} היא "קטנה יותר", אבל כאמור - יש לנו פונקציה חח"ע ועל ביניהן, אז הן מאותו גודל. הבלבול שהדבר הזה גורם התבטא בפרדוקס של גלילאו, עם קבוצת הטבעיים וקבוצת הריבועים של טבעיים, שגם הן באותו גודל למרות שהתחושה היא שבקבוצת הריבועים יש "הרבה פחות" - הבלבול הזה גרם לגלילאו למשוך את ידיו מכל העיסוק בקבוצות אינסופיות.

אם כן, אולי האינטואיציה צריכה להיות ש<strong>לא</strong> קיים דבר כזה, שתי קבוצות אינסופיות שאינן מאותו גודל? אולי בעצם כל הקבוצות האינסופיות הן מאותו "גודל", לא? {% equation %}\infty{% endequation %} או משהו כזה? וכאן באה תורת הקבוצות של גאורג קנטור, שהוא זה שהחליט להשוות קבוצות באמצעות פונקציות חח"ע ועל, ומספרת לנו שלא - העולם הרבה יותר גדול ומורכב מהפשטנות הזו של "אינסוף זה אינסוף וזהו".

<h2>האלכסון של קנטור</h2>

הדוגמא הראשונה לשתי קבוצות אינסופיות שהאחת גדולה מהשניה ניתנת באמצעות טיעון שנקרא "האלכסון של קנטור" וכבר <a href="https://gadial.net/2007/08/29/cantor_diagonal/">כתבתי עליו פוסט</a> בראשית ימי הבלוג, אבל הנה הזדמנות טובה להציג אותו שוב. הרעיון הוא להראות שעוצמת המספרים הטבעיים קטנה מעוצמת המספרים הממשיים: {% equation %}\left|\mathbb{N}\right|<\left|\mathbb{R}\right|{% endequation %}. ברור ש-{% equation %}\left|\mathbb{N}\right|\le\left|\mathbb{R}\right|{% endequation %} כי הפונקציה {% equation %}f\left(n\right){% endequation %} מ-{% equation %}\mathbb{N}{% endequation %} אל {% equation %}\mathbb{R}{% endequation %} היא חח"ע; רק נשאר להוכיח שפשוט <strong>לא קיימת</strong> פונקציה חח"ע ועל מ-{% equation %}\mathbb{N}{% endequation %} אל {% equation %}\mathbb{R}{% endequation %}.

כדי לפשט את הנימוק מספיק להראות שלא קיימת פונקציה חח"ע ועל מ-{% equation %}\mathbb{N}{% endequation %} אל הקטע הפתוח {% equation %}\left(0,1\right){% endequation %} של כל המספרים הממשיים בין 0 ו-1, כי לא כזה קשה להראות (לא הפעם!) ש-{% equation %}\left(0,1\right)\sim\mathbb{R}{% endequation %}, אז אם היה מתקיים {% equation %}\mathbb{N}\sim\mathbb{R}{% endequation %} היה נובע מכך ש-{% equation %}\mathbb{N}\sim\left(0,1\right){% endequation %}. כרגע עדיין לא ברור איך לדבר על {% equation %}\left(0,1\right){% endequation %} מפשט משהו, אבל זה יגיע בקרוב - בינתיים השאלה הדוחקת יותר היא איך בכלל מרים משהו בסגנון "לא קיימת פונקציה חח"ע ועל מ-{% equation %}\mathbb{N}{% endequation %} לאנשהו". זה בעצם האתגר הגדול של המתמטיקה באופן כללי: אם משהו <strong>קיים</strong>, אז לעתים קרובות אפשר פשוט להציג אותו וזהו (זה לא תמיד המצב, כפי שמלמדת אותנו <strong>אקסיומת הבחירה</strong>, אבל זה לפעם אחרת). אבל אם משהו <strong>לא קיים</strong>, איך נראה את זה? לכאורה אנחנו צריכים לעבור על <strong>כל</strong> הפונקציות האפשריות ביקום בין {% equation %}\mathbb{N}{% endequation %} ו-{% equation %}\left(0,1\right){% endequation %} ולהראות שאף אחת מהן היא לא חח"ע ועל. איך נעשה את זה? מאיפה נתחיל? זו נראית כמו משימה מפלצתית! וזה גם <strong>בדיוק</strong> מה שנעשה, וזה לא ייקח לנו יותר מכמה שורות ספורות (אם ממש רוצים, אפשר לקצר את ההוכחה לשורה אחת).

הרעיון הוא לקחת פונקציה {% equation %}f:\mathbb{N}\to\left(0,1\right){% endequation %} <strong>כלשהי</strong>, בלי להניח עליה שום הנחות, ולהוכיח שהיא לא יכולה להיות <strong>על</strong>. אמרתי לפני רגע שאם משהו <strong>קיים</strong> אז אפשר להציג אותו וזהו? זה מה שנעשה! אנחנו הולכים להציג מספר ב-{% equation %}\left(0,1\right){% endequation %} שלא שייך לתמונה של {% equation %}f{% endequation %} - כלומר, שאין {% equation %}n\in\mathbb{N}{% endequation %} כך ש-{% equation %}f\left(n\right){% endequation %} שווה אליו, ונעשה זאת על ידי כך שנבנה אותו בצורה מפורשת, כמובן בעזרת {% equation %}f{% endequation %} עצמה.

כדי להבין את הרעיון של הבניה, בואו נדגים אותה עבור {% equation %}f{% endequation %} ספציפית אחת - אבל לא כזו שנראית "נחמדה" אלא כזו שנראית כמו בוקה ומבולקה. אכתוב אותה חצי במפורש כך: 

{% equation %}\begin{array}{ccccccccc} f\left(0\right) & = & 0 & . & 3 & 5 & 8 & 1 & \ldots\\ f\left(1\right) & = & 0 & . & 4 & 4 & 4 & 4 & \ldots\\ f\left(2\right) & = & 0 & . & 5 & 8 & 7 & 6 & \ldots\\ f\left(3\right) & = & 0 & . & 4 & 3 & 4 & 3 & \ldots\\  & \vdots \end{array}{% endequation %}

הרעיון בצורת הכתיבה הוא זה: לכל מספר טבעי {% equation %}n{% endequation %}, הפלט {% equation %}f\left(n\right){% endequation %} של הפונקציה {% equation %}f:\mathbb{N}\to\left(0,1\right){% endequation %} הוא איבר של {% equation %}\left(0,1\right){% endequation %}. מספר כזה הוא מספר ממשי בין 0 ל-1, וככזה אפשר להציג אותו בעזרת <strong>ייצוג עשרוני</strong> שהוא מהצורה "משהו <strong>נקודה</strong> משהו משהו משהו". מכיוון שהמספר הוא בין 0 ל-1, לא כולל 1, מה שיש משמאל לנקודה הוא תמיד 0; נשאר לנו האקשן שמתרחש מימין לנקודה, שאני כותב כמו מין מערך של ספרות. {% equation %}f\left(0\right)=0.3581\ldots{% endequation %}, כאשר שלוש הנקודות אומרות "ומכאן והלאה זה נמשך עד אינסוף בדרך כלשהי". שימו לב שגם במספר כמו {% equation %}0.5{% endequation %} שלכאורה יש לו רק מספר סופי של ספרות אחרי הנקודה העשרונית, בעצם יש אינסוף כי גם 0 היא ספרה: {% equation %}0.5=0.5000\ldots{% endequation %}. אחרי ארבעת האיברים שכתבתי במפורש הוספתי שלוש נקודות אנכיות שרומזות שמה שהולך פה נמשך בצורה דומה עם הפעלה של {% equation %}f{% endequation %} על כל הטבעיים.

עכשיו אני רוצה לבנות מספר {% equation %}d{% endequation %} שיהיה בעל שתי תכונות:

<ol> <li>{% equation %}d\in\left(0,1\right){% endequation %}, כלומר {% equation %}d{% endequation %} שייך לקטע ש-{% equation %}f{% endequation %} <strong>אמורה לתפוס במלואו</strong>.</li>


<li>{% equation %}f{% endequation %} <strong>לא תופסת</strong> את {% equation %}d{% endequation %}. כלומר, לכל {% equation %}n\in\mathbb{N}{% endequation %}, מתקיים {% equation %}f\left(n\right)\ne d{% endequation %}.</li>

</ol>

האופן שבו אעשה את זה יהיה לבנות את {% equation %}d{% endequation %} <strong>ספרה-ספרה</strong>. יש לי אינסוף ספרות לבחור, ואני "אנצל" כל ספרה שאבחר עבור {% equation %}d{% endequation %} כדי "לנטרל" את האפשרות של אחד מהמספרים הטבעיים לתפוס את {% equation %}d{% endequation %}. הספרה הראשונה של {% equation %}d{% endequation %} תיבחר בצורה כזו שמבטיחה ש-{% equation %}f\left(0\right)\ne d{% endequation %}, הספרה השניה של {% equation %}d{% endequation %} תיבחר בצורה כזו שמבטיח ש-{% equation %}f\left(1\right)\ne d{% endequation %} וכן הלאה.

מכיוון ש-{% equation %}d\in\left(0,1\right){% endequation %} הוא מתחיל תמיד ב-{% equation %}0.{% endequation %} ואז הספרות שמימין לנקודה העשרונית, שהן מה שאני בוחר. עכשיו, {% equation %}f\left(0\right){% endequation %} מתחיל עם הספרה 3, אז אני אתחיל לבנות את {% equation %}d{% endequation %} עם הספרה {% equation %}4{% endequation %}. כלומר, כרגע המצב הוא זה: {% equation %}d=0.4\ldots{% endequation %}, כששלוש הנקודות אומרות "עדיין לא החלטתי מה יהיה שם". כבר במצב הזה אנחנו <strong>יודעים בודאות</strong> ש-{% equation %}f\left(0\right)\ne d{% endequation %}, פשוט כי הם נבדלים בספרה הראשונה, ושני מספרים ממשיים הם זהים רק אם יש להם את אותו פיתוח עשרוני (עד כדי מקרה קצה אחד שאתייחס אליו בפירוט בהמשך).

נעבור ל-{% equation %}f\left(1\right){% endequation %}. הוא מתחיל גם ב-{% equation %}0.4{% endequation %}, אז עדיין <strong>ייתכן בתיאוריה</strong> ש-{% equation %}d=0.4\ldots{% endequation %} יהיה שווה אליו. אבל יש לנו חופש בחירה - עוד לא בחרנו את הספרה <strong>השניה</strong> של {% equation %}d{% endequation %}. אז פשוט נבחר אותה להיות משהו שונה מ-4, נאמר 3. קיבלנו את {% equation %}d=0.43\ldots{% endequation %} שבבירור שונה מ-{% equation %}f\left(1\right)=0.44\ldots{% endequation %}.

עבור {% equation %}f\left(2\right){% endequation %} נראה שאין מה לעשות - הוא מתחיל ב-{% equation %}0.58\ldots{% endequation %} ששונה מאוד מ-{% equation %}d=0.43\ldots{% endequation %}, אבל למה לסבך את שיטת העבודה שלי? שיטת העבודה כרגע אומרת - תבחר את הספרה הבאה שלך (במקרה שלנו, הספרה השלישית ב-{% equation %}d{% endequation %}) כך שהיא שונה מהספרה באותו מקום במספר הנוכחי שאתה "תוקף". במקרה הזה הספרה היא 7, אז נבחר... אה... 4? ונקבל {% equation %}d=0.434\ldots{% endequation %}. אחר כך נעבור לספרה <strong>הרביעית</strong> ב-{% equation %}f\left(3\right){% endequation %} שהיא 3 ושוב נבחר 4, ונקבל {% equation %}d=0.4344\ldots{% endequation %} וכך זה יימשך עוד ועוד.

יש לנו אינסוף צעדים, ובכל צעד נפסל אחד מהמספרים הטבעיים {% equation %}n{% endequation %} מלקיים {% equation %}f\left(n\right)=d{% endequation %}. מכיוון שזה קורה <strong>לכל</strong> הטבעיים, תכונה 2 שרצינו עבור {% equation %}d{% endequation %} מתקיימת. זה מוכיח שה-{% equation %}f{% endequation %} שהצגתי לא תופסת את כל הקטע {% equation %}\left(0,1\right){% endequation %} ומסיים את הסיפור מבחינה. אבל מה עם פונקציות אחרות?

ובכן, לא הצגתי את {% equation %}f{% endequation %} יותר מדי לעומק, נכון? הצגתי רק כמה איברים ראשונים וזהו. אחרי ש"הבנו את הקטע" היה אפשר להמשיך בצורה דומה גם לאיבר שלא ראינו. אז את אותו טיעון אפשר להחיל על כל {% equation %}f{% endequation %} שהיא. בואו ננסח עכשיו את הטיעון הפורמלי, שרק ידרוש מאיתנו עוד כמה סימונים קונקרטיים. אני אקח {% equation %}f:\mathbb{N}\to\left(0,1\right){% endequation %} כללית ואסמן את איבריה באופן הבא:

{% equation %}\begin{array}{ccccccccc} f\left(0\right) & =a_{0}= & 0 & . & a_{0}^{0} & a_{0}^{1} & a_{0}^{2} & a_{0}^{3} & \ldots\\ f\left(1\right) & =a_{1}= & 0 & . & a_{1}^{0} & a_{1}^{1} & a_{1}^{2} & a_{1}^{3} & \ldots\\ f\left(2\right) & =a_{2}= & 0 & . & a_{2}^{0} & a_{2}^{1} & a_{2}^{2} & a_{2}^{3} & \ldots\\ f\left(3\right) & =a_{3}= & 0 & . & a_{3}^{0} & a_{3}^{1} & a_{3}^{2} & a_{3}^{3} & \ldots\\  & \vdots \end{array}{% endequation %}

באופן כללי: אני קורא ל-{% equation %}f\left(n\right){% endequation %} בשם {% equation %}a_{n}=f\left(n\right){% endequation %}, ואז כותב את {% equation %}a_{n}{% endequation %} בתור סדרה של ספרות אחרי הנקודה העשרונית: {% equation %}a_{n}=0.a_{n}^{0}a_{n}^{1}\dots{% endequation %}. לספרה הראשונה אחרי הנקודה העשרונית אני קורא {% equation %}a_{n}^{0}{% endequation %}, לספרה השניה אני קורא {% equation %}a_{n}^{1}{% endequation %} וכן הלאה. זה מאפשר לי להתייחס לכל תא ב"טבלה" שלעיל בצורה מפורשת.

ועכשיו אני בונה את {% equation %}d=0.d^{0}d^{1}d^{2}\ldots{% endequation %} שלי בצורה הפשוטה הבאה:

{% equation %}d^{n}=\begin{cases} 4 & a_{n}^{n}\ne4\\ 3 & a_{n}^{n}=4 \end{cases}{% endequation %}

במילים אחרות, אני אומר - כדי להחליט מה תהיה הספרה ה-{% equation %}n{% endequation %}-ית בתוך {% equation %}d{% endequation %}, אני מסתכל מה הספרה ה-{% equation %}n{% endequation %}-ית במספר {% equation %}a_{n}{% endequation %}. אם הספרה הזו ב-{% equation %}a_{n}{% endequation %} <strong>שונה</strong> מ-4, אז אני אבחר אותה ב-{% equation %}d{% endequation %} להיות 4. אם היא דווקא הייתה שווה ל-4, אני אבחר אותה להיות 3, כדי שתהיה שונה מ-4. סוף הסיפור: לכל {% equation %}n\in\mathbb{N}{% endequation %}, {% equation %}d\ne f\left(n\right){% endequation %} כי הן נבדלות בספרה ה-{% equation %}n{% endequation %}-ית.

אם נסתכל שוב על הטבלה שלמעלה, אפשר לראות שהאופן שבו אני בונה את {% equation %}d{% endequation %} הוא על ידי כך שאני לוקח את <strong>האלכסון</strong> של הטבלה (שבו נמצאים {% equation %}a_{0}^{0},a_{1}^{1},a_{2}^{2}{% endequation %} וכן הלאה) וסוג של "הופך" אותו. לכן השיטה הזו נקראת <strong>האלכסון של קנטור</strong>, אבל אני משתדל לא לשים יותר מדי דגש על האספקט הויזואלי הזה שלה, כי הנסיון שלי הוא שזה מקשה על הבנה של שלל ההכללות האפשריות של השיטה, שברובן כבר אין ציור נחמד של אלכסון שאפשר להשתמש בו.

אני רוצה לעזוב עכשיו את הדוגמא הזו ולעבור לדבר על תוצאה כללית יותר, אבל לפני כן יש לי חוב של איזו נקודה עדינה להתייחס אליה שהיא <strong>מאוד</strong> ספציפית לפרטים של ההוכחה הזו. אם מה שאני מדבר עליו פה לא ברור אפשר פשוט לדלג להמשך.

ובכן, הבעיה הבסיסית שלא התייחסתי אליה עדיין היא ש-{% equation %}0.999\ldots=1{% endequation %}.

השוויון הזה נראה שגוי? ובכן, יש לי <a href="https://gadial.net/2008/06/07/almost_1_is_one/">פוסט</a> בנושא, גם כן מראשית ימי הבלוג. השוויון נכון לגמרי (לא "בקירוב" או "בשאיפה"), ולא רק הוא: <strong>כל</strong> מספר עשרוני שמסתיים בסדרה אינסופית של 9 ניתן בעצם לכתיבה בשתי דרכים שונות. למשל, {% equation %}0.4999\ldots=0.5000\ldots{% endequation %}. הבשורות הטובות הן שזה היוצא מן הכלל היחיד - כל מספר ממשי שלא מסתיים בסדרה אינסופית של 0 או 9 ניתן לכתיבה רק בדרך אחת.

למה זה לא יוצר בעיות? ראשית, שימו לב שהמספר שאני בונה כולל רק את הספרות 3 ו-4, כך שזה לא יכול לקרות לו - יש לו ייצוג יחיד. לכן בפרט לא ייתכן שאני אבנה "בטעות" את {% equation %}0.999\ldots{% endequation %} ולכן אבנה בפועל מספר שלא שייך ל-{% equation %}\left(0,1\right){% endequation %}. שנית, בהחלט <strong>ייתכן</strong> שהשטיק הזה של ה-{% equation %}999{% endequation %} יקלקל לי את טיעון ה"שונה בספרה אחת". למשל, אם בניתי עד כה את {% equation %}d=0.44\dots{% endequation %} והמספר הבא שאני תוקף הוא {% equation %}0.443999\ldots{% endequation %}, אז אני אוסיף ל-{% equation %}d{% endequation %} את הספרה {% equation %}4{% endequation %} ואקבל {% equation %}d=0.444\ldots{% endequation %} ש<strong>אינו</strong> שונה מ-{% equation %}0.443999\ldots{% endequation %} בספרה השלישית. כל הטיעון שלי קורס! אבל, למרות ש-{% equation %}d{% endequation %} לא שונה מהמספר הזה בספרה <strong>השלישית</strong>, הוא בהכרח שונה ממנו <strong>בכל יתר הספרות</strong> כי יתר הספרות במספר ההוא הן 9, ואילו אצלי הן 3 ו-4. או במילים פשוטות יותר: מכיוון ש-{% equation %}d{% endequation %} נבנה בצורה כזו שהוא בעל ייצוג יחיד, הוא אוטומטית שונה מכל המספרים <strong>שאינם בעלי ייצוג יחיד</strong>, ונשאר רק לבחון אם הוא שונה מהמספרים שהם כן בעלי ייצוג יחיד.

אז עם זה סיימנו את האלכסון של קנטור, אבל בעצם זו רק נקודת הפתיחה שלנו למשהו מגניב עוד יותר.

<h2>משפט קנטור על קבוצת החזקה</h2>

מה שראינו באלכסון של קנטור הוא שיש לפחות <strong>שני</strong> גדלים שונים של אינסוף: זה של {% equation %}\mathbb{N}{% endequation %} וזה של {% equation %}\mathbb{R}{% endequation %}. עכשיו, במחי הוכחה שהיא אפילו עוד יותר קצרה, אני אוכל להראות שיש <strong>אינסוף</strong> גדלים שונים של אינסוף. הנה הטענה: אם {% equation %}A{% endequation %} היא קבוצה <strong>כלשהי</strong> (סופית, לא סופית, לא משנה מה), אז {% equation %}\left|A\right|<\left|\mathcal{P}\left(A\right)\right|{% endequation %} כאשר כאן {% equation %}\mathcal{P}\left(A\right)\triangleq\left\{ B\ |\ B\subseteq A\right\} {% endequation %} היא <strong>קבוצת החזקה</strong> של {% equation %}A{% endequation %} - אוסף כל תתי-הקבוצות של {% equation %}A{% endequation %}. עבור קבוצות סופיות אנחנו יודעים שזה נכון כי יש לנו את השוויון {% equation %}\left|\mathcal{P}\left(A\right)\right|=2^{\left|A\right|}{% endequation %} וכמובן ש-{% equation %}n<2^{n}{% endequation %} לכל מספר טבעי, כולל 0. אבל מה קורה עם קבוצות אינסופיות?

ראשית, צריך להוכיח ש-{% equation %}\left|A\right|\le\left|\mathcal{P}\left(A\right)\right|{% endequation %} כלומר שיש פונקציה חח"ע מ-{% equation %}A{% endequation %} אל {% equation %}\mathcal{P}\left(A\right){% endequation %}. את זה קל לעשות: הפונקציה {% equation %}f\left(a\right)=\left\{ a\right\} {% endequation %} עובדת. לכן כל מה שנשאר לעשות הוא להוכיח ש-{% equation %}\left|A\right|\ne\left|\mathcal{P}\left(A\right)\right|{% endequation %} ואת זה הוכיח קנטור באמצעות טיעון שמאוד מזכיר את טיעון האלכסון שלו, אבל יש מצב שבמבט ראשון ייראה לא קשור בעליל.

ובכן, קנטור אומר את הדבר הבא: בואו ניקח פונקציה {% equation %}f:A\to\mathcal{P}\left(A\right){% endequation %} <strong>כלשהי</strong>, ונוכיח כי {% equation %}f{% endequation %} אינה יכולה להיות על. כלומר, אנחנו רוצים לבנות איבר {% equation %}D\in\mathcal{P}\left(A\right){% endequation %} כך ש-{% equation %}f\left(a\right)\ne D{% endequation %} לכל {% equation %}a\in A{% endequation %}. כיצד נעשה זאת? נגדיר את {% equation %}D{% endequation %} בצורה קצת מחוכמת שמתבססת על {% equation %}f{% endequation %}: {% equation %}D\triangleq\left\{ a\in A\ |\ a\notin f\left(a\right)\right\} {% endequation %}. כלומר, {% equation %}D{% endequation %} כוללת את כל אברי {% equation %}A{% endequation %} שאינם שייכים לקבוצה שמתקבלת מההפעלה של {% equation %}f{% endequation %} עליהם - האיברים שאינם שייכים <strong>לתמונה</strong> שלהם.

עכשיו, אומר קנטור, בואו נניח בשלילה לרגע שיש {% equation %}d\in A{% endequation %} כך ש-{% equation %}f\left(d\right)=D{% endequation %}. מה קורה כעת? יש שתי אפשרויות:

<ol> <li>אם {% equation %}d\in D{% endequation %} אז על פי הגדרת {% equation %}D{% endequation %}, האיבר {% equation %}d{% endequation %} צריך לקיים את קריטריון השייכות ל-{% equation %}D{% endequation %}, כלומר לקיים {% equation %}d\notin f\left(d\right){% endequation %}. אבל {% equation %}f\left(d\right)=D{% endequation %}, כלומר קיבלנו {% equation %}d\notin D{% endequation %} בסתירה לנקודת המוצא שלנו.</li>


<li>אם לעומת זאת {% equation %}d\notin D{% endequation %} אז מכיוון ש-{% equation %}D=f\left(d\right){% endequation %} קיבלנו ש-{% equation %}d\notin f\left(d\right){% endequation %}. זה אומר ש-{% equation %}d{% endequation %} מקיימת את הקריטריון שמגדיר את {% equation %}D{% endequation %}, ולכן {% equation %}d\in D{% endequation %} - שוב, בסתירה לנקודת המוצא שלנו.</li>

</ol>

מכיוון שבשני המקרים הגענו לסתירה, המסקנה היא שההנחה שלנו שבכלל קיימת {% equation %}d\in A{% endequation %} כך ש-{% equation %}f\left(d\right)=D{% endequation %} אינה נכונה, מה שמסיים את ההוכחה: הראינו ש-{% equation %}D{% endequation %} לא שייכת לתמונה של {% equation %}f{% endequation %} ולכן {% equation %}f{% endequation %} אינה על, ומכיוון ש-{% equation %}f{% endequation %} הייתה פונקציה כלשהי, המסקנה היא שלא קיימת פונקציה חח"ע ועל מ-{% equation %}A{% endequation %} אל {% equation %}\mathcal{P}\left(A\right){% endequation %}.

יש <strong>המון</strong> שאלות שאני מרגיש שצצות בעקבות ההוכחה הזו. מעבר ל"מה לכל הרוחות" שהרגשתי בפעם הראשונה שראיתי אותה, הנה שאלות קונקרטיות יותר:

<ol> <li>למה זה מזכיר לנו בצורה חשודה את הפרדוקס של ראסל?</li>


<li>איך זה בכלל קשור לאלכסון של קנטור?</li>


<li>רגע, כמה אינסופים בכלל יש?</li>

</ol>

בואו נתחיל מ-3. משפט קנטור נותן לנו שיטה לבנות סדרה אינסופית של אינסופים: {% equation %}\left|\mathbb{N}\right|<\left|\mathcal{P}\left(\mathbb{N}\right)\right|<\left|\mathcal{P}\left(\mathcal{P}\left(\mathbb{N}\right)\right)\right|<\ldots{% endequation %}. יש בתורת הקבוצות סימון פורמלי לגדלים הללו: {% equation %}\left|\mathbb{N}\right|=\beth_{0}{% endequation %} (כן, זו האות העברית ב', בפונט מתמטי מוזר) ו-{% equation %}\left|\mathcal{P}\left(\mathbb{N}\right)\right|=\beth_{1}{% endequation %} ו-{% equation %}\left|\mathcal{P}\left(\mathcal{P}\left(\mathbb{N}\right)\right)\right|=\beth_{2}{% endequation %} וכן הלאה: קיבלנו סדרה אינסופית. מכיוון שיש לנו התאמה חח"ע ועל בין {% equation %}\mathbb{N}{% endequation %} ובין קבוצת הבתים הזו, הראינו שיש אינסוף "קטן" של קבוצות אינסופיות. אבל בפועל <strong>זו מראית עין מטעה</strong> כי יש <strong>הרבה יותר</strong> קבוצות אינסופיות שעדיין לא דיברתי עליהן ולא ברור לנו איך אפשר "לבנות" בכלל. פורמלית האינסוף של "אוסף כל האינסופים" הולך להיות <strong>כל כך גדול</strong> שאוסף כל האינסופים הזה לא יוכל להיות קבוצה. אבל על זה אי אפשר לדבר פורמלית כרגע אז נעזוב את זה.

שנית, זה מזכיר בצורה חשודה את הפרדוקס של ראסל כי <strong>ככה ראסל גילה את הפרדוקס של ראסל</strong> - על ידי זה שהוא קרא את ההוכחה של קנטור וניסה לשחק איתה. אבל בניגוד לפרדוקס של ראסל, ההוכחה של קנטור לא יוצרת פרדוקס במתמטיקה כי הקבוצה {% equation %}D\triangleq\left\{ a\in A\ |\ a\notin f\left(a\right)\right\} {% endequation %} הוגדרה בצורה תקינה פורמלית, על ידי לקיחת קבוצה קיימת {% equation %}A{% endequation %} וגזירת תת-קבוצה שלה באמצעות קריטריון קונקרטי כלשהו.

לבסוף, איך זה קשור לאלכסון של קנטור? כאן לא היו לנו מספרים ממשיים, או אלכסון, או שום דבר. אבל אני רוצה שנשתכנע שזו בעצם אותה הוכחה בדיוק על ידי כך שנזהה את "רוח" ההוכחה - מה שמשתמשים בו תמיד גם בטיעוני לכסון מתוחכמים הרבה יותר.

<h2>מה זה בעצם לכסון?</h2>

ובכן, בואו ננסה להציג טיעון "לכסון" בצורה כללית ונראה איך הוא בא לידי ביטוי בשתי ההוכחות הללו. בטיעון "לכסון" יש לנו שתי קבוצות, {% equation %}A\subseteq B{% endequation %} ואנחנו רוצים להוכיח ש-{% equation %}A\ne B{% endequation %} על ידי בניה של איבר של {% equation %}B{% endequation %} שאינו שייך ל-{% equation %}A{% endequation %}.

בהוכחה של האלכסון של קנטור, {% equation %}A{% endequation %} הייתה {% equation %}f\left(\mathbb{N}\right){% endequation %} - קבוצת כל המספרים שסימנתי בתור {% equation %}\left\{ a_{0},a_{1},a_{2},\ldots\right\} {% endequation %} ו-{% equation %}B{% endequation %} הייתה {% equation %}\left(0,1\right){% endequation %}.

בהוכחה של המשפט {% equation %}\left|X\right|<\left|\mathcal{P}\left(X\right)\right|{% endequation %} (שיניתי לאיקס כדי לא להתנגש עם {% equation %}A{% endequation %}), הקבוצה {% equation %}A{% endequation %} היא הקבוצה {% equation %}f\left(X\right){% endequation %} - כל התמונות של הפעלת {% equation %}f{% endequation %} על אברי {% equation %}X{% endequation %}, ו-{% equation %}B{% endequation %} הייתה {% equation %}\mathcal{P}\left(X\right){% endequation %}.

בשני המקרים הללו הקבוצה {% equation %}A{% endequation %} נבחרת בתור "התמונה של פונקציה שאנחנו רוצים להראות שאינה על" אבל יש טיעוני לכסון אחרים (למשל בתורת החישוביות) שבהן לא רוצים להראות שפונקציה היא על אלא שקבוצה כלשהי מוכלת ממש באחרת ("כל הפונקציות שאפשר לחשב בזמן פולינומי הן תת-קבוצה ממש של כל הפונקציות שאפשר לחשב בזמן אקספוננציאלי") ולכן הניסוח שלי.

עכשיו, הרעיון הוא שכדי להוכיח ש-{% equation %}A\ne B{% endequation %} אנחנו בונים איבר ספציפי {% equation %}b\in B{% endequation %} בצורה כזו שהוא יהיה שונה מכל אברי {% equation %}A{% endequation %}. כדי לעשות את זה אנחנו מנצלים <strong>חופש בחירה</strong> שיש לנו בבניה של אברי {% equation %}B{% endequation %}. אפשר לחשוב על אברי {% equation %}B{% endequation %} כבעלי "תכונות" מסויימות, שאפשר לשלוט עליהן בצורה בלתי תלויה פחות או יותר, וכשאנחנו בונים את {% equation %}b{% endequation %} אז לכל {% equation %}a\in A{% endequation %}, אנחנו מהנדסים את אחת מהתכונות של {% equation %}b{% endequation %} כדי שתהיה שונה מאותה התכונה אצל {% equation %}a{% endequation %}.

באלכסון של קנטור, {% equation %}b{% endequation %} היה האיבר שכינתי {% equation %}d=0.d_{0}d_{1}d_{2}\ldots{% endequation %} וה"תכונות" הן פשוט הספרות של {% equation %}d{% endequation %}. את {% equation %}d_{0}{% endequation %} הינדסתי כדי להיות שונה מ-{% equation %}a_{0}{% endequation %}, אז {% equation %}d_{1}{% endequation %} כדי להיות שונה מ-{% equation %}a_{1}{% endequation %} וכן הלאה. שימו לב שלא היה לי חופש בחירה <strong>מוחלט</strong> של הספרות {% equation %}d_{i}{% endequation %} הללו - נזהרתי לא להשתמש ב-0 או 9 כדי לא להתנגש בתופעה הקטנונית והמצערת של {% equation %}0.999\ldots=1{% endequation %}.

במשפט על קבוצת החזקה, {% equation %}b{% endequation %} היה הקבוצה {% equation %}D{% endequation %} שבניתי וה"תכונות" היו האיברים של {% equation %}D{% endequation %}. לכל {% equation %}x\in X{% endequation %}, ה"תכונה" הייתה השאלה האם {% equation %}x\in D{% endequation %} או {% equation %}x\notin D{% endequation %}, ואת זה באמת שיכלתי לבחור באופן בלתי תלוי לכל {% equation %}x{% endequation %}.

עכשיו, נקודה שכדאי לשים אליה לב היא שבשתי ההוכחות, הייתה לי דרך כלשהי <strong>לאנדקס</strong> את האיברים של {% equation %}A{% endequation %}, והתבססתי על שיטת האינדקס הזו כשבניתי את {% equation %}b{% endequation %}. באלכסון של קנטור, {% equation %}A=\left\{ a_{0},a_{1},a_{2},\ldots\right\} {% endequation %} והאינדקסים של האיברים הם פשוט מספרים טבעיים. נעזרתי את זה כשבניתי את {% equation %}d=0.d_{0}d_{1}d_{2}\ldots{% endequation %}: השתמשתי <strong>באותה קבוצת אינדקסים</strong> כדי לאנדקס את <strong>הספרות</strong> של {% equation %}d{% endequation %}. שימו לב שזה לא מובן מאליו: יצרנו כאן קשר בין האינדקסים של <strong>אברים</strong> של {% equation %}A{% endequation %} ובין האינדקסים של <strong>הספרות שמרכיבות</strong> את {% equation %}d{% endequation %}.

בהוכחה של המשפט עם קבוצת החזקה, ה"אינדקסים" היו האיברים של {% equation %}X{% endequation %}. כזכור, הגדרתי את {% equation %}A{% endequation %} בתור {% equation %}f\left(X\right){% endequation %}, כלומר כל איבר של {% equation %}A{% endequation %} היה קבוצה מהצורה {% equation %}f\left(x\right){% endequation %} עבור {% equation %}x\in X{% endequation %}, ואני ניצלתי את האינדקס הזה כדי לבנות קבוצה {% equation %}D{% endequation %} כך ש-{% equation %}x\in D\iff x\notin f\left(x\right){% endequation %}, כך ש-{% equation %}D{% endequation %} (הקבוצה שאני בונה) ו-{% equation %}f\left(x\right){% endequation %} (הקבוצה שמאונדקסת על ידי {% equation %}x{% endequation %}) נבדלו ביניהן בתכונה "{% equation %}x{% endequation %} שייך אלי".

אני מקווה שהדמיון בין שתי ההוכחות ברור יותר עכשיו, אבל אם אני מתפאר כל כך בכלליות של שיטת הלכסון, אולי כדאי לי להציג <strong>עוד</strong> דוגמא או שתיים לפני שאני בורח.

<h2>עוד דוגמאות ללכסונים</h2>

אני רוצה לתת עוד דוגמא או שתיים לאופן שבו משתמשים בכלי של לכסון כדי להוכיח שקבוצה כלשהי היא גדולה יותר מהמספרים הטבעיים. לשם כך אני אסתכל על קבוצת ה<strong>סדרות</strong> של טבעיים: קבוצת הפונקציות {% equation %}f:\mathbb{N}\to\mathbb{N}{% endequation %}, ואקח ממנה תת-קבוצות מסוימות.

בדוגמא הראשונה שלי, {% equation %}B{% endequation %} היא קבוצת הסדרות של טבעיים שבה במקומות <strong>האי-זוגיים</strong> יש תמיד 42. למה? ככה. כדי להקשות. פורמלית, {% equation %}B=\left\{ f\in\mathbb{N}^{\mathbb{N}}\ |\ \forall n\in\mathbb{N}:f\left(2n+1\right)=42\right\} {% endequation %}. טיעון לכסון שמטרתו להוכיח ש-{% equation %}\left|\mathbb{N}\right|\ne\left|B\right|{% endequation %} מתחיל כך: ניקח פונקציה כלשהי {% equation %}g:\mathbb{N}\to B{% endequation %} ונוכיח שאינה חח"ע. נסמן {% equation %}A=g\left(\mathbb{N}\right)=\left\{ f_{0},f_{1},f_{2},\ldots\right\} {% endequation %} - הנה יש לנו "אינדוקס" של אברי {% equation %}A{% endequation %} כמו קודם. עכשיו אני אבנה פונקציה חדשה, {% equation %}h\in B{% endequation %}, בצורה שמבטיחה ש-{% equation %}h\ne f_{n}{% endequation %} לכל {% equation %}n\in\mathbb{N}{% endequation %}.

הדבר ה"טבעי" היה אולי להגדיר כך: {% equation %}h\left(n\right)=\begin{cases} 4 & f_{n}\left(n\right)\ne4\\ 3 & f_{n}\left(n\right)=4 \end{cases}{% endequation %}. זה מאוד מתאים לאלכסון של קנטור שראינו קודם. זה גם מאוד <strong>שגוי</strong> כי אין לנו חופש בחירה כזה כשאנחנו בונים את {% equation %}h{% endequation %}. כזכור, היעד שלנו הוא שיתקיים {% equation %}h\in B{% endequation %} וכדי שזה יקרה, על ערכים <strong>אי זוגיים</strong> אני חייב להגדיר את {% equation %}h{% endequation %} להחזיר 42.

אם כך, לכאורה אני בצרות! איך אני אוכל להבטיח ש-{% equation %}h{% endequation %} שונה מ-{% equation %}f_{1}{% endequation %} אם אני לא יכול להגדיר אותה על {% equation %}1{% endequation %} איך שבא לי?! אם {% equation %}h\left(1\right)=f_{1}\left(1\right)=42{% endequation %}, כל טיעון האלכסון של קנטור נהרס! הו לא!

כמובן שבפועל זה מכשול זניח שקל מאוד לעקוף. אני <strong>עדיין</strong> אשתמש באינדקס של {% equation %}f_{n}{% endequation %}; אני פשוט אכפול אותו ב-2:

{% equation %}h\left(n\right)=\begin{cases} 42 & n=2k+1\\ 4 & n=2k\wedge f_{k}\left(n\right)\ne4\\ 3 & n=2k\wedge f_{k}\left(n\right)\ne4 \end{cases}{% endequation %}

מה עשיתי פה? כש-{% equation %}h{% endequation %} מקבלת קלט, קודם כל היא בודקת אם הוא זוגי או לא. אם הוא אי זוגי, אין לה ברירה - היא מחזירה 42. אם הוא זוגי, היא <strong>מחלקת אותו ב-</strong><strong>2</strong> והתוצאה שהיא מקבלת היא האינדקס של ה-{% equation %}f{% endequation %} שהיא "תתקוף" באמצעות הקלט {% equation %}n{% endequation %}. שימו לב שאני מגדיר את {% equation %}h\left(n\right){% endequation %} כך ש-{% equation %}h\left(n\right)\ne f_{k}\left(n\right){% endequation %} - כלומר, ש-{% equation %}h{% endequation %} ו-{% equation %}f_{k}{% endequation %} יבדלו זו מזו במקום ה-{% equation %}n{% endequation %}-י. אם הייתי מגדיר {% equation %}h\left(n\right)\ne f_{k}\left(k\right){% endequation %} אז מה שיש בצד ימין היה מזכיר יותר את האלכסון ה"קלאסי" של קנטור, אבל הוא גם לא היה אומר שום דבר - אם {% equation %}n\ne k{% endequation %} אין שום דבר מעניין שאפשר להסיק {% equation %}h\left(n\right)\ne f_{k}\left(k\right){% endequation %}; אי אפשר להסיק מזה {% equation %}h\ne f_{k}{% endequation %}.

הדוגמא הזו היא המחשה לסיבה שבגללה אני לא אוהב שמדברים על אלכסון ויזואלי בהוכחת האלכסון של קנטור - אם ננסה לכתוב את רשימת הערכים של הפונקציות, כמו בטבלה היפה שציירתי למעלה עבור האלכסון, נגלה שמה ש-{% equation %}h{% endequation %} "תוקפת" הם ערכים שמסודרים במין אלכסון עקום שכזה, עם שיפוע ששונה מ-45 מעלות - ויש דוגמאות שבהן זה עוד יותר מתחרבש.

נעבור לדוגמא השניה שלי. בדוגמא הזו, {% equation %}B{% endequation %} תהיה קבוצת הסדרות של טבעיים שהן <strong>מונוטוניות עולות</strong>. סדרה {% equation %}f{% endequation %} היא מונוטונית עולה אם לכל {% equation %}n<m{% endequation %} מתקיים {% equation %}f\left(n\right)<f\left(m\right){% endequation %} - או במילים אחרות, לכל שני איברים סמוכים בסדרה, הראשון קטן מהשני. כמקודם, הטיעון האלכסוני מגיע לכך שיש לי קבוצה {% equation %}\left\{ f_{0},f_{1},\ldots\right\} {% endequation %} של סדרות כאלו ואני רוצה לבנות אחת חדשה {% equation %}h{% endequation %} ששונה מהן.

הפעם הבניה {% equation %}h\left(n\right)=\begin{cases} 4 & f_{n}\left(n\right)\ne4\\ 3 & f_{n}\left(n\right)=4 \end{cases}{% endequation %} לא תעבור כי {% equation %}h{% endequation %} לא תהיה מונוטונית. מה שטוב בדרישת המונוטוניות הזו הוא בכך שהיא קצת מקלקלת לי את ה<strong>אי-תלות</strong> בין ערכים שונים של {% equation %}h{% endequation %}. אם נעיף מבט בתיאור הכללי של של שיטת הלכסון נראה שכתבתי ניסוח מאוד מעורפל: "אפשר לחשוב על אברי {% equation %}B{% endequation %} כבעלי "תכונות" מסויימות, שאפשר לשלוט עליהן בצורה בלתי תלויה <strong>פחות או יותר</strong>". עכשיו אנחנו ב"פחות" הזה. אבל אין סיבה שזה יעצור אותנו - כל מה שאנחנו צריכים הוא שכל איבר יהיה גדול יותר מהקודם <strong>וגם</strong> מהאיבר המקביל אצל {% equation %}f{% endequation %}. אז אני אשתמש בסימון {% equation %}h\left(-1\right)=0{% endequation %}, וכעת אגדיר {% equation %}h\left(n\right)=h\left(n-1\right)+f_{n}\left(n\right)+1{% endequation %}. כאן אפילו לא צריך חלוקה למקרים.

מה קורה פה? ראשית, בגלל שאנחנו מוסיפים 1, אז {% equation %}h\left(n\right)>f_{n}\left(n\right){% endequation %} ולכן {% equation %}h\ne f_{n}{% endequation %}. שנית, בגלל אותה תוספת 1, אנחנו מקבלים {% equation %}h\left(n\right)>h\left(n-1\right){% endequation %} ולכן הסדרה מונוטונית עולה. זה מסיים את ההוכחה. למעשה, זה טיעון כל כך פשוט שלא ברור למה באלכסון המקורי של קנטור לא הגדרתי {% equation %}d_{n}=a_{n}^{n}+1{% endequation %}, אבל התשובה פשוטה: שם ה-{% equation %}d{% endequation %}-ים היו <strong>ספרות</strong> בייצוג עשרוני, כלומר היו מוגבלים להיות בין 0 ל-9. כאן אין לי הגבלה כזו.

<h2>ועכשיו למשהו לא קשור בעליל - פונקציות שאינן ניתנות לחישוב</h2>

אני לא יכול לסיים פוסט על לכסון בלי לגלוש לתחום שאהוב עלי במיוחד ולכסונים מככבים גם בו - תורת החישוביות. מכיוון ששולי הפוסט הזה צרים מלהכיל מבוא מלא לחישוביות, הנה התקציר: במרכז מה שעושים בחישוביות נמצא <strong>מודל חישובי</strong> כלשהו. לעתים קרובות מדברים על משהו שנקרא <strong>מכונת טיורינג</strong> אבל אני לא צריך את זה פה ואדבר על תוכניות מחשב בשפה קונקרטית כלשהי - נאמר, פייתון. לא צריך להכיר את פייתון בשביל המשך הטיעון - רק לדעת שכל תוכנית מחשב כזו אפשר <strong>לקודד</strong> באמצעות מספר טבעי (זה האופן שבו קבצי טקסט נשמרים בזכרון של המחשב, פחות או יותר). הקידוד הזה הוא חד-חד-ערכי ועל ולכן אפשר לסמן את קבוצת כל תוכניות הפייתון ב-{% equation %}\left\{ M_{0},M_{1},M_{2},\ldots\right\} {% endequation %}.

עכשיו, הרבה תוכניות פייתון הן "ג'יבריש" - יש בהן איזו שגיאת כתיב או משהו דומה ואי אפשר בכלל להריץ אותן. הן לא מעניינות אותי. תוכניות אחרות, כשמריצים אותן, עושות כל מני דברים מגניבים כמו סימולציה של חישוב קוונטי וכדומה - גם זה לא מעניין אותי. כל מה שמעניין אותי הוא תוכניות שפועלות כך: מקבלות כקלט מספר טבעי, רצות עליו ואם סיימו - עונות "כן" או "לא". אלו תוכניות שבמהותן <strong>מזהות</strong> קבוצה של מספרים - למשל, יש תוכניות שיודעות לזהות את קבוצות המספרים הראשוניים, הזוגיים, מספרי פרמה ומה שתרצו. על תוכניות ש<strong>לא</strong> מתאימות לתבנית הזו - תוכניות ג'יבריש וסימולטורים קוונטים וכל היתר - אני אחשוב בתור תוכניות שפשוט אומרות "לא" על הכל ולכן "מזהות" את הקבוצה הריקה של טבעיים.

נניח ש-{% equation %}L{% endequation %} היא קבוצה של מספרים טבעיים ו-{% equation %}M{% endequation %} היא תוכנית מחשב כלשהי. אני אומר ש-{% equation %}M{% endequation %} <strong>מכריעה</strong> את {% equation %}L{% endequation %} אם:

<ul> <li>לכל {% equation %}a\in L{% endequation %}, התוכנית {% equation %}M{% endequation %} עוצרת על הקלט {% equation %}a{% endequation %} עם התשובה "כן"</li>


<li>לכל {% equation %}a\notin L{% endequation %} התוכנית {% equation %}M{% endequation %} עוצרת על הקלט {% equation %}a{% endequation %} עם התשובה "לא"</li>

</ul>

ועכשיו בואו נסבך: אני אומר ש-{% equation %}M{% endequation %} <strong>מקבלת</strong> את {% equation %}A{% endequation %} אם:

<ul> <li>לכל {% equation %}a\in L{% endequation %}, התוכנית {% equation %}M{% endequation %} עוצרת על הקלט {% equation %}a{% endequation %} עם התשובה "כן"</li>


<li>לכל {% equation %}a\notin L{% endequation %} התוכנית {% equation %}M{% endequation %} עוצרת על הקלט {% equation %}a{% endequation %} עם התשובה "לא" <strong>או שאינה עוצרת בכלל</strong></li>

</ul>

כלומר, "לקבל" את {% equation %}L{% endequation %} זה משהו שקצת יותר קל לעשות מאשר "להכריע" את {% equation %}L{% endequation %}, כי על קלטים שלא שייכים ל-{% equation %}L{% endequation %} אפשר פשוט לא לעצור. האם יש הבדל מהותי בין שתי ההגדרות? כלומר, האם קיימת קבוצה {% equation %}L{% endequation %} שאפשר <strong>לקבל</strong> אבל אי אפשר <strong>להכריע</strong>? התשובה חיובית ואני הולך להראות איך מוכיחים את זה בלכסון.

הנה איך שמבנה הלכסון שהצגתי קודם עובד כאן: {% equation %}B{% endequation %} שלי תהיה קבוצת כל קבוצות הטבעיים {% equation %}L{% endequation %} שאפשר <strong>לקבל</strong> ואילו {% equation %}A\subseteq B{% endequation %} תהיה קבוצת כל קבוצות הטבעיים {% equation %}L{% endequation %} שאפשר <strong>להכריע</strong>. יש לי דרך פשוטה לאנדקס את אברי {% equation %}A{% endequation %}: אם אפשר להכריע את {% equation %}L{% endequation %} אז <strong>קיימת</strong> תוכנית {% equation %}M{% endequation %} שמכריעה את {% equation %}L{% endequation %}. כבר ראינו קודם שאפשר למספר את <strong>כל</strong> התוכניות, כך שגם ל-{% equation %}M{% endequation %} הזו יש מספר סידורי כלשהו, {% equation %}n{% endequation %}, כלומר אני מסמן אותה ב-{% equation %}M_{n}{% endequation %}. עכשיו אני אבנה קבוצה {% equation %}D{% endequation %} של טבעיים באופן הבא: {% equation %}D{% endequation %} תכיל את ה-{% equation %}n{% endequation %}-ים ש-{% equation %}M_{n}{% endequation %} אומרת עליהם "לא".

הנה איך נובע מההגדרה הזו שלא קיימת מכונה {% equation %}M{% endequation %} שמכריעה את {% equation %}D{% endequation %}: נסתכל על המכונה {% equation %}M_{n}{% endequation %}, עבור {% equation %}n{% endequation %} כלשהו. מה המכונה {% equation %}M_{n}{% endequation %} עושה על הקלט {% equation %}n{% endequation %}? ייתכן ש-{% equation %}M_{n}{% endequation %} <strong>בכלל לא עוצרת</strong> על הקלט הזה, אבל אז {% equation %}M_{n}{% endequation %} היא לא מכונה שמכריעה קבוצות; מכונה שמכריעה קבוצות חייבת לעצור על כל קלט. מכיוון שכל מה שאנחנו רוצים לעשות הוא להראות ש-{% equation %}D{% endequation %} לא מוכרעת על ידי {% equation %}M_{n}{% endequation %}, סיימנו במקרה הזה. נשארנו עם המקרה שבו {% equation %}M_{n}{% endequation %} כן עוצרת על {% equation %}n{% endequation %}. במקרה הזה, אם {% equation %}M_{n}{% endequation %} אומרת "לא" אז {% equation %}n\in D{% endequation %} על פי הגדרת {% equation %}D{% endequation %}. אם לעומת זאת {% equation %}M_{n}{% endequation %} אומרת "כן" אז {% equation %}n\notin D{% endequation %} על פי הגדרת {% equation %}D{% endequation %}. בכל אחד משני המקרים הללו, {% equation %}M_{n}{% endequation %} עונה את התשובה <strong>הלא נכונה</strong> מבחינת {% equation %}D{% endequation %}, ולכן הקבוצה ש-{% equation %}M_{n}{% endequation %} מכריעה איננה {% equation %}D{% endequation %}.

האם סיימנו? עוד לא, כי עדיין צריך להראות ש-{% equation %}D{% endequation %} שלנו שייכת ל-{% equation %}B{% endequation %} - כלומר, ש-{% equation %}D{% endequation %} היא שפה שאפשר <strong>לקבל</strong>. בשביל זה צריך להציג תוכנית מחשב שעושה את זה בפועל, ואת זה אעשה בנפנוף ידיים (כלומר, לא אכתוב פה קוד פייתון). הרעיון הוא פשוט: התוכנית שלנו תקבל קלט {% equation %}n{% endequation %}. בעזרת הקלט הזה היא תבנה את הקוד של תוכנית המחשב {% equation %}M_{n}{% endequation %}, תריץ את {% equation %}M_{n}{% endequation %} על {% equation %}n{% endequation %} ו<strong>אם</strong> {% equation %}M_{n}{% endequation %} עצרה ואמרה "לא", התוכנית שלנו תגיד "כן". אם {% equation %}M_{n}{% endequation %} עצרה ואמרה "כן" התוכנית שלנו תגיד "לא", ואם {% equation %}M_{n}{% endequation %} לא עצרה גם התוכנית שלנו מן הסתם לא תעצור (כי היא מריצה את {% equation %}M_{n}{% endequation %} עד אינסוף ולא יודעת מתי "להתייאש"). קל לראות שהתוכנית שלנו אכן מקבלת את {% equation %}D{% endequation %} על פי ההגדרה שהצגתי.

איך נפנוף הידיים שלי בא לידי ביטוי? ראשית, בהנחה שאפשר לשחזר את {% equation %}M_{n}{% endequation %} מתוך {% equation %}n{% endequation %} - כדי להסביר את זה צריך להיכנס לפרטים של איך בדיוק מקודדים תוכניות מחשב - לא אעשה את זה כאן, וממילא זה מה שעורכי טקסט עושים כשהם טוענים תוכניות מחשב מקבצים. שנית, בהנחה שתוכנית מחשב שלי יודעת להריץ תוכנית מחשב אחרת, שנתונה לה כקלט - גם את זה קל לעשות במחשבים מודרניים. מתי הדברים הללו לא היו מובנים מאליהם? בשנת 1936, כשאלן טיורינג פרסם את המאמר שלו ``On computable numbers, with an application to the Entscheidungsproblem'' שבו הוא:

<ol> <li>הציג את המודל של מכונת טיורינג, שהיא סוג של מחשב מאוד פשוט לתכנות.</li>


<li>הראה איך אפשר לקודד את המודל הזה באמצעות מספרים טבעיים כך שאפשר יהיה "לשחזר" את המכונה מתוך הקידוד.</li>


<li>הראה איך אפשר להריץ מכונה בהינתן קידוד שלה (מה שיודע לבצע הרצה כזו נקרא "מכונת טיורינג אוניברסלית").</li>

</ol>

על הרעיונות המאוד לא טריוויאליים לשעתו הללו הוא הרכיב את טיעון הלכסון, שכבר היה נפוץ יחסית בתקופה הזו וקורט גדל השתמש בוריאציה עליו בהוכחת משפטי אי השלמות שלו כמה שנים קודם, והגיע לתוצאה שהיא פחות או יותר מה שהראיתי כאן. למעשה, טיורינג עשה קצת יותר מזה - הוא לא סתם הוכיח ש<strong>קיימת</strong> קבוצה שאי אפשר להכריע אלא נתן אחת קונקרטית מאוד ("בעיית העצירה"). היתרון בהוכחה האלכסונית שהצגתי פה הוא שקל להכליל אותה לעוד סיטואציות: למשל, קבוצות שצריך להכריע תחת מגבלת זמן מסויימת אל מול קבוצות שעבורן אין מגבלת זמן שכזו.

בזאת סיימנו את מה שיש לי להגיד כרגע על לכסונים - בפוסט הבא של תורת הקבוצות נחזור לדבר על דברים קונקרטיים יותר, כמו המספרים הרציונליים: מה בעצם קורה איתם? מה הגודל האינסופי שלהם? הרי יש קטע כזה שבין כל שני מספרים ממשיים יש מספר רציונלי, אז בוודאי צריך להתקיים {% equation %}\left|\mathbb{Q}\right|=\left|\mathbb{R}\right|{% endequation %}. נכון? נכון? נכון? לא נכון...? 
