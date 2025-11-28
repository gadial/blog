---
title: "בעקבות השערת הרצף, חלק ג': רלטיביזציה ועקרון הרפלקציה"
layout: post
categories:
  - תורת הקבוצות
tags:
  - השערת הרצף
image: "/assets/img/main/forcing.png"
---


<h2>מבוא</h2>

המטרה שלנו בסדרת הפוסטים הזו היא להוכיח שהשערת הרצף בלתי תלויה במערכת האקסיומות ZFC, שהצגתי בפוסט הקודם. אסטרטגיית ההוכחה הכללית היא זו: מתוך היקום הגדול של תורת הקבוצות אנחנו הולכים לבנות שני "יקומים זעירים", כך שבשני היקומים הזעירים הללו ZFC מתקיימת במובן מסוים, אבל באחד מהם השערת הרצף היא נכונה בזמן שביקום השני השערת הרצף אינה נכונה. זה יסיים את ההוכחה של אי-תלות השערת הרצף, כי אם היה אפשר להוכיח את השערת הרצף מתוך ZFC המשמעות של כך הייתה ש<strong>בכל</strong> יקום שבו ZFC מתקיימת, גם השערת הרצף מתקיימת (ובדומה גם עבור הפרכה).

זו אסטרטגיה פשוטה אבל בניסוח הפשטני והלא פורמלי שלה היא גם מבלבלת. מה זה בכלל אומר, "יקום זעיר"? זה נשמע ממש מטופש. אז הנה הסבר קצת יותר מפורט.

בפוסט שלי על <a href="https://gadial.net/2012/06/17/first_order_logic/">לוגיקה מסדר ראשון</a> דיברתי על מושג שנקרא "מודל" עבור קבוצת אקסיומות. אני אחזור על זה בקצרה. תורה מסדר ראשון, כמו ZFC מתחילה עם קבוצה של סימני יחס, סימני פונקציה וסימני קבועים, ואז בונים בעזרת הסימונים הללו פסוקים, ולבסוף אוספים חלק מהפסוקים יחד לקבוצה של <strong>אקסיומות</strong> עבור התורה. דווקא ZFC היא לא הדוגמא הכי אינפורמטיבית לנושא, כי יש בה רק שני סימני יחס: {% equation %}\in{% endequation %} ו-{% equation %}={% endequation %} ואין בה בכלל סימני פונקציה וסימני קבועים. יותר מכך - עם ZFC יש לנו איזו הנחה אינטואיטיבית שיש "יקום יחיד" ש-ZFC אמורה לתאר. אז בואו ניקח דוגמא שונה, מהעולם של <strong>תורת החבורות</strong> (שלא חייבים להכיר בשביל הפוסט הזה).

בשפה של תורת החבורות סימן היחס היחיד הוא {% equation %}={% endequation %}, אבל יש לנו סימן פונקציה, {% equation %}f{% endequation %} ("כפל") וסימן קבוע {% equation %}e{% endequation %} ("יחידה") והאקסיומות הן

<ol> <li>{% equation %}\forall a\forall b\forall c\left(f\left(a,f\left(b,c\right)\right)=f\left(f\left(a,b\right),c\right)\right){% endequation %}</li>


<li>{% equation %}\forall a\left(f\left(a,e\right)=a\wedge f\left(e,a\right)=a\right){% endequation %}</li>


<li>{% equation %}\forall a\exists b\left(f\left(a,b\right)=e\right){% endequation %}</li>

</ol>

בתור קיצור, במקום לכתוב {% equation %}f\left(a,b\right){% endequation %} אנחנו כותבים {% equation %}a\cdot b{% endequation %} או אפילו סתם {% equation %}ab{% endequation %}, מה שמפשט את האקסיומות שהופכות להיות 

<ol> <li>לכל {% equation %}a,b,c{% endequation %}: {% equation %}\left(ab\right)c=a\left(bc\right){% endequation %} .</li>


<li>לכל {% equation %}a{% endequation %}: {% equation %}a\cdot e=e\cdot a=a{% endequation %}.</li>


<li>לכל {% equation %}a{% endequation %} קיים {% equation %}b{% endequation %} כך ש-{% equation %}ab=e{% endequation %}.</li>

</ol>

מה שעושים עכשיו הוא להתחיל להסתכל על <strong>מבנים</strong>: מבנה הוא קבוצה {% equation %}\mathcal{M}{% endequation %} של איברים, ובנוסף "פרשנות" שמתאימה לכל סימן יחס בשפה יחס מעל {% equation %}\mathcal{M}{% endequation %} (חוץ מאשר סימן היחס {% equation %}={% endequation %} שתמיד מייצג שוויון), לכל סימן פונקציה מתאים פונקציה מעל {% equation %}\mathcal{M}{% endequation %} ולכל סימן קבוע מתאים קבוע מתוך {% equation %}\mathcal{M}{% endequation %}. למשל, עבור תורת החבורות, אפשר לקחת {% equation %}\mathcal{M}=\mathbb{Z}{% endequation %} ולהתאים ל-{% equation %}f{% endequation %} את הפונקציה {% equation %}+{% endequation %} (חיבור רגיל) ול-{% equation %}e{% endequation %} להתאים את האיבר {% equation %}0{% endequation %}.

אם נעשה את זה, ונסתכל על שלוש האקסיומות שכתבתי קודם, נראה שהן כולן מתקיימות (כלומר ערך האמת שלהן הוא T) כאשר מפרשים את הסימנים באופן שתיארתי, והכמתים שבפסוקים רצים על האיברים של {% equation %}\mathcal{M}{% endequation %} (כלומר, כשכתוב {% equation %}\forall a{% endequation %} הכוונה היא "לכל {% equation %}a\in\mathbb{Z}{% endequation %}"). במקרה כזה אומרים ש-{% equation %}\mathcal{M}{% endequation %} הוא <strong>מודל</strong> של קבוצת האקסיומות.

עוד מודלים עבור אותן אקסיומות: {% equation %}\mathbb{R}{% endequation %} עם פעולת החיבור הרגילה ו-{% equation %}e=0{% endequation %}; {% equation %}\mathbb{Q}\backslash\left\{ 0\right\} {% endequation %} עם פעולת הכפל הרגיל ו-{% equation %}e=1{% endequation %}; מרחב המטריצות ההפיכות מסדר {% equation %}2\times2{% endequation %} מעל הממשיים, {% equation %}Gl_{2}\left(\mathbb{R}\right){% endequation %} עם פעולת כפל המטריצות הרגילה ו-{% equation %}e=I{% endequation %}, וכן הלאה. אפשר כמובן גם להציע מבנים שלא יעברו את המחסום של האקסיומות: למשל {% equation %}\mathbb{N}{% endequation %} עם פעולת החיבור הרגילה לא יקיים את האקסיומה השלישית; {% equation %}\mathbb{Z}{% endequation %} עם פעולת החיבור הרגילה ו-{% equation %}e=1{% endequation %} לא יקיים את האקסיומה השניה; ו-{% equation %}\mathbb{Z}{% endequation %} עם פעולת החיסור במקום חיבור לא יקיים את 1. בכל המקרים הללו יש לנו מבנה לגיטימי שפשוט אינו מודל של קבוצת האקסיומות.

עכשיו, הבה ונתבונן על הפסוק הבא:

<ul> <li>{% equation %}\forall a\forall b\left(f\left(a,b\right)=f\left(b,a\right)\right){% endequation %}</li>

</ul>

כלומר, לכל {% equation %}a,b{% endequation %} מתקיים {% equation %}ab=ba{% endequation %}. זה פסוק שמתקיים על ידי {% equation %}\mathbb{Z}{% endequation %} ופעולת החיבור הרגילה, אבל לא מתקיים על ידי {% equation %}Gl_{2}\left(\mathbb{R}\right){% endequation %}. משני אלו אנו מקבלים שמערכת ההוכחה הרגילה שלנו לא יכולה להוכיח את הפסוק הזה מתוך האקסיומות. הסיבה לכך היא שמערכת ההוכחה הרגילה שלנו מקיימת משהו שנקרא <strong>משפט הנאותות</strong>; הוא אומר שאם קבוצת אקסיומות מוכיחה טענה כלשהי, אז נובע מכך שהיא <strong>גוררת אותה לוגית</strong>: כלומר, שכל מודל של האקסיומות הוא גם מודל של הטענה. גם את זה <a href="https://gadial.net/2013/02/23/first_order_logic_proof_system/">תיארתי פה כבר</a> בעבר.

אם כן, בהקשר של תורת החבורות נראה לנו די טבעי שיש לאותה מערכת אקסיומות כמה מודלים שונים - כל מודל הוא חבורה אחרת, וברור לנו שיש המון חבורות בעולם. אבל כשזה מגיע ל-ZFC אולי קצת יותר קשה לעכל את זה כי אנחנו חושבים על ZFC בתור המערכת שבאה לתאר את "כל המתמטיקה" ולכן לכאורה צריך להיות לה רק מודל יחיד, שהוא "כל המתמטיקה". מילת המפתח כאן היא "לכאורה", לא צריך להניח את זה.

בעיה אחרת היא שעד עכשיו התייחסתי אל מבנה בתור <strong>קבוצה</strong>, אבל מלכתחילה העולם המתמטי שעליו אנחנו מדברים בתורת הקבוצות הוא גדול מכדי להיות קבוצה - הוא מה שקראנו לו <strong>מחלקה</strong>. אז הדבר הראשון שאני רוצה לעשות הוא לעזוב את העולם הגדול והמסובך הזה ולבסס את ההוכחה שלנו על מודלים <strong>זעירים</strong> - מודלים שהם קבוצות, וקבוצות קטנות ככל שרק אפשר: אקסיומת האינסוף מחייבת אותן להיות אינסופיות, אבל הן הולכות להיות <strong>בנות מניה</strong>, כלומר האינסוף הקטן ביותר. אני נזהר מאוד לא לומר שהקבוצות הללו יהיו מודלים של ZFC; כפי שנראה בהמשך, זה יהיה <strong>טיפה</strong> יותר מסובך מזה. אבל אני מקווה שזה לפחות מסביר את הבחירה שלי, כשאני מדבר באופן לא פורמלי, לדבר על "יקום זעיר" שבו ZFC מתקיימת.

בואו נעבור לדבר מתמטיקה בצורה יותר קונקרטית.

<h2>רלטיביזציה ורפלקציה</h2>

הכלי הטכני הבסיסי שאנחנו מסתמכים עליו נקרא <strong>רלטיביזציה</strong> של נוסחאות. הרעיון הוא לקחת נוסחה כללית {% equation %}\phi{% endequation %} בשפה של ZFC ולקחת משתנה {% equation %}M{% endequation %} (משתנה שבא לתאר קבוצה) ולשנות את {% equation %}\phi{% endequation %} כך שבכל פעם שבה מופיע כמת, הטווח של הכמת הזה יהיה רק אברי הקבוצה {% equation %}M{% endequation %}. בצורה הזו הנוסחה הכללית {% equation %}\phi{% endequation %} הופכת לנוסחה {% equation %}\phi|_{M}{% endequation %} שהיא <strong>יחסית</strong> ל-{% equation %}M{% endequation %}.

פורמלית:

<ul> <li>אם {% equation %}\phi=\forall x\varphi{% endequation %} אז {% equation %}\phi|_{M}=\forall x\left(x\in M\to\varphi\right){% endequation %} </li>


<li>אם {% equation %}\phi=\exists x\varphi{% endequation %} אז {% equation %}\phi|_{M}=\exists x\left(x\in M\wedge\varphi\right){% endequation %} </li>

</ul>

כלומר, במקרה של {% equation %}\forall{% endequation %} אנחנו מצמצמים את הדרישות שלנו מ-{% equation %}\varphi{% endequation %}: במקום ש-{% equation %}\varphi{% endequation %} יתקיים לכל איבר, הוא צריך להתקיים רק לאיברים של {% equation %}M{% endequation %}. עבור {% equation %}\exists{% endequation %} אנחנו מחמירים את הדרישות שלנו: במקום שהוא סתם יתקיים ל-{% equation %}x{% endequation %} כלשהו, אנחנו מוסיפים את הדרישה ש-{% equation %}x\in M{% endequation %}.

בואו נראה דוגמא. אחת מהאקסיומות הפשוטות ביותר של ZFC היא אקסיומת הזיווג:

{% equation %}\phi=\forall x\forall y\exists A\left(x\in A\wedge y\in A\right){% endequation %}

ממנה נקבל את האקסיומה היחסית ל-{% equation %}M{% endequation %}:

{% equation %}\phi|_{M}=\forall x\left(x\in M\to\forall y\left(y\in M\to\exists A\left(A\in M\wedge x\in A\wedge y\in A\right)\right)\right){% endequation %}

עכשיו הטרמינולוגיה שדיברתי עליה קודם עושה קאמבק: אם {% equation %}\phi|_{M}{% endequation %} מקבלת ערך T אז אומרים על זה ש-{% equation %}M{% endequation %} הוא "מודל" של {% equation %}\phi{% endequation %}, אבל שימו לב שזו סיטואציה שונה ממה שדיברנו עליה קודם: קודם היה לנו פסוק {% equation %}\phi{% endequation %} ואז הבאנו ממקור חיצוני מבנה {% equation %}\mathcal{M}{% endequation %} שיהיה מודל שלו; הפעם {% equation %}M{% endequation %} הוא <strong>משתנה</strong> ולכן הערך שלו נקבע כשאנחנו מסתכלים על השמה כלשהי למשתנים של הפסוק. זה לא משהו שבא "מבחוץ". אבל אפשר לנקוט בגישה שמשלבת את הטוב שבשני העולמות: אם יש לנו קבוצה קונקרטית {% equation %}M{% endequation %} ופסוק {% equation %}\phi{% endequation %} נהוג לסמן {% equation %}M\models\phi{% endequation %} אם {% equation %}M{% endequation %} היא מודל של {% equation %}\phi{% endequation %} (כלומר, הפסוק {% equation %}\phi{% endequation %} מסתפק כאשר הכמתים שמופיעים בו רצים על אברי {% equation %}M{% endequation %}); זה אותו דבר כמו לומר שהנוסחה {% equation %}\phi|_{M}{% endequation %} מסתפקת כאשר אנו מציבים את הקבוצה {% equation %}M{% endequation %} בתוך המשתנה {% equation %}M{% endequation %} שמופיע ב-{% equation %}\phi|_{M}{% endequation %}. יש כאן כפל משמעות מזעזע בסימון: {% equation %}M{% endequation %} מייצג גם קבוצה, וגם את "המשתנה שבו מציבים את הקבוצה". אני לא חושש שזה יגרום לבלבול, כי אפשר להבין מהי {% equation %}M{% endequation %} מתוך ההקשר: האם היא קבוצה, או סימבול שמופיע בתוך נוסחה.

עכשיו יש לנו מספיק טרמינולוגיה כדי שאוכל להציג את "מטרת העל" שלנו בפוסט הזה: אני רוצה שנוכיח שלכל פסוק {% equation %}\phi{% endequation %} קיימת קבוצה {% equation %}M{% endequation %} שהיא פשוטה במיוחד: היא <strong>בת מניה</strong> והיא <strong>טרנזיטיבית</strong>, כך שמתקיים {% equation %}\phi\leftrightarrow\phi|_{M}{% endequation %}. כאן "מתקיים" פירושו שהנוסחה {% equation %}\phi\leftrightarrow\phi|_{M}{% endequation %}, כאשר מציבים את {% equation %}M{% endequation %} בתוך המשתנה {% equation %}M{% endequation %} שבה, היא בעלת ערך T (המשתנה החופשי היחיד בה היה {% equation %}M{% endequation %} ולכן מרגע שהצבנו ערך בתוכו קיבלנו פסוק שערך האמת שלו נקבע באופן יחיד). ה-{% equation %}M{% endequation %} הזו היא מה שכיניתי קודם "יקום זעיר". שימו לב שזה יקום זעיר קונקרטי שמתאים לפסוק אחד ויחיד {% equation %}\phi{% endequation %}; זה לא יקום שמתאים בו זמנית לכל ZFC (וכפי שנראה בהמשך, גם לא נבנה יקום שמתאים בו זמנית <strong>לכל</strong> ZFC, אבל לא נצטרך).

הקיום של {% equation %}M{% endequation %} הזו לכל {% equation %}\phi{% endequation %} נקרא <strong>עקרון השיקוף</strong>; האינטואיציה היא שהתכונות של יקום הקבוצות הגדול משתקפות איכשהו באופן חלקי ביקום הקבוצות הזעיר {% equation %}M{% endequation %}. מרגע שיהיה לנו את היכולת לבנות {% equation %}M{% endequation %}-ים שכאלו, האתגר הנוסף, והמרכזי, יהיה <strong>להרחיב</strong> את ה-{% equation %}M{% endequation %}-ים הללו בצורה שבה מובטח שהשערת הרצף מתקיימת או מובטח שהיא לא מתקיימת, אבל לא נעסוק בזה בפוסט הזה.

בואו ניגש לעיקר העבודה הטכנית. האזהרה שלי היא שמדובר <strong>בהרבה</strong> עבודה טכנית; אני אוכיח סדרה של טענות עד שאוכיח את עקרון השיקוף. אף טענה לא חשובה בפני עצמה ולא אשתמש בהן בהמשך, וההוכחות שלהן הן אמנם נחמדות אבל לא מאירות עיניים - הן משהו שבספרים בעיקר מחפפים כי הקורא יכול להשלים את הפרטים בעצמו (ואני אולי מטרחן אותן בהמשך שלא לצורך). אז בהחלט אפשר לדלג על ההמשך הישר אל הפוסט הבא אם לא רוצים את הפרטים הטכניים; בפוסט הבא אני אחזור על כל מה שרלוונטי.

<h2>רלטיביזציה ואיזומורפיזם</h2>

בואו ניקח נוסחה {% equation %}\phi\left(x_{1},\ldots,x_{n}\right){% endequation %} כלשהי. ההבדל בין "נוסחה כלשהי" ובין "פסוק" הוא שפסוק הוא מקרה פרטי של נוסחה שאין לה משתנים חופשיים; כשאני כותב את ה-{% equation %}x_{i}{% endequation %}-ים הללו בסוגריים אני מתכוון שהמשתנים החופשיים של {% equation %}\phi{% endequation %} נמנים על {% equation %}x_{1},\ldots,x_{n}{% endequation %} (לאו דווקא שכל אחד מה-{% equation %}x_{i}{% endequation %}-ים הזה הוא משתנה חופשי של {% equation %}\phi{% endequation %}, רק שכל המשתנים החופשיים של {% equation %}\phi{% endequation %} נמנים איתם).

המטרה שלי היא להבין מתי הרלטיביזציה של {% equation %}\phi{% endequation %} לשתי קבוצות שונות {% equation %}M,N{% endequation %} היא "אותו דבר", כחלק מהמאמץ שלי למצוא קבוצה "קנונית נחמדה" (בת מניה וטרנזיטיבית) שאליה נעשה רלטיביזציה. הכלי הסטנדרטי בלוגיקה בהקשר הזה הוא מה שנקרא <strong>איזומורפיזם של מבנים</strong>, שזו פונקציה {% equation %}f:M\to N{% endequation %} שהיא חח"ע ועל ומשמרת את פרשנות יחסי הסדר/קבועים/פונקציות. בשפה שלנו יש רק את יחס הסדר {% equation %}\in{% endequation %} אז הדרישה מ-{% equation %}f{% endequation %}, בנוסף לזה שהיא חח"ע ועל, היא רק שיתקיים {% equation %}x\in y\iff f\left(x\right)\in f\left(y\right){% endequation %}.

בהינתן {% equation %}f{% endequation %} כזו, הטענה שאנחנו רוצים להוכיח היא זו: לכל {% equation %}a_{1},\ldots,a_{n}\in M{% endequation %}, מתקיים

{% equation %}\phi|_{M}\left(a_{1},\ldots,a_{n}\right)\leftrightarrow\phi|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a_{n}\right)\right){% endequation %}

במילים (שיוצאות הרבה יותר מסורבלות): אם נסתכל על הנוסחה שמתקבלת מכך שלוקחים את {% equation %}\phi{% endequation %}, יוצרים שני עותקים שלו, מבצעים רלטיביזציה לשני העותקים, פעם עם המשתנה {% equation %}M{% endequation %} ופעם עם המשתנה {% equation %}N{% endequation %}, מציבים את הקבוצה {% equation %}M{% endequation %} במשתנה הראשון ואת הקבוצה {% equation %}N{% endequation %} במשתנה השני, ואז ניגשים אל המשתנים החופשיים של העותק הראשון ומציבים בהם {% equation %}a_{1},\ldots,a_{n}{% endequation %} ובמשתנים החופשיים של העותק השני מציבים {% equation %}f\left(a_{1}\right),\ldots,f\left(a_{n}\right){% endequation %} ובסוף לוקחים את שני העותקים ומחברים אותם עם הקשר {% equation %}\leftrightarrow{% endequation %} - אחרי כל המהומה הזו מתקבלת נוסחה אחת עם הצבה עבורה, וערך האמת של הנוסחה בהצבה הזו הוא T.

כדי להוכיח טענות כאלו משתמשים בכלי ההוכחה האהוב עלינו מלוגיקה מתמטית: אינדוקציה על <strong>המבנה</strong> של הנוסחה. כזכור, נוסחה היא או <strong>אטומית</strong> מהצורה {% equation %}x_{1}=x_{2}{% endequation %} או {% equation %}x_{1}\in x_{2}{% endequation %}, או שהיא מהצורה {% equation %}\neg\psi{% endequation %}, או {% equation %}\psi_{1}\to\psi_{2}{% endequation %}, או {% equation %}\forall\psi_{1}{% endequation %}, או... או שום דבר נוסף, בעצם; אפשר להראות שכל קשר וכל כמת אחר ניתן להחלפה באלו הקיימים לקבל נוסחה שקולה, ומספיק להוכיח את הטענה עבור הנוסחה השקולה הזו (אבל איך אומרים? זה <strong>תרגיל טוב</strong> להוכיח גם עבור הקשרים והכמתים האחרים).

אם {% equation %}\phi{% endequation %} היא מהצורה {% equation %}x_{1}=x_{2}{% endequation %} הטענה מאוד פשוטה: רלטיביזציה במקרה הזה לא עושה כלום (כי אין כמתים) ולכן אנחנו רוצים להוכיח שלכל {% equation %}a_{1},a_{2}\in M{% endequation %} מתקיים {% equation %}\left(a_{1}=a_{2}\right)\iff\left(f\left(a_{1}\right)=f\left(a_{2}\right)\right){% endequation %} , וזה נובע מיידית מכך ש-{% equation %}f{% endequation %} פונקציה חח"ע.

אם {% equation %}\phi{% endequation %} היא מהצורה {% equation %}x_{1}\in x_{2}{% endequation %} אז באופן דומה צריך לראות ש-{% equation %}\left(a_{1}\in a_{2}\right)\iff\left(f\left(a_{1}\right)\in f\left(a_{2}\right)\right){% endequation %} וזה נובע ישירות מהדרישה ש-{% equation %}f{% endequation %} היא איזומורפיזם (מכאן הדרישה הזו הגיעה, כמובן). אז לטפל במקרי הבסיס סיימנו.

עכשיו, נניח ש-{% equation %}\phi=\left(\neg\psi\right){% endequation %}, אז

{% equation %}\phi|_{M}=\left(\neg\psi\right)|_{M}=\neg\left(\psi|_{M}\right){% endequation %}

כי כאשר מבצעים רלטיביזציה לנוסחה, זה משפיע רק על המקומות שבהם מופיע כמת, לא על הקשר הלוגי החיצוני. עכשיו, אנחנו מניחים באופן אינדוקטיבי שהטענה כבר הוכחה עבור {% equation %}\psi{% endequation %}, כלומר

{% equation %}\psi|_{M}\left(a_{1},\ldots,a_{n}\right)\leftrightarrow\psi|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a_{n}\right)\right){% endequation %}

בגלל השקילות בין שני האגפים (שמשמעותה שבהצבה שעליה אנו מסתכלים שניהם מקבלים את אותו ערך אמת), אם נוסיף {% equation %}\neg{% endequation %} בהתחלה של כל אחד מהם נהפוך את ערך האמת שהוא מקבל, אבל שניהם עדיין יקבלו את אותו ערך אמת ולכן הנוסחה כולה עדיין תהיה T.

עבור {% equation %}\phi=\left(\psi_{1}\to\psi_{2}\right){% endequation %} קורה משהו דומה - רלטיביזציה משפיעה רק על תתי-הפסוקים, כלומר

{% equation %}\phi|_{M}=\left(\psi_{1}\to\psi_{2}\right)|_{M}=\left(\psi_{1}|_{M}\to\psi_{2}|_{M}\right){% endequation %}

נאחד את קבוצות המשתנים החופשיים שמופיעים ב-{% equation %}\psi_{1}{% endequation %} וב-{% equation %}\psi_{2}{% endequation %} ונסמן את קבוצת המשתנים שקיבלנו ב-{% equation %}x_{1},\ldots,x_{n}{% endequation %} (הנה מקום שבו אנחנו משתמשים בזה שהמשתנים שנכתבים בסוגריים עשויים להיות יותר מאשר המשתנים החופשיים של הנוסחה), ניקח ערכים {% equation %}a_{1},\ldots,a_{n}\in M{% endequation %} ונקבל מהנחת האינדוקציה

{% equation %}\psi_{1}|_{M}\left(a_{1},\ldots,a_{n}\right)\leftrightarrow\psi_{1}|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a_{n}\right)\right){% endequation %}

{% equation %}\psi_{2}|_{M}\left(a_{1},\ldots,a_{n}\right)\leftrightarrow\psi_{2}|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a_{n}\right)\right){% endequation %}

משני אלו אנחנו רוצים להסיק ש-

{% equation %}\left(\psi_{1}\to\psi_{2}\right)|_{M}\left(a_{1},\ldots,a_{n}\right)\leftrightarrow\left(\psi_{1}\to\psi_{2}\right)|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a_{n}\right)\right){% endequation %}

כדי להראות את זה צריך להראות ששני האגפים מקבלים את אותו ערך אמת. הדרך היחידה שבה אגף שמאל יכול לקבל F היא אם {% equation %}\psi_{1}|_{M}\left(a_{1},\ldots,a_{n}\right){% endequation %} מקבל T וגם {% equation %}\psi_{2}|_{M}\left(a_{1},\ldots,a_{n}\right){% endequation %} מקבל F, והשקילויות שקיבלנו מהנחת האינדוקציה מראות שבמקרה הזה {% equation %}\psi_{1}|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a_{n}\right)\right){% endequation %} מקבל T ו-{% equation %}\psi_{2}|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a_{n}\right)\right){% endequation %} מקבל F ולכן גם אגף ימין מקבל F בסך הכל והשקילות נשמרת; אותו הדבר אפשר לעשות גם בכיוון השני, אם מניחים שאגף ימין מקבל F.

כל זה הוא בעצם דרך לומר בהרבה מלל משהו שנראה טריוויאלי לגמרי. איפה החלק המסובך של ההוכחה? כמובן, כשמכניסים כמתים לתמונה.

אם כן, נסתכל על {% equation %}\phi=\forall x_{i}\psi\left(x_{1},\ldots,x_{n}\right){% endequation %}. הוספת הכמת ל-{% equation %}\phi{% endequation %} עלולה לגרום לאחד מהמשתנים החופשיים של {% equation %}\psi{% endequation %} להיעלם - להפוך למשתנה קשור, וכזה שכבר לא מציבים בו {% equation %}a_{i}{% endequation %}. בנוסף, רלטיביזציה של {% equation %}\phi{% endequation %} הולכת לשנות אותו: נקבל את

{% equation %}\phi|_{M}=\forall x_{i}\left(x_{i}\in M\to\psi\left(x_{1},\ldots,x_{n}\right)\right){% endequation %}

עכשיו, מה הנחת האינדוקציה נותנת לנו כאן? אנחנו יודעים שלכל {% equation %}a_{1},\ldots,a_{n}\in M{% endequation %} מתקיים

{% equation %}\psi|_{M}\left(a_{1},\ldots,a_{n}\right)\leftrightarrow\psi|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a_{n}\right)\right){% endequation %}

ומה שאנחנו צריכים לעשות הוא להראות שלכל {% equation %}a_{1},\ldots,a_{i-1},a_{i+1},\ldots,a_{n}\in M{% endequation %} מתקיים

{% equation %}\phi|_{M}\left(a_{1},\ldots,a_{n}\right)\leftrightarrow\phi|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a_{n}\right)\right){% endequation %}

נניח שתחת ההשמה שמציבה את הערכים הללו במשתנים (ואת {% equation %}M,N{% endequation %} במשתנים המתאימים שלהם) אגף שמאל מקבל T. אנחנו צריכים להוכיח שגם אגף ימין מקבל T. בשלב הזה אגף ימין הוא

{% equation %}\phi|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a_{n}\right)\right){% endequation %}

או, אם נפתח את ההגדרה של {% equation %}\phi|_{N}{% endequation %}, אגף ימין הוא

{% equation %}\forall x_{i}\left(x_{i}\in N\to\psi|_{N}\left(f\left(a_{1}\right),\ldots,x_{i},\ldots,f\left(a_{1}\right)\right)\right){% endequation %}

זה אומר שכדי להראות שהאגף הזה הוא T, צריך להראות שלכל הצבה של ערך {% equation %}b{% endequation %} ב-{% equation %}x_{i}{% endequation %}, <strong>אם</strong> {% equation %}b\in N{% endequation %} <strong>אז</strong> {% equation %}\psi|_{N}\left(f\left(a_{1}\right),\ldots,b,\ldots,f\left(a_{1}\right)\right)=\text{T}{% endequation %}.

האתגר התקבל! בואו ניקח ערך {% equation %}b{% endequation %} כזה ונניח ש-{% equation %}b\in N{% endequation %} אחרת אין לנו מה לעשות. עכשיו אנחנו סוף כל סוף משתמשים בתכונה של {% equation %}f{% endequation %} שטרם השתמשנו בה: {% equation %}f:M\to N{% endequation %} היא <strong>פונקציה על</strong> ולכן קיים {% equation %}a\in M{% endequation %} כך ש-{% equation %}f\left(a\right)=b{% endequation %}. מכאן שמה שצריך להראות הוא

{% equation %}\psi|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a\right),\ldots,f\left(a_{1}\right)\right)=\text{T}{% endequation %}

עכשיו, בואו ניזכר מה הנחת האינדוקציה נתנה לנו; היא נתנה את 

{% equation %}\psi|_{M}\left(a_{1},\ldots,a_{n}\right)\leftrightarrow\psi|_{N}\left(f\left(a_{1}\right),\ldots,f\left(a_{n}\right)\right){% endequation %}

אז מספיק אם נוכיח שעבור {% equation %}a_{1},\ldots,a_{i-1},a,a_{i+1},\ldots,a_{n}{% endequation %} מתקיים

{% equation %}\psi|_{M}\left(a_{1},\ldots,a_{n}\right)=\text{T}{% endequation %}

לצורך כך, בואו ניזכר בהנחה שהתחלנו איתה את השלב הזה בהוכחה, איפה שכתבתי "אגף שמאל מקבל T". אותו אגף שמאל היה

{% equation %}\phi|_{M}\left(a_{1},\ldots,a_{n}\right){% endequation %}

וכשפותחים את ההגדרה, מקבלים

{% equation %}\forall x_{i}\left(x_{i}\in M\to\psi|_{M}\left(a_{1},\ldots,x_{i},\ldots,a_{n}\right)\right){% endequation %}

ולכן, אם הנוסחה הזו מקבלת ערך T תחת ההשמה הנתונה, היא בפרט מקבלת ערך T אם מציבים ב-{% equation %}x_{i}{% endequation %} את {% equation %}a{% endequation %}. מכיוון ש-{% equation %}a\in M{% endequation %} אז נובע מכך

{% equation %}\psi|_{M}\left(a_{1},\ldots,a,\ldots,a_{n}\right)=\text{T}{% endequation %}

וזה בדיוק מה שרצינו. זה מסיים את הכיוון הזה של ההוכחה; צריך גם להתחיל עם ההנחה שאגף ימין הוא T ולהוכיח שאגף שמאל הוא T אבל זה אותו רעיון, רק קצת קל יותר כי לא צריך להשתמש בכך ש-{% equation %}f{% endequation %} היא על (אלא רק בכך שהיא פונקציה, כלומר מוגדרת לכל {% equation %}M{% endequation %}).

<h2>שובן של הקבוצות הטרנזיטיביות</h2>

עכשיו, כשיש לנו את הכלי החדש של איזומורפיזם, בואו נשתמש בו! הרעיון הוא למצוא לכל מבנה {% equation %}M{% endequation %} מבנה איזומורפי {% equation %}N{% endequation %} שהוא "נחמד". כרגע "נחמד" עבורי יהיה <strong>טרנזיטיבי</strong>. כזכור, קבוצה היא טרנזיטיבית אם כל איבר שלה הוא תת-קבוצה שלה; זו התכונה הבסיסית שמאחורי סודרים, למשל (אבל יש קבוצות טרנזיטיביות שאינן סודרים; סודר צריך להיות גם טרנזיטיבי וגם סדור בסדר טוב).

לא נוכל למצוא דבר כזה עבור <strong>כל</strong> קבוצה {% equation %}M{% endequation %}; בהוכחה נראה מה שהכרחי הוא ש<strong>אקסיומת ההיקפיות</strong> תהיה ניתנת לרלטיביזציה אל {% equation %}M{% endequation %}. מה זה אומר? כזכור, אקסיומת ההיקפיות היא "שתי קבוצות הן שוות אם ורק אם יש להן אותם איברים":

{% equation %}\forall A\forall B\left(\forall x\left(x\in A\leftrightarrow x\in B\right)\to A=B\right){% endequation %}

אז הרלטיביזציה של זה אומרת "לכל {% equation %}A,B\in M{% endequation %} , אם {% equation %}A\cap M=B\cap M{% endequation %} אז {% equation %}A=B{% endequation %}": אין שתי קבוצות שונות ב-{% equation %}M{% endequation %} ש"החלק שלהן שמוכל ב-{% equation %}M{% endequation %}" נראה אותו דבר. או בניסוח אחר: כדי להראות ש-{% equation %}A\ne B{% endequation %} צריך להציג איבר ששייך לאחת הקבוצות אבל לא לשנייה; מובטח לנו שאחד מהאיברים הללו יהיה שייך ל-{% equation %}M{% endequation %}.

לקבוצה {% equation %}M{% endequation %} שמקיימת את התכונה הזו נקרא <strong>היקפית</strong> והטענה היא שלכל קבוצה היקפית קיימת ויחידה קבוצה טרנזיטבית {% equation %}N{% endequation %} כך ש-{% equation %}M\cong N{% endequation %} על פי הגדרת האיזומורפיזם שראינו קודם. ההוכחה לא תהיה קלה, אבל למרבה השמחה היא תהיה כולה "תורת-קבוצתית" באופיה ולא "לוגיקה מסדר ראשון-ית" באופיה כמו הקודמת.

הוכחת היחידות היא קלה יותר, אז נתחיל ממנה. נניח שקיימות {% equation %}N_{1}\ne N_{2}{% endequation %} כך ש-{% equation %}N_{1}\cong M\cong N_{2}{% endequation %}. מטרנזיטיביות האיזומורפיזם נקבל {% equation %}N_{1}\cong N_{2}{% endequation %}; נסמן את האיזומורפיזם הזה ב-{% equation %}g{% endequation %}. מכיוון ש-{% equation %}N_{1}\ne N_{2}{% endequation %} אז {% equation %}g{% endequation %} הוא לא הזהות, כלומר קיים {% equation %}a\in N_{1}{% endequation %} כך ש-{% equation %}g\left(a\right)\ne a{% endequation %}, ובעזרת אקסיומת היסוד אפשר לבחור את {% equation %}a{% endequation %} להיות האיבר המינימלי של {% equation %}N_{1}{% endequation %} ביחס ל-{% equation %}\in{% endequation %} שמקיים את התכונה הזו.

עכשיו משתמשים בטריק די סטנדרטי עבור קבוצות טרנזיטיביות: מכיוון ש-{% equation %}N_{1},N_{2}{% endequation %} טרנזיטיביות, אז {% equation %}a\subseteq N_{1}{% endequation %} ו-{% equation %}g\left(a\right)\subseteq N_{2}{% endequation %}. בפרט, לכל {% equation %}x\in a{% endequation %} מתקיים {% equation %}a\in N_{1}{% endequation %} ולכן {% equation %}g{% endequation %} מוגדר על {% equation %}x{% endequation %}, ומכיוון ש-{% equation %}g{% endequation %} היא איזומורפיזם אז {% equation %}x\in a\iff g\left(x\right)\in g\left(a\right){% endequation %}, כלומר {% equation %}g{% endequation %} היא פונקציה חח"ע ועל בין הקבוצות {% equation %}a,g\left(a\right){% endequation %}. עכשיו, בגלל המינימליות של {% equation %}a{% endequation %}, אנחנו יודעים שלכל {% equation %}x\in a{% endequation %} מתקיים {% equation %}g\left(x\right)=x{% endequation %}, ולכן מסיקים ש-{% equation %}a=g\left(a\right){% endequation %}, וזו סתירה לכך שבחרנו את {% equation %}a{% endequation %} להיות איבר שמקיים {% equation %}g\left(a\right)\ne a{% endequation %}, מה שמסיים את החלק הזה של ההוכחה.

גם חלק ה"קיום" הולך להיות דומה לדברים שראינו כשהתעסקנו עם קבוצות טרנזיטיביות, אבל זה עדיין ידרוש מאיתנו עבודה. הרעיון הוא שבהינתן קבוצה היקפית כלשהי {% equation %}M{% endequation %}, אנחנו יכולים להסתכל על תת-קבוצות של {% equation %}M{% endequation %} שאיזומורפיות לקבוצה טרנזיטיבית, ואז להרכיב מכל האיזומורפיזמים הללו איזומורפיזם אחד גדול של {% equation %}M{% endequation %} עם קבוצה טרנזיטיבית. זו גישה סטנדרטית, אבל היא מצריכה זהירות.

ראשית, בואו נסתכל על אותן תת-קבוצות של {% equation %}M{% endequation %} ש"ביחס אל {% equation %}M{% endequation %} נראות טרנזיטיביות". אם טרנזיטיביות של {% equation %}A\in M{% endequation %} פירושה שלכל {% equation %}a\in A{% endequation %} מתקיים {% equation %}a\subseteq A{% endequation %}, כאן אנו רוצים שיתקיים {% equation %}a\cap M\subseteq A{% endequation %}. מבין הקבוצות ה"נראות טרנזיטיביות" הללו אנחנו מתעניינים רק באלו שאיזומורפיות לקבוצה טרנזיטיבית - אני אקרא לקבוצות הללו "קבוצות נחמדות". אני כמובן רוצה להראות ש-{% equation %}M{% endequation %} עצמה היא נחמדה; הטריק יהיה להסתכל על איחוד כל הקבוצות הנחמדות ב-{% equation %}M{% endequation %}, שאסמן {% equation %}Z{% endequation %}, ולהוכיח שני דברים:

<ul> <li>{% equation %}Z{% endequation %} היא בעצמה קבוצה נחמדה.</li>


<li>{% equation %}Z=M{% endequation %}.</li>

</ul>

דווקא את החלק השני קל להראות. אם {% equation %}Z{% endequation %} נחמדה, אז יש איזומורפיזם {% equation %}f:Z\to N{% endequation %} עבור קבוצה טרנזיטיבית {% equation %}N{% endequation %} כלשהי. עכשיו, אם {% equation %}M\ne Z{% endequation %}, ומכיוון שמלכתחילה {% equation %}Z{% endequation %} היא איחוד של תת-קבוצות של {% equation %}M{% endequation %} ולכן {% equation %}Z\subseteq M{% endequation %}, אנו מקבלים ש- {% equation %}M\backslash Z\ne\emptyset{% endequation %}; ניקח {% equation %}a\in M\backslash Z{% endequation %} מינימלי (ביחס ל-{% equation %}\in{% endequation %}) שמקיים זאת (אפשר, על פי אקסיומת היסוד).

עכשיו נרחיב את האיזומורפיזם {% equation %}f{% endequation %} על ידי ההגדרה {% equation %}f\left(a\right)=\left\{ f\left(x\right)\ |\ x\in a\right\} {% endequation %}; כלומר, הוספנו את {% equation %}a{% endequation %} אל {% equation %}Z{% endequation %}, והוספנו את {% equation %}\left\{ f\left(x\right)\ |\ x\in a\right\} {% endequation %} אל {% equation %}N{% endequation %}. האיבר החדש הזה ב-{% equation %}N{% endequation %} כולל רק איברים של {% equation %}N{% endequation %} ולכן מוכל ב-{% equation %}N{% endequation %} כך שהוספתו לא פוגמת בטרנזיטיביות; את {% equation %}f{% endequation %} הרחבנו על ידי איבר חדש שעובר לאיבר חדש, כך שהפונקציה המתקבלת היא עדיין חח"ע ועל; וכדי להראות שעדיין יש שימור סדר ראשית נשים לב לכך שלא ייתכן ש-{% equation %}a\in x{% endequation %} עבור {% equation %}x\in Z{% endequation %}, כי מכיוון ש-{% equation %}Z{% endequation %} היא קבוצה נחמדה אז {% equation %}a\in x{% endequation %} היה גורר {% equation %}a\in Z{% endequation %}. לכן הדבר היחיד שאפשרי הוא {% equation %}x\in a{% endequation %} עבור {% equation %}x\in Z{% endequation %}, ובסיטואציה כזו {% equation %}f\left(x\right)\in f\left(a\right){% endequation %} על פי ההגדרה, כך שגם יחס הסדר נשמר.

המסקנה היא שההרחבה הזו של {% equation %}Z{% endequation %} היא עדיין קבוצה נחמדה בעצמה, אבל אם {% equation %}Z{% endequation %} היא איחוד כל הקבוצות הנחמדות, היא לא יכולה להיות מוכלת ממש בקבוצה נחמדה; אנו מקבלים, אם כן, ש-{% equation %}Z=M{% endequation %}.

אבל עדיין לא הוכחנו שאיחוד כל הקבוצות הנחמדות הוא קבוצה נחמדה. התוכנית היא כזו: לכל קבוצה נחמדה {% equation %}A\subseteq M{% endequation %} קיימת קבוצה טרנזיטיבית {% equation %}N_{A}{% endequation %} ואיזומורפיזם {% equation %}f_{A}:A\to N_{A}{% endequation %}. עכשיו נבנה את האיחוד {% equation %}\bigcup A{% endequation %}; אני רוצה לומר שהוא איזומרפי אל {% equation %}\bigcup N_{A}{% endequation %} עם האיזומורפיזם {% equation %}\bigcup f_{A}{% endequation %}. עיקר הקושי הוא להראות שהקבוצה {% equation %}\bigcup f_{A}{% endequation %} היא אכן פונקציה, ולא סתם פונקציה אלא איזומורפיזם; אם יש לנו את זה, צריך להראות ש-{% equation %}\bigcup N_{A}{% endequation %} היא קבוצה טרנזיטיבית אבל זה קל - איחוד של קבוצות טרנזיטיביות הוא טרנזיטיבי ישירות מההגדרה.

אז אנחנו מתמקדים ב-{% equation %}f=\bigcup f_{A}{% endequation %}. הקבוצה הזו נוצרת מכך ש"מדביקים ביחד" את כל ה-{% equation %}f_{A}{% endequation %}-ים השונים. החשש הראשון הוא ש-{% equation %}f{% endequation %} לא תהיה בכלל פונקציה; כלומר, שבקבוצה {% equation %}\bigcup f_{A}{% endequation %} יהיו שני איברים {% equation %}\left(a,n_{1}\right),\left(a,n_{2}\right){% endequation %} שהורסים את תכונת ה"יחידות" שמגדירה פונקציה (לכל קלט קיים פלט יחיד). עכשיו, אם יש שני איברים כאלו, הם חייבים להגיע משני {% equation %}A{% endequation %}-ים שונים (כי אם הם היו נובעים מאותו {% equation %}A{% endequation %}, כבר {% equation %}f_{A}{% endequation %} לא הייתה פונקציה). אז ניקח קבוצות {% equation %}A_{1},A_{2}{% endequation %} כלשהן עם איזומורפיזמים {% equation %}f_{A_{1}}:A_{1}\to N_{1}{% endequation %} ו-{% equation %}f_{A_{2}}:A_{2}\to N_{2}{% endequation %} ונוכיח שלכל איבר משותף להן, {% equation %}a\in A_{1}\cap A_{2}{% endequation %}, מתקיים {% equation %}f_{A_{1}}\left(a\right)=f_{A_{2}}\left(a\right){% endequation %}.

בשביל לראות את זה, הנה טענה כללית: אם {% equation %}g:A\to N{% endequation %} הוא איזומורפיזם של קבוצה {% equation %}A\subseteq M{% endequation %} וקבוצה טרנזיטיבית {% equation %}N{% endequation %}, ואם {% equation %}B\subseteq A{% endequation %}, ואם בנוסף לכך {% equation %}B{% endequation %} היא מה שקראתי לו קודם "טרנזיטיבית ביחס ל-{% equation %}M{% endequation %}", אז גם {% equation %}g\left(B\right){% endequation %} הוא קבוצה טרנזיטיבית (תת-קבוצה של {% equation %}N{% endequation %}). כדי לראות את זה, ניקח {% equation %}y\in x\in g\left(B\right){% endequation %} ונוכיח ש-{% equation %}y\in g\left(B\right){% endequation %}: מכיוון ש-{% equation %}x\in g\left(B\right){% endequation %} קיים {% equation %}b_{x}\in B{% endequation %} כך ש-{% equation %}g\left(b_{x}\right)=x{% endequation %}. עכשיו בגלל ש-{% equation %}N{% endequation %} טרנזיטיבית ו-{% equation %}y\in x\in N{% endequation %} אז {% equation %}y\in N{% endequation %} ומכך ש-{% equation %}g{% endequation %} על נקבל שקיים {% equation %}b_{y}\in A{% endequation %} כך ש-{% equation %}g\left(b_{y}\right)=y{% endequation %}. אבל מכיוון ש-{% equation %}g{% endequation %} איזומורפיזם, {% equation %}b_{y}\in b_{x}\iff g\left(b_{y}\right)\in g\left(b_{x}\right){% endequation %}, וקיבלנו שיש שרשרת {% equation %}b_{y}\in b_{x}\in B{% endequation %}. מכיוון ש-{% equation %}b_{y}\in A\subseteq M{% endequation %} ומכיוון ש-{% equation %}B{% endequation %} היא טרנזיטיבית ביחס ל-{% equation %}M{% endequation %}, נובע מכך ש-{% equation %}b_{y}\in B{% endequation %} ולכן {% equation %}y=g\left(b_{y}\right)\in g\left(B\right){% endequation %}, שזה מה שרצינו.

עכשיו אני משתמש במה שהראיתי בפסקה הקודמת זה על החיתוך {% equation %}A_{1}\cap A_{2}{% endequation %}. בשביל זה צריך להראות טרנזיטיביות שלו ביחס ל-{% equation %}M{% endequation %}, וזה נובע מכך שאם {% equation %}a\in A_{1}\cap A_{2}{% endequation %} אז {% equation %}a\in A_{1}{% endequation %} וגם {% equation %}a\in A_{2}{% endequation %} ולכן {% equation %}a\cap M\subseteq A_{1}{% endequation %} וגם {% equation %}a\cap M\subseteq A_{2}{% endequation %} ולכן {% equation %}a\cap M\subseteq A_{1}\cap A_{2}{% endequation %}. מכל זה קיבלנו ש-{% equation %}A_{1}\cap A_{2}{% endequation %} היא אכן קבוצה נחמדה.

איך זה עוזר לנו? בקלות: אני מסתכל על התמונות {% equation %}f_{A_{1}}\left(A_{1}\cap A_{2}\right)\cong A_{1}\cap A_{2}\cong f_{A_{2}}\left(A_{1}\cap A_{2}\right){% endequation %}. קיבלתי ששתי התמונות הללו הן קבוצות טרנזיטיביות שאיזומורפיות זו לזו, ולכן הוכחת היחידות שממנה התחלתי עובדת עבורן - אני מקבל שזו אותה קבוצה, והאיזומורפיזמים, כשמצמצמים אותם ל-{% equation %}A_{1}\cap A_{2}{% endequation %}, הם אותו איזומורפיזם. זה בדיוק מה שרציתי להראות.

כל זה הוכיח רק ש-{% equation %}f=\bigcup f_{A}{% endequation %} היא פונקציה. למה היא חח"ע ועל, ולמה היא משמרת את היחס {% equation %}\in{% endequation %}?

זה ש-{% equation %}f{% endequation %} היא על זה מובן מאליו: הטווח של {% equation %}f{% endequation %} הוא {% equation %}\bigcup N_{A}{% endequation %}, שהיא איחוד של קבוצות שהתקבלו בתור תמונות של {% equation %}A{% endequation %}-ים; התחום של {% equation %}f{% endequation %} הוא איחוד ה-{% equation %}A{% endequation %}-ים הללו, אז לכל איבר ב-{% equation %}\bigcup N_{A}{% endequation %}, המקור שלו נמצא באחד ה-{% equation %}A{% endequation %}-ים הללו וכשאנחנו מפעילים את {% equation %}f{% endequation %} על המקור אנחנו מקבלים את האיבר הזה.

למה {% equation %}f{% endequation %} חח"ע? זה טיפה יותר טריקי. אני צריך להראות שעבור שני {% equation %}a_{1},a_{2}\in\bigcup A{% endequation %} ששונים זה מזה, אם {% equation %}f\left(a_{1}\right)=f\left(a_{2}\right){% endequation %} אז {% equation %}a_{1}=a_{2}{% endequation %}. עכשיו, אם {% equation %}a_{1},a_{2}\in A{% endequation %} עבור קבוצה {% equation %}A{% endequation %} כלשהי זה ברור - ה-{% equation %}f_{A}{% endequation %} על אותה קבוצה היא חח"ע ולכן מקבלים את מה שרוצים. אבל מה אם {% equation %}a_{1}\in A_{1}{% endequation %} ו-{% equation %}a_{2}\in A_{2}{% endequation %} עבור קבוצות שונות?

זה הזמן להחזיר הנחה שלא השתמשתי בה בכלל עד עכשיו - ש-{% equation %}M{% endequation %} היא <strong>היקפית</strong>. כלומר, שאם {% equation %}a_{1},a_{2}\in M{% endequation %} (כמו במקרה שלנו) אז מספיק להראות {% equation %}a_{1}\cap M=a_{2}\cap M{% endequation %} כדי להסיק {% equation %}a_{1}=a_{2}{% endequation %}. במילים אחרות, מספיק להראות שלכל {% equation %}x\in M{% endequation %} מתקיים {% equation %}x\in a_{1}\iff x\in a_{2}{% endequation %}.

כעת, {% equation %}A_{1},A_{2}{% endequation %} הן קבוצות "נחמדות", ובפרט טרנזיטיביות ביחס ל-{% equation %}M{% endequation %}. כלומר, אם למשל {% equation %}x\in a_{1}\in A_{1}{% endequation %} אז {% equation %}x\in A_{1}{% endequation %}. זה אומר ש-{% equation %}f{% endequation %} מוגדר על {% equation %}x{% endequation %}, ומכך ש-{% equation %}f{% endequation %} איזומורפיזם אנחנו מקבלים {% equation %}f\left(x\right)\in f\left(a_{1}\right)=f\left(a_{2}\right){% endequation %}, ועכשיו מ-{% equation %}f\left(x\right)\in f\left(a_{2}\right){% endequation %} אנחנו מקבלים {% equation %}x\in a_{2}{% endequation %}, וזה מה שרצינו; הכיוון השני ({% equation %}x\in a_{2}{% endequation %} גורר {% equation %}x\in a_{1}{% endequation %}) זהה. זה מוכיח ש-{% equation %}a_{1}=a_{2}{% endequation %} ומסביר למה הייתי צריך להניח ש-{% equation %}M{% endequation %} היקפית.

הוכחנו ש-{% equation %}f{% endequation %} היא פונקציה חח"ע ועל; רק נשאר לטפל בשימור הסדר, כלומר להראות שאם {% equation %}x,a\in\bigcup A{% endequation %} וגם {% equation %}x\in a{% endequation %} אז {% equation %}f\left(x\right)\in f\left(a\right){% endequation %}. זה נראה כמו תכונה שהשתמשתי בה זה עתה! וזה נכון: זה ש-{% equation %}a\in\bigcup A{% endequation %} אומר ש-{% equation %}a\in A{% endequation %} עבור קבוצה נחמדה כלשהי {% equation %}A{% endequation %}; זה ש-{% equation %}A{% endequation %} נחמדה מאפשר להסיק מ-{% equation %}x\in a{% endequation %} את {% equation %}x\in A{% endequation %} <strong>בתנאי</strong> שאנחנו יודעים ש-{% equation %}x\in M{% endequation %}, אבל הרי התחלנו מכך שגם {% equation %}x\in\bigcup A\subseteq M{% endequation %}, כך שאנחנו יודעים את זה. קיבלנו ש-{% equation %}x,a{% endequation %} שייכים לאותה קבוצה ולכן {% equation %}x\in a{% endequation %} גורר {% equation %}f_{A}\left(x\right)\in f_{A}\left(a\right){% endequation %} אבל כפי שכבר ראינו, {% equation %}f=f_{A}{% endequation %} עבור אברי {% equation %}A{% endequation %}. זה מסיים את ההוכחה!

<h2>נעבור לרפלקציה</h2>

בואו נעצור לרגע וניזכר מה אנחנו רוצים להוכיח, שנקרא "עקרון הרפלקציה": שלכל פסוק {% equation %}\phi{% endequation %} (פסוק הוא נוסחה ללא משתנים חופשיים, כלומר שערך האמת שלו קבוע ואינו תלוי בהשמה ספציפית) קיימת קבוצה טרנזיטיבית ובת מניה {% equation %}M{% endequation %} כך ש-{% equation %}\phi\leftrightarrow\phi|_{M}{% endequation %}.

את {% equation %}\phi\leftrightarrow\phi|_{M}{% endequation %} צריך להבין בתור נוסחה (לא פסוק) שיש בה משתנה חופשי {% equation %}M{% endequation %}, וכשאני אומר ש-{% equation %}\phi\leftrightarrow\phi|_{M}{% endequation %} "מתקיים" אני מתכוון שבהשמה שבה אני מציב את הקבוצה {% equation %}M{% endequation %} בתוך המשתנה {% equation %}M{% endequation %}, הנוסחה מקבלת ערך T.

את החלק של הטרנזיטיביות של {% equation %}M{% endequation %} עשינו קודם: הוכחנו שאם {% equation %}M{% endequation %} היא מה שכיניתי <strong>היקפית</strong> אז היא איזומורפית לקבוצה טרנזיטיבית. לכן מה שאני צריך לבנות הוא {% equation %}M{% endequation %} שתהיה בת מניה והיקפית. כפי שנראה, הבניה לא תתקשה "על הדרך" להבטיח ש-{% equation %}M{% endequation %} היקפית כך שהחלק של "בת מניה" הוא עיקר הסיפור פה.

לב הרעיון הוא זה: לא משנה כמה {% equation %}\phi{% endequation %} היא נוסחה גדולה ומורכבת ומסובכת, היא עדיין נוסחה. נוסחה היא משהו שנבנה מנוסחאות קודמות בעזרת כמה צעדי בניה פשוטים, ובמספר <strong>סופי</strong> של צעדים. מה שנעשה הוא לקחת את {% equation %}\phi{% endequation %} ולפרק אותה לגורמים - לכל אותם מרכיבים שבהם משתמשים בתהליך הבניה שלה, ואז לבנות את {% equation %}M{% endequation %} באופן סדרתי עבור המרכיבים הללו כך שנוכל אינדוקטיבית להראות ש-{% equation %}M{% endequation %} מקיימת רפלקציה גם עבורם. רפלקציה במובן הקצת יותר רחב, שבו יש לנוסחאות משתנים חופשיים ואנחנו מציבים בהם ערכים שמגיעים מתוך {% equation %}M{% endequation %}. כדי להבטיח ש-{% equation %}M{% endequation %} תהיה היקפית נזרוק פנימה לאוסף הנוסחאות הזה גם את הפירוק של אקסיומת ההיקפיות.

בואו נתחיל עם הבניה של {% equation %}M{% endequation %}. כאמור, מה שעומד לנגד העיניים שלנו כשאנחנו בונים את {% equation %}M{% endequation %} לא יהיה פסוק בודד אלא קבוצה <strong>סופית</strong> של נוסחאות, {% equation %}\phi_{1},\ldots,\phi_{n}{% endequation %}, כך שהמשתנים החופשיים של כל אחת מהנוסחאות הללו נופלים בתוך הקבוצה {% equation %}x_{1},\ldots,x_{m}{% endequation %}. אני אבנה את {% equation %}M{% endequation %} כך שמתקיים הדבר הבא: לכל {% equation %}1\le i\le n{% endequation %} ו-{% equation %}1\le j\le m{% endequation %} ולכל קבוצה של ערכים {% equation %}a_{1},\ldots,a_{j-1},a_{j+1},\ldots,a_{m}\in M{% endequation %}:

<strong>אם</strong> {% equation %}\exists x_{j}\phi_{i}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} מקבל את הערך T

<strong>אז</strong> {% equation %}\exists x_{j}\left(x_{j}\in M\wedge\phi_{i}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right)\right){% endequation %} מקבל את הערך T (כשמציבים את הקבוצה {% equation %}M{% endequation %} במשתנה {% equation %}M{% endequation %}).

הרעיון פה הוא שכדי לספק נוסחאות של "קיים" מספיק <strong>איבר אחד</strong>, ומכיוון שמלכתחילה יש לנו רק מספר סופי של נוסחאות, קבוצת כל האיברים שנזדקק להם היא לא גדולה. למה זה לא טריוויאלי לחלוטין? כי ברגע שהוספנו ל-{% equation %}M{% endequation %} משהו, גם הגדלנו את טווח הסיטואציות שלנו. "סיטואציה" כזו כוללת נוסחה {% equation %}\phi_{i}{% endequation %} ומשתנה {% equation %}x_{j}{% endequation %} ויש רק מספר סופי של זוגות כאלו, אבל היא כוללת גם את <strong>ההצבה</strong> שהצבנו בכל משתני {% equation %}\phi_{i}{% endequation %} למעט {% equation %}x_{j}{% endequation %}, וכשאני מגדיל את {% equation %}M{% endequation %} אני גם מוסיף הרבה הצבות חדשות שכאלו. 

אז מצד אחד לכאורה אני נמצא בתוך תהליך אינסופי שרק הולך ומסתבך - ככל שאני מוסיף איברים ככה אני מגדיל את כמות הסיטואציות שאני צריך להתמודד איתן. זו אכן הסיבה שבגללה אני לא אוכל לבנות קבוצה <strong>סופית</strong> {% equation %}M{% endequation %} שכזו. אבל אז נכנס לתמונה הקסם הגדול של המתמטיקה, זה שעובד גם במלון של הילברט ובעצם בחצי מתורת הקבוצות - היכולת שלנו "לדחוק את השגיאה לאינסוף". לא לפתור את הבעיה, אלא כל הזמן לדחוף אותה עוד ועוד קדימה ואז להסתכל על התהליך כולו ולראות שאיזה פלא, התהליך פתר את הבעיה למרות שבשום שלב היא לא נפתרה (ואצלנו, כאמור, היא רק הולכת ומחמירה עם הזמן).

כמובן, זה לא היה נשמע מרשים או מעניין כל כך אם כל מה שהיה קיים בעולם שלנו הוא קבוצות בנות מניה. רק ההבנה שלנו שקבוצות בנות מניה הן למעשה מקרה פשוט וקליל יחסית היא שהופכת את הסיפור למעניין.

טוב, קשקשתי מספיק והגיע הזמן להוכחה. הטריק כאמור יהיה לבנות את {% equation %}M{% endequation %} בשלבים, {% equation %}M_{0},M_{1},M_{2},\ldots{% endequation %} כשבכל שלב נוסיף ל-{% equation %}M_{k}{% endequation %} איברים לקבלת {% equation %}M_{k+1}{% endequation %} ובסוף נגדיר {% equation %}M=\bigcup_{k=0}^{\infty}M_{k}{% endequation %}. הבניה עצמה פשוטה: נגדיר {% equation %}M_{0}=\left\{ \emptyset\right\} {% endequation %} ובהינתן {% equation %}M_{k}{% endequation %} נבנה מתוכה את {% equation %}M_{k+1}{% endequation %} על ידי כך שניקח את כל אברי {% equation %}M_{k}{% endequation %} ובנוסף לכל {% equation %}1\le i\le n{% endequation %} וכל {% equation %}1\le j\le m{% endequation %} וכל סדרת ערכים {% equation %}a_{1},\ldots,a_{j-1},a_{j+1},\ldots,a_{m}\in M_{k}{% endequation %}, <strong>אם</strong> קיים איבר (ביקום הגדול של תורת הקבוצות, לא ב-{% equation %}M_{k}{% endequation %} או משהו) שכשמציבים אותו ב-{% equation %}x_{j}{% endequation %} הנוסחה {% equation %}\phi_{i}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} מקבלת T, אז נוסיף את האיבר הזה אל {% equation %}M_{k+1}{% endequation %}. בבניה הזו {% equation %}M_{0}{% endequation %} סופית ואם {% equation %}M_{k}{% endequation %} סופית גם {% equation %}M_{k+1}{% endequation %} סופית, ולכן קיבלנו בסך הכל אוסף סופי של קבוצות, ומכיוון ש-{% equation %}M{% endequation %} היא איחוד בן מניה של קבוצות סופיות קיבלנו ש-{% equation %}M{% endequation %} בת מניה.

עכשיו, בואו ניזכר מה צריך להוכיח ש-{% equation %}M{% endequation %} מקיימת:

לכל {% equation %}1\le i\le n{% endequation %} ו-{% equation %}1\le j\le m{% endequation %} ולכל קבוצה של ערכים {% equation %}a_{1},\ldots,a_{j-1},a_{j+1},\ldots,a_{m}\in M{% endequation %}:

<strong>אם</strong> {% equation %}\exists x_{j}\phi_{i}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} מקבל את הערך T

<strong>אז</strong> {% equation %}\exists x_{j}\left(x_{j}\in M\wedge\phi_{i}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right)\right){% endequation %} מקבל את הערך T

כל אחד מהערכים {% equation %}a_{1},\ldots,a_{m}{% endequation %} הללו התווסף אל {% equation %}M{% endequation %} בשלב כלשהו, אז אם ניקח את {% equation %}k{% endequation %} להיות השלב <strong>המקסימלי</strong> מביניהם אנחנו מקבלים שכל האיברים הללו שייכים אל {% equation %}M_{k}{% endequation %}, ולכן ב-{% equation %}M_{k+1}{% endequation %} יש לנו בדיוק איבר קונקרטי של {% equation %}M{% endequation %} שעבורו הנוסחה השניה מקבלת T, כי כך בנינו את {% equation %}M{% endequation %}. זה מסיים את הבניה.

עכשיו אנחנו רוצים לחזור אל המטרה שלנו: נתון פסוק {% equation %}\phi{% endequation %} ואנחנו רוצים לבנות {% equation %}M{% endequation %} כך ש-

{% equation %}\phi\leftrightarrow\phi|_{M}{% endequation %}

מה שנעשה הוא לקחת את {% equation %}\phi{% endequation %} וליצור ממנה רשימת נוסחאות באופן הבא:

<ul> <li>אם {% equation %}\neg\psi{% endequation %} ברשימה, נוסיף לרשימה גם את {% equation %}\psi{% endequation %}</li>


<li>אם {% equation %}\psi_{1}\to\psi_{2}{% endequation %} ברשימה, נוסיף לרשימה גם את {% equation %}\psi_{1},\psi_{2}{% endequation %}</li>


<li>אם {% equation %}\forall x_{j}\psi{% endequation %} ברשימה, נוסיף לרשימה גם את {% equation %}\psi{% endequation %}</li>

</ul>

אנחנו מפעילים את הכללים הללו על רשימה שבהתחלה כוללת רק את {% equation %}\phi{% endequation %} ואת אקסיומת ההיקפיות (כזכור, צריך גם אותה), ומקבלים רשימה <strong>סופית</strong> של נוסחאות, {% equation %}\phi_{1},\ldots,\phi_{n}{% endequation %} שהמשתנים החופשיים שלהם נופלים בתוך הקבוצה {% equation %}x_{1},\ldots,x_{m}{% endequation %}. עד כאן, הכל מתקדם על פי התוכנית. שימו לב שגם פה השתמשתי בכך שמספיקים הקשרים {% equation %}\neg,\to{% endequation %} והכמת {% equation %}\forall{% endequation %} כדי לתאר את כל הנוסחאות, כי כל נוסחה שיש לה קשר או כמת אחרת ניתן להחליף בנוסחה שקולה בלעדיו. זה מרגיש לי קצת מוזר כי הרי לפני רגע ההוכחה שלי דיברה על נוסחאות שמופיע בהן הכמת {% equation %}\exists{% endequation %}, אבל זו לא בעיה כי אני הולך להשתמש בטריק: כזכור, {% equation %}\exists x_{j}\psi{% endequation %} שקול אל {% equation %}\neg\forall x_{j}\left(\neg\psi\right){% endequation %}, ומה שאני אעשה, במקום לבנות {% equation %}M{% endequation %} עבור הנוסחאות {% equation %}\phi_{1},\ldots,\phi_{n}{% endequation %}, זה לבנות {% equation %}M{% endequation %} עבור <strong>השלילה</strong> שלהן, {% equation %}\neg\phi_{1},\ldots,\neg\phi_{n}{% endequation %}. עכשיו בואו נראה שזה עובד.

כרגיל, כשעובדים עם נוסחאות נוח להוכיח באינדוקציה על המבנה שלהן. בזכות האופן שבו בנינו את קבוצת הנוסחאות שלנו, כל נוסחה בקבוצה שלנו שאינה אטומית נבנית מנוסחאות פשוטות יותר שגם כן שייכות לקבוצה, ולכן הוכחה אינדוקטיבית תעבוד כאן. הטענה הכללית שאנחנו מוכיחים היא שלכל השמה של הערכים {% equation %}a_{1},\ldots,a_{m}\in M{% endequation %} למשתנים של {% equation %}\psi{% endequation %} מתקיים

{% equation %}\psi\left(a_{1},\ldots,a_{m}\right)\leftrightarrow\psi|_{M}\left(a_{1},\ldots,a_{m}\right){% endequation %}

כבר ראינו הוכחה אינדוקטיבית אחת שמערבת רלטיביזציה, וכזכור רובה הייתה טריוויאלית: אם {% equation %}\psi{% endequation %} היא נוסחה אטומית אז רלטיביזציה שלה לא משנה אותה בכלל ולכן כמובן ש-{% equation %}\psi\leftrightarrow\psi|_{M}{% endequation %}. עבור {% equation %}\psi=\neg\psi^{\prime}{% endequation %} אנחנו יודעים ש-{% equation %}\psi|_{M}=\neg\left(\psi^{\prime}|_{M}\right){% endequation %} ומהנחת האינדוקציה {% equation %}\psi^{\prime}|_{M}\leftrightarrow\psi^{\prime}{% endequation %} ולכן נקבל {% equation %}\psi|_{M}\leftrightarrow\psi{% endequation %} (הטיעון המובלע פה הוא שאם {% equation %}\psi_{1}\leftrightarrow\psi_{2}{% endequation %} אז {% equation %}\neg\psi_{1}\leftrightarrow\neg\psi_{2}{% endequation %}).

באופן דומה, אם {% equation %}\psi=\psi_{1}\to\psi_{2}{% endequation %} אז מכך ש-{% equation %}\psi|_{M}=\psi_{1}|_{M}\to\psi_{2}|_{M}{% endequation %} נקבל {% equation %}\psi|_{M}\leftrightarrow\psi{% endequation %}. החלק המאתגר היחיד מגיע כשהנוסחה היא מהצורה {% equation %}\forall x_{j}\psi\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %}.

עכשיו מגיעה הוכחה דו כיוונית שאני אעשה טיפה שונה מבדרך כלל. ראשית אני אניח ש-{% equation %}\forall x_{j}\psi\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} מקבלת T ואוכיח שגם {% equation %}\forall x_{j}\psi|_{M}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} מקבלת T . אחר כך אני אניח ש-{% equation %}\forall x_{j}\psi\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} מקבלת F ואוכיח שגם {% equation %}\forall x_{j}\psi|_{M}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} מקבלת F. יאללה לעבודה.

בואו נניח קודם כל שהנוסחה {% equation %}\forall x_{j}\psi\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} מקבלת ערך T, ונוכיח מזה שהנוסחה {% equation %}\forall x_{j}\left(x_{j}\in M\to\psi|_{M}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right)\right){% endequation %} מקבלת T. זה כמובן החלק הקל; לכל ערך שנציב ב-{% equation %}x_{j}{% endequation %}, ההנחה שלנו אומרת ש-{% equation %}\psi\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} תקבל T ולכן מהנחת האינדוקציה גם {% equation %}\psi|_{M}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} תקבל T.

שימו לב! אנחנו כפסע מסוף הההוכחה, ועדיין לא השתמשנו <strong>בכלל</strong> באופן שבו {% equation %}M{% endequation %} נבנתה! הגיע הרגע שלקראתו אנו בונים במשך פוסט שלם! איזו התרגשות! וכעת, בואו נצלול חזרה לדברים טכניים.

נניח עכשיו ש-{% equation %}\forall x_{j}\psi\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} מקבלת F. בניסוח שקול: {% equation %}\neg\left(\forall x_{j}\psi\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right)\right){% endequation %} מקבלת T, והרי הנוסחה הזו שקולה אל {% equation %}\exists x_{j}\neg\psi\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %}. והנה זה הגיע: בשביל זה כשבנינו את {% equation %}M{% endequation %} השתמשנו ב<strong>שלילה</strong> של ה-{% equation %}\psi{% endequation %}-ים שלנו.

בואו ניזכר שוב באופן שבו בנינו את {% equation %}M{% endequation %}. עשינו זאת כך שיתקיים

<strong>אם</strong> {% equation %}\exists x_{j}\phi_{i}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right){% endequation %} מקבל את הערך T

<strong>אז</strong> {% equation %}\exists x_{j}\left(\phi_{i}|_{M}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right)\right){% endequation %} מקבל את הערך T.

ראינו שהחלק העליון, שאינו תלוי ב-{% equation %}M{% endequation %}, מתקיים; זה אומר שעל פי בניית {% equation %}M{% endequation %}, יש בה איבר כלשהו שמאפשר גם לרלטיביזציה להיות T. כלומר, הנוסחה הבאה מקבלת T:

{% equation %}\exists x_{j}\left(\left(\neg\psi\right)|_{M}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right)\right){% endequation %}

מכיוון שההשמה ל-{% equation %}x_{j}{% endequation %} שמראה שהנוסחה מקבלת T מציבה בו איבר מתוך {% equation %}M{% endequation %} (כלומר, כזה שמקיים את הנוסחה האטומית {% equation %}x_{j}\in M{% endequation %}) נקבל שגם הנוסחה הבאה מקבלת T:

{% equation %}\exists x_{j}\left(x_{j}\in M\wedge\left(\neg\psi\right)|_{M}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right)\right){% endequation %}

מה שאומר שבאופן שקול, הנוסחה הבאה מקבלת F:

{% equation %}\forall x_{j}\left(x_{j}\in M\to\psi|_{M}\left(a_{1},\ldots,x_{j},\ldots,a_{m}\right)\right){% endequation %}

וזה בדיוק מה שרצינו להגיע אליו, מה שמסיים את ההוכחה, ואת כל שרשרת ההוכחות שהייתה בפוסט הזה.

זה זמן טוב לעצור ולקחת הפסקה; מכיוון שכל החלק הזה של הפוסט היה טכני להחריד אין טעם להמשיך ולדבר על התמונה הגדולה ולאן הולכים מכאן; את זה אעשה בפוסט הבא. 