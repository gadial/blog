---
title: "מה הקטע עם שורשים של מינוס 1?"
layout: post
categories:
  - מספרים
tags:
  - מספרים מרוכבים
image: "2021/fake_complex_root.png"
description: 'האם להשתמש במספרים מרוכבים מוביל לסתירה איהרנטית במתמטיקה?! או שסתם התרגלנו יותר מדי לאיך שמתנהגים שורשים ריבועיים של מספרים חיוביים?'
social_media_share: true
---

המטרה שלי בפוסט הזה היא להסביר את הסתירה השערורייתית הזו במתמטיקה שאפשר לראות פה ושם:

$$\begin{eqnarray} 
-1 & =i\cdot i\\  & =\sqrt{-1}\cdot\sqrt{-1}\\  & =\sqrt{\left(-1\right)\cdot\left(-1\right)}\\  & =\sqrt{1}\\  & =1 
\end{eqnarray}$$

זו סתירה, כי אנחנו מתחילים עם {% equation %}-1{% endequation %} ובעזרת סדרה של שוויונות מגיעים אל 1, כלומר לכאורה {% equation %}1=-1{% endequation %} ואנחנו יודעים שזה לא המצב. אז מה הולך פה? איפה הרמאות?

ובכן, ייתכן שלחלק גדול מכם, הרמאות מופיעה כבר בשורה הראשונה, כשאני כותב {% equation %}-1=i\cdot i{% endequation %}. מה זה {% equation %}i{% endequation %} הזה? הוא אולי נראה כמו <a href="https://gadial.net/2007/04/29/i_fail/">יצור מוזר בתכלית, פרי דמיון מתמטי פרוע</a> אבל האמת היא שהמספר הזהת שנקרא <strong>מספר מדומה</strong> הוא חבר של כבוד במתמטיקה; הוא מושג נפוץ ושימושי מאוד. הבעיה בפירוש <strong>אינה</strong> בכך שאנחנו משתמשים בו, אבל היא כן נובעת מכך שכאשר משתמשים בו, צריכים להיות זהירים יותר עם כללי החשבון המוכרים לנו. ספציפית, השוויון {% equation %}\sqrt{-1}\cdot\sqrt{-1}=\sqrt{\left(-1\right)\cdot\left(-1\right)}{% endequation %} אינו נכון אלא צריך להסתכל על גרסה כללית יותר שלו, שבה הסתירה נעלמת מעצמה. זה מה שארצה להראות בפוסט הזה.

מה שנחמד בסתירה לכאורה הזו הוא שהיא מכריחה אותנו להסתכל מחדש על מושגים שאולי חלקנו כבר התרגלנו אליהם בצורה אינטואיטיבית, ולהבין יותר טוב מה הם <strong>בדיוק</strong> אומרים. אז נרצה להבין

<ul> <li>מה זה {% equation %}\sqrt{a}{% endequation %}?</li>


<li>למה בעצם מתקיים {% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %} כמו שלמדנו בבית הספר?</li>


<li>מה זה {% equation %}i{% endequation %}?</li>


<li>מה הולך פה?!</li>

</ul>

בואו נתחיל עם {% equation %}\sqrt{a}{% endequation %}. הסימן הזה בא לתאר <strong>שורש ריבועי</strong> של {% equation %}a{% endequation %}. מה זה שורש ריבועי? אנחנו אומרים ש-{% equation %}x{% endequation %} הוא שורש ריבועי של {% equation %}a{% endequation %} אם {% equation %}x^{2}=a{% endequation %}. למשל, עבור {% equation %}a=9{% endequation %}, שורש ריבועי הוא {% equation %}x=3{% endequation %} כי {% equation %}x^{2}=9{% endequation %}. אבל תראו, הגענו כבר עכשיו לשלב שבו העסק מתחיל להסתבך! כי גם עבור {% equation %}x=-3{% endequation %} מתקיים {% equation %}x^{2}=9{% endequation %}, כלומר גם {% equation %}-3{% endequation %} הוא שורש ריבועי של {% equation %}9{% endequation %}. ל-9 יש שני שורשים ריבועיים! אפשר היה אולי לומר שמתקיים {% equation %}\sqrt{9}=\pm3{% endequation %} אבל זה <strong>לא נכון</strong>. לא ככה משתמשים בסימן {% equation %}\sqrt{a}{% endequation %}. המטרה של הסימן הזה היא לתאר שורש אחד, ספציפי, של {% equation %}a{% endequation %}. עבור 9 זה השורש 3, ובאופן כללי עבור כל מספר ממשי {% equation %}a{% endequation %} שקיים לו שורש {% equation %}x{% endequation %}, יש לו בדיוק שני שורשים: {% equation %}x,-x{% endequation %}. העניין הוא שהמינוס של {% equation %}-x{% endequation %} מבטל את עצמו כשמכפילים את {% equation %}-x{% endequation %} בעצמו ולכן מקבלים את אותו הדבר כמו {% equation %}x{% endequation %}. במילים אחרות - שורשים ריבועיים באים בזוגות. אם אחד מהם חיובי, השני יהיה שלילי, ולכן החליטו להגדיר את {% equation %}\sqrt{a}{% endequation %} להיות השורש <strong>החיובי</strong>. זה מה שהסימן מתאר. החריג היחיד הוא 0, שיש לו רק שורש ריבועי אחד - 0 עצמו, ואנחנו מגדירים {% equation %}\sqrt{0}=0{% endequation %}.

העניין הבא שצריך לתת עליו את הדעת הוא ש<strong>לא לכל מספר ממשי</strong> קיים שורש שהוא מספר ממשי. {% equation %}-1{% endequation %} הוא הדוגמא הקלאסית: לכל {% equation %}x{% endequation %} ממשי, {% equation %}x\cdot x{% endequation %} הולך להיות אי-שלילי; אין שום דרך לקבל את {% equation %}-1{% endequation %} ככה. למה חוסר הצדק הזה? ובכן, מכפלה של שני מספרים חיוביים היא חיובית, ומכפלה של שני מספרים שליליים גם היא חיובית (כמו שראינו קודם - מינוס כפול מינוס זה פלוס) ולכן אין דרך לקבל את {% equation %}-1{% endequation %}. מה שאומר שהסימון {% equation %}\sqrt{-1}{% endequation %} שהשתמשתי בו קודם הוא <strong>חשוד מאוד</strong>. אחזור אליו בהמשך, כמובן.

נעבור עכשיו אל כלל כפל השורשים שלומדים בבית הספר: {% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %}. מה השוויון הזה אומר? אתן פה שתי משמעויות, אחת אינטואיטיבית וקלילה יותר והשני פדנטית בהרבה. תנחשו איזו גרסה תהיה זו שמובילה לסתירות במתמטיקה ועצב גדול ואיזו גרסה תוביל להתרת הסבך הזה.

המשמעות האינטואיטיבית והקלילה של {% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %} היא זו: אם {% equation %}x{% endequation %} מקיים {% equation %}x^{2}=a{% endequation %} וגם {% equation %}y{% endequation %} מקיים ש-{% equation %}y^{2}=b{% endequation %} אז {% equation %}xy{% endequation %} מקיים ש-{% equation %}\left(xy\right)^{2}=x^{2}y^{2}=ab{% endequation %}. האמירה הזו היא בבירור נכונה לגמרי, מה ש"מוכיח" את השוויון {% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %}. אם כן, איך אפשר להציל את המתמטיקה מהסתירה שאליה נקלענו?

המשמעות הפדנטית והמעצבנת של {% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %} נחלצת עכשיו לעזרתנו. היא אומרת: אם {% equation %}a,b{% endequation %} הם <strong>מספרים ממשיים</strong> שיש להם <strong>שורש ממשי</strong>, ואם {% equation %}x{% endequation %} מקיים {% equation %}x^{2}=a{% endequation %} <strong>וגם</strong> {% equation %}x{% endequation %} הוא אי-שלילי, ואם {% equation %}y{% endequation %} מקיים {% equation %}y^{2}=b{% endequation %} <strong>וגם</strong> {% equation %}y{% endequation %} הוא אי-שלילי, אז אפשר להסיק שגם למספר הממשי {% equation %}ab{% endequation %} יש שורשים ממשיים, והשורש האי-שלילי של {% equation %}ab{% endequation %} הוא {% equation %}xy{% endequation %}.

המשמעות הפדנטית והמעצבנת הזו היא נכונה לגמרי - אפשר להוכיח אותה יחסית בקלות. העניין הוא שהמשמעות הזו באה עם סייגים גדולים: היא דורשת ש-{% equation %}a,b{% endequation %} יהיו מספרים ממשיים שיש להם שורש. אם הם לא כאלו, השוויון לא יהיה נכון <strong>במשמעות הפדנטית והמעצבנת</strong>. הוא עדיין יהיה נכון במשמעות האינטואיטיבית והקלילה; אבל כפי שנראה בהמשך, במשמעות הזו אין פה שום סתירה.

נעבור אם כן לדבר על הכוכב של הפוסט - היצור המוזר בתכלית {% equation %}\sqrt{-1}{% endequation %}. מה זה? ראשית כל, זה <strong>שימוש חדש</strong> בסימן {% equation %}\sqrt{a}{% endequation %} שעד כה השתמשתי בו רק במקרה שבו {% equation %}a{% endequation %} היה מספר ממשי שיש לו שורש ממשי. לא אמרתי עד כה מה זה אומר, "מספר ממשי"; הכוונה היא לכל מספר שנמצא על ציר המספרים {% equation %}\mathbb{R}{% endequation %}; כל מספר שאפשר לכתוב בייצוג עשרוני, למשל {% equation %}\pi=3.14\ldots{% endequation %}. במילים אחרות, <strong>אין לי פה שום הגדרה</strong> של מה זה מספר ממשי; אני מתפלל שנתקלתם במושג הזה מתישהו (בבית הספר?) כי ההגדרות הפורמליות הן מסובכות. אולי ההגדרה הכי טובה היא "כל מספר ששמעתם עליו בבית הספר חוץ אולי ממספרים מרוכבים".

מה שאמרתי כבר הוא של-{% equation %}-1{% endequation %} אין שורש שהוא מספר ממשי. אבל במתמטיקה קיים מספר, שמסומן ב-{% equation %}i{% endequation %}, שמקיים {% equation %}i^{2}=-1{% endequation %}, כלומר {% equation %}i{% endequation %} הוא שורש של {% equation %}-1{% endequation %} על פי ההגדרה שנתתי למעלה; הוא פשוט אינו מספר ממשי. זה כמובן מעלה שאלות הרות גורל - אם {% equation %}i{% endequation %} איננו מספר ממשי, מה הוא <strong>כן</strong>? האם סתם המצאתי אותו כרגע? ובכן, לא. יש מספר דרכים לבנות פורמלית את {% equation %}i{% endequation %} הזה גם אם כל המספרים שיש בארגז הכלים שלי הם מספרים ממשיים, באופן די דומה לאיך שאפשר לבנות שברים מתוך מספרים שלמים. <a href="https://gadial.net/2007/06/21/imaginary_numbers/">דיברתי על זה בראשית ימי הבלוג</a> אבל הנה שיטה אחת, לא הטבעית או האלגנטית ביותר, אבל זו שעשתה את העבודה מבחינתי והרגיעה את החששות שלי בשעתו.

הרעיון הוא להגדיר מספרים חדשים בעזרת <strong>זוגות</strong> של מספרים ממשיים. לפני שיתחילו לעוף צעקות שאסור לעשות דברים כאלו, בואו נסתכל על שברים: שבר הוא מספר מהצורה {% equation %}\frac{a}{b}{% endequation %} שבו {% equation %}a,b{% endequation %} שניהם מספרים <strong>שלמים</strong>. במקום לסמן {% equation %}\frac{a}{b}{% endequation %} הייתי יכול לסמן {% equation %}\left(a,b\right){% endequation %}, ואז שתי המשוואות הנחמדות שאנחנו מכירים מבית הספר

<ul> <li>{% equation %}\frac{a}{b}+\frac{x}{y}=\frac{ay+bx}{by}{% endequation %}</li>


<li>{% equation %}\frac{a}{b}\cdot\frac{x}{y}=\frac{ax}{by}{% endequation %}</li>

</ul>

היו ניתנות להצגה בצורה "המוזרה" הבאה:

<ul> <li>{% equation %}\left(a,b\right)+\left(x,y\right)=\left(ay+bx,by\right){% endequation %}</li>


<li>{% equation %}\left(a,b\right)\cdot\left(x,y\right)=\left(a\cdot x,b\cdot y\right){% endequation %}</li>

</ul>

המשוואה השניה, של הכפל, נראית די אינטואיטיבית; אנחנו כופלים את הזוגות "רכיב-רכיב" - האיבר השמאלי בתוצאה יהיה מכפלת האיברים השמאליים במוכפלים, ובדומה עבור האיבר הימני. לעומת זאת, החיבור הוא פחד אלוהים. הוא בוודאי לא "רכיב-רכיב". קורה פה משהו מוזר, שיכול להיראות מאוד שרירותי אם לא ברור לנו מאיפה הוא הגיע ולאיזו מטרה, ואת זה אנחנו יודעים כי למדנו ביסודי חיבור שברים.

עכשיו, מה שאני הולך לעשות כדי ליצור את {% equation %}i{% endequation %} יהיה דומה מאוד. אני מגדיר קבוצה חדשה של מספרים, שאני קורא לה <strong>מספרים מרוכבים</strong> ומסמן ב-{% equation %}\mathbb{C}{% endequation %}, ואיבריה הם זוגות {% equation %}\left(a,b\right){% endequation %} כך ש-{% equation %}a,b{% endequation %} הם מספרים ממשיים. ומה שמייחד את הקבוצה הזו הוא חוקי החיבור והכפל שלה. חיבור יהיה "רכיב-רכיב" והכפל יהיה "משהו מוזר, שיכול להיראות מאוד שרירותי אם לא ברור לנו מאיפה הוא הגיע ולאיזו מטרה":

<ul> <li>{% equation %}\left(a,b\right)+\left(x,y\right)=\left(a+x,b+y\right){% endequation %}</li>


<li>{% equation %}\left(a,b\right)\cdot\left(x,y\right)=\left(ax-by,ay+bx\right){% endequation %}</li>

</ul>

בואו נסתכל עכשיו על המספר המרוכב {% equation %}\left(0,1\right){% endequation %} ונכפול אותו בעצמו. על פי כלל הכפל המוזר שלנו, נקבל:

{% equation %}\left(0,1\right)\cdot\left(0,1\right)=\left(0\cdot0-1\cdot1,0\cdot1+1\cdot0\right)=\left(-1,0\right){% endequation %}

כל הסימונים הללו עם סוגריים הם מאוד מסורבלים, אז אני אציג סימון חדש: במקום לכתוב {% equation %}\left(a,b\right){% endequation %} אני אכתוב {% equation %}a+bi{% endequation %}. במקרה של {% equation %}\left(0,1\right){% endequation %}, שבו {% equation %}a=0,b=1{% endequation %}, הסימון הזה נהיה עוד יותר פשוט - {% equation %}i{% endequation %} ותו לא. ובמקרה של {% equation %}\left(-1,0\right){% endequation %} הסימון הזה הוא {% equation %}-1+0\cdot i{% endequation %}, שגם אותו אפשר לפשט אל {% equation %}-1{% endequation %}. קיבלנו ש-{% equation %}i\cdot i=-1{% endequation %}.

אפשר להגיד, ובצדק גמור, שאני "מרמה". שהשוויון {% equation %}i\cdot i=-1{% endequation %} לא מראה שמצאתי שורש למספר הממשי {% equation %}-1{% endequation %} אלא שמצאתי שורש <strong>למספר מרוכב</strong> שאני בחוצפתי קורא לו {% equation %}-1{% endequation %} למרות שהוא בעצם הזוג {% equation %}\left(-1,0\right){% endequation %}. זה כמובן נכון; אני אגיד שמה שאני עושה הוא <strong>לשכן</strong> את המספרים הממשיים שאני מכיר בתוך המספרים המרוכבים. זה נשמע חשוד מאוד, אבל זה בדיוק מה שעושים גם עבור שברים; כותבים 7 בתור סימון מקוצר של {% equation %}\left(7,1\right){% endequation %} וחושבים עליו בתור מספר טבעי נחמד ולא בתור זוג מספרים שלמים.

למה אני מספר את כל זה? כי מצד אחד, חשוב לי להדגיש שהמספרים המרוכבים הם <strong>סבבה</strong>. אין בהם משהו עקום באופן מהותי שמכריח את המתמטיקה להישבר, ההפך; המתמטיקה מסתדרת איתם יפה. מצד שני המתמטיקה <strong>באמת</strong> נשברת בגלל עניין השורשים הזה, וצריך להבין איך.

בואו נחזור אל השוויון {% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %}. דיברתי קודם על שתי משמעויות שלו - אינטואיטיבית ופדנטית. המשמעות האינטואיטיבית אומרת את הדבר הבא: אם במקום {% equation %}\sqrt{a}{% endequation %} נכתוב שורש <strong>כלשהו</strong> של {% equation %}a{% endequation %} ובמקום {% equation %}\sqrt{b}{% endequation %} נכתוב שורש כלשהו של {% equation %}b{% endequation %}, ואם במקום {% equation %}\sqrt{ab}{% endequation %} נכתוב שורש <strong>כלשהו</strong> של מה שמתחת לסימן השורש, כלומר של {% equation %}ab{% endequation %}, אז כשנעלה בריבוע את שני האגפים נקבל את אותו הדבר.

לדוגמא, אם {% equation %}a=9{% endequation %} ו-{% equation %}b=4{% endequation %} אז השוויון שלמעלה הוא {% equation %}\sqrt{9}\cdot\sqrt{4}=\sqrt{36}{% endequation %}. אם למשל אקח את השורש {% equation %}-3{% endequation %} של {% equation %}a{% endequation %} והשורש {% equation %}2{% endequation %} של {% equation %}b{% endequation %} והשורש {% equation %}6{% endequation %} של 36, אז אקבל את הטענה:

{% equation %}\left[\left(-3\right)\cdot2\right]^{2}=6^{2}{% endequation %}

זו טענה נכונה, אבל אני מקווה שברור שזה לא מה ש-{% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %} <strong>באמת</strong> אומר. הוא לא אומר "המספר {% equation %}\sqrt{a}\cdot\sqrt{b}{% endequation %} (בדוגמה שלנו, {% equation %}-6{% endequation %}) הוא שורש כלשהו של {% equation %}ab{% endequation %}". הוא אומר "המספר {% equation %}\sqrt{a}\cdot\sqrt{b}{% endequation %} <strong>שווה בדיוק</strong> לשורש <strong>מסויים</strong> של {% equation %}ab{% endequation %}, השורש האי-שלילי". הדבר הזה פשוט לא עובד, כי השורש האי-שלילי של {% equation %}36{% endequation %} הוא {% equation %}6{% endequation %}, והוא שונה מ-{% equation %}-6{% endequation %}. כדי שהשוויון הזה יעבוד, הכרחי שגם בבניית המספר {% equation %}\sqrt{a}\cdot\sqrt{b}{% endequation %} ניקח רק את השורש האי-שלילי של {% equation %}a,b{% endequation %}.

טוב ויפה, אז למה זה לא עובד עם {% equation %}\sqrt{-1}{% endequation %}? כי פה אין בכלל משמעות ל"שורש שלילי" ו"שורש חיובי" במובן הרגיל. השורשים של {% equation %}\sqrt{-1}{% endequation %} הם {% equation %}i{% endequation %} ו-{% equation %}-i{% endequation %}. מה חיובי ושלילי כאן?

"אה-הא!" אתם בוודאי אומרים: "ברור ש-{% equation %}i{% endequation %} חיובי ואילו {% equation %}-i{% endequation %} שלילי, הרי ליד {% equation %}-i{% endequation %} יש סימן מינוס!". ובכן, זה לא באמת כל כך פשוט; למשל, במספר המרוכב {% equation %}z=1-i{% endequation %} מתקיים {% equation %}-z=-1+i{% endequation %} וקצת קשה לומר מי משני המספרים הללו הוא החיובי והשלילי על פי גישת ה"חפשו את סימן המינוס". אבל זו אפילו לא הבעיה המרכזית. הבעיה המרכזית היא שכדי להוכיח את {% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %} אנחנו מניחים שמספרים חיוביים יתנהגו בצורה <strong>מאוד נחמדה</strong>, ואם אני אנסה לומר בכוח ש-{% equation %}i{% endequation %} הוא "חיובי" אני אאבד את הצורה המאוד נחמדה הזו.

ספציפית, הדבר הנחמד שאני מתבסס עליו כאן הוא <strong>סגירות</strong>: אם כופלים שני מספרים חיוביים, התוצאה תהיה בעצמה מספר חיובי. אם {% equation %}a>0,b>0{% endequation %} אז גם {% equation %}ab>0{% endequation %}. זה כמובן לא עובד עם {% equation %}i{% endequation %}, כי כשכופלים את {% equation %}i{% endequation %} בעצמו מקבלים מספר שלילי, {% equation %}-1{% endequation %}. אם נקרא ל-{% equation %}i{% endequation %} חיובי נאבד את תכונת הסגירות של החיוביים ולכן נאבד את התכונה {% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %}.

למה הסגירות כל כך חשובה? בשביל זה בואו נראה הוכחה בנפנוף ידיים של הטענה. אם {% equation %}x^{2}=a{% endequation %} וגם {% equation %}y^{2}=b{% endequation %}, אז חשבון פשוט במיוחד נותן לנו ש-

{% equation %}\left(xy\right)^{2}=x^{2}y^{2}=ab{% endequation %}

אנחנו מסתמכים כאן במובלע על מה שנקרא <strong>חוק החילוף</strong>; על כך ש-{% equation %}xy=yx{% endequation %} ולכן {% equation %}\left(xy\right)^{2}=xyxy=xxyy=x^{2}y^{2}{% endequation %}. אבל חוק החילוף הוא תכונה בסיסית שמתקיימת גם במספרים הממשיים וגם במספרים המרוכבים, אז אין עם זה בעיה (הוא לא מתקיים, למשל, עבור <strong>כפל מטריצות</strong>, או <strong>כפל קווטרניונים</strong> אבל זה סיפור שונה). קיבלנו, אם כן, הוכחה לטענה הכללית "אם {% equation %}x{% endequation %} הוא שורש של {% equation %}a{% endequation %} ו-{% equation %}y{% endequation %} הוא שורש של {% equation %}b{% endequation %} אז {% equation %}xy{% endequation %} הוא שורש של {% equation %}ab{% endequation %}". הטענה הזו <strong>נכונה</strong> גם עבור מספרים מרוכבים וספציפית עבור השורשים של {% equation %}-1{% endequation %} שהם כזכור {% equation %}\pm i{% endequation %}. בואו נראה את זה על ידי כך שנתבונן במפורש על כל ארבע המכפלות של שורשים של {% equation %}-1{% endequation %}:

<ul> <li>{% equation %}i\cdot i=-1{% endequation %}</li>


<li>{% equation %}i\cdot\left(-i\right)=1{% endequation %}</li>


<li>{% equation %}\left(-i\right)\cdot i=1{% endequation %}</li>


<li>{% equation %}\left(-i\right)\cdot\left(-i\right)=-1{% endequation %}</li>

</ul>

כל ארבע המכפלות הללו הניבו לנו את 1 או את {% equation %}-1{% endequation %}, שהם השורשים של {% equation %}1{% endequation %}. הדבר היחיד שנכשל הוא הציפיה שלנו לקבל את השורש <strong>החיובי</strong> של 1. אנחנו אמנם מקבלים אותו, אבל רק במכפלה כמו {% equation %}i\cdot\left(-i\right){% endequation %}, שמערבת את השורש "הלכאורה חיובי" {% equation %}i{% endequation %} והשורש "הלכאורה שלילי" {% equation %}-i{% endequation %} ביחד.

נניח עכשיו לרגע ש-{% equation %}x,y{% endequation %} הם מספרים ממשיים <strong>חיוביים</strong> שמקיימים {% equation %}x^{2}=a,y^{2}=b{% endequation %}. אז אנחנו יודעים ש-{% equation %}xy{% endequation %} הוא שורש של {% equation %}ab{% endequation %}; ואנחנו יודעים, בגלל שהממשיים החיוביים <strong>סגורים לכפל</strong>, שגם {% equation %}ab{% endequation %} הוא מספר ממשי חיובי. לכן, אם הסימון {% equation %}\sqrt{\cdot}{% endequation %} משמש אותנו כדי לתאר את השורש החיובי של מספר כלשהו, אנחנו יודעים שמתקיים {% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %}, כי בגלל ש-{% equation %}x,y{% endequation %} חיוביים הם אלו שמופיעים באגף שמאל, ובגלל ש-{% equation %}xy{% endequation %} חיובי הוא מי שמופיע באגף ימין.

מה שהסימן {% equation %}\sqrt{\cdot}{% endequation %} עושה הוא לא רק להוציא שורש; הוא מוציא שורש ו<strong>בוחר</strong> אחד מהשורשים האפשריים ומחזיר אותו. הוא עושה את זה באמצעות <strong>כלל בחירה</strong> מסוים - במקרה שלנו, "קח את השורש החיובי". השוויון {% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %} לא מתאר איזו תכונה כללית של פונקציית השורש; הוא מתאר תכונה כללית של <strong>כלל הבחירה</strong> הזה, וכלל הבחירה הזו מלכתחילה קיים רק למספרים ממשיים. מה שראינו עכשיו הוא שאם ננסה להרחיב את כלל הבחירה הזה למספרים נוספים, התכונה היפה שתיארנו לא תשתמר.

כל הסיפור הזה מתקשר לבעיה כללית הרבה יותר בתורת הפונקציות המרוכבות. יש כמה וכמה סיטואציות שבהן יש לנו "פונקציות" כמו שורש שיכולות להחזיר יותר מתוצאה אחת; אפשר לחשוב עליהן כאילו הן מחזירות קבוצה של תוצאות אפשריות. לעתים קרובות מה שמועיל לעשות הוא לקחת פונקציה כזו וליצור ממנה פונקציה שכן מחזירה ערך מספרי יחיד לכל קלט - פונקציה כזו נקראת <strong>ענף</strong> של הפונקציה המקורית. האתגר הוא לבחור את הענף הזה כך שיקיים תכונות נחמדות ככל האפשר - למשל, <strong>רציפות</strong>, כלומר ששינויים קטנים בקלט לא יובילו לשינויים גדולים בפלט. מה שראינו פה הוא שהענף של פונקציית השורש <strong>על המספרים הממשיים</strong> שמוגדר בתור "קחו תמיד את השורש החיובי" מקיים תכונת <strong>כפליות</strong> (פונקציה {% equation %}f{% endequation %} היא כפלית אם {% equation %}f\left(ab\right)=f\left(a\right)f\left(b\right){% endequation %}) אבל על המספרים המרוכבים אין לנו ענף שיקיים כפליות. זה אחד מהחסרונות של שימוש במרוכבים; היתרונות כל כך גדולים שאנחנו יכולים לקבל את זה בשמחה.

אם כן, לסיכום: אין סתירה במתמטיקה; אין בעיה עם השימוש ב-{% equation %}i{% endequation %}; ואין בעיה עם {% equation %}\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}{% endequation %} כל עוד אנחנו יודעים באיזה הקשר אנחנו משתמשים בו. מה שכן יש פה הוא תירוץ נפלא לכתוב פוסטים על מרוכבים. 