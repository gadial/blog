---
title: "חישוב קוונטי בגישה מתמטית, חלק ב'"
layout: post
categories:
  - תורת הסיבוכיות
tags:
  - חישוב קוונטי
description: 'ייצוג של מצב קוונטי של כמה קיוביטים הוא הדוגמא שאנחנו משתמשים בה כדי להבין מכפלות טנזוריות, ואנחנו רואים מה זו ה"שזירה" הקוונטית שמדברים עליה כל הזמן'
image: "2022/quantum_computer2.png"
---


<h2>מה קורה כשיש לנו שני קיוביטים ביחד?</h2>

<a href="https://gadial.net/2022/07/28/quantum_computing_math/">הפוסט הקודם</a> שלי על חישוב קוונטי הציג מתמטית את המושג של <strong>קיוביט</strong>: מערכת פיזיקלית כלשהי שאפשר לתאר את המצב הכללי שלה בתור <strong>סופרפוזיציה</strong>, שהיא וקטור ב-{% equation %}\mathbb{C}^{2}{% endequation %} מנורמה 1 שאהבתי לסמן ב-{% equation %}\alpha\left|0\right\rangle +\beta\left|1\right\rangle {% endequation %}. הראיתי איך מבצעים חישובים עם קיוביט בודד שכזה, והאמת היא שזה לא היה מרשים בכלל כי את הכל אפשר לסמלץ בנוחות במחשב רגיל; לא צריך מחשב קוונטי בשביל חישוב עם קיוביט יחיד ולא משנה עד כמה סופרפוזיציה היא תופעה מופלאה.

אז בפוסט הזה אנחנו הולכים לדבר על מערכות שכוללות יותר מקיוביט יחיד. במערכות הללו קורה קסם קוונטי שנקרא <strong>שזירה</strong>: אני אגדיר אותו פורמלית בהמשך, אבל הרעיון בשזירה הוא ששתי מערכות קוונטיות הן מחוברות זו לזו בצורה כזו שלא ניתן לחשוב עליהן בתור שתי מערכות נפרדות; השלם גדול מסך חלקיו.כדי לראות למה זה מעניין, תחשבו על שעון - כשפותחים אותו רואים המון גלגלי שיניים מתרוצצים להם וזה נראה כמו מערכת גדולה ומורכבת, אבל אם נסתכל על גלגל שיניים בודד נוכל להבין בדיוק מה הוא עושה. הוא כמובן משפיע על מערכות אחרות שצמודות אליו, אבל אפשר להסתכל עליו באופן מבודד. בשזירה אי אפשר. אותו הדבר עם חישוב רגיל: הערך של כל ביט בחישוב רגיל הוא או 0 או 1, וזהו; הערך של הביט לא תלוי בערכים של ביטים אחרים. כמובן, אם אנחנו מבצעים פעולה חישובית כלשהי, היא תיקח את הערך של הרבה ביטים ותשנה אותו, בהתאם לכל הקלטים שקיבלה; הערכים של הביטים השונים יכולים להשפיע אחד על השני . אבל כשמסתכלים על מצב נתון של מערכת, אנחנו יכולים להסתכל על כל ביט בנפרד.

נשמע לא ברור? בהחלט! זו הבעיה עם חישוב קוונטי, שדברים נהיים ברורים, ואפילו קלים ממש להבנה, רק כשמערבים מתמטיקה. למרבה המזל זו המטרה שלנו פה, לערב מתמטיקה. אז בואו נעבור לשאלה מתמטית כללית לרגע: נניח שיש לנו שני מרחבים וקטוריים, {% equation %}U,W{% endequation %} (אצלנו המרחבים יהיו קיוביטים, אבל נחזור לזה בהמשך) - איך אני יכול לבנות משני המרחבים הללו מרחב וקטורי חדש?

התשובה הנפוצה, שרואים מהר מאוד בכל קורס אלגברה לינארית, היא באמצעות פעולה שנקראת <strong>סכום ישר</strong> (או <strong>סכום ישר חיצוני</strong> עבור מה שאציג כאן, או <strong>מכפלה ישרה</strong>, שהיא מושג שונה אבל עם משמעות זהה כשיש רק שני מרחבים): אני בונה מרחב וקטורי {% equation %}V=U\oplus W{% endequation %} שכל איבר בו הוא מהצורה {% equation %}\left(u,w\right){% endequation %} כך ש-{% equation %}u\in U,w\in W{% endequation %}, ופעולות החיבור והכפל בסקלר הן "נקודתיות", כלומר {% equation %}\left(u_{1},w_{1}\right)+\left(u_{2},w_{2}\right)=\left(u_{1}+u_{2},w_{1}+w_{2}\right){% endequation %} ו-{% equation %}\lambda\left(u,w\right)=\left(\lambda u,\lambda w\right){% endequation %}. בגישה הזו, אפשר לחשוב על כל איבר ב-{% equation %}V{% endequation %} כאילו הוא מיוצג על ידי <strong>זוג איברים</strong>, אחד מ-{% equation %}u{% endequation %} ואחד מ-{% equation %}w{% endequation %}. למשל, כשאני מסתכל על {% equation %}\mathbb{R}^{2}{% endequation %} האיברים שלו הם קווים במישור, אבל אפשר גם לחשוב עליו בתור {% equation %}\mathbb{R}\oplus\mathbb{R}{% endequation %}: מרחב שבו כל איבר מיוצג על ידי קו בציר {% equation %}x{% endequation %} וקו בציר {% equation %}y{% endequation %} - <strong>ההיטלים</strong> של הקו ב-{% equation %}\mathbb{R}^{2}{% endequation %}. אם יש לנו בסיס {% equation %}e_{1},\ldots,e_{n}{% endequation %} ל-{% equation %}U{% endequation %} ובסיס {% equation %}f_{1},\ldots,f_{m}{% endequation %} ל-{% equation %}W{% endequation %}, אז בסיס ל-{% equation %}V=U\oplus W{% endequation %} יהיה {% equation %}\left(e_{1},0\right),\ldots,\left(e_{n},0\right),\left(0,f_{1}\right),\ldots,\left(0,f_{m}\right){% endequation %}, כלומר {% equation %}V{% endequation %} יהיה ממימד {% equation %}n+m{% endequation %} ואפשר יהיה לחשוב על כל איבר בו כאילו הוא נוצר מתוך איברי הבסיסים של {% equation %}U,W{% endequation %}. זו כאמור בניה סטנדרטית ומועילה ביותר והיא <strong>לחלוטין לא</strong> מה שאנחנו הולכים לעשות הפעם. הקסם של חישוב קוונטי - הקסם של <strong>שזירה קוונטית</strong>, הוא בכך שהמרחב {% equation %}V{% endequation %} שמתקבל משילוב של שתי מערכות קוונטיות {% equation %}U,W{% endequation %} הוא לא סכום ישר אלא מה שנקרא <strong>מכפלה טנזורית</strong>, {% equation %}V=U\otimes W{% endequation %}.

<a href="https://gadial.net/2014/06/10/vector_space_tensor_product/">יש לי פוסט</a> על מכפלות טנזוריות אבל אני לא הולך להסתמך עליו כאן. בכללי, מכפלות טנזוריות זה תחום מורכב ועשיר עם שלל דרכים להציג אותו; אני אנסה להציג אותו בדרך הכי קונקרטית ובסיסית שאני יכול, כדי שיהיה קל להבין איך זה עובד במקרה של קיוביטים. הדרך הפשוטה ביותר לתאר את {% equation %}V=U\otimes W{% endequation %} היא זו: כבר ראינו בסיס {% equation %}e_{1},\ldots,e_{n}{% endequation %} של {% equation %}U{% endequation %} ובסיס {% equation %}f_{1},\ldots,f_{m}{% endequation %} של {% equation %}W{% endequation %}, אז עכשיו ניצור מרחב חדש לגמרי "מלמטה למעלה". ראשית, נגדיר איברים חדשים שאסמן {% equation %}e_{i}\otimes f_{j}{% endequation %} לכל {% equation %}1\le i\le n{% endequation %} ו-{% equation %}1\le j\le m{% endequation %}. כלומר, קיבלתי {% equation %}n\times m{% endequation %} איברים חדשים שכאלו, שכל אחד מהם בנוי מאיבר בסיס של {% equation %}U{% endequation %}, איבר בסיס של {% equation %}W{% endequation %} ואיזה סימן {% equation %}\otimes{% endequation %} מוזר בין שניהם שלא אומר לנו כלום כרגע. עכשיו אני מגדיר את {% equation %}V{% endequation %} בתור

{% equation %}V=\text{span}\left\{ e_{i}\otimes f_{j}\ |\ 1\le i\le n,1\le j\le m\right\} {% endequation %}

מה זה אומר? בעיקרון, זה אומר שאיבר כללי של {% equation %}V{% endequation %} הוא מהצורה {% equation %}\sum\lambda_{ij}\left(e_{i}\otimes f_{j}\right){% endequation %} - קיבלנו מרחב שמתקבל מ"סכום פורמלי" של כל האיברים {% equation %}e_{i}\otimes f_{j}{% endequation %}. זה קצת מזכיר את האופן שבו אפשר לחשוב על המרחב הוקטורי של הפולינומים בתור המרחב הוקטורי שמורכב מכל הסכומים הסופיים של האיברים מהצורה {% equation %}x^{0},x^{1},x^{2},\ldots{% endequation %}. במרחב כזה, פעולות החיבור והכפל בסקלר מוגדרות בצורה הטבעית שאפשר לצפות לה:

{% equation %}\sum\lambda_{ij}\left(e_{i}\otimes f_{j}\right)+\sum\mu_{ij}\left(e_{i}\otimes f_{j}\right)=\sum\left(\lambda_{ij}+\mu_{ij}\right)\left(e_{i}\otimes f_{j}\right){% endequation %}

{% equation %}\mu\cdot\sum\lambda_{ij}\left(e_{i}\otimes f_{j}\right)=\sum\left(\mu\lambda_{ij}\right)\left(e_{i}\otimes f_{j}\right){% endequation %}

זה אבסטרקטי מאוד, אז בואו נראה מה קורה עם קיוביטים. אצלנו {% equation %}U=W=\mathbb{C}^{2}{% endequation %} וכזכור, סימנתי ב-{% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %} את אברי הבסיס הסטנדרטי. אז עבור שני קיוביטים אני הולך לקבל את המרחב {% equation %}\mathbb{C}^{2}\otimes\mathbb{C}^{2}{% endequation %} שנפרש על ידי ארבעת האיברים הבאים:

{% equation %}\left|0\right\rangle \otimes\left|0\right\rangle {% endequation %}

{% equation %}\left|0\right\rangle \otimes\left|1\right\rangle {% endequation %}

{% equation %}\left|1\right\rangle \otimes\left|0\right\rangle {% endequation %}

{% equation %}\left|1\right\rangle \otimes\left|1\right\rangle {% endequation %}

מכיוון שמעייף מאוד לכתוב את ה-{% equation %}\otimes{% endequation %} הזה בכל פעם, לרוב משמיטים אותו; במקום לכתוב {% equation %}\left|0\right\rangle \otimes\left|0\right\rangle {% endequation %} כותבים {% equation %}\left|0\right\rangle \left|0\right\rangle {% endequation %} או אפילו עוד יותר בקיצור, {% equation %}\left|00\right\rangle {% endequation %}. אם כן, איבר כללי שמתאר את המצב של שני קיוביטים הוא

{% equation %}\alpha\left|00\right\rangle +\beta\left|01\right\rangle +\gamma\left|10\right\rangle +\delta\left|11\right\rangle {% endequation %}

יש בעיה עקרונית עם מרחב של שני קיוביטים: הוא ממימד 4, בדיוק כמו הסכום הישר {% equation %}\mathbb{C}^{2}\oplus\mathbb{C}^{2}{% endequation %}, כך שלא ברור מה ההבדל. לכן אני אקפוץ לרגע אל מרחב בן שלושה קיוביטים. מרחב כזה נפרש על ידי האיברים

{% equation %}\left|000\right\rangle ,\left|001\right\rangle ,\left|010\right\rangle ,\left|011\right\rangle ,\left|100\right\rangle ,\left|101\right\rangle ,\left|110\right\rangle ,\left|111\right\rangle {% endequation %}

זה כבר שונה מסכום ישר של שלושה מרחבים {% equation %}\mathbb{C}^{2}\oplus\mathbb{C}^{2}\oplus\mathbb{C}^{2}{% endequation %}, שנפרש על ידי <strong>שישה</strong> איברים:

{% equation %}\left(\left|0\right\rangle ,0,0\right),\left(\left|1\right\rangle ,0,0\right),\left(0,\left|0\right\rangle ,0\right),\left(0,\left|1\right\rangle ,0\right),\left(0,0,\left|0\right\rangle \right),\left(0,0,\left|1\right\rangle \right){% endequation %}

הסימון הזה די מבלבל: {% equation %}\left|0\right\rangle {% endequation %} הוא הסימון שלי לוקטור {% equation %}\left(\begin{array}{c} 1\\ 0 \end{array}\right){% endequation %} בזמן ש-0 הוא הסימון שלי לוקטור האפס, {% equation %}\left(\begin{array}{c} 0\\ 0 \end{array}\right){% endequation %}; זכרו ש-{% equation %}\left|0\right\rangle {% endequation %} זה סימון שרירותי והייתי יכול גם להשתמש ב-{% equation %}\left|42\right\rangle {% endequation %} אם היה מתחשק לי (להבדיל מ-0 שמתאים לתפיסה הרגילה שלנו של מה זה "אפס"). למרבה המזל, אני לא אדרש כמעט לשימוש ב-0 או בסכומים ישרים, אז עכשיו שראינו שזה משהו שונה ממכפלה טנזורית, אפשר לשכוח מהם.

ראינו קיוביט אחד, שני קיוביטים ושלושה קיוביטים, אז באינדוקציה אפשר להראות עכשיו {% equation %}n{% endequation %} קיוביטים. מרחב של {% equation %}n{% endequation %} קיוביטים נפרש על ידי {% equation %}2^{n}{% endequation %} איברים בסיס: לכל מחרוזת בינארית {% equation %}x\in\left\{ 0,1\right\} ^{n}{% endequation %} יש לנו איבר בסיס {% equation %}\left|x\right\rangle {% endequation %}, ואפשר לסמן איבר כללי בתור

{% equation %}\sum_{x\in\left\{ 0,1\right\} ^{n}}\alpha_{x}\left|x\right\rangle {% endequation %}

כלומר, ה"אינפורמציה" שיש במצב כללי של מערכת של {% equation %}n{% endequation %} קיוביטים מקודדת על ידי {% equation %}2^{n}{% endequation %} מספרים מרוכבים. זה הבדל <strong>עצום</strong> מהאינפורמציה שמקודדת במצב כללי של מערכת של {% equation %}n{% endequation %} ביטים קלאסיים, שהיא... {% equation %}n{% endequation %} ספרות של 0 ו-1. שימו לב - אני מדבר כאן על כמות המידע שנדרש כדי לייצג את המצב, לא על מספר המצבים הפוטנציאליים שבו הוא יכול להיות (שהוא {% equation %}2^{n}{% endequation %} למצב קלאסי, אבל גם אם נצמצמם את המקדמים של המצב הקוונטי להיות 0 ו-1 אחרי נרמול, מספר המצבים הפוטנציאליים של המצב הקוונטי יהיה {% equation %}2^{2^{n}}{% endequation %}).

אז זהו, סיימנו את ההגדרה? לגמרי לא, בואו נסבך את העניין עוד קצת לפני שהעניינים יירגעו.

<h2>מה זו בעצם מכפלה טנזורית?</h2>

עבורי ההגדרה שנתנו למעלה נראית סבבה ומוצלחת ואני מרוצה ממנה - עד שפתאום צריך לעשות איתה דברים, ואז צצות השאלות המוזרות. הנה משהו שאפשר לעשות איתה: ראינו את האיבר {% equation %}\left|00\right\rangle {% endequation %} בלי להסביר יותר מדי מה הוא; קונספטואלית, הוא בא לייצג מצב של מערכת של שני קיוביטים שבהם הקיוביט הראשון במצב {% equation %}\left|0\right\rangle {% endequation %} וגם הקיוביט השני במצב {% equation %}\left|0\right\rangle {% endequation %}. כזכור, זה היה קיצור של {% equation %}\left|0\right\rangle \otimes\left|0\right\rangle {% endequation %}. עכשיו, ראינו בפוסט הקודם מצב שקראתי לו {% equation %}\left|+\right\rangle \triangleq\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %} - זה מצב שמייצג במובן כלשהו סופרפוזיציה "אחידה" של {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %}. בואו נניח שיש לנו מערכת קוונטית של שני קיוביטים שכל אחד מהם נמצא במצב {% equation %}\left|+\right\rangle {% endequation %} הזה, אז מה התיאור המתמטי של המערכת הקוונטית הזו?

האינטואיציה שלי אומרת שמצב המערכת יהיה {% equation %}\left|+\right\rangle \otimes\left|+\right\rangle {% endequation %} (או בקיצור, {% equation %}\left|++\right\rangle {% endequation %}) ותכף נראה שזו אינטואיציה נכונה ופורמלית לגמרי, אבל כרגע ההגדרה המתמטית שנתתי פשוט לא תומכת באינטואיציה הזו: לא הגדרתי בשום צורה ביטוי כמו {% equation %}\left|+\right\rangle \otimes\left|+\right\rangle {% endequation %}; הדבר היחיד שהגדרתי הוא את {% equation %}\left|0\right\rangle \otimes\left|0\right\rangle ,\left|1\right\rangle \otimes\left|0\right\rangle ,\left|0\right\rangle \otimes\left|1\right\rangle ,\left|1\right\rangle \otimes\left|1\right\rangle {% endequation %}: ארבעה איברים ספציפיים שמתקבלים ממכפלה טנזורית של <strong>שני איברי בסיס</strong>. כך זה היה גם בהגדרה הכללית שלי:

{% equation %}V=\text{span}\left\{ e_{i}\otimes f_{j}\ |\ 1\le i\le n,1\le j\le m\right\} {% endequation %}

ההגדרה שלי למכפלה טנזורית <strong>תלויה בבחירת בסיס</strong>, ואנחנו במתמטיקה לא אוהבים הגדרות כאלו; היינו מעדיפים שהגדרות יהיו כמה שיותר חופשיות מבחירות שרירותיות. זה לא תמיד אפשרי, והדוגמא המפורסמת בהקשר של אלגברה לינארית היא האיזומורפיזם בין מרחב וקטורי ומרחב הפונקציונלים שלו ("המרחב הדואלי"), איזומורפיזם שתלוי בבחירת בסיס. אז מה אפשר לעשות? האם אפשר לתת הגדרה חופשיה מבחירת בסיס למכפלה טנזורית, שתתלכד עם ההגדרה שכבר נתתי? כמובן שכן, אבל לפני שאציג אותה פורמלית, בואו נקבל קצת אינטואיציה למה היא אמורה להיות.

כשלומדים על מספרים מרוכבים, אפשר להתחיל מ"להמציא" מספר {% equation %}i{% endequation %} שמקיים {% equation %}i^{2}=-1{% endequation %}, ואז לקחת שני איברים כלליים, {% equation %}a+bi{% endequation %} ו-{% equation %}c+di{% endequation %}, לכפול אותם, לפתוח על פי כללי החשבון הרגילים ולקבל {% equation %}\left(a+bi\right)\left(c+di\right)=\left(ac-bd\right)+\left(ad+bc\right)i{% endequation %}. זו משוואה שהגענו אליה בצורה מאוד אינטואיטיבית אבל יש לה בעיה פורמלית כי "המצאנו" את {% equation %}i^{2}=-1{% endequation %}. אז אפשר להפוך את הקערה על פיה: <strong>להגדיר</strong> מספרים מרוכבים בתור זוגות {% equation %}\left(a,b\right){% endequation %} של מספרים ממשיים - זה אובייקט מתמטי שאין לנו ספק לגבי קיומו - ואז לתת לזוגות הללו <strong>מבנה אלגברי</strong> חדש על ידי חיבור "איבר-איבר" וכפל ש<strong>מוגדר</strong> בתור {% equation %}\left(a,b\right)\times\left(c,d\right)=\left(ac-bd,ad+bc\right){% endequation %}. אחר כך אפשר לבדוק את תכונות הכפל והחיבור ולראות שקיבלנו שדה ולשמוח, אבל אם היינו מתחילים מההגדרה הזו, היא הייתה נראית שרירותית לגמרי כי לא היה ברור מה אנחנו מנסים להשיג. זה בדיוק מה שאעשה כאן - בנוגע למכפלה טנזורית וההגדרה הכללית שלה: אעשה חשבון לפי מה שנראה לי אינטואיטיבי, ואז אגיע מתוכו אל ההגדרה הכללית.

מה שאני רוצה להבין זה מה {% equation %}\left|+\right\rangle \otimes\left|+\right\rangle {% endequation %} אמור להיות במונחים של המכפלה הטנזורית שכבר הגדרתי, זו שכל איבר בה נפרש על ידי {% equation %}\left|00\right\rangle ,\left|01\right\rangle ,\left|10\right\rangle ,\left|11\right\rangle {% endequation %}. אז אני ארשה לעצמי לדמיין ש-{% equation %}\otimes{% endequation %} מתנהג כמו כפל נחמד ו"אפתח" את הביטוי:

{% equation %}\left|+\right\rangle \otimes\left|+\right\rangle =\left(\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}\right)\otimes\left(\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}\right)=\frac{\left(\left|0\right\rangle +\left|1\right\rangle \right)\otimes\left(\left|0\right\rangle +\left|1\right\rangle \right)}{\sqrt{2}\cdot\sqrt{2}}={% endequation %}

{% equation %}=\frac{\left|0\right\rangle \otimes\left|0\right\rangle +\left|0\right\rangle \otimes\left|1\right\rangle +\left|1\right\rangle \otimes\left|0\right\rangle +\left|1\right\rangle \otimes\left|1\right\rangle }{2}=\frac{1}{2}\left|00\right\rangle +\frac{1}{2}\left|01\right\rangle +\frac{1}{2}\left|10\right\rangle +\frac{1}{2}\left|11\right\rangle {% endequation %}

קיבלתי ייצוג של {% equation %}\left|+\right\rangle \otimes\left|+\right\rangle {% endequation %} שנראה הגיוני: הוא באמת איבר של {% equation %}\mathbb{C}^{2}\otimes\mathbb{C}^{2}{% endequation %} על פי ההגדרה שכבר הראיתי, הנורמה שלו שווה 1 ({% equation %}4\cdot\left(\frac{1}{2}\right)^{2}=1{% endequation %}) והוא סימטרי בצורה שאנחנו מצפים לה בהתחשב בסימטריה של {% equation %}\left|+\right\rangle {% endequation %}. השאלה היחידה היא אילו פעולות ביצעתי כדי להגיע לייצוג הזה. אם נסתכל על החשבון שעשיתי, אפשר לראות שני דברים שקרו: ראשית, ה-{% equation %}\sqrt{2}{% endequation %} שבמכנה הוכפלו בצורה "רגילה", כלומר מכפלה טנזורית של סקלרים מתפרשת איכשהו בתור מכפלה רגילה. שנית, "פתחתי" את הביטוי {% equation %}\left(\left|0\right\rangle +\left|1\right\rangle \right)\otimes\left(\left|0\right\rangle +\left|1\right\rangle \right){% endequation %} בעזרת חוק הפילוג הרגיל, כלומר מכפלה טנזורית מכבדת את חוק הפילוג. מתברר ששני אלו מספיקים בשביל ההגדרה הכללית של מכפלה טנזורית. בואו נכתוב את הכללים הללו רגע בצורה פורמלית:

<ul> <li>{% equation %}\left(\lambda u\right)\otimes w=\lambda\left(u\otimes w\right){% endequation %}</li>


<li>{% equation %}u\otimes\left(\lambda w\right)=\lambda\left(u\otimes w\right){% endequation %}</li>


<li>{% equation %}\left(u_{1}+u_{2}\right)\otimes w=u_{1}\otimes w+u_{2}\otimes w{% endequation %}</li>


<li>{% equation %}u\otimes\left(w_{1}+w_{2}\right)=u\otimes w_{1}+u\otimes w_{2}{% endequation %}</li>

</ul>

כל אחד משני הכללים הופיע כאן בעצם פעמיים - פעם אחת כשהוא עובד עבור הרכיב השמאלי, ופעם אחת עבור הרכיב הימני, אבל בשני המקרים זה אותו הכלל. אם אתם רוצים, קחו לעצמכם רגע כדי להשתכנע שבחישוב שלי עבור {% equation %}\left|+\right\rangle \otimes\left|+\right\rangle {% endequation %} אכן השתמשתי בכללים הללו.

כשאנחנו מצוידים בכללים הללו, אנחנו מוכנים לתת את ההגדרה הפורמלית הכללית של מכפלה טנזורית, שמסתמכת על המושג שנקרא <strong>מרחב מנה</strong>. זה מושג נפוץ מאוד באלגברה מופשטת, אבל באלגברה לינארית רואים אותו הרבה פחות, ולכן יותר קשה לי להניח שהוא מוכר. לכן אתחיל מהגדרה אינטואיטיבית ואעבור משם לפורמליזם (שהוא ממש לא קריטי לנו).

הבניה שלנו של המכפלה {% equation %}U\otimes W{% endequation %} מתחילה עם הקבוצה {% equation %}U\times W{% endequation %}, קבוצת כל הזוגות {% equation %}\left(u,w\right){% endequation %}. הזכרתי אותה בתחילת הפוסט: זו הקבוצה שממנה אנחנו מקבלים את {% equation %}U\oplus W{% endequation %}, כשאנחנו מגדירים חיבור וכפל בסקלר "איבר-איבר". אלא שעכשיו אני עושה עם הקבוצה הזו משהו שונה לחלוטין - במקום להסתכל רק על האיברים {% equation %}\left(u,w\right){% endequation %}, אני מסתכל על קבוצת <strong>הסכומים הפורמליים</strong> שלהם. כלומר על כל הביטויים שאפשר לכתוב בתור {% equation %}\sum\lambda_{u,w}\left(u,w\right){% endequation %} כאשר {% equation %}\lambda_{u,w}{% endequation %} הם סקלרים, כשהמגבלה היחידה שלי היא שכל סכום פורמלי כזה חייב להכיל <strong>מספר סופי</strong> של מחוברים. האנלוג המיידי הוא פולינומים, שהם בסך הכל סכומים פורמליים שנבנים מאינסוף האיברים {% equation %}\left\{ x^{0},x^{1},x^{2},\ldots\right\} {% endequation %}. למרות שזה מושג פורמלי ותקין לגמרי, אם הוא מפריע לכם אפשר לתת לו בניה יותר פורמלית: מסתכלים על מרחב הפונקציות {% equation %}f:U\times W\to\mathbb{C}{% endequation %} עם תומך סופי (כלומר, שמחזירות משהו שונה מאפס על מספר סופי של קלטים) וזה מרחב שאין לנו ספק שקיים; הסכום הפורמלי {% equation %}\sum\lambda_{u,w}\left(u,w\right){% endequation %} מיוצג על ידי הפונקציה {% equation %}f\left(u,w\right)=\lambda_{u,w}{% endequation %}.

קבוצת הסכומים הפורמליים היא מרחב וקטורי עם החיבור והכפל בסקלר הרגילים, כלומר {% equation %}\sum\lambda_{u,w}\left(u,w\right)+\sum\rho_{u,w}\left(u,w\right)=\sum\left(\lambda_{u,w}+\rho_{u,w}\right)\left(u,w\right){% endequation %} ו-{% equation %}\rho\sum\lambda_{u,w}\left(u,w\right)=\sum\left(\rho\lambda_{u,w}\right)\left(u,w\right){% endequation %} - רק צריך לוודא שהסכום והכפל הזה משמרים את תכונת ה"יש רק מספר סופי של מחוברים", מה שכמובן קורה. זה מרחב וקטורי גדול מאוד - הרבה יותר גדול מ-{% equation %}U\times W{% endequation %}, וגם יותר גדול ממה שאנחנו רוצים שיהיה {% equation %}U\otimes W{% endequation %}, אז מה שנעשה יהיה להקטין את הקבוצה הזו על ידי <strong>זיהוי איברים</strong>. למשל, אנחנו יודעים ש-{% equation %}\left|++\right\rangle {% endequation %} ו-{% equation %}\frac{1}{2}\left|00\right\rangle +\frac{1}{2}\left|01\right\rangle +\frac{1}{2}\left|10\right\rangle +\frac{1}{2}\left|11\right\rangle {% endequation %} "אמורים" להיות שווים, אז נגדיר שהם שווים.

קצת יותר פורמלית, מה שעושים הוא לקחת את ארבעת השוויונות שהראיתי קודם ולהחיל אותם על כל האיברים במרחב:

<ul> <li>{% equation %}\left(\lambda u\right)\otimes w=\lambda\left(u\otimes w\right){% endequation %}</li>


<li>{% equation %}u\otimes\left(\lambda w\right)=\lambda\left(u\otimes w\right){% endequation %}</li>


<li>{% equation %}\left(u_{1}+u_{2}\right)\otimes w=u_{1}\otimes w+u_{2}\otimes w{% endequation %}</li>


<li>{% equation %}u\otimes\left(w_{1}+w_{2}\right)=u\otimes w_{1}+u\otimes w_{2}{% endequation %}</li>

</ul>

ואז להסתמך על כך ששוויון הוא טרנזיטיבי, כלומר שכל שני איברים שאפשר לעבור מהראשון לשני דרך סדרת שוויונות הם שווים. זו לא בדיוק ההגדרה הפורמלית של מרחב מנה, אבל זה העיקרון הטכני שבו נשתמש בפועל.

כדי לתת את ההגדרה הפורמלית ממש, הנה בזריזות האופן שבו מרחב מנה מוגדר עבור מרחבים וקטוריים, בהינתן שכבר מכירים יחסי שקילות (<a href="https://gadial.net/2020/01/06/equivalence_relations/">הנה פוסט</a> שלי עליהם): אם {% equation %}V{% endequation %} הוא מרחב וקטורי ו-{% equation %}N{% endequation %} הוא תת-מרחב שלו, מגדירים על {% equation %}V{% endequation %} <strong>יחס שקילות</strong> על ידי {% equation %}v\sim u{% endequation %} אם ורק אם {% equation %}v-u\in N{% endequation %} (תרגיל: להראות שזה יחס שקילות). עכשיו מסתכלים על קבוצת המנה {% equation %}V/N=\left\{ \left[v\right]\ |\ v\in V\right\} {% endequation %} שמתקבלת מיחס השקילות הזה ומגדירים עליה חיבור וכפל בסקלר באמצעות נציגים: {% equation %}\left[v\right]+\left[w\right]=\left[v+w\right]{% endequation %} ו-{% equation %}\lambda\left[v\right]=\left[\lambda v\right]{% endequation %} (צריך להוכיח שזה מוגדר היטב; זה נובע מכך ש-{% equation %}N{% endequation %} הוא מרחב וקטורי ולא סתם קבוצה). לבסוף צריך לבדוק ש-{% equation %}V/N{% endequation %} עם הפעולות הללו הוא מרחב וקטורי.

במקרה הפרטי שלנו, {% equation %}V=U\times W{% endequation %}. יותר מעניין מהי הקבוצה {% equation %}N{% endequation %}, שאיכשהו אמורה לייצג את ארבעת השוויונות שלמעלה. נסתכל למשל על השוויון {% equation %}\left(\lambda u\right)\otimes w=\lambda\left(u\otimes w\right){% endequation %}: אם אנחנו רוצים שהוא יתקיים <strong>במנה</strong> אז צריך ששני האגפים יהיו שקולים על פי יחס השקילות, כלומר שיתקיים {% equation %}\left(\lambda u\right)\otimes w\sim\lambda\left(u\otimes w\right){% endequation %}, או במילים אחרות - {% equation %}\left(\lambda u\right)\otimes w-\lambda\left(u\otimes w\right)\in N{% endequation %}. גיליתי איבר שחייב להיות ב-{% equation %}N{% endequation %}; עכשיו אני פשוט אקח את כל האיברים מהצורה הזו, ומשלוש הצורות האחרות, ואסתכל על המרחב שנפרש על ידי כולם. זה מה שנחמד במרחבים וקטוריים - כדי לקבל מרחב וקטורי אני לוקח קבוצה שרירותית של איברים, "פורש" אותה והופס, קיבלתי מרחב וקטורי חדש שמתנהג נחמד גם הוא.

זה מסיים עם השאלה של בניית מכפלה טנזורית - קיבלנו הגדרה פורמלית שלא תלויה בבסיס כלשהו, שאני מקווה שגם מבהירה יותר טוב מאיפה המרחבים הללו באים ולאן הם הולכים (ולא השתמשתי בכלל בביטוי "פונקציה בילינארית"! אני לא בטוח אם זה טוב או רע, רוב התיאורים של מכפלות טנזוריות כוללים את זה).

<h2>מה זה מצבים שזורים?</h2>

השוויון {% equation %}\left|++\right\rangle =\frac{1}{2}\left|00\right\rangle +\frac{1}{2}\left|01\right\rangle +\frac{1}{2}\left|10\right\rangle +\frac{1}{2}\left|11\right\rangle {% endequation %} מלמד אותנו דבר חשוב: בהחלט ייתכן שלאיבר כלשהו של המכפלה הטנזורית יהיו <strong>כמה ייצוגים שונים</strong>, כלומר זה שיש לי איבר {% equation %}u\otimes w{% endequation %} לא אומר שאי אפשר לכתוב אותו גם בדרכים שונות, למשל כסכום של איברים אחרים. כדי לקבל ייצוג יחיד צריך לעשות את מה שעשיתי בהתחלה - לקחת בסיסים לשני המרחבים שכופלים, ולהסתכל על הקבוצה {% equation %}\left\{ e_{i}\otimes f_{j}\ |\ 1\le i\le n,1\le j\le m\right\} {% endequation %} - הקבוצה הזו תהיה בסיס (כלומר, כל איבר של המכפלה הטנזורית יהיה ניתן לכתיבה כצירוף לינארי <strong>יחיד</strong> של איברי הבסיס). זה פותח פתח לשאלה הבאה: נניח שנתון לי איבר של {% equation %}U\otimes W{% endequation %} בתור סכום כלשהו; האם בהכרח קיים לו ייצוג בתור {% equation %}u\otimes w{% endequation %}? התשובה היא <strong>לחלוטין לא</strong>. ב-{% equation %}U\otimes W{% endequation %} קיימים הרבה איברים ש<strong>אינם</strong> מהצורה {% equation %}u\otimes w{% endequation %}, וזו חלק מהסיבה שבגללה {% equation %}U\otimes W{% endequation %} הוא כזה מרחב עשיר.

בואו נראה דוגמא קוונטית לזה, במקרה של מרחב של שני קיוביטים: המצב {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %}. זה מצב תקין - הוא צירוף לינארי של אברי הבסיס {% equation %}\left|00\right\rangle ,\left|11\right\rangle {% endequation %} והוא מנורמה 1. בפוסט הבא אני גם אראה איך אפשר לייצר אותו בפועל במהלך חישוב קוונטי וזה די פשוט. אבל אי אפשר לכתוב את המצב הזה בתור מכפלה טנזורית של שני מצבים בודדים של קיוביט יחיד. כדי לראות את זה נלכלך טיפה ידיים. נכתוב שני מצבים כלליים:

{% equation %}\alpha_{1}\left|0\right\rangle +\beta_{1}\left|1\right\rangle {% endequation %}

{% equation %}\alpha_{2}\left|0\right\rangle +\beta_{2}\left|1\right\rangle {% endequation %}

נכפול את שניהם טנזורית, נפתח בעזרת הכללים שראינו, ונקבל:

{% equation %}\left(\alpha_{1}\left|0\right\rangle +\beta_{1}\left|1\right\rangle \right)\left(\alpha_{2}\left|0\right\rangle +\beta_{2}\left|1\right\rangle \right)=\alpha_{1}\alpha_{2}\left|00\right\rangle +\alpha_{1}\beta_{2}\left|01\right\rangle +\beta_{1}\alpha_{2}\left|10\right\rangle +\beta_{1}\beta_{2}\left|11\right\rangle {% endequation %}

זה ייצוג עם אברי הבסיס הסטנדרטי, אז אם אני משווה אותו אל {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} אני חייב לקבל שוויון במקדמים עצמם, כלומר

{% equation %}\alpha_{1}\alpha_{2}=\frac{1}{\sqrt{2}}{% endequation %}

{% equation %}\alpha_{1}\beta_{2}=0{% endequation %}

{% equation %}\beta_{1}\alpha_{2}=0{% endequation %}

{% equation %}\beta_{1}\beta_{2}=\frac{1}{\sqrt{2}}{% endequation %}

מהמשוואה הראשונה אנחנו לומדים ש-{% equation %}\alpha_{1}\ne0{% endequation %} וגם {% equation %}\alpha_{2}\ne0{% endequation %}, אז מהמשוואה השניה אנחנו מסיקים ש-{% equation %}\beta_{1}=0{% endequation %}, וזה סותר לנו את המשוואה הרביעית, {% equation %}\beta_{1}\beta_{2}=\frac{1}{\sqrt{2}}{% endequation %}, מה שמסיים את העניין: לא ניתן לכתוב את {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} בתור {% equation %}u\otimes w{% endequation %}, ולא משנה איזה {% equation %}u,w{% endequation %} נבחר.

במתמטיקה קוראים לאיבר כמו {% equation %}u\otimes w{% endequation %} "טנזור טהור" וזאת להבדיל מטנזור שתמיד נכתב בתור סכום, שנקרא "טנזור מעורב". חייבים להודות שהשמות הללו הם לא להיט גדול... יותר מעניין לחשוב על זה מבחינה פיזיקלית. על {% equation %}u\otimes w{% endequation %} אפשר לחשוב בתור "שני קיוביטים שיושבים זה לצד זה וכל אחד מתעסק בעניינו": האחד נמצא במצב {% equation %}u{% endequation %}, השני נמצא במצב {% equation %}w{% endequation %}, וחישוב שאני מפעיל על אחד מהם לא ישפיע על השני, אלא אם זה חישוב שמערב במפורש את שני הקיוביטים.

עם המצב {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} זה לא קורה. זה מצב שמתאר את המערכת של שני הקיוביטים בצורה כזו שאני לא יכול לפרק אותו קונספטואלית למה שקורה אצל כל קיוביט בנפרד. וזו לא שאלה של הבסיס שבו אני עובד. ראינו ש-{% equation %}\left|++\right\rangle {% endequation %} הוא מצב שכשכותבים אותו בבסיס הסטנדרטי הוא סכום, אבל אפשר לכתוב אותו בתור מכפלה טנזורית של שני איברים. עם המצב {% equation %}\frac{\left|00\right\rangle +\left|11\right\rangle }{\sqrt{2}}{% endequation %} לא משנה איזה בסיס נבחר לשני הקיוביטים, אפילו אם זה בסיס "מעורבב" שהאיברים בו הם מהצורה {% equation %}\left|+0\right\rangle {% endequation %} וכאלה, עדיין לא יהיה לנו כתיב של המצב בתור מכפלה של שני קיוביטים נפרדים; זה משהו אינהרטי למצב. השם שיש לדבר הזה בפיזיקה הוא <strong>מצב שזור</strong>.

מצבים שזורים הם הסיבה שבגללה חישוב קוונטי עם {% equation %}n{% endequation %} קיוביטים דורש וקטור עם {% equation %}2^{n}{% endequation %} כניסות כדי לתאר אותו במקום שנוכל להסתפק בייצוג קומפקטי יותר. למעשה, יש טכניקות לסימולציה קלאסית של מחשבים קוונטיים שגודל האתגר שהן מתמודדות איתו הוא פרופורציוני לכמה המצב שמסמלצים הוא שזור (ככל שהשזירה גבוהה יותר - ככל ש"קשה יותר", במובן טכני מסוים, לייצג את המצב עם כמות מחוברים קטנה - כך החישוב קשה יותר לסימולציה). אם הצלחנו להבין את הפורמליזם של מכפלה טנזורית ואת הרעיון של מצבים שזורים, שום דבר לא עוצר אותנו מלהבין עד הסוף איך חישובים קוונטיים עובדים. אל הפרטים הטכניים נגיע בפוסט הבא. 