---
id: 1504
title: "עם קצת עבודה, מגיעים למכפלה סקלרית"
date: 2012-02-02 16:46:32
layout: post
categories: 
  - אלגברה לינארית
tags: 
  - מכפלה סקלרית
---
אחד המושגים שתמיד בלבל אותי בפיזיקה הוא מושג ה<strong>עבודה</strong>. בואו נציג אותו בקצרה עבור מי שלא מכירים. נקודת המוצא שלנו היא החוק השני של ניוטון, {% equation %}F=ma{% endequation %}, שאומר שאם כוח כלשהו פועל על גוף ({% equation %}F{% endequation %} הוא גודל הכוח, והוא חיובי אם הכוח מופעל "ימינה" ושלילי אם הוא מופעל "שמאלה") אז הוא גורם לגוף לתאוצה {% equation %}a{% endequation %} שפרופורציונית הפוכה למסת הגוף {% equation %}m{% endequation %} (תכפילו את המסה פי 2, והתאוצה לה גורם אותו כוח תקטן פי 2). אני מציג כאן בכוונה גרסה פשוטה של החוק כי לא נצטרך יותר מכך. בנוסף, שימו לב שהעולם שלי בינתיים הוא חד ממדי - עצמים יכולים לנוע רק ימינה או שמאלה. זה יסתבך בקרוב.

כעת, מהי תאוצה? היא מוגדרת בתור השינוי במהירות לאורך זמן. ומהי מהירות? השינוי במיקום לאורך זמן. אם גוף מתחיל ממיקום {% equation %}x_{0}{% endequation %} כשמהירותו ההתחלתית {% equation %}v_{0}{% endequation %} ומאותו רגע והלאה הוא מאיץ בתאוצה קבועה {% equation %}a{% endequation %}, אז אחרי זמן {% equation %}t{% endequation %} מהירותו תהיה {% equation %}v\left(t\right)=at+v_{0}{% endequation %} ומיקומו יהיה {% equation %}x\left(t\right)=\frac{at^{2}}{2}+v_{0}t+x_{0}{% endequation %} (למשוואות הללו ניתן להגיע באמצעות אינטגרציה: {% equation %}\int adt=at+v_{0}{% endequation %} ו-{% equation %}\int\left(at+v_{0}\right)dt=\frac{at^{2}}{2}+v_{0}t+x_{0}{% endequation %}, אבל למי שזה לא אומר לו כלום, לא נורא). יש לנו אם כן שלושה גורמים שונים שאיכשהו מתקשרים ביניהם יחדיו - מהירות הגוף, מיקום הגוף, והכוח שפעל על הגוף. האם יש לנו דרך לתאר את כל הסיפור הזה מבלי להכניס לתמונה בכלל גורמים כמו התאוצה והזמן?

באופן די מפתיע, מתברר שכן. בואו נניח שניה ש-{% equation %}x_{0}=v_{0}=0{% endequation %} כדי לפשט את המשוואות, ונתבונן במהירות ובמיקום אחרי זמן {% equation %}t{% endequation %} מסויים. המהירות היא {% equation %}v=at{% endequation %} והמיקום הוא {% equation %}x=\frac{at^{2}}{2}{% endequation %} . מכיוון ש-{% equation %}t{% endequation %} מופיע בריבוע במשוואה של המיקום, בואו נעלה גם את משוואת המהירות בריבוע ונקבל {% equation %}v^{2}=a^{2}t^{2}{% endequation %}. עכשיו, בואו נבודד את {% equation %}t^{2}{% endequation %} ממשוואת המיקום ונקבל {% equation %}t^{2}=\frac{2x}{a}{% endequation %}. נציב במשוואת המהירות ונקבל {% equation %}v^{2}=2xa{% endequation %}. כעת נחליף את {% equation %}a{% endequation %} ב-{% equation %}\frac{F}{m}{% endequation %}, בעזרת החוק השני של ניוטון, ונקבל {% equation %}v^{2}=2x\frac{F}{m}{% endequation %}. נחלק ב-{% equation %}\frac{2}{m}{% endequation %} וקיבלנו את המשוואה {% equation %}\frac{mv^{2}}{2}=Fx{% endequation %}.

מה שמעניין במשוואה הזו (וכעת אנפנף קצת בידיים) הוא שהיא מתארת באגף ימין שלה תהליך שהתרחש לאורך זמן, בלי לציין את הזמן בכלל - הכוח {% equation %}F{% endequation %} פעל על הגוף לכל אורך תנועתו של הגוף מרחק של {% equation %}x{% endequation %}. באגף שמאל, לעומת זאת, יש לנו גודל "רגעי" - {% equation %}\frac{mv^{2}}{2}{% endequation %} מתאר את המהירות והמסה כאן ועכשיו. כאמור, זה נפנוף ידיים שאין לו משמעות אמיתית, אבל אני חושב שהוא נותן אינטואיציה טובה לסיבה שבגללה מייחדים ל-{% equation %}\frac{mv^{2}}{2}{% endequation %} שם - <strong>אנרגיה קינטית</strong>. להסביר עכשיו מה הכוונה במילה "אנרגיה" (בוריאציה על איניגו מונטויה - הרבה אנשים משתמשים שוב ושוב במילה הזו, אך איני חושב שהיא אומרת מה שהם חושבים שהיא אומרת) לא אנסה אפילו; אני מסתפק בהצהרה ש-{% equation %}\frac{mv^{2}}{2}{% endequation %} היא כמות "מעניינת" ואסמן אותה ב-{% equation %}E{% endequation %}.

כעת בואו לא נתעצל ונחשוב מה קורה אם {% equation %}x_{0}{% endequation %} ו-{% equation %}v_{0}{% endequation %} הם ערכים כלליים. וכשאני אומר "לא נתעצל" אני מתכוון - קחו נייר ועט ועשו את החישוב בעצמכם כדי לראות שהבנתם. אני את החישוב עשיתי בצד, והנה מה שמקבלים: {% equation %}\frac{m\left(v^{2}-v_{0}^{2}\right)}{2}=F\left(x-x_{0}\right){% endequation %}. ברשותכם, אסמן {% equation %}E=\frac{mv^{2}}{2}{% endequation %} ו-{% equation %}E_{0}=\frac{mv_{0}^{2}}{2}{% endequation %} - אלו האנרגיות בהתחלה ובסוף, ואסמן {% equation %}\Delta E=E-E_{0}{% endequation %} - זהו השינוי באנרגיה הקינטית של הגוף, ואסמן {% equation %}\Delta x=x-x_{0}{% endequation %} - זה השינוי במיקום הגוף, וקיבלנו את המשוואה

{% equation %}\Delta E=F\cdot\Delta x{% endequation %}

ובמילים - השינוי באנרגיה הקינטית של הגוף כתוצאה מפעולת הכוח {% equation %}F{% endequation %} שווה לגודל הכוח הזה כשהוא מוכפל בשינוי המיקום של הגוף (שימו לב ש"שינוי המיקום של הגוף" - מה שנקרא לפעמים "ההעתק" - אינו בדיוק המרחק שלו; אם הגוף היה בהתחלה בנקודה 0 ובסיום התנועה בנקודה {% equation %}-10{% endequation %}, אז {% equation %}\Delta x=-10{% endequation %} למרות שהגוף עבר מרחק של 10).

הביטוי הזה באגף ימין - הכוח-כפול-העתק, הוא מה שנקרא <strong>עבודה</strong> - עבודת הכוח {% equation %}F{% endequation %} על הגוף. לכאורה הכל טוב ויפה, אלא שכל מה שראינו עד עכשיו היה מאוד פשטני והסיפור הולך עכשיו להסתבך.

מה שדיברנו עליו עד כה היה עולם חד-ממדי. בעולם הזה לכוחות ולמהירויות ולהעתקים אין ממש כיוון, אם כי הם יכולים להיות חיוביים או שליליים ולפי זה נקבע הסימן שלהם. מה שעשיתי עד כה היה עקבי עם הגישה הזו - למשל, אם {% equation %}\Delta x{% endequation %} הוא חיובי אבל {% equation %}F{% endequation %} הוא שלילי, מה שהמשוואות מתארות הוא גוף שנע בכיוון החיובי כשבאותו הזמן פועל עליו כוח <strong>בכיוון הנגדי</strong>, כלומר כוח שדווקא מאיט אותו. התוצאה? שינוי <strong>שלילי</strong> באנרגיה הקינטית (מכפלה של {% equation %}\Delta x{% endequation %} החיובי ב-{% equation %}F{% endequation %} השלילי), מה שמתאים לנו להאטה. שימו לב שאנחנו רואים כאן ש-{% equation %}F{% endequation %} בכלל לא חייב להיות הגורם לשינוי במיקום; הנקודה היא ש-{% equation %}F{% endequation %} <strong>משפיע</strong> על אופי השינוי במיקום, ואיכשהו אפשר לחלץ מההשפעה הזו בדיוק את השינוי באנרגיה הקינטית ש-{% equation %}F{% endequation %} גרם לגוף. זה רעיון לא טריוויאלי כלל לטעמי.

אבל כשעוברים לעולם דו-ממדי, פתאום הכל הופך להיות מוזר בהרבה. ראשית, מעכשיו אני מסמן גדלים כמו כוח, מהירות והעתק עם חץ קטן מעליהם כדי לציין שהם <strong>וקטורים:</strong> מבחינתנו לעת עתה, וקטור הוא שילוב של גודל מספרי חיובי (<strong>סקלר</strong>) עם כיוון במרחב. כך למשל {% equation %}\vec{F}{% endequation %} הוא וקטור כוח שפועל בכיוון מסויים; ב-{% equation %}F{% endequation %} אסמן את הגודל שלו (או לפעמים ב-{% equation %}\left|\vec{F}\right|{% endequation %} אם ממש לא ארצה לגרום לבלבול).

כל עוד הכוח שבו אנו עוסקים הוא עדיין באותו כיוון כמו ההעתק של הגוף, או בדיוק בכיוון ההפוך, הניתוח שלנו זהה. אבל מה אם הכוח פועל בזווית כלשהי ביחס לכיוון ההעתק? הנה דוגמה קלאסית: לווין שנמצא הרחק מעל כדור הארץ. כדור הארץ מושך אותו לכיוון המרכז, אבל אם יש ללווין מהירות התחלתית כלשהי בכיוון שניצב לזה של הכוח, אז ההשפעה של הכוח תהיה לשנות את <strong>כיוון</strong> הלווין אבל לא את מהירותו, באופן כזה שהכוח ימשיך להיות ניצב לכיוון הלווין לכל משך תנועת הלווין. בסיטואציה הזו הלווין יבצע תנועה <strong>מעגלית</strong> סביב כדור הארץ, תוך שגודל המהירות שלו נשאר קבוע ולכן האנרגיה הקינטית שלו נשארת קבועה. המסקנה המפתיעה היא שכוח הכובד לא ביצע שום עבודה על הלווין - הוא לא גרם לשום שינוי באנרגיה הקינטית שלו. זה כמובן לא מתאים לדימוי המנטלי שיש לנו בראש של כדור הארץ ששולח יד וגורם ללווין לשנות את כיוונו כל הזמן וכדור הארץ מזיע ומתאמץ כדי שהתנועה הזו תימשך כך; לכן כדאי לזרוק לפח את הדעות הקדומות שבאות עם שימוש במילה "עבודה" ולהתמקד במשמעות הרלוונטית עבורנו של המושג.

בעיה נוספת, שגם היא צצה כבר בתנועה מעגלית וקצת טאטאתי עד כה מתחת לשטיח, היא מה קורה אם הגוף שעליו הכוח פועל לא נע בקו ישר. איך בעצם מחשבים את העבודה עליו, אם כל מה שדיברנו עליו היה תנועה בקו ישר? התשובה היא שצריך להיעזר כאן בחשבון אינפיניטסימלי - מקרבים את מסלול הגוף בעזרת קווים ישרים, על כל אחד מהם מחשבים את העבודה בנפרד, סוכמים ומקבלים קירוב לעבודה ה"אמיתית"; וככל שהקירוב בעזרת קווים ישרים טוב יותר, כך גם הקירוב לעבודה האמיתית טוב יותר, ובעזרת הפלא שנקרא "אינטגרל" (במקרה הזה, אינטגרל קווי) מקבלים <strong>בדיוק</strong> את העבודה. זה לא פוסט על אינפי ולכן לא ארחיב יותר על כך.

מעכשיו נחזור לדבר על תנועה בקו ישר, רק עם כוח שעשוי לפעול בזווית, מתוך הכרה בכך שזה לא בהכרח גורם למסלול התנועה להשתנות. דוגמה קלאסית לסיטואציה כזו היא גוף שמתגלגל ב<strong>משטח משופע.</strong> על גוף כזה פועלים שני כוחות בו זמנית - מצד אחד, כוח הכובד שמושך אותו "למטה"; מצד שני, המשטח עצמו מפעיל עליו כוח שהוא מאונך למשטח, ולכן גם מאונך לכיוון התנועה של הגוף. הכוח הזה נקרא "כוח נורמלי" ("נורמל" כאן פירושו "מאונך" ומכאן השם). מכיוון שהוא מאונך לכיוון התנועה הוא לא מבצע עבודה; השינוי באנרגיה נובע רק מעבודת כוח הכובד.

נניח שהגוף שלנו נמצא כרגע בגובה {% equation %}h{% endequation %} מעל פני הקרקע. אפשר לשים אותו על הרבה משטחים משופעים - למשל, משטח שנמצא בזווית של {% equation %}90^{\circ}{% endequation %} ביחס לקרקע, כך שהגוף פשוט ייפול באופן חופשי לקרקע; או משטח בזווית של {% equation %}45^{\circ}{% endequation %} שהוא נקודת האמצע בין משטח ניצב ומשטח שטוח; או משטח שהוא "כמעט שטוח", נאמר עם זווית של מעלה בודדת, ובו הכדור בקושי יזוז בהתחלה. באופן כללי אם אורך המשטח הוא {% equation %}L{% endequation %} והוא מגיע לגובה {% equation %}h{% endequation %}, אז הזווית שהוא יוצר עם ניצב לפני הקרקע, שאסמן ב-{% equation %}\alpha{% endequation %}, מקיימת {% equation %}\cos\alpha=\frac{h}{L}{% endequation %}. תכף תהיה לזווית הזו חשיבות רבה.

את ההשפעה של כוח הכובד על גוף שמתגלגל במשטח המשופע אפשר לחלק לשניים - יש את החלק שמושך את הגוף בכיוון אופקי למשטח, והוא מה שמאיץ את הגוף קדימה; ויש את החלק שמושך את הגוף בכיוון אנכי למשטח, והוא מתבטל על ידי הכוח הנורמלי שהמשטח מפעיל על הגוף (למעשה, מקור הכוח הזה הוא בדיוק בכך שכוח המשיכה מושך את הגוף "לתוך" המשטח). כלומר, את כוח הכובד פירקנו כאן לשני "רכיבים" שרק אחד מהם משפיע על הגוף.

איך הפירוק הזה נראה? לצורך כך בואו נחשוב על הסיטואציה, במערכת צירים שבה נוח לנו לעבוד. המערכת הזו תשמע אולי קצת מוזר בהתחלה - ציר {% equation %}x{% endequation %} שלי יהיה מאוזן למשטח המשופע, וציר {% equation %}y{% endequation %} שלי יהיה מאונך לו, ובנוסף לכך הכיוון החיובי של ציר {% equation %}y{% endequation %} ("למעלה") דווקא יהיה הכיוון שהולך לעבר הקרקע. המטרה היא שהוקטור של כוח הכובד יהיה ממוקם ברבע הראשון של מערכת הצירים, כי כך יוצא פשוט יותר.

במערכת הצירים הזו, הכיוון החיובי של ציר {% equation %}x{% endequation %} הוא פני המשטח המשופע, ולכן הזווית שיוצר וקטור כוח הכובד עם ציר {% equation %}x{% endequation %} היא {% equation %}\alpha{% endequation %} (אל תתעצלו! שבו וציירו את זה בעצמכם! זו הדרך הכי טובה להבין מה הולך כאן). את כוח הכובד עצמו אנחנו מפרקים לסכום של שני וקטורים - {% equation %}\vec{F}=\vec{F}_{x}+\vec{F}_{y}{% endequation %}, כך ש-{% equation %}\vec{F}_{x}{% endequation %} הוא וקטור שכיוונו ככיוון ציר {% equation %}x{% endequation %} ואילו {% equation %}\vec{F}_{y}{% endequation %} הוא וקטור שכיוונו ככיוון ציר {% equation %}y{% endequation %} (חיבור וקטורים פועל כך: לוקחים את אחד הוקטורים ושמים בראשית הצירים, מדביקים את השני בקצהו, ואז הוקטור החדש הוא הוקטור מראשית הצירים אל נקודת הקצה של הוקטור השני). בעזרת טריגונומטריה אנחנו יודעים לחשב את גדלי הוקטורים הללו: {% equation %}F_{y}=F\sin\alpha{% endequation %} ו-{% equation %}F_{x}=F\cos\alpha{% endequation %}. במילים אחרות, הכוח שגורם לתנועה של העצם על המשטח המשופע הוא {% equation %}F\cos\alpha{% endequation %}, וכוח זה פועל באותו כיוון כמו ההעתק של הגוף. כשהגוף מגיע לתחתית המשטח המשופע הוא עבר מרחק של {% equation %}L{% endequation %}, ולכן העבודה של {% equation %}F{% endequation %} הייתה בדיוק {% equation %}F\cdot L\cdot\cos\alpha{% endequation %}. זו המשוואה החשובה ביותר בפוסט; הסיבה שבגללה כתבתי אותו מלכתחילה.

לפני שאני מרחיב על המשוואה הזו, בואו רק נשים לב לכך שמכיוון ש-{% equation %}\cos\alpha=\frac{h}{L}{% endequation %} הרי שהעבודה של כוח הכובד על הגוף היא בעצם {% equation %}F\cdot L\cdot\cos\alpha=F\cdot h{% endequation %}. כעת, אם כוח הכובד גורם לתאוצה {% equation %}g{% endequation %} בגוף, כלומר {% equation %}F=mg{% endequation %}, אפשר לכתוב את המשוואה הזו גם כ-{% equation %}F\cdot h=mgh{% endequation %}, וקיבלנו שהשינוי באנרגיה הקינטית של הגוף הוא בדיוק {% equation %}mgh{% endequation %}. כעת שימו לב ש-{% equation %}mgh{% endequation %} הוא גודל שתלוי בשני ערכים שהם קבועים במערכת שלנו - {% equation %}m,g{% endequation %} ובערך שלישי, שהוא הגובה שהגוף "איבד". אפשר לחשוב על זה גם כך - כאשר הגוף היה בגובה {% equation %}h{% endequation %}, היה לו <strong>פוטנציאל</strong> לזכות באנרגיה קינטית של {% equation %}mgh{% endequation %} אם רק ייפול/יתגלגל במשטח המשופע; לכן קוראים ל-{% equation %}mgh{% endequation %} אנרגיה <strong>פוטנציאלית</strong> של הגוף, והמשטח המשופע הוא כלי שממיר את האנרגיה הפוטנציאלית שלו לאנרגיה קינטית. באופן כללי אנרגיה פוטנציאלית היא מושג מורכב יותר - צריך להסביר פוטנציאלית ביחס למה (כאן זה ביחס לכדור הארץ), ולא תמיד {% equation %}g{% endequation %} קבוע, ולא תמיד {% equation %}m{% endequation %} קבוע, ואני לא הולך להיכנס לדברים הללו בכלל.

חזרה למשוואה {% equation %}F\cdot L\cdot\cos\alpha{% endequation %}. בעצם לקחנו את הוקטור {% equation %}\vec{F}{% endequation %} שמתאר את כל פעולת כוח הכובד על הגוף, לא רק בכיוון ה"נכון", ואת הוקטור {% equation %}\vec{L}{% endequation %} שמתאר את ההעתק של הגוף, וכפלנו את הגדלים שלהם זה בזה, ואת כל זה הכפלנו ב-{% equation %}\cos\alpha{% endequation %} כאשר {% equation %}\alpha{% endequation %} היא הזווית שלהם. את הדבר הזה אפשר לעשות באופן כללי, לכל שני וקטורים: {% equation %}\vec{v}\cdot\vec{u}=\left|v\right|\cdot\left|u\right|\cdot\cos\alpha{% endequation %} כאשר {% equation %}\alpha{% endequation %} היא הזווית בין {% equation %}u{% endequation %} ו-{% equation %}v{% endequation %}. למכפלה כזו קוראים <strong>מכפלה סקלרית</strong>.

שאלה שחלקכם ודאי שואלים עכשיו היא מה זה אומר "הזווית בין שני וקטורים", הרי תמיד אפשר לחשוב על שתי זוויות (האחת היא הזווית שבה יש לסובב את {% equation %}\vec{u}{% endequation %} נגד כיוון השעון כדי שינוח על {% equation %}\vec{v}{% endequation %}, והשניה היא הזווית שבה יש לסובב את {% equation %}\vec{v}{% endequation %} נגד כיוון השעון כדי שינוח על {% equation %}\vec{u}{% endequation %}). ובכן, זה נכון - יש שתי זוויות שונות בין הוקטורים - {% equation %}\alpha{% endequation %}ו-{% equation %}360^{\circ}-\alpha{% endequation %}. למרבה המזל, {% equation %}\cos\left(\alpha\right)=\cos\left(360^{\circ}-\alpha\right){% endequation %} ולכן זה לא משנה.

הרעיון במכפלה סקלרית הוא לכפול את גדלי שני הוקטורים, אבל תוך "תיקון" שמתחשב בכך שיש ביניהם זווית. אם זה לא אינטואיטיבי לכם, הנה דרך אחרת לחשוב על העניין. נניח ש-{% equation %}\vec{v},\vec{u}{% endequation %} הם וקטורים כלשהם, ואנחנו קובעים מערכת צירים כלשהי שבה הצירים {% equation %}x,y{% endequation %} מאונכים זה לזה. עכשיו נפרק את שני הוקטורים לרכיבים: {% equation %}\vec{v}=\vec{v}_{x}+\vec{v_{y}}{% endequation %} ו-{% equation %}\vec{u}=\vec{u}_{x}+\vec{u_{y}}{% endequation %}. נניח ש-{% equation %}\vec{u}{% endequation %} יוצר זווית {% equation %}\theta{% endequation %} כלשהי עם ציר {% equation %}x{% endequation %}, אז {% equation %}\vec{v}{% endequation %} יוצר זווית {% equation %}\theta+\alpha{% endequation %} עם ציר {% equation %}x{% endequation %} כש-{% equation %}\alpha{% endequation %} הוא הזווית שמעבירה את {% equation %}\vec{u}{% endequation %} אל {% equation %}\vec{v}{% endequation %}. כעת, שימו לב לקסם הבא:

{% equation %}\left|u_{x}\right|\left|v_{x}\right|+\left|u_{y}\right|\left|v_{y}\right|=\left(\left|u\right|\cos\theta\right)\left(\left|v\right|\cos\left(\theta+\alpha\right)\right)+\left(\left|u\right|\sin\theta\right)\left(\left|v\right|\sin\left(\theta+\alpha\right)\right){% endequation %}

{% equation %}=\left|u\right|\left|v\right|\left(\cos\theta\cos\left(\theta+\alpha\right)+\sin\theta\sin\left(\theta+\alpha\right)\right){% endequation %}

{% equation %}=\left|u\right|\left|v\right|\cos\left(\theta+\alpha-\theta\right)=\left|u\right|\left|v\right|\cos\alpha{% endequation %}

השתמשתי כאן בזהות הטריגונומטרית לקוסינוס של הפרש - {% equation %}\cos\left(\alpha-\beta\right)=\cos\alpha\cos\beta+\sin\alpha\sin\beta{% endequation %}.

המסקנה היא שאפשר לחשוב על מכפלה סקלרית גם באופן שונה - לוקחים מערכת צירים כלשהי (עם צירים מאונכים - זה חשוב), מפרקים את שני הוקטורים שכופלים לרכיבים, מכפילים כל זוג רכיבים בנפרד, ואז מחברים. כאשר נכליל את ההגדרה של מכפלה סקלרית בפוסט הבא הגישה הזו תהיה המועילה יותר עבורנו; החשיבות והכוח של הגישה הראשונה היא בכך שאחרי שנכליל את מושג המכפלה הסקלרית נוכל להפוך את היוצרות ו<strong>להגדיר</strong> אורך וזווית באמצעות ההכללה הזו; אבל עוד חזון למועד.