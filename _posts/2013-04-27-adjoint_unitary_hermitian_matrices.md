---
id: 2515
title: "מטריצות צמודות, הרמיטיות, אוניטריות"
date: 2013-04-27 18:43:39
layout: post
categories: 
  - אלגברה לינארית
tags: 
  - אלגברה לינארית
  - מטריצות אוניטריות
  - מטריצות הרמיטיות
  - מרחבי מכפלה פנימית
---
אולי התוצאה המעניינת ביותר באלגברה לינארית בסיסית היא הקשר שיש בין טרנספורמציות לינאריות {% equation %}T:V\to V{% endequation %} המוגדרות על מרחב וקטורי ממימד סופי {% equation %}V{% endequation %} ובין מטריצות. כזכור, מרגע שבו אנחנו קובעים בסיס {% equation %}B{% endequation %} ל-{% equation %}V{% endequation %}, אוטומטית נובעת מכך התאמה חד-חד-ערכית ועל בין אוסף הטרנספורמציות הלינאריות {% equation %}T:V\to V{% endequation %} (לפעמים אכתוב "אופרטור לינארי" במקום; המילה "אופרטור" רומזת שמדובר על טרנספורמציה ממרחב לעצמו) ובין המטריצות מסדר {% equation %}n\times n{% endequation %} מעל אותו שדה כמו {% equation %}V{% endequation %}, כאשר {% equation %}n{% endequation %} הוא מימד המרחב {% equation %}V{% endequation %}. הרעיון בהתאמה הזו הוא שמתקיים השוויון {% equation %}\left[T\right]_{B}\left[v\right]_{B}=\left[T\left(v\right)\right]_{B}{% endequation %} - במילים, הכפלת המטריצה שמייצגת את האופרטור {% equation %}T{% endequation %} בוקטור הקואורדינטות שמייצג את הוקטור {% equation %}v{% endequation %} על פי הבסיס {% equation %}B{% endequation %} מחזירה את וקטור הקואורדינטות של {% equation %}T\left(v\right){% endequation %} על פי {% equation %}B{% endequation %}. עבור בסיסים שונים, ל-{% equation %}T{% endequation %} יהיו מטריצות מייצגות שונות, ואחד מהדברים שעוסקים בהם באלגברה לינארית הוא השאלה הבאה: בהינתן {% equation %}T{% endequation %}, אילו בסיסים קיימים שבהם {% equation %}\left[T\right]_{B}{% endequation %} היא פשוטה במיוחד (למשל, אלכסונית)?

על כל זה <a href="http://www.gadial.net/2011/10/27/coordinates_transformations_matrices/">כבר דיברתי בעבר</a>. ההקשר הנוכחי שלנו הוא מרחבים וקטוריים עם מבנה נוסף - מרחבי מכפלה פנימית. בפרט, אנחנו רוצים להבין איך המושג של <strong>אופרטור צמוד</strong> בא לידי ביטוי במטריצות. <a href="http://www.gadial.net/2012/04/29/inner_product_space_adjoint/">כזכור</a>, אם {% equation %}T{% endequation %} הוא אופרטור אז קיים אופרטור יחיד {% equation %}T^{*}{% endequation %} כך שמתקיים {% equation %}\left\langle T\left(v\right),u\right\rangle =\left\langle v,T^{*}\left(u\right)\right\rangle {% endequation %} לכל {% equation %}v,u\in V{% endequation %}. הוכחת הקיום של {% equation %}T^{*}{% endequation %} היא אמנם קונסטרוקטיבית, במובן זה שאפשר להבין ממנה איך למצוא את {% equation %}T^{*}{% endequation %}, אבל בדרך עקיפה וסבוכה; יהיה הרבה יותר פשוט לקבוע בסיס כלשהו ולמצוא ל-{% equation %}T^{*}{% endequation %} מטריצה מייצגת על פי הבסיס הזה בהינתן המטריצה המייצגת של {% equation %}T{% endequation %}. אלא שכפי שנראה בקרוב, כבר אי אפשר לקחת "סתם" בסיס - כדי שמציאת המטריצה של {% equation %}T^{*}{% endequation %} מתוך המטריצה של {% equation %}T{% endequation %} תהיה פשוטה, אנחנו צריכים לקחת בסיס <strong>אורתונורמלי</strong> למרחב. למזלנו מובטח לנו שתמיד יש כזה, אבל מציאה של בסיס כזה עשויה להיות כרוכה לפעמים בחישובים לא נעימים.

אם כן, יהא {% equation %}B=\left\{ b_{1},\dots,b_{n}\right\} {% endequation %} בסיס אורתונורמלי ל-{% equation %}V{% endequation %} ותהא {% equation %}T{% endequation %} טרנספורמציה כלשהי. נסמן {% equation %}A=\left[T\right]_{B}{% endequation %}. איך נראית {% equation %}A{% endequation %}? העמודה ה-{% equation %}j{% endequation %}-ית של {% equation %}A{% endequation %} היא בעצם וקטור הקואורדינטות, לפי {% equation %}B{% endequation %}, של {% equation %}T\left(b_{j}\right){% endequation %} (למה? ובכן, צריך להוכיח את זה). עכשיו, עבור בסיסים אורתונורמליים אנחנו יודעים למצוא בקלות את הקואורדינטות של וקטור {% equation %}v{% endequation %} לפי הבסיס {% equation %}B{% endequation %}: הקואורדינטה שמתאימה לאיבר הבסיס {% equation %}b_{i}{% endequation %} היא פשוט {% equation %}\left\langle v,b_{i}\right\rangle {% endequation %}. לכן במקרה שלנו, {% equation %}A_{ij}=\left\langle T\left(b_{j}\right),b_{i}\right\rangle {% endequation %} (הכניסה בשורה ה-{% equation %}i{% endequation %} והעמודה ה-{% equation %}j{% endequation %} במטריצה היא המכפלה הפנימית {% equation %}\left\langle T\left(b_{j}\right),b_{i}\right\rangle {% endequation %}).

באופן דומה, אם {% equation %}A^{*}{% endequation %} היא המטריצה המייצגת של {% equation %}T^{*}{% endequation %} אז יתקיים עבורה {% equation %}A_{ij}^{*}=\left\langle T^{*}\left(b_{j}\right),b_{i}\right\rangle {% endequation %}. עכשיו אעשה תעלול קטן ופשוט אחליף את האינדקסים: {% equation %}A_{ji}^{*}=\left\langle T^{*}\left(b_{i}\right),b_{j}\right\rangle {% endequation %}. כעת שימו לב לזה:

{% equation %}A_{ij}=\left\langle T\left(b_{j}\right),b_{i}\right\rangle =\left\langle b_{j},T^{*}\left(b_{i}\right)\right\rangle =\overline{\left\langle T^{*}\left(b_{i}\right),b_{j}\right\rangle }=\overline{A_{ji}^{*}}{% endequation %}

מה הלך פה? השתמשתי במעברים פה בכך ש-{% equation %}T^{*}{% endequation %} צמודה ל-{% equation %}T{% endequation %}, ובכך שמכפלה פנימית מקיימת <strong>הרמיטיות</strong> - אפשר להחליף את הסדר של שני המוכפלים, במחיר של הצמדה (במשמעות של "צמוד מרוכב") של הערך של המכפלה (כבר <a href="http://www.gadial.net/2012/02/06/inner_products_intro/">הסברתי בעבר</a> למה ההצמדה הזו הכרחית). הגענו למסקנה ש-{% equation %}A^{*}{% endequation %} מתקבלת מ-{% equation %}A{% endequation %} על ידי הצמדה (מרוכבת) ושחלוף של {% equation %}A{% endequation %} (הפיכת השורה ה-{% equation %}i{% endequation %} של {% equation %}A{% endequation %} לעמודה ה-{% equation %}i{% endequation %} של {% equation %}A^{*}{% endequation %}). לדוגמה, אם

{% equation %}A=\left[\begin{array}{cc}1 & -3\\5-i & i\end{array}\right]{% endequation %}

אז

{% equation %}A^{*}=\left[\begin{array}{cc}1 & 5+i\\-3 & -i\end{array}\right]{% endequation %}

זה מוביל אותנו להגדרה - אם {% equation %}A{% endequation %} היא מטריצה ריבועית, אז {% equation %}A^{*}{% endequation %} היא המטריצה שמתקבלת משחלוף והצמדה של {% equation %}A{% endequation %} והיא נקראת <strong>המטריצה הצמודה</strong> של {% equation %}A{% endequation %}. זה זמן טוב להזכיר עוד מטריצה שגם היא נקראת לפעמים "המטריצה הצמודה" והתנגשות השמות הזו היא אסון - מטריצה שקראתי לה <strong>המטריצה המצורפת</strong> ל-{% equation %}A{% endequation %}, שמסומנת בתור {% equation %}\mbox{adj}A{% endequation %} ו<a href="http://www.gadial.net/2011/11/21/matrix_revolutions/">תיארתי בעבר</a> בבלוג.

עכשיו, דיברנו על אופרטורים צמודים לעצמם ועל אופרטורים אוניטריים, וההגדרות עוברות באופן חלק למטריצות: מטריצה שמקיימת {% equation %}A^{*}=A{% endequation %} נקראת <strong>מטריצה צמודה לעצמה</strong> או <strong>מטריצה הרמיטית</strong>, ואילו מטריצה שמקיימת {% equation %}A^{-1}=A^{*}{% endequation %} נקראת <strong>מטריצה אוניטרית</strong>. בואו ננסה להבין איך הן נראות.

בתור התחלה, אם {% equation %}A^{*}=A{% endequation %} עבור מטריצה שכל הכניסות בה ממשיות, פירוש הדבר הוא שהמטריצה <strong>סימטרית</strong>. כי היא שווה לשחלוף של עצמה. עבור כניסות מרוכבות המצב קצת יותר מסובך. הנה דוגמה למטריצה הרמיטית:

{% equation %}\left[\begin{array}{cc}1 & -i\\i & 1\end{array}\right]{% endequation %}

כמו שאתם רואים, היא לא בדיוק סימטרית. אם נפרק אותה לסכום של שתי מטריצות שאחת מהן כוללת את כל הרכיבים הממשיים והשניה את כל הרכיבים המדומים נקבל שהמטריצה הממשית היא סימטרית, בעוד שהמטריצה המדומה היא אנטי-סימטרית (מטריצה אנטי סימטרית היא מטריצה {% equation %}A{% endequation %} כך ש-{% equation %}A^{t}=-A{% endequation %}). בפרט, האיברים על האלכסון הראשי של המטריצה שווים להצמדה של עצמם ולכן הם חייבים להיות מספרים ממשיים "טהורים". זה יהיה חשוב בהמשך.

בואו נעבור לדבר על מטריצות אוניטריות. ראשית כל אני רוצה להבין מה הדטרמיננטה של מטריצה כזו יכולה להיות. אם {% equation %}A^{-1}=A^{*}{% endequation %} אז {% equation %}A\cdot A^{*}=I{% endequation %} ולכן {% equation %}1=\left|I\right|=\left|AA^{*}\right|=\left|A\right|\left|A^{*}\right|{% endequation %}. ומהי {% equation %}\left|A^{*}\right|{% endequation %}? תחושת הבטן היא ש-{% equation %}\left|A^{*}\right|=\overline{\left|A\right|}{% endequation %}, כלומר הדטרמיננטה של הצמוד היא ההצמדה המרוכבת של הדטרמיננטה של {% equation %}A{% endequation %}. לא קשה לראות את זה ישירות מההגדרה הפורמלית של דטרמיננטה, למשל בתור סכום של מכפלות. זכרו שלכל מספר מרוכב {% equation %}z{% endequation %} מתקיים {% equation %}z\cdot\overline{z}=\left|z\right|^{2}{% endequation %}, ולכן המסקנה היא ש-{% equation %}\left|\det A\right|^{2}=1{% endequation %} (עברתי לסמן דטרמיננטה ב-{% equation %}\det{% endequation %} מסיבות ברורות). מכאן שהדטרמיננטה של {% equation %}A{% endequation %} חייבת להיות 1 בערכה המוחלט (מכיוון שהיא עשויה להיות מספר מרוכב זה עדיין נותן לה לא מעט אפשרויות).

עכשיו בואו נעבור לדבר על מקרה קונקרטי יותר. ראשית כל, הבה וניזכר באופן כללי מהי ההופכית של מטריצה מסדר {% equation %}2\times2{% endequation %} כלשהי. אם

{% equation %}A=\left[\begin{array}{cc}a & b\\c & d\end{array}\right]{% endequation %}

אז ההופכית שלה היא

{% equation %}A^{-1}=\frac{1}{\left|A\right|}\left[\begin{array}{cc}d & -b\\-c & a\end{array}\right]{% endequation %}

לא מאמינים? פשוט תכפילו ותראו... הנוסחה הזו היא מקרה פרטי של המשפט לפיו {% equation %}A^{-1}=\frac{\mbox{adj}A}{\left|A\right|}{% endequation %} שהראיתי בעבר. עכשיו, באופן כללי מתקיים

{% equation %}A^{*}=\left[\begin{array}{cc}\overline{a} & \overline{c}\\\overline{b} & \overline{d}\end{array}\right]{% endequation %}

כך שאם מתקיים {% equation %}A^{-1}=A^{*}{% endequation %} אנחנו יכולים להסיק את {% equation %}c,d{% endequation %} בתור פונקציות של {% equation %}a,b{% endequation %}:

{% equation %}c=-\left|A\right|\overline{b}{% endequation %}

{% equation %}d=\left|A\right|\overline{a}{% endequation %}

מכיוון ש-{% equation %}\left|A\right|=ad-bc{% endequation %} אז בפרט נקבל {% equation %}\left|A\right|=\left|A\right|a\overline{a}+\left|A\right|b\overline{b}=\left|A\right|\left(\left|a\right|^{2}+\left|b\right|^{2}\right){% endequation %}, כלומר {% equation %}\left|a\right|^{2}+\left|b\right|^{2}=1{% endequation %}.

כעת, אפשר לכתוב קונקרטית {% equation %}\left|A\right|=e^{i\theta}{% endequation %} עבור {% equation %}0\le\theta\le2\pi{% endequation %} - זו דרך ההצגה הקוטבית של מספר מרוכב עם ערך מוחלט 1. לכן נקבל שמטריצה {% equation %}A{% endequation %} מסדר {% equation %}2\times2{% endequation %} היא אוניטרית אם ורק אם היא מהצורה

{% equation %}\left[\begin{array}{cc}a & b\\-e^{i\theta}\overline{b} & e^{i\theta}\overline{a}\end{array}\right]{% endequation %}

כך ש-{% equation %}\left|a\right|^{2}+\left|b\right|^{2}=1{% endequation %}.

במקרה של מטריצה עם מקדמים ממשיים העסק הופך לפשוט מאוד: במקרה הזה {% equation %}\overline{a}=a,\overline{b}=b{% endequation %} ואילו {% equation %}e^{i\theta}{% endequation %} יכול להיות רק 1 או {% equation %}-1{% endequation %}. לכן נקבל שיש בדיוק שני סוגים של מטריצות אוניטריות ממשיות:

{% equation %}\left[\begin{array}{cc}a & b\\-b & a\end{array}\right]{% endequation %}

או

{% equation %}\left[\begin{array}{cc}a & b\\b & -a\end{array}\right]{% endequation %}

בשני המקרים חייב להתקיים {% equation %}a^{2}+b^{2}=1{% endequation %}.

עכשיו, כל מטריצה כזו מגדירה אופרטור לינארי על {% equation %}\mathbb{R}^{2}{% endequation %}. מה האופרטורים הללו עושים? ראשית כל, השוויון הנחמד {% equation %}a^{2}+b^{2}=1{% endequation %} מזכיר לי את הזהות המתמטית {% equation %}\sin^{2}\theta+\cos^{2}\theta=1{% endequation %}, אז בואו נסמן {% equation %}a=\cos\theta{% endequation %} ו-{% equation %}b=-\sin\theta{% endequation %} (שימו לב שצריך <strong>להוכיח</strong> שזה אפשרי - אשאיר זאת לכם). אז מטריצה מהסוג הראשון היא מהצורה

{% equation %}\left[\begin{array}{cc}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{array}\right]{% endequation %}

יש סיכוי טוב שהמטריצה הזו מוכרת לכם, אבל במקרה שלא, בואו נבין מה המשמעות של כפל בה. מספיק להבין איך היא פועלת על אברי הבסיס הסטנדרטי:

{% equation %}\left[\begin{array}{cc}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{array}\right]\left[\begin{array}{c}1\\0\end{array}\right]=\left[\begin{array}{c}\cos\theta\\\sin\theta\end{array}\right]{% endequation %}

{% equation %}\left[\begin{array}{cc}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{array}\right]\left[\begin{array}{c}0\\1\end{array}\right]=\left[\begin{array}{c}-\sin\theta\\\cos\theta\end{array}\right]{% endequation %}

אני מתעצל לצייר את זה, אבל ציירו! השוויון הראשון אומר שהוקטור האופקי שפונה "ימינה" (לצד החיובי של ציר {% equation %}x{% endequation %}) עובר לוקטור שיוצר זווית של {% equation %}\theta{% endequation %} <strong>מעל</strong> הכיוון החיובי של ציר {% equation %}x{% endequation %}. הוקטור שפונה "למעלה" עובר לוקטור שיוצר זווית {% equation %}\theta{% endequation %} <strong>משמאל</strong> לכיוון החיובי של ציר {% equation %}y{% endequation %}, ובסך הכל המטריצה <strong>מסובבת</strong> את שני הוקטורים הללו בזווית {% equation %}\theta{% endequation %} <strong>נגד כיוון השעון</strong>. מכיוון שהיא עושה זאת לוקטורים של בסיס כלשהו למרחב, זה מה שהיא עושה לכל וקטור - זוהי מטריצת סיבוב בזווית {% equation %}\theta{% endequation %} (ובחרתי את {% equation %}a{% endequation %} להיות {% equation %}\cos\theta{% endequation %} ואת {% equation %}b{% endequation %} להיות {% equation %}-\sin\theta{% endequation %} כדי לקבל סיבוב במובן שאנחנו רגילים אליו - אם הייתי בוחר, למשל {% equation %}a=\sin\theta{% endequation %} ו-{% equation %}b=\cos\theta{% endequation %} עדיין הייתי מקבל סיבוב, אבל חשבו מה תהיה הזווית ומה יהיה הכיוון של הסיבוב).

מי שעדיין לא משוכנע יכול לכתוב במפורש מה המטריצה עושה על וקטור כללי, אבל כזה שנכתב בצורה קוטבית, של רדיוס וזווית עם הכיוון החיובי של ציר {% equation %}x{% endequation %}:

{% equation %}\left[\begin{array}{cc}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{array}\right]\left[\begin{array}{c}r\cos t\\r\sin t\end{array}\right]=\left[\begin{array}{c}r\cos\theta\cos t-r\sin\theta\sin t\\r\sin\theta\cos t+r\sin t\cos\theta\end{array}\right]=\left[\begin{array}{c}r\cos\left(t+\theta\right)\\r\sin\left(t+\theta\right)\end{array}\right]{% endequation %}

כאשר המעבר האחרון נובע מהזהויות הטריגונומטריות הסטנדרטיות על סכום זוויות, וכעת אפשר לראות בבירור שהכפל במטריצה סובב את הוקטור בזווית של {% equation %}\theta{% endequation %}.

אם כן, הבנו מה עושה <strong>כל</strong> מטריצה אוניטרית מהצורה {% equation %}\left[\begin{array}{cc}a & b\\-b & a\end{array}\right]{% endequation %}. מה עם מטריצות מהצורה השניה? יש כמה דרכים להבין מה הן עושות, אבל בואו נתחיל מדרך שבה כדאי לנקוט תמיד עם מטריצות לא ברורות - ננסה ללכסן. המטריצה שלנו, כזכור, היא מהצורה

{% equation %}\left[\begin{array}{cc}a & b\\b & -a\end{array}\right]{% endequation %}

כאשר {% equation %}a^{2}+b^{2}=1{% endequation %}. הפולינום האופייני, אם כן, הוא

{% equation %}\left(a-x\right)\left(-a-x\right)-b^{2}=x^{2}-a^{2}-b^{2}=x^{2}-1{% endequation %}

והשורשים שלו הם 1 ו-{% equation %}-1{% endequation %}. מה אומר ערך עצמי 1? שיש תת-מרחב ממימד 1 - קו ישר העובר דרך הראשית - שהאופרטור <strong>מקבע</strong> - משאיר במקום ללא שינוי. ומה זה ערך עצמי {% equation %}-1{% endequation %}? זהו קו ישר שהאופרטור מעביר כל נקודה בו אל הנגדי שלה - הנקודה האחרת על אותו קו שמרחקה מהראשית זהה. נסו לצייר את זה ותראו (אני מקווה) חיש קל שהאופרטור הזה הוא אופרטור של <strong>שיקוף</strong> ביחס לציר שהוא הישר שהאופרטור מקבע. בואו נמצא אותו על ידי כך שנמצא וקטור עצמי שמתאים לערך העצמי 1. לשם כך צריך לפתור את מערכת המשוואות הלינארית

{% equation %}\left[\begin{array}{cc}a-1 & b\\b & -a-1\end{array}\right]\left[\begin{array}{c}x\\y\end{array}\right]=\left[\begin{array}{c}0\\0\end{array}\right]{% endequation %}

נניח ש-{% equation %}b\ne0{% endequation %} ונפתור אותה עם דירוג סטנדרטי, תוך שימוש בכך ש-{% equation %}a^{2}+b^{2}=1{% endequation %}:

{% equation %}\left[\begin{array}{cc}a-1 & b\\b & -a-1\end{array}\right]\to\left[\begin{array}{cc}-1 & b+\frac{a\left(a+1\right)}{b}\\b & -a-1\end{array}\right]\to\left[\begin{array}{cc}1 & -\frac{1+a}{b}\\b & -\left(1+a\right)\end{array}\right]\to\left[\begin{array}{cc}1 & -\frac{1+a}{b}\\0 & 0\end{array}\right]{% endequation %}

מכאן נקבל שכל פתרון של המשוואה הוא מהצורה {% equation %}\left(\frac{1+a}{b}t,t\right){% endequation %}. אם נבחר, לצורך נוחות, {% equation %}t=b{% endequation %} נקבל את היוצר {% equation %}\left(1+a,b\right){% endequation %}. בדקו ישירות כדי לראות שהוא אכן וקטור עצמי!

אם תחזרו ל<a href="http://www.gadial.net/2011/11/29/eigenvalues_intro/">אחד הפוסטים המוקדמים</a> שלי על אלגברה לינארית תראו שכבר חישבנו פעם במפורש את המטריצה עבור אופרטור שיקוף, אבל הגענו לתוצאה שנראית מפחידה בהרבה. מטריצת השיקוף דרך ציר שנפרש על ידי {% equation %}\left(x,y\right){% endequation %} הייתה

{% equation %}\frac{1}{x^{2}+y^{2}}\left[\begin{array}{cc}x^{2}-y^{2} & 2xy\\2xy & y^{2}-x^{2}\end{array}\right]{% endequation %}

ומה שראינו עכשיו הוא שאם {% equation %}\left(x-1\right)^{2}+y^{2}=1{% endequation %} אז המטריצה שמתקבלת היא מהצורה

{% equation %}\left[\begin{array}{cc}x-1 & y\\y & 1-x\end{array}\right]{% endequation %}

שהיא נחמדה יותר, אבל לא תמיד {% equation %}\left(x-1\right)^{2}+y^{2}=1{% endequation %} ולא פשוט למצוא {% equation %}\left(x,y\right){% endequation %} שמקיימים את זה אם נתון לנו הישר שאנו רוצים לשקף דרכו.

בואו ננסה להבין את האופרטור הזה בצורה נוספת, כפי שעשינו עבור סיבוב - לכתוב הכל בצורה טריגונומטרית ולראות מה מקבלים:

{% equation %}\left[\begin{array}{cc}\cos\theta & \sin\theta\\\sin\theta & -\cos\theta\end{array}\right]\left[\begin{array}{c}r\cos t\\r\sin t\end{array}\right]=\left[\begin{array}{c}r\cos\theta\cos t+r\sin\theta\sin t\\r\sin\theta\cos t-r\sin t\cos\theta\end{array}\right]=\left[\begin{array}{c}r\cos\left(\theta-t\right)\\r\sin\left(\theta-t\right)\end{array}\right]{% endequation %}

זה מזכיר סיבוב, אבל זה לא סיבוב בגלל שהזווית של הוקטור המקורי, {% equation %}t{% endequation %}, הפכה למינוס {% equation %}t{% endequation %}. קצת חשבון מראה שעבור {% equation %}t=\frac{\theta}{2}{% endequation %} נקבל נקודות שבת של האופרטור, ולכן הפעולה שהאופרטור מבצע היא שיקוף ביחס לציר שהזווית שלו עם הכיוון החיובי של ציר {% equation %}x{% endequation %} היא {% equation %}\frac{\theta}{2}{% endequation %}.

כל החישובים הללו מראים את שלל הדרכים שבהן ניתן להגיע למסקנה הבאה: האופרטורים הלינאריים היחידים על {% equation %}\mathbb{R}^{2}{% endequation %} שמשמרים זווית ואורך הם סיבובים ושיקופים. זו לא תוצאה מובנת מאליה, ולדעתי זה יפה למדי איך שאפשר להגיע אליה בהתבסס על מה שאנחנו כבר יודעים על טרנספורמציות אוניטריות וקצת חשבונות.

אחרי שסיימנו עם המשחקים והדוגמאות מגיעה מאליה השאלה - מה הלאה? מה האתגר האמיתי שלנו? התשובה היא שהגיע הזמן לנסות להבין איך המושג של לכסינות של מטריצות משתלב עם מרחבי מכפלה פנימית, ובניסוח קונקרטי - בהינתן אופרטור לינארי מעל מרחב מכפלה פנימית, מתי קיים למרחב בסיס <strong>אורתונורמלי</strong> שבו האופרטור מיוצג על ידי מטריצה ריבועית, כלומר מתי קיים למרחב בסיס אורתונורמלי שמורכב כולו מוקטורים עצמיים של האופרטור? בשאלה הזו נעסוק בפוסט הבא בנושא.
